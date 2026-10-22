#!/usr/bin/env node
/**
 * Auditoría de fichas de Google Business Profile (Google Maps).
 *
 * Uso:
 *   GOOGLE_MAPS_API_KEY=... node gbp_audit.js "bares en Alcalá de Henares" [--max 20] [--out auditoria.csv]
 *   GOOGLE_MAPS_API_KEY=... node gbp_audit.js --ids ChIJ...,ChIJ...
 *
 * Fuente: Places API (New) de Google. Es la vía oficial: necesita una clave con
 * "Places API (New)" habilitada en Google Cloud. Coste: Text Search y Place Details
 * se cobran por campo; con la cuota gratuita mensual de Google, 20-50 fichas no cuestan nada.
 *
 * Qué SÍ puede comprobar la API: nombre, categoría principal y secundarias, valoración,
 * nº de reseñas, web, teléfono, horario, nº de fotos (hasta 10 devueltas), descripción
 * editorial, estado (abierto/cerrado permanentemente), accesibilidad, 5 reseñas recientes.
 * Qué NO puede comprobar: respuestas del propietario a reseñas, publicaciones (posts),
 * productos/servicios, preguntas y respuestas, si la ficha está reclamada. Eso solo se ve
 * abriendo la ficha en Maps a mano o con un navegador, y Google no lo expone en la API.
 */
const fs = require('fs');

const KEY = process.env.GOOGLE_MAPS_API_KEY;
if (!KEY) { console.error('Falta GOOGLE_MAPS_API_KEY'); process.exit(1); }

const args = process.argv.slice(2);
const opt = (name, def) => { const i = args.indexOf(name); return i >= 0 ? args[i + 1] : def; };
const query = args.find(a => !a.startsWith('--') && args[args.indexOf(a) - 1] !== '--max' && args[args.indexOf(a) - 1] !== '--out' && args[args.indexOf(a) - 1] !== '--ids');
const max = parseInt(opt('--max', '20'), 10);
const out = opt('--out', 'auditoria_gbp.csv');
const ids = opt('--ids', '');

const FIELDS = [
  'id','displayName','primaryType','types','rating','userRatingCount','websiteUri',
  'nationalPhoneNumber','regularOpeningHours','photos','editorialSummary','businessStatus',
  'googleMapsUri','formattedAddress','reviews','priceLevel'
].join(',');

async function gfetch(url, body, fieldMask) {
  const r = await fetch(url, {
    method: body ? 'POST' : 'GET',
    headers: { 'Content-Type': 'application/json', 'X-Goog-Api-Key': KEY, 'X-Goog-FieldMask': fieldMask },
    body: body ? JSON.stringify(body) : undefined,
  });
  if (!r.ok) throw new Error(`${r.status} ${await r.text()}`);
  return r.json();
}

async function textSearch(q, n) {
  const places = []; let pageToken;
  while (places.length < n) {
    const data = await gfetch('https://places.googleapis.com/v1/places:searchText',
      { textQuery: q, pageSize: Math.min(20, n - places.length), pageToken, languageCode: 'es', regionCode: 'ES' },
      'places.id,nextPageToken');
    (data.places || []).forEach(p => places.push(p.id));
    pageToken = data.nextPageToken; if (!pageToken) break;
  }
  return places.slice(0, n);
}

async function details(id) {
  return gfetch(`https://places.googleapis.com/v1/places/${id}?languageCode=es`, null, FIELDS);
}

function audit(p) {
  const f = []; // fallos detectados
  const rating = p.rating ?? 0, n = p.userRatingCount ?? 0;
  const photos = (p.photos || []).length; // la API devuelve máx. 10
  const reviews = p.reviews || [];
  const lastReview = reviews.map(r => r.publishTime).sort().pop();
  const daysSinceReview = lastReview ? Math.round((Date.now() - new Date(lastReview)) / 86400000) : null;
  const lowStars = reviews.filter(r => (r.rating ?? 5) <= 2).length;

  if (!p.websiteUri) f.push('sin web');
  if (!p.nationalPhoneNumber) f.push('sin teléfono');
  if (!p.regularOpeningHours) f.push('sin horario');
  if (n < 20) f.push(`pocas reseñas (${n})`);
  if (rating && rating < 4.2) f.push(`valoración baja (${rating})`);
  if (photos < 5) f.push(`pocas fotos (${photos} devueltas)`);
  if (!(p.types || []).length || (p.types || []).length < 2) f.push('sin categorías secundarias');
  if (daysSinceReview !== null && daysSinceReview > 180) f.push(`última reseña hace ${daysSinceReview} días`);
  if (lowStars >= 2) f.push(`${lowStars} de las 5 últimas reseñas con 1-2 estrellas`);
  if (p.businessStatus && p.businessStatus !== 'OPERATIONAL') f.push(`estado ${p.businessStatus}`);

  // Puntuación 0-100: cada fallo resta; pesos mayores a lo que más mueve el ranking local
  const weights = { 'sin web': 15, 'sin teléfono': 10, 'sin horario': 15, 'pocas reseñas': 20, 'valoración baja': 15, 'pocas fotos': 10, 'sin categorías': 5, 'última reseña': 10, 'estrellas': 10, 'estado': 20 };
  let score = 100;
  for (const fail of f) { const k = Object.keys(weights).find(w => fail.startsWith(w) || fail.includes(w)); score -= weights[k] || 5; }
  return { score: Math.max(0, score), fallos: f.join('; '), rating, n, photos, daysSinceReview };
}

const csvEsc = v => `"${String(v ?? '').replace(/"/g, '""')}"`;

(async () => {
  const placeIds = ids ? ids.split(',').map(s => s.trim()).filter(Boolean) : await textSearch(query, max);
  if (!placeIds.length) { console.error('Sin resultados'); process.exit(2); }
  const rows = [];
  for (const id of placeIds) {
    try {
      const p = await details(id);
      const a = audit(p);
      rows.push({
        nombre: p.displayName?.text, categoria: p.primaryType, direccion: p.formattedAddress,
        valoracion: a.rating, resenas: a.n, fotos: a.photos, web: p.websiteUri || '', telefono: p.nationalPhoneNumber || '',
        horario: p.regularOpeningHours ? 'sí' : 'no', dias_ultima_resena: a.daysSinceReview ?? '',
        puntuacion: a.score, fallos: a.fallos, maps: p.googleMapsUri,
      });
      console.error(`${a.score.toString().padStart(3)}  ${p.displayName?.text}  — ${a.fallos || 'sin fallos detectables por API'}`);
    } catch (e) { console.error('ERROR', id, e.message.slice(0, 200)); }
  }
  rows.sort((a, b) => a.puntuacion - b.puntuacion); // peores primero = mejores prospectos
  const header = Object.keys(rows[0]);
  fs.writeFileSync(out, [header.join(','), ...rows.map(r => header.map(h => csvEsc(r[h])).join(','))].join('\n'));
  console.error(`\n${rows.length} fichas auditadas → ${out} (ordenadas de peor a mejor).`);
  console.error('Recuerda: respuestas del propietario, posts y "ficha reclamada" NO salen en la API; revísalos a mano en las 5-10 peores.');
})();
