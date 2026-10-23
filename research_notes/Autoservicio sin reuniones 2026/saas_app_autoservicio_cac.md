# Micro-SaaS y apps de autoservicio B2B/prosumer: CAC frente a LTV (investigación adversarial)

Fecha: 23 oct 2026. Fila: micro-SaaS y apps vendidos sin ventas humanas, con distribución prestada (marketplaces) y utilidades de cálculo/documentación para ingeniería y pymes. Idioma: español. Moneda: la de la fuente (USD salvo que se indique €/£).

Marcas: [ABIERTA] = página abierta y leída con pwfetch/curl/API; [FRAGMENTO] = dato visto solo en un resumen de buscador o en un fragmento de página, no en la página original; NO ENCONTRADO = se buscó y no hay dato. Nunca se inventa una cifra; donde no hay dato se escribe "sin dato".

Convenciones: CAC = coste de adquirir un cliente de pago; LTV = precio mensual / churn mensual (bruto, sin descontar comisiones ni margen); payback = CAC / precio mensual.

---

## 0. Veredictos H1-H7

| Hipótesis | Veredicto | Resumen de la evidencia |
|---|---|---|
| H1. CAC de pago en SaaS pyme <50 €/mes está entre 200 y 700 € e inviable sin orgánico | **CORREGIDA** | Único benchmark primario abierto con CAC de pago para B2B SaaS: First Page Sage (ene 2026, clientes 2022-2025, EE. UU.): inorgánico 341 $, orgánico 205 $, combinado 239 $; vertical "Engineering SaaS" 551 $, "Legaltech" 299 $, "eCommerce SaaS" 274 $. Fuente secundaria (wearefounders.uk, feb 2026): CAC medio B2B SaaS 1.200 $ todos los canales, CPA pagado medio 802 $, eCommerce SMB 200-300 $. El cálculo por embudo (H2) da 240-1.500 € en los escenarios centrales y hasta 6.000 € en el pesimista: la banda 200-700 es demasiado estrecha. La conclusión "inviable solo con ads" se sostiene en el caso base (LTV/CAC 0,4-1,2 con precio 20-35 €) y falla solo si se exige tarjeta en el trial (t→p 25 %) y el CPC es ≤3 €. ChartMogul, OpenView/High Alpha, KeyBanc, Paddle/ProfitWell: las URL de informes dieron 404 o no publican CAC por tramo de precio (ver §7). |
| H2. CPC España keywords software 1,5-6 €; visita→trial 2-5 %; trial→pago 10-25 % | **CORREGIDA** | CPC: ningún dato público por keyword para España 2025-2026 fuera de muros de pago (Statista/Semrush dic 2024 oculta las cifras). Datos reales del Planificador de Google Ads (cuenta de Jorge, 4 oct 2026, ya en el repo): pujas rango alto ES 2,34 € (iso 9001), 2,65 € (claude code), 4,99 € (bloque verifactu/controles), 5,56 € (google business profile), 11,26 € (iso 27001), 15,59 € (cyber resilience act). Europa tecnología/software 2,30-4,50 € (codedesign.org, 2025, sin muestra). EE. UU. 2026: media todas las industrias 5,42 $, Business Services 5,87 $, Industrial & Commercial 5,87 $ (LocaliQ/WordStream). La banda 1,5-6 € es plausible para "software gestión/facturación" pero sube a 11-16 € en nichos regulatorios. Conversión: visita→registro 5 % (trial) y 9 % (freemium) (OpenView/Lenny 2023, 1.000+ productos) → el 2-5 % es conservador-correcto. Trial→pago: mediana 8 % y bimodal (ChartMogul/Growth Unhinged/ProductLed, ene 2026, 200 productos); trial sin tarjeta 4-6 % (p50) y 10-15 % (p75); con tarjeta 25-35 % (p50); freemium 3-5 %. El 10-25 % de la hipótesis es el cuartil superior sin tarjeta o la mediana con tarjeta, no la mediana general. Cálculo CAC = CPC / (v→t × t→p) en §2 y §5. |
| H3. Churn mensual micro-SaaS pyme 3-8 %; LTV 250-1.600 € con 20-50 €/mes | **CONFIRMADA** (con matiz) | Recurly vía Paddle: churn mensual medio SaaS 4,8 %, cuartiles 2,9 % y 8,5 %; con ARPU <100 $/mes churn bruto de ingresos 3-16 %, mediana 6-9 %. ChartMogul (nov 2023): el cuartil superior con ARPA <50 $/mes retiene solo 60-70 % bruto anual (≈3-4 % mensual); solo 5,3 % de los negocios con ARPA <10 $ superan 85 % de retención bruta. Vena 2025: SMB 3-7 % mensual. LTV = precio/churn: 20 €/8 % = 250 €; 50 €/3 % = 1.667 €. Matiz: 3 % mensual es cuartil superior, no mediana; la mediana realista para 20-50 €/mes es 5-8 % → LTV 250-1.000 €. |
| H4. La distribución prestada baja el CAC a casi 0 | **CORREGIDA** | El coste monetario por instalación es ~0, pero la distribución efectiva es escasa y está concentrada: Shopify App Store jun 2026: 22.546 apps, 51 % sin ninguna reseña, 81 % con <10, top 1 % (225 apps) ≈72 % de ingresos (estimado), solo ≈36 % parece ingresar algo, precio de entrada mediano 9,99 $; 584-1.588 apps nuevas al mes según tracker. Comisión: 0 % hasta 1 M$ acumulado, luego 15 %. Atlassian: 8.000+ apps, 1.800+ partners, 4.000 M$ ventas acumuladas (ene 2024); comisión Connect 15 %→20 % en 2026 [FRAGMENTO]. Chrome: ExtensionPay declara 800.000 $ pagados en total a todos sus desarrolladores desde 2021 (sitio, oct 2026); casos en r/chrome_extensions 2026: 209 $ MRR tras 1 año, 135 € MRR con 3 extensiones, 100 $ MRR tras 8 meses de app Shopify con 106 instalaciones. WordPress.org: 76.000+ plugins gratuitos; Freemius: conversión freemium habitual 2-5 %, feature-gated típico 2,1 %; informe de datos Freemius 2024-2026: NO ENCONTRADO. El CAC pasa de dinero a tiempo (reseñas, soporte, listado) y el reparto es ganador-se-lleva-casi-todo. |
| H5. Existen micro-SaaS de ingeniería/técnicos en autoservicio con éxito hechos por una persona | **CORREGIDA / parcialmente SIN DATOS** | Existen productos técnicos en autoservicio con suscripción por tarjeta: Steel Beam Calculator (UK, 40-50 £/mes, desde 2011, 2 socios), WebStructural (Pro 29 $/mes), ClearCalcs (79-149 $/mes, "3.000+ ingenieros al mes"), SkyCiv (desde 69 $/mes según Capterra), BeamGuru (4,99 $ por 2 cálculos; 39 $/año), calcresource (gratis con anuncios, un solo autor), Omni Calculator (3.938 calculadoras gratis, empresa polaca), Wonder.Legal ES (490 modelos, 4,2 M usuarios declarados). Ningún caso verificado de fundador solo con ingresos públicos en ingeniería; el más cercano es un equipo de 2 (Steel Beam Calculator) y un autor único sin suscripción (calcresource). Tráfico Similarweb: bloqueado (403), sin dato. |
| H6. Tiempo a 1.000 $ y 5.000 $ MRR para solos con orgánico/marketplace: mediana >12 meses | **CORREGIDA / SIN DATOS 2024-2026** | No hay encuesta 2024-2026 con "meses hasta 1k MRR". Dato más cercano: análisis Indie Hackers 2022 con ingresos verificados por Stripe: media ≈9 meses, mediana ≈8, cuartiles 5 y 12 [FRAGMENTO, IH bloqueado]. Lo que sí hay (TrustMRR, sep 2026, 10.150 productos, ingresos verificados): 26,1 % nunca cobró nada; 49,1 % cobró algo en los últimos 30 días; mediana de los que cobraron 169 $; 2,4 % ≥ 8.333 $ MRR; categorías "Productivity" y "Utilities" (894 productos) tienen solo 5 por encima de 5.000 $ MRR. MicroConf 2024 (≈700 respuestas): 17,7 % de los fundadores bajo 1.000 $ MRR (mayor grupo), 50,7 % solos. Conclusión: la mediana del producto no llega nunca a 1k; entre los que llegan, el único dato (2022) dice ~8 meses. A 5k MRR: sin dato de tiempo; solo el 3,7-4,2 % de "SaaS" en TrustMRR supera 5k. |
| H7. La IA generativa hunde precios y multiplica competidores en 2025-2026 | **CONFIRMADA en oferta; SIN DATOS en precios** | Product Hunt (hunted.space, 23 oct 2026): 597.723 lanzamientos acumulados; 18.385 en los últimos 30 días; día récord 20 oct 2026 con 1.382; julio 2026 21.487 (antes de feb 2024: 800-1.600/mes). Product Hunt propio: 2.345 lanzamientos Q2 2026 vs 1.508 Q2 2025 [FRAGMENTO vía blog.mean.ceo]. Shopify: 584 apps nuevas/mes (AppJubilee, may 2026) a 1.588 en 30 días (+81 % interanual, tracker citado por Taylor Sicard, 2026); RevenueHunt: "lo que era un build de 6 meses ahora es un fin de semana". Reddit oct 2026: dueño de 2 extensiones Chrome ve copias "vibe-coded" a precios muy bajos y fuga de clientes nuevos; hilo r/microsaas mar 2026 "15 alternativas gratis hacen lo mismo"; contrapunto con 320 votos: "vibe coding no está matando al SaaS" (coste real está en mantener, soporte, seguridad). Caídas de precio medidas: NO ENCONTRADO (solo anécdotas). |

