#!/usr/bin/env node
/**
 * Auditoría de fichas de Google Maps SIN clave de API, abriendo Maps con Chromium (Playwright).
 * Uso: node gbp_audit_browser.js "clínicas dentales Alcalá de Henares" [--max 20] [--out fichero.csv]
 * Lee lo que un humano vería en la ficha: nombre, categoría, valoración, nº reseñas, web, teléfono,
 * horario, nº fotos, descripción del propietario, "Reclamar esta empresa" (ficha sin reclamar),
 * nº de respuestas del propietario entre las reseñas visibles, y publicaciones ("Novedades").
 * Es más frágil que la API (Google cambia el HTML) y debe usarse para auditorías puntuales, no masivas.
 */
const { chromium } = require('playwright');
const fs = require('fs');
const args = process.argv.slice(2);
const opt = (n, d) => { const i = args.indexOf(n); return i >= 0 ? args[i + 1] : d; };
const query = args.filter((a, i) => !a.startsWith('--') && !['--max', '--out'].includes(args[i - 1]))[0];
const max = parseInt(opt('--max', '20'), 10);
const out = opt('--out', 'auditoria_gbp_browser.csv');
const sleep = ms => new Promise(r => setTimeout(r, ms));
const num = s => { const m = (s || '').replace(/\./g, '').match(/\d+/); return m ? parseInt(m[0], 10) : null; };

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', headless: true,
    proxy: process.env.HTTPS_PROXY ? { server: process.env.HTTPS_PROXY } : undefined });
  const ctx = await browser.newContext({ locale: 'es-ES', viewport: { width: 1400, height: 900 }, userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36' });
  const page = await ctx.newPage();
  await page.goto(`https://www.google.com/maps/search/${encodeURIComponent(query)}/?hl=es`, { waitUntil: 'domcontentloaded', timeout: 45000 });
  await sleep(4000);
  // Aceptar consentimiento si aparece
  for (const t of ['Aceptar todo', 'Accept all']) { const b = page.getByRole('button', { name: t }); if (await b.count()) { await b.first().click().catch(() => {}); await sleep(2000); break; } }
  // Scroll del panel de resultados para cargar hasta max
  const feed = page.locator('div[role="feed"]');
  let links = [];
  for (let i = 0; i < 12 && links.length < max; i++) {
    links = await page.$$eval('a[href*="/maps/place/"]', as => [...new Set(as.map(a => a.href))]);
    if (await feed.count()) await feed.evaluate(el => el.scrollBy(0, 2000)).catch(() => {});
    await sleep(1500);
  }
  // Extraer place_id (tras "19s") y navegar por place_id: carga más fiable que la URL larga
  links = [...new Set(links.map(h => (h.match(/19s(ChIJ[\w-]+)/) || [])[1]).filter(Boolean))].slice(0, max)
    .map(id => `https://www.google.com/maps/place/?q=place_id:${id}&hl=es`);
  console.error(`${links.length} fichas encontradas para "${query}"`);

  const rows = [];
  for (const url of links) {
    try {
      await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 }).catch(() => {});
      let name = '';
      for (let i = 0; i < 8 && !name; i++) { await sleep(2000); name = (await page.locator('h1').first().innerText().catch(() => '')).trim(); }
      // esperar a que carguen valoración (N) y pestañas; Google a veces tarda o no las pinta
      for (let i = 0; i < 6; i++) { const t = (await page.innerText('body')).replace(/\s+/g, ' '); if (/\d,\d\s*\(\d/.test(t) || /Reseñas/.test(t)) break; await sleep(2000); }
      await sleep(1000);
      const text = (await page.innerText('body')).replace(/\s+/g, ' ');
      const head = text.slice(text.indexOf(name) + name.length, text.indexOf(name) + name.length + 80);
      const headM = head.match(/(\d,\d)\s*\((\d[\d.]*)\)/);
      const ratingAria = await page.locator('[role="img"][aria-label*="estrellas"]').first().getAttribute('aria-label').catch(() => null);
      const rating = headM ? parseFloat(headM[1].replace(',', '.')) : (ratingAria ? parseFloat(ratingAria.replace(',', '.').match(/[\d.]+/)[0]) : null);
      const reviewsBtn = await page.locator('button[aria-label*="reseñas"], button[aria-label*="reseña"]').first().getAttribute('aria-label').catch(() => null);
      const reviews = headM ? num(headM[2]) : num(reviewsBtn);
      const category = (await page.locator('button[jsaction*="category"]').first().innerText().catch(() => '')).trim();
      const website = await page.locator('a[data-item-id="authority"]').count() > 0;
      const phone = await page.locator('button[data-item-id^="phone"]').count() > 0;
      const hours = /Abierto|Cierra|Cerrado|Abre/.test(text);
      const photosM = text.match(/(\d[\d.]*)\s+fotos?/i); const photos = photosM ? num(photosM[1]) : null;
      const unclaimed = /Reclamar esta empresa|¿Eres el propietario de esta empresa\?/i.test(text);
      const hasDescription = await page.locator('div[data-attrid="description"], div.PYvSYb').count() > 0 || /Del propietario|De la empresa/.test(text);
      const posts = /Novedades|Actualizaciones del propietario/i.test(text);
      const products = /Productos|Servicios/.test(text);
      // Pestaña de reseñas: contar respuestas del propietario entre las visibles
      let ownerReplies = null, visibleReviews = null;
      const tab = page.getByRole('tab', { name: /Reseñas/ });
      if (await tab.count()) {
        await tab.first().click().catch(() => {}); await sleep(2500);
        for (let i = 0; i < 3; i++) { await page.mouse.wheel(0, 3000); await sleep(1200); }
        const rt = (await page.innerText('body')).replace(/\s+/g, ' ');
        ownerReplies = (rt.match(/Respuesta del propietario/g) || []).length;
        visibleReviews = await page.locator('div[data-review-id]').count();
      }
      const fails = [];
      if (unclaimed) fails.push('ficha SIN RECLAMAR');
      if (!website) fails.push('sin web');
      if (!phone) fails.push('sin teléfono');
      if (!hours) fails.push('sin horario');
      if (reviews !== null && reviews < 20) fails.push(`pocas reseñas (${reviews})`);
      if (rating !== null && rating < 4.2) fails.push(`valoración baja (${rating})`);
      if (photos !== null && photos < 10) fails.push(`pocas fotos (${photos})`);
      if (!hasDescription) fails.push('sin descripción');
      if (!posts) fails.push('sin publicaciones');
      if (visibleReviews && ownerReplies !== null && ownerReplies / visibleReviews < 0.3) fails.push(`responde ${ownerReplies}/${visibleReviews} reseñas`);
      const weights = { 'SIN RECLAMAR': 30, 'sin web': 10, 'sin teléfono': 10, 'sin horario': 10, 'pocas reseñas': 15, 'valoración baja': 15, 'pocas fotos': 10, 'sin descripción': 5, 'sin publicaciones': 5, 'responde': 10 };
      let score = 100; for (const f of fails) { const k = Object.keys(weights).find(w => f.includes(w)); score -= weights[k] || 5; }
      const row = { nombre: name, categoria: category, valoracion: rating, resenas: reviews, fotos: photos, web: website ? 'sí' : 'no', telefono: phone ? 'sí' : 'no', horario: hours ? 'sí' : 'no', reclamada: unclaimed ? 'NO' : 'sí', descripcion: hasDescription ? 'sí' : 'no', publicaciones: posts ? 'sí' : 'no', respuestas_propietario: ownerReplies === null ? '' : `${ownerReplies}/${visibleReviews}`, puntuacion: Math.max(0, score), fallos: fails.join('; '), url };
      rows.push(row);
      console.error(`${String(row.puntuacion).padStart(3)}  ${name}  ${rating}★ ${reviews} reseñas — ${fails.join('; ') || 'ok'}`);
    } catch (e) { console.error('ERROR', url.slice(0, 80), e.message.split('\n')[0]); }
  }
  await browser.close();
  rows.sort((a, b) => a.puntuacion - b.puntuacion);
  const h = Object.keys(rows[0] || {});
  fs.writeFileSync(out, [h.join(','), ...rows.map(r => h.map(k => `"${String(r[k] ?? '').replace(/"/g, '""')}"`).join(','))].join('\n'));
  console.error(`\n${rows.length} fichas → ${out}`);
})();
