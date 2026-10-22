# Auditoría de fichas de Google Business Profile

Script: `gbp_audit.js` (Node 18+, sin dependencias). Usa la Places API (New) de Google, que es la vía oficial.

## Preparación (10 minutos)
1. Google Cloud Console → proyecto nuevo → "APIs y servicios" → habilitar **Places API (New)**.
2. Credenciales → crear clave de API → restringir a Places API (New).
3. Facturación activada (Google exige tarjeta, pero la cuota gratuita mensual cubre de sobra 20-50 fichas; comprueba el precio vigente de Text Search y Place Details en la tabla de precios de Google Maps Platform antes de lanzar cientos).

## Uso
```
set GOOGLE_MAPS_API_KEY=TU_CLAVE          (Windows cmd)   |   export GOOGLE_MAPS_API_KEY=TU_CLAVE (bash)
node gbp_audit.js "clínicas dentales en Alcalá de Henares" --max 20 --out dentistas_alcala.csv
node gbp_audit.js "talleres mecánicos en Guadalajara" --max 20
node gbp_audit.js --ids ChIJxxxx,ChIJyyyy
```
Salida: CSV ordenado de peor a mejor ficha, con puntuación 0-100 y lista de fallos.

## Qué comprueba y qué no
Comprueba: web, teléfono, horario, nº de reseñas, valoración, nº de fotos (la API devuelve máx. 10), categorías secundarias, antigüedad de la última reseña, reseñas recientes de 1-2 estrellas, estado del negocio.
No puede comprobar (Google no lo expone): respuestas del propietario, publicaciones, productos/servicios, preguntas y respuestas, si la ficha está reclamada. Revísalo a mano en las 5-10 peores antes de contactar.

## Para qué sirve en la prueba
1. Auditar 20 fichas de un sector y ciudad.
2. Enviar a 20 agencias de SEO local un ejemplo real de auditoría (sin nombre del negocio) con una oferta de marca blanca por ficha/mes.
3. Medir respuestas. Si ninguna agencia responde a una auditoría concreta y gratuita, el canal está muerto igual que el de ISO.