---

## 1. Benchmarks CAC / churn / conversión

| Métrica | Valor | Segmento | Fuente, fecha, muestra | Estado |
|---|---|---|---|---|
| CAC inorgánico (PPC/paid social) | 341 $ | B2B SaaS | First Page Sage, "Average CAC by Industry: B2B", 26 ene 2026; clientes propios ene 2022-ago 2025; sesgo: agencia SEO, inorgánico = sobre todo PPC. https://firstpagesage.com/reports/average-customer-acquisition-cost-cac-by-industry-b2b-edition/ | [ABIERTA] |
| CAC orgánico (SEO/social orgánico) | 205 $ | B2B SaaS | ídem | [ABIERTA] |
| CAC combinado | 239 $ (75 % orgánico / 25 % inorgánico) | B2B SaaS | ídem | [ABIERTA] |
| CAC por vertical SaaS | Engineering 551 $; Industrial 542 $; Construction 610 $; Legaltech 299 $; eCommerce 274 $; Building Mgmt & IoT 574 $ | SaaS por industria | ídem (22 industrias SaaS) | [ABIERTA] |
| CAC medio B2B SaaS, todos los canales | 1.200 $; CPA pagado medio 802 $; eCommerce SMB 200-300 $ | B2B SaaS | wearefounders.uk, "SaaS Churn Rates and CAC by Industry", actualizado feb 2026; agregador secundario sin muestra propia. https://www.wearefounders.uk/saas-churn-rates-and-customer-acquisition-costs-by-industry-2025-data/ | [ABIERTA] (secundaria) |
| Churn mensual medio SaaS | 4,8 % (cuartiles 2,9 % / 8,5 %) | SaaS general | Recurly Research citado por Paddle, "SaaS churn rate" (sin fecha en página; datos Recurly 2018-2023). https://www.paddle.com/blog/saas-churn-rate | [ABIERTA] |
| Churn bruto mensual de ingresos con ARPU <100 $/mes | 3-16 %, mediana 6-9 % | SaaS barato | ídem (Paddle) | [ABIERTA] |
| Retención bruta anual cuartil superior, ARPA <50 $/mes | 60-70 % (≈3-4 % mensual) | SaaS prosumer/pyme | ChartMogul, SaaS Retention Report, 1 nov 2023 (base de clientes ChartMogul). https://chartmogul.com/reports/saas-retention-report/ | [ABIERTA] |
| % negocios con ARPA <10 $/mes con GRR >85 % | 5,3 % (vs 35,7 % con ARPA >500 $) | ídem | ídem | [ABIERTA] |
| Churn mensual SMB SaaS | 3-7 % (30-58 % anual) | SMB | Vena Solutions, 19 sep 2025, tabla sin muestra propia. https://www.venasolutions.com/blog/saas-churn-rate | [ABIERTA] (secundaria) |
| Churn mensual B2B medio | 3,5 % (≈35 % anual) | B2B | wearefounders.uk (ídem arriba) | [ABIERTA] (secundaria) |
| Churn anual por segmento | Small business 7,5 %; mid-market 5,2 %; enterprise 3,8 % | por tamaño | UserJot blog, 24 nov 2025, sin muestra. https://userjot.com/blog/saas-churn-rate-benchmarks | [ABIERTA] (secundaria, cifras anuales incompatibles con las mensuales de arriba) |
| Anécdota churn vs precio | 19 $/mes: churn 31 %/mes, 180 tickets/mes, 84 clientes; 99 $/mes: churn 8 %, 52 tickets. Afirma "B2B <25 $/mes churn anual medio 34 %" | B2B micro | r/microsaas, 7 feb 2026, 12 votos, sin verificación. https://reddit.com/r/microsaas/comments/1qy8bkt/charging_19month_killed_my_b2b_saas/ | [ABIERTA] (anécdota) |
| Visita→registro | 5 % (free trial) / 9 % (freemium) | B2B SaaS | OpenView + Lenny + Pendo, 1 ago 2023, 1.000+ productos. https://www.lennysnewsletter.com/p/what-is-a-good-free-to-paid-conversion | [ABIERTA] |
| Free→paid freemium self-serve | bueno 3-5 %, excelente 6-8 %; 20 % de productos <2,5 % | B2B SaaS | ídem | [ABIERTA] |
| Trial→paid | bueno 8-12 %, excelente 15-25 %; 24 % de productos en 7,5-10 % | B2B SaaS | ídem | [ABIERTA] |
| Trial→paid mediana 2026 | 8 %, bimodal: 20 % <2,5 %, 23 % >25 % | B2B software | Kyle Poyar + ProductLed + ChartMogul, ene 2026, 200 productos; citado íntegro en Userpilot (19 ago 2026). https://userpilot.com/blog/free-trial-conversion-rate/ | [ABIERTA] (vía Userpilot) |
| Trial→paid por modelo (p50 / p75) | Freemium 3-5 % / 8-12 %; trial sin tarjeta 4-6 % / 10-15 %; reverse trial 4-6 % / 8-12 %; trial con tarjeta 25-35 % / 50-60 %; B2B 6-10 % / 15-20 % | B2B | ídem (ChartMogul 2026) | [ABIERTA] (vía Userpilot) |
| Trial→paid orgánico | 18,2 % opt-in; 48,8 % opt-out (tarjeta) | B2B SaaS | First Page Sage, 50+ clientes propios (citado por Userpilot) | [FRAGMENTO] |
| Free→paid freemium WordPress | "norma 2-5 %"; feature-gated 2,1 %; caso trial ilimitado >15 % | plugins/temas WP | Freemius blog, "Freemium pricing strategy", 23 jul 2026. https://freemius.com/blog/increase-freemium-upgrades-wordpress-plugin-theme/ | [ABIERTA] |
| Conversión web Google Ads 2026 (lead, no trial) | 8,18 % media; Business Services 6,10 %; Industrial 6,57 % | todas las industrias EE. UU. | LocaliQ/WordStream, "Search Advertising Benchmarks 2026", miles de cuentas. https://localiq.com/blog/search-advertising-benchmarks/ | [ABIERTA] |
| Coste por lead 2026 | Business Services 93,69 $; Industrial & Commercial 75,19 $ | ídem | ídem | [ABIERTA] |
| Fundadores bajo 1.000 $ MRR | 17,7 % (grupo mayor); 50,7 % fundadores solos; ~700 respuestas | SaaS bootstrapped | MicroConf State of Independent SaaS 2024 (página y podcast ep. 721). https://microconf.com/saas-this-year ; https://www.startupsfortherestofus.com/episodes/episode-721-7-key-takeaways-from-the-2024-state-of-independent-saas-report | [FRAGMENTO] (cifras del resumen de buscador; el PDF requiere formulario) |
| Tarjeta en el trial | 71 % la piden (2024) vs 73 % (2020) y 78 %; no pedirla = 2× LTV pero menor crecimiento mensual | ídem | podcast ep. 721 (Rob Walling y Asia Orangio) | [ABIERTA] |
| Crecimiento mensual medio fundador solo | ≈17 % (media), tríos 2-3× más | ídem | ídem | [ABIERTA] |

