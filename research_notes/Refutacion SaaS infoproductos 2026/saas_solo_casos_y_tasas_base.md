# SaaS para fundador solo sin capital ni audiencia: casos reales y tasas base (refutación adversarial)

Fecha de la investigación: 22-oct-2026. Método: ~150 URLs abiertas con Chromium headless (Indie Hackers, TrustMRR, MicroConf, Stripe Atlas, Acquire vía BigIdeasDB, ChartMogul, Lighter Capital, Belkins, blogs de fundadores) + búsquedas web. Etiquetas: **[ABIERTA]** = página leída entera o en su parte relevante; **[FRAGMENTO]** = sólo resumen de buscador o parte tras muro de registro; **NO ENCONTRADO** = buscado y no localizado. En cada caso se indica si la cifra está **verificada por Stripe/Paddle** o es **autodeclarada**.

Afirmación a refutar (analista): *"Para un fundador solo, sin capital, sin audiencia previa y cuya única distribución es el correo frío B2B, el SaaS no es una vía realista en 2025-2026: los casos de éxito son el 2-5 % con distribución previa, y la mediana de ingresos de un SaaS indie es casi cero."*

---

## 1. Tasas base encontradas (con muestra y fuente)

| # | Dato | Muestra | Fuente / fecha | Estado | Lectura |
|---|------|---------|----------------|--------|---------|
| 1 | **Mediana de ingresos mensuales = 169 $**; top 25 % > ~800 $/mes; top 10 % > 10.000 $/mes; top 1 % > 98.500 $/mes. Sólo 48 proyectos (0,9 %) "despegan" (>10k $/mes y >50 %/mes). Mediana por antigüedad: año 0 = 148 $, año 1 = 334 $, año 2 = 656 $, año 4 = 2.399 $, año 5 = 2.509 $. | 5.079 proyectos con Stripe verificado (TrustMRR) | IH post "I analyzed 5,079 Stripe-verified startups", mar-2026 | [ABIERTA] | Confirma "mediana casi cero". Verificado por Stripe, pero autoselección de quien lista. |
| 2 | **Distribución TrustMRR hoy**: 0–1k $ = 67,6 %; 1k–10k = 17,0 %; 10k–100k = 10,3 %; 100k–1M = 4,1 %; >1M = 1,0 % (ingreso acumulado total, no MRR). Meses hasta hitos (sólo quienes llegan): 1 $ = 5 meses; 1k $ = 6 meses; 10k $ = 1,1 años; 100k $ = 2,2 años. Mediana de ingreso acumulado por proveedor: Stripe 265 $; Paddle 40 $; LemonSqueezy 143 $. **54 % de los fundadores tienen 0–1k seguidores en X**; correlación ingresos~seguidores r = 0,25 (n = 5.981); "los ingresos crecieron más rápido que los seguidores en el 80 % de los casos" (n = 355). Correlación ingresos~antigüedad r = 0,47 (n = 7.378); ingresos~Domain Rating r = 0,43 (n = 6.666). | 7.378 startups, 1.958 M$ de ingreso verificado | trustmrr.com/stats, snapshot 22-oct-2026 | [ABIERTA] | ~15 % supera 10k $ acumulados; el peso de la audiencia previa es **débil** (r = 0,25) y la mayoría de fundadores no tiene audiencia. |
| 3 | **Fundadores solos en IH con Stripe verificado**: 80,9 % < 500 $ MRR; 6,4 % > 5.000 $; **4,8 % > 10.000 $ MRR**. 593/970 (61 %) están a 0 $. Mediana de los que tienen ingreso positivo: 303 $/mes (distribución log-normal). | 970 productos | IH "Making bank as a solo founder seems to be rare", abr-2021 | [ABIERTA] | Base del "2-5 %" del analista. Sesgo: quien gana deja de publicar cifras (comentarios en el hilo). |
| 4 | **IH, todos los productos con Stripe verificado**: 54 % no genera ingresos; **~5 % supera 8.333 $/mes (100k $/año)**. | 937 productos | Scraping Fish, jul-2022 | [ABIERTA] | Idem. Recuento posterior (998 productos): 48,7 % a 0 $ [FRAGMENTO]. |
| 5 | IH scrape completo: 2.868 productos; 1.516 a 0 $; 915 > 10k $/mes (autodeclarado). Subconjunto Stripe verificado (285): 118 a 0 $, 28 en 0–100 $, 25 en 100–1.000 $, 37 en 1k–10k, 74 > 10k. | 2.868 (285 verificados) | softwaredesign.ing, sep-2023 | [ABIERTA] | Distribución bimodal: "o despega o no funciona". |
| 6 | **MicroConf State of Independent SaaS 2024**: ~700 respuestas útiles (Rob Walling, ep. 721); 469 fundadores citados en páginas de MicroConf. **50,7 % dirige la empresa solo**. **28 % está por debajo de 1.000 $ MRR** (el grupo más grande). **65 % tiene 1–10 clientes de pago**; más de la mitad < 50. 30 % crece 1–4 %/mes y ~30 % está plano o decrece. SEO y boca a boca = canales de mayor impacto (2,2x). Planes de entrada ≥ 1.000 $/mes añaden ~1.073 $ MRR/mes vs ~316 $ para precios de 1–9 $. 29 % de quienes hacen ads espera >7 meses o no sabe si funcionan. Fundadores a tiempo completo crecen 30 % más rápido. 60 % de exits a 1–3x ARR. | ~700 / 469 | microconf.com/founders/* (citas p.25, 34, 35, 39, 61); ep. 721 SftRoU | [ABIERTA] (páginas MicroConf y transcripción podcast; el PDF requiere email) | Muestra sesgada a fundadores **ya con ingresos** (comunidad MicroConf). Aun así: la mayoría está < 1k $ MRR con < 10 clientes. |
| 7 | **Stripe Atlas 2025**: 20 % cobra su primer cliente en 30 días (8 % en 2020). **Solos = 63 % de las C-corps del T2-2026**. Mediana de ingresos de los primeros 6 meses de fundadores solos **cayó 23 % interanual en 2025**; el decil superior subió 19 %; top decil = **61x** la mediana (34x hace 4 años). Top decil 2x más probable que sea AI-native; vende a 10 países el primer mes vs 3; **~30 % más probable que sea B2B; la mediana B2B solo gana >4x la mediana B2C a 24 meses, también entre bootstrapped**; retención mes 2: 30 % vs 8 %. | 23.000 incorporaciones 2025; "miles" de solos 2022-23 con 2 años de datos | stripe.com/blog (dic-2025 y may-2026) | [ABIERTA] | Mediana empeora, cola mejora: refuerza "winner-take-most"; B2B y retención temprana son los discriminantes. |
| 8 | **Acquire.com (via BigIdeasDB)**: 615 listados SaaS en venta; mediana precio pedido 190.000 $ (P25 75k, P75 500k); mediana ingreso TTM 118.000 $ (P25 43k – P75 304k); beneficio TTM 55k; **ingreso del último mes mediano 10.000 $**. 2,0x ingresos / 3,4x beneficio. Razones de venta: 32 % nuevo proyecto; 8 % "builder, not marketer". | 615 | PDF "State of SaaS Acquisitions 2026", jun-2026 | [ABIERTA] (PDF) | Lo que llega a venderse ya es la cola buena (~10k $ MRR). No hay dato público de cuántos listados < 1k $ MRR en Acquire; en TrustMRR marketplace sí hay decenas listados a 49–945 $ MRR. |
| 9 | Lighter Capital 2025: 155 B2B SaaS privadas (datos conectados, no encuesta): crecimiento anual mediano 28 % (47 % en 2024); churn de ingresos mediano 12,5 %; las < 50k $ ARR son las que más se frenan (~50 %). | 155 | lightercapital.com, sep-2025 | [ABIERTA] | Benchmark de empresas ya financiadas por deuda, no indies. |
| 10 | ChartMogul: mediana 2 años 9 meses hasta 1M $ ARR; sólo 13 % alcanza 10M $ tras 10 años; sólo 2,7 % de SaaS con ARPA < 10 $/mes tiene NRR > 100 % vs 41 % con ARPA > 500 $. | >2.200 / >2.100 empresas | Growth Report ago-2023, Retention Report nov-2023 | [ABIERTA] | Precio alto = retención; refuerza B2B con ticket alto. |
| 11 | **Correo frío (Belkins 2026)**: 7,5 M emails en 2025; **tasa de respuesta 0,45 % sobre enviados** (0,57 % a founders/owners; 0,22 % en empresas 10k+). Caída 20 % del 1.º al 2.º semestre. | 7,5 M emails | belkins.io, jun-2026 | [ABIERTA] | Benchmark de agencia. Las cifras de 3–10 % de otros vendedores miden "sobre abiertos" o "respuestas positivas". |
| 12 | Product Hunt: "97,4 % de 500 lanzamientos SaaS en PH no superó 1.000 $ MRR a 6 meses" y "~70 % de 1.000 micro-SaaS nunca superó 1k $ MRR" | 500 / 1.000 | collab365 citando shubhq citando un hilo de Reddit (sep-2026) | [FRAGMENTO] – fuente primaria **NO ENCONTRADA** | No usar como dato duro. |
| 13 | Starter Story: proporción de proyectos sin ingresos | — | — | **NO ENCONTRADO** (su base sólo lista "3.408 proyectos con ingresos") | — |
| 14 | TinySeed: 210+ empresas B2B SaaS, 329 fundadores; vertical > horizontal (ep. 812). Sin datos de % solos ni de tasa de éxito. | 210 | SftRoU ep. 812, dic-2025 | [ABIERTA] | Sin cifra útil para la pregunta. |

**Síntesis de tasas base.** Tres bases de datos independientes con pago verificado (IH 2021/2022, TrustMRR 2026) coinciden: mediana ≈ 150–300 $/mes, 50–68 % por debajo de 1.000 $/mes acumulados o a 0 $, y **≈ 5 % (IH) a ≈ 15 % (TrustMRR, acumulado) por encima de 10k $/mes**. La encuesta MicroConf (sólo gente con ingresos) sigue dando 28 % < 1k $ MRR y 65 % con ≤ 10 clientes. El analista acierta en la mediana y en el orden de magnitud del "2-5 %" (para fundadores solos verificados en IH: 4,8 % > 10k $ MRR; 100k $/año es el umbral de ese 5 %).

---

## 2. Tabla de casos (ingresos declarados; se indica verificación)

Leyenda canal: SEO, PH = Product Hunt, CE = cold email, LI = LinkedIn/DM frío, AUD = audiencia propia (X/newsletter), MKT = marketplace (Shopify/Slack/AWS/App Store), OSS = open source/GitHub, WOM = boca a boca/partners, AG = clientes previos de agencia/empleo.

### 2a. Productos con ingreso **verificado por Stripe** en Indie Hackers (listado "verified first", 22-oct-2026) [ABIERTA]

| Producto | Ingreso verificado (mes) | Fundadores | Inicio | Hitos de tiempo conocidos | Canal principal declarado | Nicho / precio | Notas |
|---|---|---|---|---|---|---|---|
| Ghost | 882.575 $ | equipo (31 pers., non-profit) | 2013 Kickstarter | 36k $ MRR con 5 pers. → 5M $/año 2022 | AUD/OSS | Creadores | No comparable con solo. |
| Whaticket | 428.060 $ | equipo | — | — | — | B2B chat | Sin detalle abierto. |
| Cloud Campaign | 423.850 $ | equipo | — | — | — | B2B agencias | — |
| Postiz | 331.586 $ | Nevo David (+equipo) | 2023 | 1,3M $ ARR en 2 años | OSS + AUD | B2B social scheduling | Fundador con gran audiencia dev. |
| Savvy Nomad | 302.643 $ | — | — | — | — | B2C servicio | — |
| browserless | 298.730 $ | Joel Griffith (+equipo) | 2017 | 1,3M $ ARR y 15k usuarios en 2023 (6 años) | OSS/GitHub, contenido propio | B2B devs | Contrata 1.er marketer en 2023. |
| Rezi | 212.024 $ | Jacob Jacquet (+equipo) | ~2018 | 60k $/mes dic-2022 | SEO (500+ páginas) + cierres B2B | B2C/B2B CV | — |
| AppraiseItNow | 145.767 $ | — | — | — | — | Servicio tech-enabled | — |
| TAXX | 124.322 $ | 3 fundadores part-time → 5,5 FTE + inversores | 2017 | — | — | B2C Luxemburgo | No solo, no bootstrapped. |
| Dealsourcr | 98.819 $ | 2 cofundadores | ~2019 | 1.500 $ MRR abr-2020 → 12.152 $ abr-2021 → £27k dic-2023 → 500k $ ARR sep-2026 (**~6 años a 500k ARR**) | **100 % partnerships + referidos** ("boca a boca orgánico no sirvió") | Inversores inmobiliarios UK (prosumer) | Autodescripción: "el producto apesta la mayor parte del tiempo". |
| QuotaGuard | 77.207 $ | adquirido por Michael Frew | 2013 | — | **MKT** (Heroku add-ons → AWS/Azure/GCP marketplaces) | B2B devs | — |
| Gigalixir | 64.999 $ | adquirido por M. Frew (2021) | — | +10 % MRR en 6 meses tras compra | WOM comunidad Elixir | PaaS B2B | — |
| Taskforce.sh / BullMQ | 43.557 $ | Manuel Astudillo (solo + dev part-time) | ~2019 | 2k → 4k $ MRR tardó ~1 año (mar-2022); 8,3k $ feb-2023; ~44k $ oct-2026 | **OSS** (3M descargas/mes) + SEO/tutoriales | B2B devs; dashboard SaaS/on-prem/Pro | ~7 años hasta 500k ARR. |
| Zanfia, Apiframe, Virlo | 43–44k $ | — | — | — | — | — | Sin detalle abierto. |
| Cola baja verificada (filtro solo + ≤1.000 $): Zyaku 1.000 $, NForce 937 $, Confluence.VC 936 $, AZLabels 915 $, localhost.run 814 $, GraphJSON 806 $, Stablecog 691 $… | | | | | | | El listado completo exige cuenta. |

### 2b. Entrevistas Indie Hackers 2025-2026 (cifras **autodeclaradas**; la parte tras el muro de registro no se pudo leer)

| Producto | MRR | Fundadores | Inicio → hito | Canal principal | Nicho / precio | ¿Audiencia/capital/experiencia previa? |
|---|---|---|---|---|---|---|
| **Zigpoll** (jul-2026) | **125k $** (1,03M ARR ene-2026 → 1,5M run-rate) | **solo**, sin cofundador ni funding ni ventas | ~2 años hasta tracción; dobla cada año | **MKT Shopify** + WOM + GEO | B2B ecommerce (encuestas) | Sí: 2 SaaS previos (uno absorbido por Shopify, otro vendido) financiaron el build; ex-agencia ecommerce. |
| **Shift** (jun-2026) | **50k $** | **solo** | 10 años | Comunidades Laravel / autoridad | Devs; "cuesta menos que un almuerzo" | Sí: desarrollador conocido en la comunidad Laravel. |
| **ScreenshotOne** (mar-2026) | **>25k $**, 800 clientes (~30 $/cliente) | solo | 4 años | Reddit/contenido/SEO devs | API devs/agentes | 10+ años ingeniero; varios fracasos previos. |
| **Pckgr** (jul-2026) | **83k $** (>1M ARR) | pequeño equipo | — | Reddit/grupos FB (gratis al inicio) + partnerships | B2B IT admins (Intune) | Experiencia directa en el nicho (consultor Intune, Capgemini). |
| **Polotno** (sep-2026) | 60k $, 200+ clientes | equipo de 3 | 6 años | **OSS** (Konva.js como distribución previa) | B2B SDK | Sí: mantenedor de Konva.js. |
| **EmailEngine** (ene-2026) | 13k $, +20 %/año lineal | solo | 5 años | **OSS** (Nodemailer) + SEO | B2B devs self-hosted | Sí: autor de Nodemailer. |
| **Youform** (mar-2026) | 18k $ | solo (freelancer) | — | Social listening (subida de precios Typeform) + precio bajo (29 $) | Formularios SMB | Vendió producto previo por 10k $. |
| **PostFast** (ago-2026) | €5,4k | solo con empleo FT | rentable en ~6 meses | **SEO** + UX | Scheduler social SMB | Sin audiencia declarada. |
| **Leadverse** (ago-2026) | 3,3k $, 130 clientes, 20k $ brutos | solo con empleo 9-5 | 10 meses | Reddit (dogfooding) | Lead-gen social B2B | "Countless apps, most made 0 $". |
| **Jobric** (jun-2026) | 3,3k $ | solo con empleo (Microsoft) | <2 meses | LinkedIn contenido | B2C candidatos | 15 años cloud. |
| **AgentOS** (oct-2026) | 9,5k $ | solo (cero empleados) | 2 meses | contenido + onboarding white-glove | Pagos para fundadores SaaS | 20 años en pagos; 3.ª startup; quemó 10k $ en la anterior. |
| **SuperX** (feb-2026) | 23k $, 650 clientes a 39 $ | 2 (con Tibo Louis-Lucas) | 6 meses; 1k $ MRR el día 1 | **AUD X** (post viral 200k vistas) | Crecimiento en X | 5 productos previos = 0 $ en 2,5 años; el cofundador aporta audiencia enorme. |
| **Lancer** (jul-2026) | 20k $ (10k $ en 60 días) | 2 | 2025 | **Afiliado clave (coach Upwork) + cold outreach + contenido**; lead magnet gratuito | Freelancers/agencias; plan 499 $ | Exit de agencia de 7 cifras y 15 FTE. |
| **Gojiberry AI** (ene-2026) | 27k $ (35k $ ventas/mes) | 2 cofundadores | 2024-25 | **Servicio manual → producto**; outbound LinkedIn por señales | B2B GTM | Exit previo de 7 cifras (CocoAI). |
| **LeadDelta** (dic-2025) | 80k $ (~1M ARR) | pequeño equipo | 3 años | Orgánico, B2C2B, red propia | B2B LinkedIn CRM | Exit previo (Autoklose). |
| **SavvyCal** (ago-2026) | >10k $ (5 cifras) | 3 pers., TinySeed | 6 años | Comunidad/contenido | Scheduling 12 $/mes + API HIPAA | Exit previo (Drip). |
| **Buttondown** (sep-2026) | >83k $ (>1M ARR) | solo → equipo | 2017 → 2026 (9 años) | WOM; side-project con empleo | Newsletters | Ex-Stripe/Amazon ("red de ingenieros senior"). |
| **Vacation Tracker** (sep-2026) | >250k $ (3M ARR) | 2 ex-agencia | 2018 | **MKT Slack/Teams** + contenido; 20/60 de waitlist | B2B HR | Agencia de 10 años como colchón. |
| **Gleap** (ago-2026) | >83k $ (7 cifras), 4.500 equipos | 3 cofundadores | 2020 | Validado con clientes de agencia; SEO + PLG | B2B soporte | Agencia previa. |
| **Nventr** (oct-2026) | >250k $ (3M/año) | fundador + org. | años | "Sin lanzamiento, sin ads": construido dentro de portfolio de family office; WOM interno | Workflows enterprise | Acceso privilegiado a clientes (family office). |
| **SignWell** (ene-2026) | >83k $ (varios M ARR) | fundador 2.ª startup | — | Distribución indirecta/SEO; MVP probado con clientes del 1.er producto | e-signature | Sí: 1.er producto. |
| **Outseta** (feb-2026) | low 7 figures | 3 cofundadores | 9 años (compromiso de 15) | Search + partnerships de integración | Infra SaaS | Cofundador de Buildium (exit 580M $). |
| **Kommodo** (mar-2026) | 42k $ | 2 + equipo de 5 | 2019 → pivot | PLG, herramientas gratis; "ads no funcionan a ese precio" | B2B vídeo docs | — |
| **SocialCrawl** (sep-2026) | 12,5k $ | 2 cofundadores | 2,5 años / 4 fracasos previos | "Give first", meetups, audiencia temprana | API datos para devs/IA | PhDs Oxford. |
| **Centori** (nov-2025) | 14k $ | **solo** | 2023 | SaaS fallido → **servicio productizado** (SEO/contenido) | Servicio | No es SaaS: pivotó a servicio. |
| **Vaultaire** (oct-2026) | 41k $ brutos ago (mayoría compras lifetime 29,99 $) | solo | 3 semanas build; 5 meses | **App Store** + 700 $/mes Apple Search Ads | B2C iOS | Ex-Google, exit previo (Pex). |
| **Personal Best** (sep-2026) | ~5k $ | solo + freelance | 6 años | App Store featured | B2C iOS | — |
| **Taskforce.sh** (nov-2025) | >8k $ (6 cifras ARR, +50 %/año) | solo | ~7 años | OSS + SEO | Devs | Ver 2a. |

### 2c. Casos cuyo canal principal fue **correo frío / outbound** (objetivo: ≥ 8)

| Caso | ¿Fundador solo? | ¿SaaS? | Cifras de outbound | Resultado | Fuente | Estado / verificación |
|---|---|---|---|---|---|---|
| **Proxycurl** (Steven Goh, SG) | No (equipo de 6 heredado; 26 pers. a 1M ARR; 30+ en 2023) | Sí, API B2B datos | Lista Crunchbase Pro de empresas recién financiadas → "miles de cold emails, cientos de respuestas", calendario lleno 1 mes; "pocos miles $ MRR en los primeros meses"; luego SEO ("linkedin api") | 1M $ ARR en 18 meses (2021); 100k $ MRR sep-2023; "7 cifras" 2024 | IH ene-2023 + sep-2023; nubela.co ago-2023 | [ABIERTA] – autodeclarado. Capital: ahorros cripto 100k SGD + 1.500 $/mes de extensión previa (1,5M usuarios). **No encaja en "sin capital, solo"**. Su 2.º producto (Sapiengraph, 2024) estaba en **740 $ MRR** con todo el equipo detrás. |
| **Tweetscrape** (gradoo) | Sí (ex-agencia) | Sí, scraper emails | ~100 emails/día vía Instantly, **~1 % conversión, ~1 cliente/día**; 90 de 100 clientes de CE | **0 → 5k $ MRR en 120 días** (feb-2023) | IH | [ABIERTA] – autodeclarado; comentarios cuestionan legalidad de la fuente de emails (GDPR / bases filtradas). |
| **ColdClicks** (William Paul) | No (2) | Sí, personalización CE | Apollo → ColdClicks → Instantly; objetivo 1 cliente/semana | **400 $ MRR en 4 semanas** (mar-2024); 600 $ MRR a las 6 semanas | IH | [ABIERTA] – autodeclarado; 10+ años en ventas SaaS. |
| **UpLead** (Will Cannon) | No | Sí, datos B2B | "Para los primeros clientes hice lo que sabía: cold email"; luego SEO/PPC/referidos | 8,4M $ ventas en 3 años (2018-21) | IH AMA ago-2021 | [ABIERTA] – autodeclarado; **10 años de agencia de cold email** previos. |
| **Instantly.ai** | No (4 cofundadores) | Sí, herramienta CE | Agencia de lead-gen (10-15k $ MRR) → sus 22 clientes = primeros clientes SaaS; AppSumo | 0 → 2,4M $ ARR en 9 meses; 2.900 clientes; **churn 10 %/mes** | GetLatka jun-2023 | [ABIERTA] – autodeclarado. |
| **Cold Email Studio** (Andrew) | Sí al inicio | **No** (servicio productizado) | 100 emails a founders YC → 2 reuniones en 30 min; "100 emails → 10 reuniones → 6-7 cierres"; precios 500 → 1.000 → 1.500 $ | **0 → 10k $ MRR en 3,5 meses** (2021) | IH (245 upvotes) | [ABIERTA] – autodeclarado; ex-CTO de empresa con 8M $ levantados. |
| **Sales.co** (Ryan Doyle + Jakob Greenfeld) | No | **No** (agencia) | 1 semana gratis a 3 empresas → 500 → 2.000 $/mes | 10k $ MRR antes de conocerse en persona; 90k $ MRR / 1M+ ARR (2024) | IH jul-2024 | [ABIERTA] – autodeclarado; ambos con audiencia en X; su SaaS previo (Magic Sales Bot) se quedó en 1k $ MRR. |
| **SignalsHunt** (Serghei) | Sí | Herramienta + agencia web | **43 emails en 3 semanas → 17 respuestas (40 %) → 1 cliente a 230 $/mes** (auditoría SEO, no SaaS) | 7 signups del SaaS | IH jul-2026 | [ABIERTA] – autodeclarado. |
| **MonitUp** (Faruk Durak) | **Sí, técnico, B2B** | Sí | **6.000 solicitudes LinkedIn → 3.000 aceptadas → ~35 reuniones → 12 ofertas → 1 venta**; 500 $ LinkedIn Ads → 127 visitas, 0 reuniones | MRR 350 → 650 $ **en un año** (dejó su empleo feb-2023) | IH mar-2024 | [ABIERTA] – autodeclarado. **Caso de confirmación del analista.** |
| **Bazzly** (Filip Panoski) | Sí | Sí | "0 $ MRR, sin audiencia, sin presupuesto" → DMs 1:1 a gente con intención en Reddit; pausa 3 meses por churn; luego contenido | **0 → 1k $ MRR en 9 meses** (mar-2026); 7,5k $/mes según ficha IH | IH mar-2026 | [ABIERTA] – autodeclarado; 5 productos fallidos antes. |
| **Breakcold** (Arnaud Belinga) | No (2) | Sí, CRM | Primeros clientes por Twitter; luego pasó a CE + LinkedIn | 24k $ ARR, 53 clientes (2022) | GetLatka may-2022 | [ABIERTA] (índice) – autodeclarado. |
| **GMass case study** ("fundador anónimo") | Sí | Sí, analítica B2B 79 $/mes | 4.500 emails → 646 respuestas (14,4 %) → 127 clientes (2,82 %) | 2,5k → 10k $ MRR en 90 días | growthhacksuite.com jul-2026 | [ABIERTA] – **publicación de vendedor, anónima, no verificable**; cifras muy por encima de todo benchmark (Belkins 0,45 %). Descartar como evidencia. |
| Lancer, Gojiberry (ver 2b) | No | Sí | Outbound como canal secundario tras afiliado/servicio | 20k / 27k $ MRR | IH 2026 | [FRAGMENTO] (tras muro). |

**Recuento**: se localizaron 12 casos con outbound como canal principal o relevante. De ellos, **SaaS B2B + fundador solo + sin capital + sin audiencia + cold email como canal principal + cifra**: sólo **Tweetscrape** (5k $ MRR, 2023, método legalmente dudoso) y, con DMs en lugar de email, **Bazzly** (1k $ MRR en 9 meses). Los casos grandes con cold email (Proxycurl, UpLead, Instantly) **no eran solos ni sin capital**: tenían equipo, ahorros o una agencia previa cuyos clientes fueron los primeros usuarios. Los dos casos puros de fundador solo técnico haciendo outbound B2B con cifras completas (MonitUp: 1 venta/año; SignalsHunt: 1 cliente de 43 emails) **confirman** la tesis del analista. Ninguna entrevista de IH 2025-2026 con >10k $ MRR declara el correo frío como canal principal.

### 2d. Fracasos con cifra (2023-2026)

| Caso | Tiempo / gasto | Usuarios / ingresos | Causa declarada | Fuente | Estado |
|---|---|---|---|---|---|
| **RecoverFlow** (Juhyun Choi, 2026) | Semanas de PRD de 50 páginas; 5 días de lanzamiento; 0 $ presupuesto | **0 signups**; 29 $/mes; cuenta X nueva | "Sin audiencia antes del producto; 0 conversaciones con clientes" | IH 2026 | [ABIERTA] |
| **Letspl** (Lily, Corea) | 2 años | **20.000 usuarios, 0 $** | Mercado sin disposición a pagar | IH may-2026 | [ABIERTA] |
| **SocialKiwi** (Idan Masas) | 6 meses; 5.º SaaS fallido; 200 $ en el banco; API X 100 $/mes | PH #15 (114 upvotes), 40 signups, 200 usuarios gratis, **1 cliente de pago (por compasión)**; ingresos netos **−282 $**; cold DM a "cientos" + ads Google/Meta sin resultado | Audiencia equivocada, sin dinero para ads ni audiencia | IH mar-2024 | [ABIERTA] – vendido por 2.200 $ en DMs de X. |
| **MonitUp** | 1 año full-time | 350 → 650 $ MRR | B2B lento, LinkedIn 6k → 1 venta | IH mar-2024 | [ABIERTA] |
| **Sitebot.ai** (Hannu Jaakkola) | mar-2018 → ene-2020 | 1.er cliente por Twitter; "convertir usuarios a clientes fue difícil" | Pérdida de motivación | IH | [ABIERTA] |
| **Sapiengraph** (equipo Proxycurl) | Marca nueva con equipo de marketing | **740 $ MRR** al lanzar; sin keywords de volumen; no rankea | TAM demasiado general | IH mar-2024 | [ABIERTA] |
| **SuperX pre-historia** (Rob Hallam) | 2,5 años | **5 productos, 0 $ total** | Sin distribución hasta que un post viral trajo clientes | IH feb-2026 | [ABIERTA] |
| **Steven Goh pre-Proxycurl** | 3 empresas cerradas (NuMoney, SharedHere…) | "6 empleados financiados con side-projects, ingresos muriendo" | — | IH ene-2023 | [ABIERTA] |
| **PricingBot** (Pierre de Wulf) | 12 meses | **3 clientes, 600 $ MRR**; ext. Chrome 3.000 usuarios sin pagar | "Vitamina, no analgésico" → ScrapingBee 180k $ ARR en 18 meses | IH roundup "SaaS graveyard" (2026) | [ABIERTA] (fuente secundaria) |
| **LeaderBird** (KP) | 2.º SaaS del año | Cerrado jul-2023 | Riesgo de plataforma (API X) | kp.substack | [ABIERTA] |
| **Magic Sales Bot** (Ryan Doyle) | 1,5 años | 1k $ MRR, financiado por Calm Fund | "Producto malo" → pivot a agencia | IH jul-2024 | [ABIERTA] |
| Ryan Goodman (add-on, Practical Founders) | 3 años de wind-down | 1,5M $, 700 clientes, 8 empleados | Absorción de features/ecosistema | practicalfounders.com | [ABIERTA] (resumen) |
| Voiczy (€118, 11 clientes, oct-2024→jul-2025) | — | — | — | citado por buscador | **NO ENCONTRADO** |
| Datos agregados Product Hunt / Starter Story | — | — | — | — | **NO ENCONTRADO** (sólo el 97,4 % de 3.ª mano) |

---

## 3. Qué tienen en común los casos de fundador solo (o casi) por encima de 100.000 $/año

Casos solos con >8,3k $ MRR localizados: Zigpoll (125k), Shift (50k), ScreenshotOne (25k+), Youform (18k), EmailEngine (13k), Taskforce.sh (44k verif.), AgentOS (9,5k), Vaultaire (41k brutos, B2C), más Buttondown (solo durante años) y Centori (servicio). Patrón:

1. **Canal**: ninguno tiene el correo frío como canal principal. Dominan **marketplace/ecosistema ajeno** (Shopify, App Store, Heroku/AWS, Slack/Teams), **open source como distribución** (Taskforce/BullMQ, EmailEngine/Nodemailer, Polotno/Konva), **SEO/contenido de nicho** y **comunidades** (Reddit, Laravel). El outbound aparece sólo como complemento (Lancer, Gojiberry, Rezi "cierres B2B").
2. **Nicho**: B2B o prosumer técnico muy estrecho (devs, IT admins, tiendas Shopify, agencias). Stripe Atlas: la mediana B2B solo gana >4x la B2C a 24 meses; ChartMogul: ARPA alto = retención.
3. **Precio**: tickets bajos-medios por asiento (≈ 12–79 $/mes; ScreenshotOne ≈ 30 $/cliente, SuperX 39 $) pero con **cientos de clientes** (650–800) o bien contratos mayores (Pckgr, Polotno 200 clientes a 60k $ MRR, Zigpoll). MicroConf: planes de entrada ≥ 1.000 $/mes añaden 3x más MRR nuevo que los de 1–9 $.
4. **Años**: 4–10 años hasta las cifras citadas (Shift 10, Buttondown 9, Taskforce ~7, Dealsourcr ~6 a 500k ARR, Polotno 6, EmailEngine 5, ScreenshotOne 4, Zigpoll "2 años hasta tracción" y luego dobla). Los "2 meses → 10k $" (Lancer, AgentOS) tienen detrás un exit de agencia o 20 años de dominio. TrustMRR: mediana 1,1 años hasta 10k $ y 2,2 hasta 100k $ **sólo entre los que llegan**; mediana por antigüedad año 5 = 2.509 $/mes.
5. **Experiencia/colchón previo**: casi todos tenían **exit o producto previo, agencia, empleo FT paralelo o reputación OSS**: Zigpoll (2 SaaS previos), Vaultaire (ex-Google, exit Pex), SavvyCal (Drip), LeadDelta (Autoklose), Gojiberry (CocoAI 7 cifras), Lancer (agencia 7 cifras), Outseta (Buildium), Buttondown (Stripe/Amazon), Nventr (family office), Proxycurl (ahorros cripto + extensión con 1,5M usuarios). Los que empezaron "sin nada" declarado (PostFast, Leadverse, Jobric, Bazzly, Youform) están entre 1k y 18k $ MRR y mantienen empleo o freelance.

**¿Cuántos de los >100k $/año empezaron sin audiencia y con outbound?** De los ~12 casos solos o de 2 personas que superan 100k $/año en esta muestra, **0** declaran outbound como canal principal de arranque; **2** lo usaron como canal secundario (Lancer, Gojiberry; ambos con exit previo). Entre los no-solos, Proxycurl y UpLead sí arrancaron con cold email, pero con equipo, capital o 10 años de agencia. TrustMRR muestra que el 54 % de los fundadores con ingresos verificados tiene <1k seguidores en X, es decir, **la "audiencia previa" no es el requisito**; lo que sí aparece en todos es **un canal de distribución prestado** (marketplace, OSS, SEO de nicho, red profesional) o un colchón económico que permite 4-10 años.

---

## 4. Veredicto: **MATIZADA** (confirmada en las tasas base; refutada en la causa que señala)

- **Confirmado**: la mediana de un SaaS indie con pago verificado es ≈ 150–300 $/mes (IH 2021: 303 $ entre los positivos; TrustMRR 2026: 169 $); 50–68 % está a 0 $ o por debajo de 1k $; ~5 % de los fundadores solos verificados en IH supera 10k $ MRR (≈ 100k $/año); Stripe Atlas documenta que la mediana de los solos **cayó 23 % en 2025** mientras el decil superior subió. El correo frío puro, para un técnico solo sin red, rinde cifras como MonitUp (1 venta/año) o SignalsHunt (1 cliente/43 emails) y Belkins mide 0,45 % de respuesta sobre enviados.
- **Matizado / refutado**: (a) "con distribución previa" no equivale a **audiencia**: el 54 % de fundadores con ingresos verificados tiene <1k seguidores y la correlación ingresos~seguidores es débil (r = 0,25); lo que comparten los ganadores es **distribución prestada** (marketplaces, open source, SEO de nicho, red profesional del empleo/agencia anterior) y **tiempo (4-10 años) financiado por un empleo o un exit**. (b) El umbral "2-5 %" es el de 100k $/año; el de **1k $ MRR lo cruza ≈ 30–40 %** de los que persisten (TrustMRR: 67,6 % < 1k acumulado; IH solo: 80,9 % < 500 $ MRR), y el de 10k $ acumulados ≈ 15 %. (c) B2B sí mejora la probabilidad (Stripe Atlas: 4x la mediana B2C; 30 % más presencia en el decil superior), pero **no vía cold email**: los pocos éxitos con cold email como motor (Proxycurl, UpLead, Instantly) tenían equipo, capital o clientes de agencia preexistentes.
- **Conclusión operativa**: para el perfil descrito (solo, sin capital, sin audiencia, sólo correo frío B2B) la evidencia abierta **no muestra ni un caso** por encima de 10k $ MRR en 2024-2026; la vía realista que sí aparece en los datos es **SaaS B2B de nicho con distribución prestada (marketplace/OSS/SEO) + empleo o servicio paralelo durante 2-5 años**, o un servicio productizado vendido por outbound (Cold Email Studio, Sales.co, Centori) que luego se convierte en producto (Instantly, Gojiberry). La afirmación del analista es correcta en su pesimismo sobre el canal, pero atribuye el éxito a la audiencia cuando los datos apuntan a distribución prestada, nicho B2B, retención temprana y años de colchón.

---

## 5. Lagunas y advertencias

- Todas las bases (IH, TrustMRR, MicroConf, Starter Story) son de **autoselección**; los que ganan dejan de publicar (sesgo a la baja) y los que fracasan borran el producto (sesgo al alza). Las cifras de IH "verified" son MRR Stripe; TrustMRR "stats" mezcla ingreso acumulado con MRR.
- Las entrevistas de IH 2025-2026 están **tras muro de registro gratuito**: sólo se leyó la introducción (cifra, equipo, resumen del canal en el índice) y los comentarios.
- Acquire.com no se pudo abrir (JS/404); se usó el PDF de BigIdeasDB (615 listados). TrustMRR marketplace sí muestra listados a 49–945 $ MRR pedidos por 3–40k $.
- NO ENCONTRADO: dato primario del "97,4 % de lanzamientos PH < 1k $ MRR"; estadística de fracasos de Starter Story; post-mortem Voiczy; % de fundadores solos en TinySeed.

---

## 6. Tabla de URLs y estado

| Estado | URL |
|---|---|
| [ABIERTA] | https://belkins.io/blog/cold-email-response-rates |
| [ABIERTA] | https://blog.mean.ceo/?p=11175 |
| [ABIERTA] | https://chartmogul.com/reports/saas-growth-report/ |
| [ABIERTA] | https://chartmogul.com/reports/saas-retention-report/ |
| [ABIERTA] | https://echai.ventures/startingup/cold-outreach/cold-email-or-cold-linkedin-dm-what-works-better-for-reaching-first-customers |
| [ABIERTA] | https://founderpath.com/resources/alan-dsouza-reachinbox-zero-to-6m-arr-affiliates/watch |
| [ABIERTA] | https://founderreports.com/interview/nventr/ |
| [ABIERTA] | https://getlatka.com/blog/new-cold-email-saas-instantly-goes-0-to-2-4m-in-9-months-using-genius-growth-strategy |
| [ABIERTA] | https://getlatka.com/companies/breakcold/interviews/breakcold-arnaud-belinga-2022/watch |
| [ABIERTA] | https://growthhacksuite.com/gmass-solopreneur-case-study |
| [ABIERTA] | https://indiehackers.com/post/400-mrr-in-4-weeks-ac92526ce1 |
| [ABIERTA] | https://instantly.ai/blog/first-100-customers-boostrapped-saas/ |
| [ABIERTA] | https://kp.substack.com/p/new-podcast-episode-and-shutting |
| [ABIERTA] | https://microconf.com/on-air-episodes/7-surprising-saas-trends-every-founder-must-know-in-2024 |
| [ABIERTA] | https://nlxukgfwdfiytdptdwxp.supabase.co/storage/v1/object/public/landing-uploads/saas-reports/state-of-saas-acquisitions-2026.pdf |
| [ABIERTA] | https://nubela.co/blog/how-cold-emailing-grew-my-b2b-startup-to-100k-mrr/ |
| [ABIERTA] | https://practicalfounders.com/articles/saas-founder-wind-down-software-startup/ |
| [ABIERTA] | https://righteous-astrodon-ae1.notion.site/Bootstrapped-B2B-SaaS-Customer-Acquisition-Case-Studies-2171ad19346f80bd905fc801b6d019eb |
| [ABIERTA] | https://scrapingfish.com/blog/indie-hackers-revenue |
| [ABIERTA] | https://shubhq.com |
| [ABIERTA] | https://siddharthsshah.substack.com/p/starting-outbound-sales |
| [ABIERTA] | https://spaces.collab365.com/posts/i-built-my-saas-and-launched-to-zero-customers-B6gbah |
| [ABIERTA] | https://spaces.collab365.com/posts/indie-saas-post-mortems-point-to-no-buyers-not-bad-code-utt3f3m2 |
| [ABIERTA] | https://startupsfyi.beehiiv.com/p/solofounder-makes-30k-mrr |
| [ABIERTA] | https://stateofindiesaas.com |
| [ABIERTA] | https://stripe.com/blog/stripe-atlas-startups-in-2025-year-in-review |
| [ABIERTA] | https://stripe.com/blog/top-solo-founder-traits |
| [ABIERTA] | https://trustmrr.com |
| [ABIERTA] | https://trustmrr.com/ |
| [ABIERTA] | https://trustmrr.com/founder/dharmendra_jago |
| [ABIERTA] | https://trustmrr.com/startups |
| [ABIERTA] | https://trustmrr.com/stats |
| [ABIERTA] | https://www.indiehackers.com/interview/04bead247c |
| [ABIERTA] | https://www.indiehackers.com/interview/9a3be77924 |
| [ABIERTA] | https://www.indiehackers.com/interview/bc43574041 |
| [ABIERTA] | https://www.indiehackers.com/interview/how-to-land-big-clients-with-cold-emailing-d28c409172 |
| [ABIERTA] | https://www.indiehackers.com/post/0-10k-mrr-in-3-5-months-a-step-by-step-guide-on-exactly-what-i-did-1f3ce44511 |
| [ABIERTA] | https://www.indiehackers.com/post/0B3bsTvvOG0wqf8cAx1v |
| [ABIERTA] | https://www.indiehackers.com/post/1BjFvs2akwfIVjMGYO54 |
| [ABIERTA] | https://www.indiehackers.com/post/24ddaphAJ0Zn3m4RKtqc |
| [ABIERTA] | https://www.indiehackers.com/post/4d64o9ev4AXXhX9ogHQQ |
| [ABIERTA] | https://www.indiehackers.com/post/5-days-0-signups-im-shutting-down-my-saas-before-writing-a-single-line-of-backend-code-8dca5b1e12 |
| [ABIERTA] | https://www.indiehackers.com/post/686390baa2 |
| [ABIERTA] | https://www.indiehackers.com/post/7FrT6FXChPOiUK4PbXFp |
| [ABIERTA] | https://www.indiehackers.com/post/9GL6b2gcc31LXjx7g3yC |
| [ABIERTA] | https://www.indiehackers.com/post/BsxsALYvpfriOYumgU0l |
| [ABIERTA] | https://www.indiehackers.com/post/BsyblK2pmWMVfkex10nU |
| [ABIERTA] | https://www.indiehackers.com/post/EprPnCt0LAVt0dmZoniL |
| [ABIERTA] | https://www.indiehackers.com/post/FF8kooe4FWGH9sHjVrT3 |
| [ABIERTA] | https://www.indiehackers.com/post/Hp57IRVPq7v51y4jVDiD |
| [ABIERTA] | https://www.indiehackers.com/post/IKfGcwhlcGQDnjExin8A |
| [ABIERTA] | https://www.indiehackers.com/post/ImP80g1nYgxFyHHRoh1E |
| [ABIERTA] | https://www.indiehackers.com/post/JhX6p14De0nagI0j1Xg1 |
| [ABIERTA] | https://www.indiehackers.com/post/N2V1Oud7cNE3G5xRP1wz |
| [ABIERTA] | https://www.indiehackers.com/post/U9btJ44RYRcAaukCqHoj |
| [ABIERTA] | https://www.indiehackers.com/post/eL15KZvm2ax20BtiM5i8 |
| [ABIERTA] | https://www.indiehackers.com/post/eb5timbPqFlDFWZjha9i |
| [ABIERTA] | https://www.indiehackers.com/post/ekxDn4Rdn8zD3uZU2asY |
| [ABIERTA] | https://www.indiehackers.com/post/got-my-first-4-paying-customers-mrr-107-c1f49a2020 |
| [ABIERTA] | https://www.indiehackers.com/post/hitting-125k-mrr-as-a-solo-founder-by-doubling-down-on-the-right-segment-c4o2Tfs6mjdpip5yZhaO |
| [ABIERTA] | https://www.indiehackers.com/post/hitting-7k-mrr-in-2-years-here-are-the-only-channels-of-customer-acquisition-that-actually-worked-f182e1e72a |
| [ABIERTA] | https://www.indiehackers.com/post/holy-heck-maybe-this-isnt-that-hard-f8b4e64536 |
| [ABIERTA] | https://www.indiehackers.com/post/how-being-arrested-for-cyber-crimes-led-to-a-100k-mrr-business-steven-goh-shares-his-growth-journey-3edb31b230 |
| [ABIERTA] | https://www.indiehackers.com/post/how-cold-emailing-grew-my-b2b-startup-to-100k-mrr-62393f7911 |
| [ABIERTA] | https://www.indiehackers.com/post/how-i-sold-my-saas-for-2-200-instead-of-shutting-it-down-cfc1c3f4e3 |
| [ABIERTA] | https://www.indiehackers.com/post/how-i-took-my-saas-from-0-to-5k-mrr-in-120-days-using-cold-emails-d4f5f56b45 |
| [ABIERTA] | https://www.indiehackers.com/post/how-much-money-do-indie-hackers-products-make-74db9631f0 |
| [ABIERTA] | https://www.indiehackers.com/post/how-to-get-your-first-10-customers-with-cold-email-42ac291f0f |
| [ABIERTA] | https://www.indiehackers.com/post/how-to-hit-10k-mrr-with-cold-email-as-a-service-within-3-months-without-experience-4d8412994e |
| [ABIERTA] | https://www.indiehackers.com/post/i-analyzed-5-079-stripe-verified-startups-f0f6bd053f |
| [ABIERTA] | https://www.indiehackers.com/post/i-bootstrapped-my-saas-uplead-to-8-4m-in-3-years-ama-52a4d58e13 |
| [ABIERTA] | https://www.indiehackers.com/post/i-cold-emailed-our-way-to-1m-arr-in-18-months-heres-the-story-dc078b4321 |
| [ABIERTA] | https://www.indiehackers.com/post/i-reached-6k-people-on-linkedin-and-finally-sold-b350ee57d9 |
| [ABIERTA] | https://www.indiehackers.com/post/i-sent-43-cold-emails-with-my-own-tool-17-replied-1-paid-heres-the-unofficial-launch-329774e623 |
| [ABIERTA] | https://www.indiehackers.com/post/indie-hackers-are-making-60-million-in-stripe-verified-arr-bac07f782d |
| [ABIERTA] | https://www.indiehackers.com/post/j5pMaED5FEbKw8qmeyj9 |
| [ABIERTA] | https://www.indiehackers.com/post/jQRZDnzwm8DFAaS4Xrq0 |
| [ABIERTA] | https://www.indiehackers.com/post/lzinCpsk21EfLwzEiubO |
| [ABIERTA] | https://www.indiehackers.com/post/making-bank-as-a-solo-founder-seems-to-be-rare-3f1ef6ee3e |
| [ABIERTA] | https://www.indiehackers.com/post/microconfs-state-of-independent-saas-survey-4b5f7d453e |
| [ABIERTA] | https://www.indiehackers.com/post/my-tiny-startup-just-hit-1k-mrr-solo-founder-0d76084647 |
| [ABIERTA] | https://www.indiehackers.com/post/our-first-customer-with-personalized-cold-email-d0940bcc57 |
| [ABIERTA] | https://www.indiehackers.com/post/rl7FbRceFPj4ZvI0nGoV |
| [ABIERTA] | https://www.indiehackers.com/post/sTo5m9qfhxXbruvhBIyH |
| [ABIERTA] | https://www.indiehackers.com/post/share-your-story-how-did-you-find-your-very-first-paying-customer-for-b2b-saas-product-a55e277e4e |
| [ABIERTA] | https://www.indiehackers.com/post/tacryeGIH66SCtD2an4r |
| [ABIERTA] | https://www.indiehackers.com/post/the-exact-playbook-i-used-to-reach-1k-mrr-no-audience-no-ads-tn8xDXbSRelPtzevf3tM |
| [ABIERTA] | https://www.indiehackers.com/post/the-saas-graveyard-is-paved-with-cool-ideas-8-brutal-mistakes-indie-founders-make-686390baa2 |
| [ABIERTA] | https://www.indiehackers.com/post/turning-cold-email-into-a-90k-mrr-business-while-traveling-the-world-eQa83dCBNztwvK9KqqH5 |
| [ABIERTA] | https://www.indiehackers.com/post/uS8zjhggjKA4eoXFAUZi |
| [ABIERTA] | https://www.indiehackers.com/post/we-built-a-directory-of-real-founder-stories-from-0-to-1k-mrr-6770dbc12f |
| [ABIERTA] | https://www.indiehackers.com/post/we-built-proxycurl-into-a-7-figure-business-watch-us-fail-with-sapiengraph-2b24c07e35 |
| [ABIERTA] | https://www.indiehackers.com/post/we-spent-2-years-building-a-side-project-got-20-000-users-made-0-then-we-shut-it-down-e2bd45dde0 |
| [ABIERTA] | https://www.indiehackers.com/post/xkng30lczEuiLG4983UN |
| [ABIERTA] | https://www.indiehackers.com/post/y1bbTHkoRJmfJzMEmPsT |
| [ABIERTA] | https://www.indiehackers.com/product/appraiseitnow |
| [ABIERTA] | https://www.indiehackers.com/product/browserless |
| [ABIERTA] | https://www.indiehackers.com/product/cloud-campaign |
| [ABIERTA] | https://www.indiehackers.com/product/dealsourcr |
| [ABIERTA] | https://www.indiehackers.com/product/ghost |
| [ABIERTA] | https://www.indiehackers.com/product/gigalixir |
| [ABIERTA] | https://www.indiehackers.com/product/postiz |
| [ABIERTA] | https://www.indiehackers.com/product/quotaguard |
| [ABIERTA] | https://www.indiehackers.com/product/rezi |
| [ABIERTA] | https://www.indiehackers.com/product/savvy-nomad |
| [ABIERTA] | https://www.indiehackers.com/product/sitebot-ai/shutting-down--LzaLU_ncJbCPvP1Qdni |
| [ABIERTA] | https://www.indiehackers.com/product/taskforce-sh |
| [ABIERTA] | https://www.indiehackers.com/product/taxx |
| [ABIERTA] | https://www.indiehackers.com/product/virlo |
| [ABIERTA] | https://www.indiehackers.com/product/whaticket |
| [ABIERTA] | https://www.indiehackers.com/products |
| [ABIERTA] | https://www.indiehackers.com/products?revenueVerification=stripe&maxRevenue=1000 |
| [ABIERTA] | https://www.indiehackers.com/products?revenueVerification=stripe&maxRevenue=500&sorting=highest-revenue |
| [ABIERTA] | https://www.indiehackers.com/products?revenueVerification=stripe&sorting=highest-revenue&page=2 |
| [ABIERTA] | https://www.indiehackers.com/products?revenueVerification=stripe&sorting=highest-revenue&teamSize=1 |
| [ABIERTA] | https://www.indiehackers.com/products?revenueVerification=stripe&sorting=lowest-revenue |
| [ABIERTA] | https://www.indiehackers.com/products?revenueVerification=stripe&teamSize=1&maxRevenue=1000 |
| [ABIERTA] | https://www.indiehackers.com/products?revenueVerification=stripe&teamSize=solo |
| [ABIERTA] | https://www.lightercapital.com/blog/2025-b2b-saas-startup-benchmarks |
| [ABIERTA] | https://www.saas-capital.com/research/private-saas-company-growth-rate-benchmarks/ |
| [ABIERTA] | https://www.saashero.net/strategy/low-budget-b2b-saas-channels/ |
| [ABIERTA] | https://www.sidetool.co/post/one-person-saas-success-stories-real-revenue-2025/ |
| [ABIERTA] | https://www.softwaredesign.ing/blog/real-world-stats-for-bootstrapping |
| [ABIERTA] | https://www.starterstory.com/data |
| [ABIERTA] | https://www.starterstory.com/explore?revenue=verified |
| [ABIERTA] | https://www.startupsfortherestofus.com/episodes/episode-721-7-key-takeaways-from-the-2024-state-of-independent-saas-report |
| [ABIERTA] | https://www.startupsfortherestofus.com/episodes/episode-812-the-2025-state-of-tinyseed |
| NO ABIERTA (HTTP 403) | https://www.producthunt.com/p/anysite/who-actually-launched-on-product-hunt-in-2026 |
| NO ABIERTA (HTTP 404) | https://acquire.com/startups-for-sale/ |
| NO ABIERTA (HTTP 404) | https://acquire.com/startups-for-sale/saas/ |
| NO ABIERTA (HTTP 404) | https://acquire.com/startups/ |
| NO ABIERTA (HTTP 404) | https://hub.causo.ai/guides/first-100-paying-customers-channel-mix-2026 |
| NO ABIERTA (HTTP 404) | https://microconf.com/state-of-independent-saas-2023 |
| NO ABIERTA (HTTP 404) | https://microconf.com/state-of-independent-saas-2024 |
| NO ABIERTA (HTTP 404) | https://microconf.com/state-of-independent-saas-2025 |
| NO ABIERTA (HTTP 404) | https://nathanbarry.com/direct-sales/ |
| NO ABIERTA (HTTP 404) | https://polder.substack.com/p/im-shutting-down-my-profitable-saas |
| NO ABIERTA (HTTP 404) | https://trustmrr.com/leaderboard |
| NO ABIERTA (HTTP 404) | https://trustmrr.com/startup/thisiswhyibuilt-com |
| NO ABIERTA (HTTP 404) | https://www.indiehackers.com/post/837-mrr-0-in-3-months-why-my-successful-saas-died-and-the-4-brutal-lessons-thats-save-your-startup-99ec07e2b9 |
| NO ABIERTA (HTTP 404) | https://www.indiehackers.com/post/cold-emails-are-adding-400-mrr-per-month-to-my-saas-1500f2c7b4 |
| NO ABIERTA (HTTP 404) | https://www.indiehackers.com/post/f3a0c3df3f |
| NO ABIERTA (HTTP 404) | https://www.indiehackers.com/product/apiframe |
| NO ABIERTA (HTTP 404) | https://www.indiehackers.com/product/zanfia |
| NO ABIERTA (HTTP 404) | https://www.starterstory.com/failure-stories |
| NO ABIERTA (HTTP 405) | https://microconf.com/saas-this-year |
| NO ABIERTA (HTTP 405) | https://microconf.com/state-of-independent-saas |
| [FRAGMENTO] (429 rate-limit) | https://bigideasdb.com/docs/revenue-benchmarks |
| [FRAGMENTO] (429 rate-limit) | https://bigideasdb.com/docs/trustmrr-overview |
| [FRAGMENTO] (429 rate-limit) | https://bigideasdb.com/solo-developer-saas-monthly-revenue-examples |
| [FRAGMENTO] (429 rate-limit) | https://bigideasdb.com/state-of-saas-valuations-2026 |
| [ABIERTA] (PDF, curl) | https://nlxukgfwdfiytdptdwxp.supabase.co/storage/v1/object/public/landing-uploads/saas-reports/state-of-saas-acquisitions-2026.pdf |
| [ABIERTA] | https://microconf.com/founders/0-10k-arr |
| [ABIERTA] | https://microconf.com/founders/10k-100k-arr |
| [ABIERTA] | https://microconf.com/founders/pre-rev |
| [ABIERTA] (formulario; el PDF del informe exige email) | https://microconf.com/saas-this-year · https://stateofindiesaas.com |
| [FRAGMENTO] (solo vía buscador) | https://www.indiehackers.com/post/holy-heck-maybe-this-isnt-that-hard-f8b4e64536 (998 productos, 48,7 % a 0 $) |
| [FRAGMENTO] (solo vía buscador) | https://changelog.com/news/9llJ · https://bigideasdb.com/state-of-saas-valuations-2026 · https://spaces.collab365.com/posts/i-built-my-saas-and-launched-to-zero-customers-B6gbah |
| NO ENCONTRADO | Post-mortem "Voiczy"; estadística de fracasos de Starter Story; fuente primaria del "97,4 %" de Product Hunt |

Nota: las entradas marcadas [ABIERTA] con URL de Indie Hackers `/post/<id>` (entrevistas 2025-2026) se leyeron hasta el muro "Create a Free Account"; cifra, equipo y canal proceden de la introducción, el índice de secciones y los comentarios.
