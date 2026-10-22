# Prompt para la sesión local (Chrome) — Ranking de tendencias de consumo con hambre de compra

Copia desde la línea "=== PROMPT ===" hasta el final y pégalo en una sesión local de Claude Code con acceso a Chrome (extensión Claude in Chrome o navegador integrado) y sesión iniciada en Google Ads.

Por qué en local: desde la nube, Google Trends devuelve error 429 en todas las aperturas y Keyword Planner exige una cuenta de Google Ads con sesión iniciada. En local ya funcionó el 20 de octubre para el informe de 20 candidatos.

=== PROMPT ===

Eres un analista de mercado. Objetivo: medir, con datos de tendencia abiertos en el navegador, qué nichos de consumo tienen más hambre de compra AHORA (octubre 2026), sin filtrar por mi perfil ni por país. Nada de opiniones: solo números leídos en pantalla, con URL y fecha. Si un dato no se puede leer, escribe "NO LEÍDO" y por qué. No inventes nada.

## Candidatos (22). Añade hasta 5 más si al abrir Trends o TikTok aparecen nichos relacionados con crecimiento mayor.

| # | Nicho | Términos semilla ES | Términos semilla EN |
|---|---|---|---|
| 1 | Nutrición y planes para menopausia/perimenopausia | dieta menopausia, perimenopausia síntomas, suplementos menopausia | menopause diet, perimenopause supplements, menopause weight loss |
| 2 | TDAH adulto (test, coaching, organización) | tdah adultos test, coach tdah, tdah mujeres | adhd test adults, adhd coach, adhd planner |
| 3 | Cuentos personalizados para niños (IA, libro impreso) | cuento personalizado niño, libro personalizado bebé | personalized children's book, custom bedtime story app |
| 4 | GLP-1: nutrición, pérdida muscular, mantenimiento tras dejarlo | ozempic dieta, mounjaro efectos, dejar ozempic | glp-1 diet plan, ozempic muscle loss, after ozempic |
| 5 | Testosterona y salud masculina 40+ | testosterona baja síntomas, trt españa | low testosterone, trt clinic online |
| 6 | Longevidad: análisis de sangre y biomarcadores | analítica completa precio, biomarcadores longevidad | longevity blood test, biological age test |
| 7 | Sueño: insomnio, apnea, mouth taping | insomnio remedios, apnea sueño test | sleep apnea test at home, mouth taping |
| 8 | Fuerza y entrenamiento mujeres 40+ | entrenamiento fuerza mujeres 40, pilates reformer | strength training women over 40, reformer pilates |
| 9 | Pickleball y pádel (material, clases, reservas) | padel clases, pala padel | pickleball paddle, pickleball lessons |
| 10 | Mascotas: comida fresca, seguro, cuidadores, ansiedad | comida fresca perro, seguro mascota | fresh dog food, pet insurance, dog separation anxiety |
| 11 | K-beauty y skincare coreano | cosmética coreana, protector solar coreano | korean skincare routine, korean sunscreen |
| 12 | Cuidado de padres mayores (coordinación, teleasistencia) | cuidador personas mayores, teleasistencia precio | elder care coordinator, aging parents help |
| 13 | Fertilidad y congelación de óvulos | congelar óvulos precio, fertilidad 35 | egg freezing cost, fertility test at home |
| 14 | Aprender IA para trabajar (cursos, prompts) | curso ia, aprender chatgpt trabajo | ai course for beginners, learn ai skills |
| 15 | Coleccionables TCG (Pokémon, Magic, cartas deportivas) | cartas pokemon precio, graduar cartas psa | pokemon cards price, psa grading |
| 16 | Casa fresca: aire portátil, ventiladores, aislamiento | aire acondicionado portátil, pingüino | portable air conditioner, heat pump cooling |
| 17 | Viajes: Camino de Santiago, Japón, viaje solo mujeres | camino de santiago etapas, viaje japón presupuesto | camino de santiago planner, japan trip budget, solo female travel |
| 18 | Finanzas personales: ahorro, inversión indexada, deuda | fondos indexados, presupuesto familiar app | budgeting app, index funds beginner |
| 19 | Ansiedad y terapia online | psicólogo online precio, ansiedad síntomas | online therapy cost, anxiety help |
| 20 | Oposiciones y exámenes (preparación online) | oposiciones 2026, test oposiciones app | exam prep app, civil service exam |
| 21 | Reacondicionados y segunda mano premium | iphone reacondicionado, ropa segunda mano | refurbished iphone, secondhand luxury |
| 22 | Bodas y eventos (planificación, DIY) | organizar boda, wedding planner precio | wedding planning checklist, wedding budget |