No abiertos/sin dato: ChartMogul SaaS Benchmarks (404), OpenView 2023 (404), High Alpha 2024/2025 (404), KeyBanc 2024 (no abierto), Paddle/ProfitWell churn 2025 (404 en /resources; blog abierto arriba), Baremetrics Open Startups (abierta pero sin tabla pública de CAC; solo portada). Freemius "informe de datos 2024-2026": NO ENCONTRADO.

---

## 2. CPC de keywords de software en España

| Keyword / bloque | CPC o puja (moneda) | Geografía, fecha | Fuente | Estado |
|---|---|---|---|---|
| iso 9001 (3 términos) | 2,34 € puja rango alto | España, Planificador Google Ads, 4 oct 2026 | research_notes/Dolores en crecimiento con pruebas/search_volume_planner_trends.md (dato real de la cuenta de Jorge) | [ABIERTA] (repo) |
| claude code (3 términos) | 2,65 € | ídem | ídem | [ABIERTA] (repo) |
| verifactu / controles (3 términos) | 4,99 € | ídem | ídem | [ABIERTA] (repo) |
| google business profile (4 términos) | 5,56 € | ídem | ídem | [ABIERTA] (repo) |
| iso 27001 | 11,26 € | ídem | ídem | [ABIERTA] (repo) |
| cyber resilience act | 15,59 € | ídem | ídem | [ABIERTA] (repo) |
| "software gestión", "programa facturación autónomos", "generador de contratos", "calculadora X" | sin dato público 2025-2026 | España | Statista/Semrush "CPC by industry in Spain, Dec 2024" existe pero las cifras están tras muro de pago (banca online la más cara, belleza la más barata). https://www.statista.com/statistics/1243710/spain-search-advertising-cpc ; Semrush ES "¿Cuánto cuestan los anuncios de Google?" (2024) no da cifras por keyword ES. Ubersuggest y Ahrefs free tools exigen login/captcha. | NO ENCONTRADO |
| Tecnología/Software, mercados europeos | 2,30-4,50 € | Europa, guía 2025 | codedesign.org (agencia PT, sin muestra). https://codedesign.org/google-ads-cost-europe-your-complete-guide/ | [ABIERTA] (secundaria) |
| Media todas las industrias, búsqueda | 5,42 $ | EE. UU. 2026 | LocaliQ/WordStream 2026 | [ABIERTA] |
| Business Services / Industrial & Commercial | 5,87 $ / 5,87 $ | EE. UU. 2026 | ídem | [ABIERTA] |
| Attorneys & Legal Services | 9,87 $ | EE. UU. 2026 | ídem | [ABIERTA] |
| B2B SaaS search ads | 6-9 $ (2024) | EE. UU. | citado por buscador (Rockingweb) | [FRAGMENTO] |

Lectura: para España, software de gestión/facturación genérico cabe en 1,5-6 € (coherente con 2,3-5,6 € observados en bloques comparables), pero cualquier nicho regulatorio o de seguridad (ISO 27001, CRA) está en 11-16 €. Pide a Jorge sacar del Planificador las keywords exactas ("programa facturación autónomos", "software gestión pyme", "generador de contratos", "calculadora sección cable", "cálculo instalación eléctrica") antes de presupuestar.

### Cálculo CAC = CPC / (visita→trial × trial→pago)

| CPC (€) | visita→trial | trial→pago | CAC (€) |
|---|---|---|---|
| 1,5 | 2 % | 5 % | 1.500 |
| 1,5 | 2 % | 10 % | 750 |
| 1,5 | 2 % | 25 % | 300 |
| 1,5 | 5 % | 5 % | 600 |
| 1,5 | 5 % | 10 % | 300 |
| 1,5 | 5 % | 25 % | 120 |
| 3,0 | 2 % | 5 % | 3.000 |
| 3,0 | 2 % | 10 % | 1.500 |
| 3,0 | 2 % | 25 % | 600 |
| 3,0 | 5 % | 5 % | 1.200 |
| 3,0 | 5 % | 10 % | 600 |
| 3,0 | 5 % | 25 % | 240 |
| 4,5 | 2 % | 5 % | 4.500 |
| 4,5 | 2 % | 10 % | 2.250 |
| 4,5 | 2 % | 25 % | 900 |
| 4,5 | 5 % | 5 % | 1.800 |
| 4,5 | 5 % | 10 % | 900 |
| 4,5 | 5 % | 25 % | 360 |
| 6,0 | 2 % | 5 % | 6.000 |
| 6,0 | 2 % | 10 % | 3.000 |
| 6,0 | 2 % | 25 % | 1.200 |
| 6,0 | 5 % | 5 % | 2.400 |
| 6,0 | 5 % | 10 % | 1.200 |
| 6,0 | 5 % | 25 % | 480 |

Ejemplo explícito: CPC 3 € → 1.000 € compran 333 clics → 5 % inician trial = 16,7 trials → 10 % pagan = 1,67 clientes → CAC = 1.000 / 1,67 = 600 €. Con tarjeta obligatoria en el trial (25 %): 4,2 clientes → CAC 240 €, pero los registros caen (OpenView: 5 % vs 9 %).

---

## 3. Distribución prestada (marketplaces)