## Qué medir para cada candidato (todo leído en pantalla, no de memoria)

1. **Google Trends** (trends.google.com), mundial y España, 12 meses y 5 años, categoría "Todas":
   - Valor medio últimos 90 días vs mismos 90 días hace un año (crecimiento interanual en %).
   - Pendiente de 5 años: creciente / plana / decreciente.
   - Las 5 "consultas relacionadas en aumento" con su porcentaje o "Breakout".
   - Top 5 países.
2. **Google Ads Keyword Planner** (ads.google.com → Herramientas → Planificador de palabras clave → "Consulta el volumen de búsquedas y las previsiones"), España y EE. UU. por separado:
   - Volumen mensual medio de los 3 términos semilla.
   - Cambio interanual (%) y de 3 meses (%).
   - Puja parte superior (rango bajo y alto). La puja alta es la medida de cuánto están dispuestos a pagar los anunciantes por ese cliente.
   - Competencia (baja/media/alta).
3. **TikTok Creative Center** (ads.tiktok.com/business/creativecenter → Trends → Hashtags), región ES y US, 30 y 120 días: visualizaciones del hashtag principal y crecimiento %.
4. **Reddit**: tamaño del subreddit principal y posts en la última semana (abre old.reddit.com/r/<sub>/new).
5. **App Store / Google Play**: para los nichos con app, los 3 primeros resultados de la búsqueda del término, su número de valoraciones y precio de suscripción (abre la ficha).
6. **Señal de pago**: ¿qué venden los 3 primeros anuncios de Google al buscar el término principal? Anota producto y precio visible. Si no hay anuncios, anótalo: es señal de que nadie paga por ese cliente.

## Puntuación (0-3 cada eje, máximo 12)
- **Tendencia**: 0 cae, 1 plana, 2 crece 10-50% interanual, 3 crece >50% o Breakout.
- **Volumen**: 0 <1.000/mes en ambos países, 1 1-10K, 2 10-100K, 3 >100K.
- **Dinero**: 0 sin anuncios y puja <0,2 €, 1 puja 0,2-1 €, 2 puja 1-3 €, 3 puja >3 € o productos >100 € en anuncios.
- **Hueco**: 0 top 3 apps con >100K valoraciones y 3 anuncios de marcas grandes, 1 líderes claros, 2 líderes medianos, 3 sin líder claro o solo productos genéricos.

## Entregable
Guarda un fichero Markdown llamado `tendencias_consumo_2026_local.md` con:
1. Tabla de los 22+ candidatos con todas las métricas, fecha de lectura y URL.
2. Ranking por puntuación total.
3. Para el top 5: las 5 consultas en aumento, los 3 anuncios y los precios vistos.
4. Lista de lo que no se pudo leer y por qué.
Después pega aquí el fichero completo. No resumas: quiero los números crudos.

Reglas: no uses datos de memoria, solo lo que leas en pantalla hoy. Si Trends limita las consultas, espera 60 segundos y sigue; si Keyword Planner pide crear campaña, usa el modo "solo previsiones" sin publicar nada. No gastes dinero ni publiques campañas.

=== FIN DEL PROMPT ===