| Marketplace | Nº apps | Ingresos mediana / concentración | Conversión free→paid | Comisión | Fuentes y estado |
|---|---|---|---|---|---|
| Shopify App Store | 22.546 apps vivas (jun 2026, RevenueHunt); 17.891 apps / 11.352 partners (may 2026, AppJubilee); 12.320 apps / 7.874 partners con app (ene 2025, Meetanshi); "más de 16.000" (Shopify, abr 2025); 25.000+ y 1.588 nuevas en 30 días, +81 % interanual (tracker citado por Taylor Sicard, 2026) | Top 1 % (225 apps) ≈72 % de ingresos; top 10 ≈30 %; solo ≈36 % de apps parecen ingresar algo; 51 % sin reseñas, 81 % <10, mediana 5 reseñas entre las que tienen alguna (todo estimado desde listados, no facturación). Shopify pagó >1.000 M$ a devs en 2024. Plan medio 66,54 $/mes (Meetanshi 2025); precio de entrada mediano y más común 9,99 $ (RevenueHunt 2026). Reddit 2026: 100 $ MRR a 8 meses (106 instalaciones, 14 suscriptores, hecho con Claude); 4.000 $ MRR a 12 meses (ARPU 60 $, India); portfolio en venta a 310 $ MRR; app de 2018 con 500+ instalaciones y 50 k$ acumulados perdiendo instalaciones (jun 2026) | sin dato agregado; 46,9 % de apps gratis, 48,6 % con trial, 4,5 % cobran de entrada; 57 % de las de pago tienen plan gratis | 0 % hasta 1 M$ acumulado desde 1 ene 2025, 15 % por encima (antes el 1 M$ se reseteaba cada año) | https://revenuehunt.com/state-of-the-shopify-app-economy/ [ABIERTA]; https://www.appjubilee.io/shopify-app-store-report-2026 [ABIERTA]; https://meetanshi.com/blog/shopify-app-store-statistics/ [ABIERTA]; https://shopify.dev/changelog/update-to-shopifys-app-developer-revenue-share [ABIERTA]; https://taylorsicard.com/blog/shopify-app-store-growth-2026 [ABIERTA]; r/ShopifyAppDev hilos 1tv3vb5, 1ryztih, 1wg37m2, 1ua8xrv [ABIERTA vía arctic-shift] |
| WordPress.org plugins | "más de 76.000 plugins gratuitos" (portada, oct 2026) | sin dato de mediana. Freemius: 50-60 % de plugins freemium siguen actualizados a 3 años vs 10-20 % de los gratuitos | norma freemium 2-5 %; feature-gated 2,1 %; informe de datos Freemius con medianas: NO ENCONTRADO | WordPress.org 0 % (no cobra); Freemius como MoR cobra comisión (no leída) | https://wordpress.org/plugins/ [ABIERTA]; https://freemius.com/blog/increase-freemium-upgrades-wordpress-plugin-theme/ [ABIERTA]; https://freemius.com/blog/freemium-wordpress-plugins-outlive-free-ones/ [ABIERTA] |
| Chrome Web Store | sin dato (chrome-stats.com bloqueado 403) | ExtensionPay: "más de 800.000 $" ganados en total por todos sus desarrolladores desde 2021 (vs 25.000 $ en feb 2022); casos citados por ExtensionPay (autoinformados, 2019-2021): GMass 130 k$/mes, Closet Tools 42 k$/mes, GoFullPage 10 k$/mes con 4 M usuarios y premium a 1 $/mes. Reddit 2026: 209,65 $ MRR y 44 suscriptores tras 1 año (2.144 instalaciones activas, 0 $ ads); 135 € MRR con 3 extensiones (150-200 h la primera); 513 $ MRR con 15.000 usuarios semanales (en venta); hilo "la matemática es deprimente": con 1 % free→paid, 2,99 $ y 20 % churn hacen falta 273 instalaciones/día para 1.000 $ MRR a 12 meses | asunción habitual 1 % (hilo Reddit); sin dato agregado | Google no cobra; ExtensionPay 5 % + Stripe | https://extensionpay.com/ [ABIERTA]; https://extensionpay.com/articles/browser-extensions-make-money [ABIERTA]; r/chrome_extensions hilos 1vsxaz2, 1v8z828, 1tu0rp9, 1ublcm3, 1xbglcb [ABIERTA vía arctic-shift] |
| Atlassian Marketplace | 8.000+ apps, 1.800+ partners (Aventis, ago 2025); empezó con 60 apps en 2012 | 4.000 M$ ventas acumuladas (ene 2024, Atlassian); ≈1.800 M$ ventas 2024 estimadas, CAGR ≈19 % desde 2021 (Aventis, estimación desde "other revenue"); Appfire concentra ~200 apps; "muchos partners con 1-2 apps". Mediana por vendor: sin dato | sin dato | Connect 15 % → 20 % desde 1 ene 2026; Forge 100 % para el dev hasta 1 M$ acumulado [FRAGMENTO, no verificado en docs Atlassian] | https://www.atlassian.com/blog/add-ons/future-of-teamwork [ABIERTA]; https://aventis-advisors.com/?p=5371 [ABIERTA]; PDF Aventis no descargable (devolvió HTML) |
| Google Workspace Marketplace | ≈5.000-5.300 apps (2024-2026) | sin dato | sin dato | sin dato | [FRAGMENTO] vía buscador; ficha FacturasApp for Sheets (719 valoraciones, 5★) https://workspace.google.com/marketplace/app/facturasapp_for_google_sheets/552858995831 [ABIERTA] |
| Microsoft AppSource | 12.000+ apps a mediados de 2025 (vs ≈7.000 en 2023; 20.000+ en 2020 con otro criterio); 234-372 apps nuevas por quincena en 2025 | sin dato | sin dato | sin dato | https://sia.hackernoon.com/microsoft-appsource-key-figures-for-2025-and-future-outlook [ABIERTA] (blog, sin fuente primaria) |
| Zapier / Make | sin cifras públicas de nº de integraciones ni ingresos en la página del programa; solo testimonios (Jotform: 1,5× retención entre usuarios que automatizan) | n/a (Zapier no reparte ingresos) | n/a | n/a | https://zapier.com/platform/partner-program [ABIERTA] |
| Google Play / App Store (referencia) | — | TrustMRR sep 2026: Mobile Apps 69 % de 474 productos ingresan algo, 8 % >5.000 $ MRR (sesgo RevenueCat) | — | 15-30 % | https://techstartups.com/?p=138900 [ABIERTA] |

---

## 4. Casos de micro-SaaS técnicos (cálculo/documentación)

| Nombre | URL | Precio | Tráfico | Modelo | Fundador solo | Estado |
|---|---|---|---|---|---|---|
| Steel Beam Calculator (UK) | https://www.steelbeamcalculator.co.uk/pricing ; /about | 40 £ + IVA/mes o 240 £/año (viga acero); 50 £/mes o 300 £/año (paquete completo); garantía 30 días; se puede contratar 1 mes para un cálculo puntual | sin dato | Suscripción autoservicio, tarjeta, sin demo; desde 2011; empresa 07453113 | No: 2 socios (Kevin Taylor, ingeniero estructural; Nick Walker, software) | [ABIERTA] |
| WebStructural (EE. UU.) | https://webstructural.com/ | Basic 0 $ sin cuenta; Pro 29 $/mes para guardar e imprimir informes; AISC 360-22, NDS 2024, ACI 318, CSA | "150+ países" (autoinformado) | Freemium → suscripción | sin dato (no hay página de equipo abierta) | [ABIERTA] |
| ClearCalcs (Calcs.com) | https://clearcalcs.com/pricing | Basic 79 $/mes (66 $/mes anual, 790 $/año); Pro 119 $/mes (1.190 $/año); Ultimate 149 $/mes (1.490 $/año); 228 calculadoras; "3.000+ ingenieros al mes" | sin dato | Suscripción autoservicio con trial | No: empresa con equipo (AU/US) | [ABIERTA] |
| SkyCiv | https://skyciv.com/pricing/ (precios cargados por JS); Capterra | "Starting from 69 $/mes" (Capterra, 34 reseñas, 4,56); plan estudiante y anual; "10.000+ profesionales" (web) | sin dato (Similarweb 403) | Suscripción autoservicio; soporte de ingeniería en Professional | No: empresa (Sídney), equipo | [ABIERTA] (Capterra) / precios propios no legibles |
| BeamGuru | https://beamguru.com/ | 4,99 $ por 2 cálculos (sin caducidad); 1/3/12 meses sin límite, 12 meses 39 $; 1 usuario, 3 IP/día | sin dato | Micropago + suscripción no renovable | sin dato (aviso de "trabajos técnicos" firmado por el sitio; probable desarrollador individual, no verificado) | [ABIERTA] |
| calcresource | https://calcresource.com/about.html | Gratis, con anuncios | sin dato | Publicidad | Sí: "la mayoría de las herramientas diseñadas y preparadas por el Dr. M.E. Lemonis, PhD" (2015-2026) | [ABIERTA] |
| EngiLab (Grecia) | https://www.engilab.com/ | Licencias de escritorio Frame.2D / Truss.2D (precio en carrito, no capturado) | sin dato | Licencia perpetua, compra online | sin dato | [ABIERTA] (precio no extraído) |
| Omni Calculator (PL) | https://www.omnicalculator.com/ | Gratis; 3.938 calculadoras (Finanzas 618, Física 546, Construcción 161) | sin dato | Publicidad/colaboraciones; Omni Calculator sp. z o.o. | No: empresa | [ABIERTA] |
| Calculat.io | https://calculat.io/en | Gratis | sin dato | Publicidad | sin dato | [ABIERTA] |
| Engineering ToolBox | https://www.engineeringtoolbox.com/ | Gratis; "usamos un tercero para monetización" (anuncios); página "about" 404 | sin dato | Publicidad | sin dato | [ABIERTA] (portada) |
| Wonder.Legal España (generador documentos legales) | https://www.wonder.legal/es | Pago por documento (precio no mostrado en portada); 490 modelos ES; 26 países; "4.212.880 usuarios" | sin dato | Autoservicio, formulario → documento | No: empresa francesa con "equipo de abogados y juristas" | [ABIERTA] |
| FacturasApp for Google Sheets (ES) | https://workspace.google.com/marketplace/app/facturasapp_for_google_sheets/552858995831 | no visible en ficha | 719 valoraciones, 5★ | Add-on Workspace | sin dato | [ABIERTA] |
| RPGMapEditor (prosumer, no ingeniería; caso de embudo SEO) | https://reddit.com/r/SaaS/comments/1xblvsx/ | 3 $/mes o 14,99 € vida | ≈1.000 clics/mes Google | Herramientas gratis → editor premium | Sí | [ABIERTA] (anécdota) |
| VectoSolve (utilidad PNG→SVG; caso de SEO masivo) | https://reddit.com/r/microsaas/comments/1xc1i6j/ | sin dato | ≈1.000 landings en 12 idiomas, 200 posts | Utilidad de pago, ingresos verificados TrustMRR 2.695 $ en 30 días (16-21 oct 2026) | sin dato | [ABIERTA] (hilo que cita TrustMRR) |
| dmELECT, CYPE, Elec Calc (software cálculo instalaciones ES) | dmelect.com/precios 404; cype.es/precios 500; elec-calc.com/es/precios 404 | sin dato | | Licencias de escritorio tradicionales, equipos | No | NO ENCONTRADO precios |

Similarweb: todas las consultas devolvieron 403 (CloudFront) también con --browser; r.jina.ai devolvió 401 por reputación de IP. Tráfico = sin dato en toda la tabla.

---

## 5. CAC vs LTV y escenarios de presupuesto

LTV = precio / churn mensual (bruto):

| Precio €/mes | churn 3 % | churn 5 % | churn 8 % |
|---|---|---|---|
| 20 | 667 | 400 | 250 |
| 35 | 1.167 | 700 | 438 |
| 50 | 1.667 | 1.000 | 625 |

LTV/CAC por combinación (CAC de §2; payback = CAC/precio):

| Escenario | CPC € | v→t | t→p | CAC € | Precio | churn | LTV € | LTV/CAC | Payback (meses) |
|---|---|---|---|---|---|---|---|---|---|
| Pesimista | 6,0 | 2 % | 5 % | 6.000 | 20 | 8 % | 250 | 0,04 | 300 |
| Pesimista | 6,0 | 2 % | 5 % | 6.000 | 35 | 5 % | 700 | 0,12 | 171 |
| Pesimista | 6,0 | 2 % | 5 % | 6.000 | 50 | 3 % | 1.667 | 0,28 | 120 |
| Base-malo | 3,0 | 2 % | 10 % | 1.500 | 20 | 8 % | 250 | 0,17 | 75 |
| Base-malo | 3,0 | 2 % | 10 % | 1.500 | 35 | 5 % | 700 | 0,47 | 43 |
| Base-malo | 3,0 | 2 % | 10 % | 1.500 | 50 | 3 % | 1.667 | 1,11 | 30 |
| Base | 3,0 | 5 % | 10 % | 600 | 20 | 8 % | 250 | 0,42 | 30 |
| Base | 3,0 | 5 % | 10 % | 600 | 35 | 5 % | 700 | 1,17 | 17 |
| Base | 3,0 | 5 % | 10 % | 600 | 50 | 3 % | 1.667 | 2,78 | 12 |
| Base-bueno (tarjeta en trial) | 3,0 | 5 % | 25 % | 240 | 20 | 8 % | 250 | 1,04 | 12 |
| Base-bueno (tarjeta en trial) | 3,0 | 5 % | 25 % | 240 | 35 | 5 % | 700 | 2,92 | 7 |
| Base-bueno (tarjeta en trial) | 3,0 | 5 % | 25 % | 240 | 50 | 3 % | 1.667 | 6,94 | 5 |
| Optimista ES (puja baja) | 1,5 | 5 % | 25 % | 120 | 20 | 8 % | 250 | 2,08 | 6 |
| Optimista ES (puja baja) | 1,5 | 5 % | 25 % | 120 | 35 | 5 % | 700 | 5,83 | 3 |
| Optimista ES (puja baja) | 1,5 | 5 % | 25 % | 120 | 50 | 3 % | 1.667 | 13,89 | 2 |

Escenarios de gasto en anuncios (clientes/mes = presupuesto / CAC; MRR añadido = clientes × precio; meses para recuperar = CAC / precio):

| Escenario (CAC) | Presupuesto €/mes | Clientes nuevos/mes | MRR añadido/mes a 20 € | a 50 € | Meses recuperar CAC a 20 € | a 50 € |
|---|---|---|---|---|---|---|
| Pesimista (6.000 €) | 300 | 0,05 | 1 | 2 | 300 | 120 |
| Pesimista (6.000 €) | 1.000 | 0,17 | 3 | 8 | 300 | 120 |
| Pesimista (6.000 €) | 2.000 | 0,33 | 7 | 17 | 300 | 120 |
| Base-malo (1.500 €) | 300 | 0,20 | 4 | 10 | 75 | 30 |
| Base-malo (1.500 €) | 1.000 | 0,67 | 13 | 33 | 75 | 30 |
| Base-malo (1.500 €) | 2.000 | 1,33 | 27 | 67 | 75 | 30 |
| Base (600 €) | 300 | 0,50 | 10 | 25 | 30 | 12 |
| Base (600 €) | 1.000 | 1,67 | 33 | 83 | 30 | 12 |
| Base (600 €) | 2.000 | 3,33 | 67 | 167 | 30 | 12 |
| Base-bueno, tarjeta en trial (240 €) | 300 | 1,25 | 25 | 62 | 12 | 5 |
| Base-bueno, tarjeta en trial (240 €) | 1.000 | 4,17 | 83 | 208 | 12 | 5 |
| Base-bueno, tarjeta en trial (240 €) | 2.000 | 8,33 | 167 | 417 | 12 | 5 |
| Optimista ES, puja baja (120 €) | 300 | 2,50 | 50 | 125 | 6 | 2 |
| Optimista ES, puja baja (120 €) | 1.000 | 8,33 | 167 | 417 | 6 | 2 |
| Optimista ES, puja baja (120 €) | 2.000 | 16,67 | 333 | 833 | 6 | 2 |

Lectura: con 300 €/mes y el caso base (CAC 600 €) se compra medio cliente al mes; a 20 €/mes se tarda 30 meses en recuperar cada cliente y la vida media con churn 8 % es 12,5 meses, así que se pierde dinero en cada cliente. La única combinación con LTV/CAC ≥3 y payback ≤12 meses usando solo anuncios es: **precio ≥35-50 €/mes, churn ≤5 % (cliente profesional, no hobbyista), trial con tarjeta (t→p ≈25 %) y CPC ≤3 €**. Añadir Stripe/MoR (3-7 %) y comisión de marketplace (0-20 %) empeora el LTV neto entre 3 y 25 %.

Datos reales de referencia: TrustMRR sep 2026 mediana 169 $/mes entre productos que cobran; Shopify precio de entrada mediano 9,99 $; Chrome 2,99-4,99 $/mes típico; ingeniería estructural 29-149 $/mes. Esto sitúa el rango 20-50 € en la parte alta de utilidades prosumer y en la parte baja de software profesional.

---

## 6. Riesgos y no verificado

1. **Sesgo de fuentes**: First Page Sage es una agencia SEO que mide sus propios clientes (B2B, EE. UU.); LocaliQ/WordStream venden gestión de ads; RevenueHunt, AppJubilee y Taylor Sicard viven del ecosistema Shopify; Freemius vende monetización de plugins. Ninguna publica muestras auditadas.
2. **Churn en un rango muy abierto**: las fuentes mezclan churn de clientes y de ingresos, mensual y anual (UserJot da 7,5 % anual para SMB mientras Recurly/Paddle dan 6-9 % mensual para ARPU <100 $). Se usó la banda mensual 3-8 % porque es la que coincide con ChartMogul por ARPA.
3. **CPC España**: ningún dato por keyword en 2025-2026 de acceso público; la banda se apoya en pujas reales del Planificador (6 bloques, oct 2026) y en una guía europea sin muestra. Riesgo de que "programa facturación" esté muy por encima de 3 € por competencia de Holded, Quipu, Sage, etc. (no comprobado).
4. **Tiempo a 1k/5k MRR**: no existe serie 2024-2026; el único dato cuantificado es de 2022 y de muestra pequeña. Las anécdotas Reddit 2026 van de 6 semanas a "nunca".
5. **Fundador solo en ingeniería**: no se encontró ningún caso con ingresos publicados. Puede existir y no publicar.
6. **Caídas de precio por IA**: solo anécdotas (Chrome, r/microsaas); no hay índice de precios de marketplaces. El precio de entrada mediano 9,99 $ en Shopify (2026) y el plan medio 66,54 $ (2025) no son comparables entre sí.
7. **Marketplaces**: la "quita" de reseñas y la caída de instalaciones en apps antiguas (hilo r/ShopifyAppDev jun 2026) sugieren riesgo de plataforma; Shopify endureció el reparto en 2025 y Atlassian sube Connect a 20 % en 2026.
8. **Bloqueos**: Indie Hackers (403 incluso con navegador), Similarweb (403), chrome-stats (403), barn2 (403), bigideasdb (429), r.jina.ai (401), arctic-shift devuelve null con consultas de varias palabras entre comillas en paralelo (hubo que lanzar en serie y con una palabra).
9. **No abierto**: PDF de MicroConf 2024 (formulario), PDF Aventis (devolvió HTML), KeyBanc 2024, informe ChartMogul/Growth Unhinged 2026 original (leído vía Userpilot), artículo Indie Hackers "it takes 5 months to reach 1k MRR".

---

## 7. URLs abiertas y estado

| URL | Qué buscaba | Estado |
|---|---|---|
| https://firstpagesage.com/reports/average-customer-acquisition-cost-cac-by-industry-b2b-edition/ | CAC por industria | ABIERTA, datos |
| https://chartmogul.com/reports/saas-benchmarks/ ; https://chartmogul.com/saas-benchmarks/ | CAC/benchmarks ChartMogul | 404 |
| https://chartmogul.com/reports/saas-retention-report/ | retención por ARPA | ABIERTA, datos |
| https://chartmogul.com/reports/saas-growth-report/ | crecimiento | ABIERTA, no usada |
| https://www.lennysnewsletter.com/p/what-is-a-good-free-to-paid-conversion | conversión free→paid | ABIERTA, datos (parte de pago cortada) |
| https://userpilot.com/blog/free-trial-conversion-rate/ ; /saas-average-conversion-rate ; /saas-free-trial-conversion-rate/ | trial→paid 2026 | ABIERTA, datos (la tercera redirige al hub) |
| https://www.paddle.com/blog/saas-churn-rate | churn Recurly | ABIERTA, datos |
| https://www.paddle.com/resources/saas-churn-rate | churn | 404 |
| https://www.highalpha.com/saas-benchmarks-report ; https://openviewpartners.com/2023-saas-benchmarks-report/ | benchmarks VC | 404 |
| https://baremetrics.com/open-startups | open startups | ABIERTA, sin tabla pública |
| https://microconf.com/state-of-independent-saas ; https://microconf.com/saas-this-year ; https://stateofindiesaas.com | informe 2024 | ABIERTA, solo formulario |
| https://www.startupsfortherestofus.com/episodes/episode-721-7-key-takeaways-from-the-2024-state-of-independent-saas-report | hallazgos 2024 | ABIERTA, transcripción |
| https://localiq.com/blog/search-advertising-benchmarks/ | CPC/CVR 2026 | ABIERTA, datos |
| https://www.wordstream.com/blog/google-ads-benchmarks | CPC | ABIERTA, cifras en imágenes |
| https://www.statista.com/statistics/1243710/spain-search-advertising-cpc | CPC España por sector | ABIERTA, cifras ocultas |
| https://es.semrush.com/blog/google-ads-coste/ | CPC España | ABIERTA, sin cifras ES |
| https://codedesign.org/google-ads-cost-europe-your-complete-guide/ | CPC Europa software | ABIERTA, 2,30-4,50 € |
| https://app.neilpatel.com/... ; https://ahrefs.com/keyword-generator/google/es?... | CPC keyword ES | login/captcha |
| https://wordpress.org/plugins/ ; https://wordpress.org/plugins/freemius/ | nº plugins | ABIERTA |
| https://freemius.com/blog/increase-freemium-upgrades-wordpress-plugin-theme/ ; /freemium-wordpress-plugins-outlive-free-ones/ ; /?p=14793 ; /wordpress-plugin-business-benchmarks/ | conversión WP | ABIERTA (3) / 404 (1) |
| https://extensionpay.com/ ; https://extensionpay.com/articles/browser-extensions-make-money | Chrome monetización | ABIERTA, datos |
| https://chrome-stats.com/ | nº extensiones | 403 Cloudflare |
| https://revenuehunt.com/state-of-the-shopify-app-economy/ | Shopify 2026 | ABIERTA, datos |
| https://www.appjubilee.io/shopify-app-store-report-2026 | Shopify 2026 | ABIERTA, datos |
| https://meetanshi.com/blog/shopify-app-store-statistics/ | Shopify 2025 | ABIERTA, datos |
| https://shopify.dev/changelog/update-to-shopifys-app-developer-revenue-share | comisión | ABIERTA, datos |
| https://taylorsicard.com/blog/shopify-app-store-growth-2026 | crecimiento apps | ABIERTA, datos |
| https://eightx.co/blog/shopify-app-bloat-report-2026 | gasto en apps por tienda | ABIERTA (1,8 % de tiendas gastan >100 $/mes en apps) |
| https://barn2.com/?p=712947 ; https://barn2.com/blog/shopify-app-revenue/ | ingresos medianos apps | 403 |
| https://www.atlassian.com/blog/add-ons/future-of-teamwork | Atlassian 4.000 M$ | ABIERTA, dato |
| https://aventis-advisors.com/?p=5371 ; PDF Aventis | Atlassian 2025 | ABIERTA / PDF falló |
| https://zapier.com/platform/partner-program | Zapier | ABIERTA, sin cifras |
| https://workspace.google.com/marketplace/app/facturasapp_for_google_sheets/552858995831?hl=es | Workspace | ABIERTA |
| https://sia.hackernoon.com/microsoft-appsource-key-figures-for-2025-and-future-outlook | AppSource | ABIERTA |
| https://trustmrr.com/ | ingresos verificados | ABIERTA (portada, leaderboard) |
| https://techstartups.com/?p=138900 | análisis TrustMRR sep 2026 | ABIERTA, datos |
| https://www.indiehackers.com/products?... ; /post/it-takes-5-months-to-reach-1k-in-mrr-491742f806 | IH | 403 (también --browser) |
| https://bigideasdb.com/state-of-indie-saas-revenue-2026 ; /bootstrapped-saas-1m-arr | mediana TrustMRR | 429 Vercel |
| https://hunted.space/product-hunt-pulse | lanzamientos PH | ABIERTA, datos |
| https://blog.mean.ceo/?p=11218 ; ?p=11175 | PH Q2 2026 / indie stats | ABIERTA (secundaria) |
| https://skyciv.com/pricing/ (http y --browser) ; /structural-3d/ ; /quick-design/pricing/ | precios SkyCiv | precios por JS / 404 |
| https://www.capterra.com/search/?query=skyciv | precio SkyCiv | ABIERTA, 69 $/mes |
| https://www.g2.com/products/skyciv/pricing | precio | 403 |
| https://clearcalcs.com/pricing | precios | ABIERTA, datos |
| https://www.steelbeamcalculator.co.uk/ ; /pricing ; /about | precios, equipo | ABIERTA, datos |
| https://webstructural.com/ ; /pricing.html | precios | ABIERTA / 404 |
| https://beamguru.com/ ; /online/pricing/ | precios | ABIERTA / redirección infinita |
| https://calcresource.com/about.html | autor | ABIERTA |
| https://www.engilab.com/ | precios | ABIERTA, precio no extraído |
| https://www.omnicalculator.com/ ; /about | equipo | ABIERTA / 404 |
| https://calculat.io/en | | ABIERTA |
| https://www.engineeringtoolbox.com/ ; /about-us-d_1360.html | monetización | ABIERTA / 404 |
| https://www.wonder.legal/es ; /es/pricing | generador legal ES | ABIERTA / 404 |
| https://www.dmelect.com/precios ; https://www.cype.es/precios/ ; https://www.elec-calc.com/es/precios | software instalaciones ES | 404 / 500 / 404 |
| https://www.similarweb.com/website/skyciv.com/ (--browser) ; r.jina.ai | tráfico | 403 / 401 |
| https://www.venasolutions.com/blog/saas-churn-rate ; https://userjot.com/blog/saas-churn-rate-benchmarks ; https://www.wearefounders.uk/saas-churn-rates-and-customer-acquisition-costs-by-industry-2025-data/ | churn/CAC secundarios | ABIERTA |
| arctic-shift r/SaaS, r/microsaas, r/ShopifyAppDev, r/chrome_extensions (búsquedas "google ads CAC", "vibe", "took", "1k MRR", "MRR", "race to the bottom"; posts 1x67q1k, 1xblvsx, 1x7lvaz, 1x7mx6r, 1x6vm44, 1xbcwhk, 1tv3vb5, 1ryztih, 1vsxaz2, 1v8z828, 1tu0rp9, 1xbglcb, 1xc1i6j, 1qy8bkt, 1rk8hfz, 1ua8xrv; comentarios 1t4gpig) | anécdotas 2026 | ABIERTA (API) |
| research_notes/Dolores en crecimiento con pruebas/search_volume_planner_trends.md | pujas reales ES | ABIERTA (repo) |

Recuento: 70+ URL solicitadas, 48 con contenido legible.
