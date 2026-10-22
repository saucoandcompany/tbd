# Refutación / contraste: "monetizar atención ya no es vía realista en 2025-2026" (webs con anuncios, YouTube sin cara e infantil, apps gratuitas con publicidad)

Fecha de la investigación: 22-10-2026. Método: apertura directa de páginas (Playwright/curl) desde el entorno; cada cifra lleva fuente, año, muestra y definición. Etiquetas: **[ABIERTA]** = página leída entera o en la parte relevante; **[FRAGMENTO]** = página abierta pero el dato clave no se cargó (JS/paywall) o se lee de forma parcial; **NO ENCONTRADO** = no se pudo abrir ninguna fuente primaria. "Autodeclarado" = cifra que da el propio interesado (creador, red publicitaria, vendedor); "verificado" = dato medido por un tercero con muestra descrita. Las conversiones usan 1 € ≈ 1,08 $.

Tesis del analista a contrastar: *"los negocios de monetizar atención ya no son una vía realista en 2025-2026 para alguien que empieza solo y sin capital: el tráfico orgánico se ha hundido con las actualizaciones de Google y las AI Overviews, YouTube penaliza el contenido repetitivo y el 'made for kids' paga CPM bajos, y la distribución de ingresos de apps es de ley de potencias extrema".*

---

## 0. Resumen de veredictos

| Vía | Veredicto | Motivo en una línea |
|---|---|---|
| Webs de contenido con anuncios (SEO como canal) | **CONFIRMADA** (con condiciones estrechas de excepción) | Caídas verificadas del 85-94 % en sitios independientes de calidad (HouseFresh, Retro Dodo, Travel Lemming), CTR −34,5 % a −60 % con AI Overviews, Ezoic sube el mínimo a 250.000 usuarios/mes (feb-2026), Raptive exige tráfico mayoritario US/UK/CA/AU/NZ. Lo que el analista exagera: la barrera de entrada (Journey by Mediavine acepta desde 1.000 sesiones; Raptive desde 25.000 PV, no 100.000). |
| YouTube infantil replicado ("Cocomelon-like") | **CONFIRMADA** | RPM de canal infantil "fuerte" ≤ 1 $ (Kidscreen, oct-2025, fuentes de la industria); hacen falta ~9 M de visualizaciones/mes para 100.000 €/año. Política de monetización literal: el contenido "mass-produced, generic, repetitive" no es elegible. |
| YouTube sin cara (no infantil) | **MATIZADA** | La política del 15-jul-2025 no prohíbe el "sin cara": renombra "repetitious" → "inauthentic" y mantiene sin cambios la política de contenido reutilizado (comentario, clips, compilaciones). Con RPM inglés 5,6-10,8 $ bastan 0,8-1,6 M de vistas/mes para 100.000 €/año; en español (RPM ≈ 1,65 $) hacen falta ~5,5 M/mes. No se pudo abrir ningún caso verificado 2024-2026 con pagos. |
| Apps gratuitas con publicidad / apps indie | **MATIZADA** | Ley de potencias confirmada (RevenueCat 2026: 17,3 % de apps nuevas llegan a 1.000 $/mes y 4,6 % a 10.000 $/mes en 2 años; top 5 % gana 400× el cuartil inferior). Pero "no realista" es demasiado fuerte: ≈1 de cada 22 apps nuevas de suscripción llega a ~100.000 €/año en 24 meses, una tasa medible y superior a la de un sitio SEO nuevo hoy. Para apps *solo con anuncios* no se encontró fuente abierta de eCPM 2025-2026 por región (NO ENCONTRADO). |

---

## 1. Webs de contenido con anuncios

### 1.1 Requisitos de entrada a las redes (2025-2026)

| Red | Requisito actual (literal) | Fuente / estado |
|---|---|---|
| **Ezoic** | "Services are determined by your businesses average monthly users -- with **250,000/mo being the required minimum**." Programa Incubator: "20 sites or apps are selected each month by Ezoic… There are no exceptions to the audience requirement or the selection process." Sitios activos antes del **18-feb-2026** exentos. | ezoic.com/pricing/ y ezoic.com/incubator/ **[ABIERTA]** (2026) |
| **Raptive** | "Your site consistently receives at least **25,000 pageviews (PVs)** each month. Your content is 100% original. **The majority of your traffic comes from the United States, Canada, the United Kingdom, Australia, or New Zealand**." Garantía de RPM solo si "at least 100,000 monthly PVs… and earned $12,000+ in net advertising revenue over the past 12 months". | raptive.com/creators/ **[ABIERTA]** (2026) |
| **Mediavine** | 50.000 sesiones/mes (confirmado indirectamente: "significantly lower than Mediavine's traditional 50,000-session requirement"). **Journey by Mediavine** "accepts applications with as few as **1,000 monthly sessions**"; exige instalar Grow 30 días. Mediavine declara "20,000+ publishers, 114M+ monthly visitors". | PPC Land, AMA del CEO Eric Hochberger 17-sep-2025 **[ABIERTA]**; journeymv.com **[ABIERTA]**; mediavine.com **[ABIERTA]**. La página oficial de requisitos de Mediavine dio 404 en 5 URLs → el 50.000 es **[FRAGMENTO]** vía fuente secundaria. |

**Lectura.** El analista cita "Raptive 100.000 PV": hoy el umbral de entrada es 25.000 PV (100.000 es solo para la garantía de RPM). El "Ezoic sin mínimo" de 2020-2024 ha desaparecido: 250.000 usuarios/mes. Y Raptive excluye de facto a un sitio en español (tráfico mayoritario debe ser anglosajón). Es decir: **entrar es más fácil por abajo (Journey) y más difícil por el medio (Ezoic) que lo que dice el analista**, y la lengua española queda fuera de la red premium.

Derivada útil: la garantía de Raptive (12.000 $ netos / 1.200.000 PV anuales) implica un suelo de **≈10 $ de RPM** (por 1.000 páginas vistas) para sitios anglosajones ya monetizados. No se abrió ningún índice público de RPM por nicho de Mediavine ni el "Ad Revenue Index" de Ezoic (URLs 404) → **RPM web por nicho 2025-2026: NO ENCONTRADO como fuente primaria.**

### 1.2 Impacto de Helpful Content Update (2023-24) y AI Overviews (2025-26)

Casos con cifras (autodeclaradas por el sitio, pero con Search Console mostrado y/o cotejadas por prensa):

- **HouseFresh** (reseñas de purificadores, EN): "Google's latest algorithm update led to a **91% loss of search traffic** to HouseFresh… since October 2023, we've gone from welcoming **4,000 people from Google Search each day to just receiving 200**." (housefresh.com, 2024, **[ABIERTA]**). Artículo "How Google is killing independent sites like ours", actualizado 17-dic-2025, mantiene la queja: "we're getting less and less traffic… endangering the future of our site" **[ABIERTA]**.
- **Retro Dodo** (retro gaming, EN, 2 personas + equipo): "Since September 2023, Google has hidden our site… reducing our organic traffic and revenue by **85%**" (retrododo.com, abr-2024, **[ABIERTA]**, con captura de Search Console/Ahrefs). CNET (dic-2024, **[ABIERTA]**): "traffic to Retro Dodo is **down 90%**, according to Google Search results performance data given to CNET… He's had to lay off his entire staff."
- **Travel Lemming** (viajes, EN): "**94% drop in search traffic** earlier this year, according to traffic data that Hake shared with CNET" (CNET dic-2024, **[ABIERTA]**).
- Retro Dodo cita el estudio de concentración: "Just 16 media companies who own over 400+ websites receive over 3.8 billion clicks a month from Google" (autodeclarado/secundario).
- **The Planet D**: la página del caso dio 404 en dos URLs y la búsqueda interna del sitio no lo devuelve → **NO ENCONTRADO**.

Estudios con muestra (verificados por terceros):

| Estudio | Muestra / fecha | Hallazgo |
|---|---|---|
| Ahrefs "AI Overviews Reduce Clicks by 34.5%" | 300.000 keywords informativas, abr-2025 **[ABIERTA]** | Presencia de AIO ↔ **CTR −34,5 %** para el primer resultado orgánico. |
| Pew Research | 900 adultos EE. UU. con tracking de navegación, mar-2025, publicado jul-2025 **[ABIERTA]** | Con AIO los usuarios clican un resultado en **8 %** de visitas vs **15 %** sin AIO; solo **1 %** clica un enlace citado en la AIO; **18 %** de las búsquedas mostraron AIO. |
| Semrush AI Overviews Study 2025 | 10 M de keywords (según el estudio), ene-nov 2025 **[ABIERTA]** | AIO en **6,49 %** de queries (ene-25) → **24,61 %** (jul-25) → **15,69 %** (nov-25). Intención informativa de las AIO cae de 91,3 % a 57,1 %; comercial sube de 8,15 % a 18,57 %; transaccional de 1,98 % a 13,94 %. ~60 % de keywords con AIO tienen ≤100 búsquedas/mes. |
| Semrush AI Overviews Study (1ª) | 200.000 keywords **[ABIERTA]** | 80 % informativas; solapamiento AIO/top-10 solo 20-26 %. |
| SparkToro/Datos 2024 zero-click | panel clickstream EE. UU./UE, jul-2024 **[ABIERTA]** | Por cada 1.000 búsquedas en Google, **360 clics (US) / 374 (EU)** van a la web abierta. |
| Press Gazette (Sistrix, Ipsos iris) | mayo-2026 **[ABIERTA]** | Con AIO arriba, CTR de la 1ª posición cae de **27 % a 11 %** (−60 %). Salud: AIO en 72 % de resultados; **Healthline −48 % de audiencia interanual**; People Inc **−63 % de tráfico Google en dos años**. Tech 49 %, viajes 39 %, dinero 35 % de AIO; fútbol 5 %, puzles 7 %. |
| AdExchanger | ene-2026 **[ABIERTA]** | Publishers reconocen pérdidas de "20%, 30% and in some cases even as much as 90% of their traffic"; Seer Interactive: CTR orgánico 1,6 % sin AIO → 0,6 % con AIO; Mail Online: CTR 13 %/20 % (desk/móvil) → 5 %/7 % con AIO. |
| TechCrunch (Similarweb vía WSJ) | jun-2025 **[ABIERTA]** | NYT: tráfico orgánico pasa de 44 % (2022) a 36,5 % (abr-2025) del total. |
| Google (blog.google) | mar/abr-2024 **[ABIERTA]** | "reduce low-quality, unoriginal content in search results by **40%**… You'll now see **45% less** low-quality, unoriginal content" (declaración de la propia Google). |

### 1.3 Mercado de compraventa de sitios (Flippa / Empire Flippers / Motion Invest)

- **Empire Flippers marketplace** **[ABIERTA]**: un único listado de contenido visible sin login: "Technology, Information, News & Education, Gaming — Monetization Amazon Associates, Display Advertising, Affiliate — Price **$2,756,567** — Net Profit **$765,713**" → múltiplo ≈ **3,6× beneficio anual (≈43× mensual)**. El informe "State of the Industry" redirige a un PNG → **[FRAGMENTO]**.
- **Flippa Data Insights** **[ABIERTA]** (navegador): existe panel "Profit & Revenue Multiples" por categoría (Content, App, YouTube…) desde 2021H2, pero los valores quedaron en "Loading..." → **[FRAGMENTO]**. Su portada afirma: "Top-quartile assets are pulling 2.7x higher multiples. AI tools are fetching half-million-dollar exits." (autodeclarado del marketplace).
- **Motion Invest**: la página de sitios en venta es 100 % JS, 227 bytes de texto → **NO ENCONTRADO**.
- Mediana de ingresos de sitios en venta 2025-2026 y % que han caído: **NO ENCONTRADO** (ningún informe primario abierto).

### 1.4 Casos de sitios nuevos que lleguen a 1.000 €/mes en 12 meses (2025-2026)

- **Fat Stacks Blog** (Jon Dykstra) **[ABIERTA]**, abr-2026: "I don't publish those anymore" (dejó de publicar informes de ingresos; el último visible: "Revenue (Ads+others): $116,434 — Expenses: $27,038 — Profit: $89,396", sin fecha legible y para una cartera madura, no un sitio nuevo).
- Niche Pursuits: buscador interno sin resultados de "income report 2025" → **NO ENCONTRADO**.
- Reddit, Indie Hackers: 403.
- **Conclusión: no se pudo abrir ni un solo caso 2025-2026 de sitio nuevo con 1.000 €/mes verificable (GA4 o pagos).** Los dos únicos ejemplos de ingresos en páginas abiertas son de sitios de 2015-2019 (HouseFresh, Retro Dodo) y están en caída.

### 1.5 Cálculo: cuánto tráfico para 100.000 €/año (≈108.000 $) y para 1.000 €/mes

Fórmula: PV necesarias = ingresos / (RPM/1000).

| RPM (por 1.000 PV) | Base | PV/año para 100.000 €/año | PV/mes | PV/mes para 1.000 €/mes |
|---|---|---|---|---|
| 25 $ (nicho EN premium, Raptive/Mediavine, Q4) | supuesto razonable, sin fuente primaria abierta | 4,3 M | **360.000** | 43.000 |
| 10 $ (suelo implícito en la garantía Raptive: 12.000 $/1,2 M PV) | derivado de raptive.com **[ABIERTA]** | 10,8 M | **900.000** | 108.000 |
| 3 $ (español; aplicando la ratio ES/EN de YouTube 1,65/5,64 ≈ 0,29 a un RPM web EN de 10 $) | derivado de Lenos 2026 **[ABIERTA]** + supuesto | 36 M | **3.000.000** | 360.000 |

Con el CTR del primer resultado cayendo de 27 % a 11 % cuando hay AIO (Sistrix) y AIO presentes en 15-25 % de queries (Semrush), el volumen de búsquedas que hay que "ganar" para sostener 900.000 PV/mes se multiplica por ~2,5 frente a 2023.

### 1.6 Veredicto webs con anuncios: **CONFIRMADA**, con estas excepciones en 2026

Funciona si se cumplen a la vez: (a) contenido en inglés con audiencia mayoritaria US/UK/CA/AU/NZ (requisito literal de Raptive; RPM 3× el español); (b) nichos donde Google muestra pocas AIO: deportes/fútbol (5 %), puzles (7 %), TV (15 %), noticias de última hora (sin AIO) según Sistrix/Press Gazette; (c) canal de adquisición no dependiente de Google (Pinterest, newsletter, comunidades, YouTube propio) — Journey exige de hecho construir audiencia con Grow 30 días antes de servir anuncios; (d) pruebas o datos propios no replicables por IA (el argumento de HouseFresh). Sin esas cuatro condiciones, los datos abiertos apoyan al analista: el tráfico informativo orgánico se ha hundido y la puerta de Ezoic se ha cerrado.

---

## 2. YouTube sin cara e infantil

### 2.1 Política oficial (literal, página de YouTube Help "YouTube channel monetization policies", answer/1311392 **[ABIERTA]**)

> "**July 15, 2025**: We're making a minor update to our 'repetitious content' policy to better clarify this includes content that is repetitive or mass-produced. We are also renaming this policy from 'repetitious content' to '**inauthentic content**.' This type of content has always been ineligible for monetization under our existing policies, where creators are rewarded for original and authentic content. **There is no change to our reused content policy** which reviews content like commentary, clips, compilations, and reaction videos."

> "If you're making money on YouTube, your content should be original and 'authentic.' This means that we expect your content to: Be your original creation. If you borrow content from someone else, you need to change it significantly to make it your own. **Not be mass-produced, generic, repetitive, or manipulative.** It should be made for the enjoyment or education of viewers, rather than for the sole purpose of getting views."

TechCrunch 9-jul-2025 **[ABIERTA]**: Rene Ritchie (YouTube) lo califica de "minor update… designed to better identify when content is mass-produced or repetitive… this type of content has been ineligible for monetization for years". Xataka 7-abr-2026 **[ABIERTA]**: Neal Mohan declaró el 21-ene-2026 que "combatir el AI slop era la prioridad del año"; siete semanas después el AI Futures Fund de Google invirtió 1 M$ en Animaj (animación infantil generada con IA).

**Requisitos YPP** (answer/72851 **[ABIERTA]**): "1,000 subscribers with 4,000 qualified watch hours in the last 12 months, or 1,000 subscribers with 10 million qualified Shorts views in the last 90 days."

**Made for kids** (answer/9527654 **[ABIERTA]**): "we don't serve personalized ads on kids content, as required by COPPA… Not serving personalized ads on kids content **may result in a decrease in revenue** for some creators." Origen: acuerdo FTC/NY de 170 M$ con Google/YouTube, sep-2019 (ftc.gov **[ABIERTA]**).

### 2.2 CPM/RPM reales por nicho e idioma

| Fuente | Tipo | Dato |
|---|---|---|
| Lenos Tube "YouTube CPM & RPM Rates 2026" (act. 2-abr-2026) **[ABIERTA]** | agregador/agencia, sin muestra publicada → autodeclarado | CPM/RPM por país: Australia 36,21/11,95 $; **EE. UU. 32,75/10,81 $**; Reino Unido 21,59/7,12; Alemania 18,79/6,20; Filipinas 0,48/0,15; Egipto 0,32/0,11. Por idioma: **inglés CPM 10,26 / RPM 5,64 $; español CPM 3,00 / RPM 1,65 $**; portugués 2,00/1,10. Finanzas CPM 15-50 $ (RPM 4,95-16,50); tecnología 5-30 $ (RPM 1,51-9,08). Estacionalidad: RPM 0,53 $ (agosto) a 1,41 $ (octubre) en la serie "media". |
| Kidscreen, "How kids creators are making YouTube work again", 27-oct-2025 **[ABIERTA]** | entrevistas a Animaj, TeamFalco/WildBrain, Soupir (industria) | "Overnight, kids content creators **lost 50% of their earnings** on YouTube on average" (ene-2020). "A strong kids channel can have an RPM… of **US $1 or lower**". "creators typically earn anywhere from US$0.20 to US$8 per 1,000 views… children's channels usually come in on the lower end". "you're looking at multi-million views to be able to build any kind of revenue". Kids & family = 15-20 % del visionado total; mercado publicitario infantil ≈ 4.000 M$. |
| vidIQ, estadísticas Cocomelon (22-oct-2026) **[ABIERTA]** | estimación algorítmica | 1,26 B de vistas en 28 días; ingreso mensual estimado **2,9 M$** → RPM implícito ≈ **2,3 $** (canal líder, inventario propio vendido por Moonbug). Días con 0 $ estimados indican que la estimación es ruidosa. |
| Wikipedia Cocomelon **[ABIERTA]** | enciclopédico | 200 M de suscriptores, 220 B de vistas (abr-2026); Treasure Studio (≈20 empleados) vendido a Moonbug en 2020; Moonbug vendido por 3.000 M$ a Candle Media en 2021. |

Social Blade: 403 incluso con navegador → **NO ENCONTRADO**. Número de canales infantiles en español y copias de Cocomelon: **NO ENCONTRADO** (ninguna fuente con conteo).

### 2.3 Casos documentados 2024-2026

- Monetizados con cifras verificables (pagos/Analytics): **NO ENCONTRADO** (Reddit 403; prensa generalista con titulares — Hollywood Reporter "Faceless Creators Take a Hit", jun-2026; Tech Times "COPPA Cuts Revenue by Up to 80%", jul-2026 — localizados en Google News pero no abiertos → **[FRAGMENTO] solo titular, no se usan como cifra**).
- Desmonetizados: los artículos de TechCrunch y Xataka abiertos describen la política y la prioridad anti-slop, sin casos nominales con cifras.

### 2.4 Cálculo: vistas necesarias para 100.000 €/año (≈108.000 $)

Vistas = 108.000 $ / (RPM/1000).

| Tipo de canal | RPM | Vistas/año | Vistas/mes |
|---|---|---|---|
| Infantil "fuerte" (Kidscreen) | 1,00 $ | 108 M | **9,0 M** |
| Infantil líder (Cocomelon, implícito vidIQ) | 2,3 $ | 47 M | 3,9 M |
| Español, general (Lenos) | 1,65 $ | 65 M | **5,5 M** |
| Inglés, general (Lenos) | 5,64 $ | 19 M | 1,6 M |
| Audiencia EE. UU. (Lenos) | 10,81 $ | 10 M | 0,83 M |
| Finanzas EN, rango (Lenos) | 4,95-16,50 $ | 22-6,5 M | 1,8-0,55 M |

Un canal infantil en español necesita **~6-11× más vistas** que uno en inglés para adultos con el mismo objetivo, y lo hace con el formato explícitamente señalado como "mass-produced/repetitive".

### 2.5 Veredicto

- **Infantil replicado: CONFIRMADA.** RPM ≤1 $, sin anuncios personalizados por ley, 9 M de vistas/mes para 100.000 €/año, formato que encaja en la definición literal de contenido inauténtico, y competencia de estudios con ventas directas de inventario (Moonbug, Animaj, pocket.watch…).
- **Sin cara (no infantil): MATIZADA.** La política no cambió para comentario/clips/compilaciones transformadas y exige "original creation… change it significantly". Condiciones en 2026: guion y voz propios, idioma inglés y audiencia US (RPM 5,6-10,8 $ vs 1,65 $ en español), nicho finanzas/tecnología/educación, y aceptar que no se encontró ningún caso verificado abierto de canal creado en 2024-2026 que lo haya logrado.

---

## 3. Apps gratuitas con publicidad / apps indie

### 3.1 Distribución de ingresos por desarrollador

| Fuente | Muestra | Dato |
|---|---|---|
| **RevenueCat, State of Subscription Apps 2026** **[ABIERTA]** | decenas de miles de apps con SDK RevenueCat (sesgo: apps de suscripción) | "**17.3% hit $1K** [monthly revenue], **4.6% hit $10K**" en los 2 primeros años (todas las categorías). Photo & Video 21,4 %/7,3 %; Gaming 20,0 %/8,9 %; Business 14,7 %/1,6 %. Mediana de días hasta 1.000 $: 58; hasta 10.000 $: 109. Nuevas apps de suscripción/mes: ~2.000 (ene-2022) → **14.700+ (ene-2026)** "likely driven by the AI app explosion", "yet apps launched before 2020 still generate **69% of all subscription revenue**". Mediana de crecimiento MRR interanual 5,3 %; top decil +306 %. RLTV anual por pagador: mediana global 23 $, Norteamérica 32 $, IN/SEA 14 $. |
| **RevenueCat 2025** **[ABIERTA]** | ídem | "At **$8,880** the top 5% of newly launched apps make over **400x** as much money after their first year, compared to the bottom 25% who make no more than **$19**" (gap era 200× el año anterior). "nearly 20% reach $1,000… while 5% reach the $10,000 mark." Apps de IA: ingreso por instalación a 60 días **0,63 $ vs mediana 0,31 $**, "But AI alone won't drive success, differentiation does." |
| **AppBrain** (22-oct-2026) **[ABIERTA]** | conteo Google Play | **2.038.736 apps**; último mes **52.400 nuevas**, 26.800 retiradas. |
| Sensor Tower, State of Mobile 2025 (landing) **[ABIERTA]** | — | gasto de consumidores 150.000 M$ (2024), 4,2 billones de horas. El informe completo exige formulario. |
| Statista (apps por tienda; eCPM por región; % apps con ingresos) **[FRAGMENTO]** | — | cifras ocultas ("***") sin suscripción. |
| Apple Newsroom (estudio del ecosistema 2025) | — | 403/404 en 4 URLs → **NO ENCONTRADO**. |

### 3.2 eCPM de publicidad in-app 2025-2026 por región

**NO ENCONTRADO**: Business of Apps (403), Appodeal (404 en 5 rutas), ironSource/Unity (página sin datos), AdMob (404), Statista (oculto), Mintegral (sin cifras). Se deja como laguna explícita; cualquier cálculo con eCPM es supuesto.

### 3.3 Casos verificables de desarrolladores solos

- Hacker News, "Tell HN: 2 years building a kids audio app as a solo dev – lessons learned" (21-ene-2026, 137 puntos) **[ABIERTA]**: app Muky (iOS, Swift), lanzada abr-2024; "Started with one-time purchase. **Revenue spikes at launch, then nothing.** Switched to subscription… Harder to sell, but sustainable." Sin cifras de ingresos → autodeclarado cualitativo.
- Indie Hackers (403), Reddit r/iOSProgramming (403), Appfigures posts específicos (404) → **NO ENCONTRADO** casos con capturas de App Store Connect.
- a16z "Top 100 Gen AI Consumer Apps, 6ª ed." (mar-2026) **[ABIERTA]**: ranking por MAU (Sensor Tower ene-2026); confirma concentración en ChatGPT/Gemini y productos AI-native; sin datos de cola larga.

### 3.4 "AI wrapper apps": coste y tasa de éxito

Único dato abierto: RevenueCat 2025-2026 (RPI 0,63 $ vs 0,31 $; lanzamientos ×7 en 4 años; el 69 % del ingreso sigue en apps pre-2020). No se abrió ninguna fuente que mida la tasa de supervivencia de wrappers → **[FRAGMENTO]**.

### 3.5 Cálculo: qué hace falta para 100.000 €/año (≈9.000 $/mes)

- **Suscripción** (datos reales RevenueCat): el hito "10.000 $/mes" ≈ 120.000 $/año ≈ 111.000 €/año. Probabilidad medida de alcanzarlo en 24 meses: **4,6 %** (1 de cada 22 apps nuevas de suscripción). Con 14.700 lanzamientos/mes, cada cohorte mensual produce ~676 apps que llegan ahí; las otras ~14.000 no.
- **Solo anuncios** (eCPM supuesto por falta de fuente): 9.000 $/mes ÷ eCPM × 1.000 = impresiones/mes. A 1 $ (banner, tier-2/LatAm): **9 M de impresiones/mes**; a 5 $ (intersticial US): 1,8 M; a 12 $ (rewarded video US): 750.000. Con 10 impresiones/usuario/mes, 1 $ de eCPM exige ~900.000 usuarios activos mensuales; con 12 $, ~75.000.

### 3.6 Veredicto apps: **MATIZADA**

La "ley de potencias extrema" es cierta y está medida (400× entre top 5 % y cuartil inferior; 4,6 % llegan a 10.000 $/mes). Pero el analista salta de ahí a "no realista": con datos abiertos, ~1 de cada 6 apps nuevas de suscripción llega a 1.000 $/mes y ~1 de cada 22 a 10.000 $/mes en 24 meses, sin depender de Google Search ni de la política de YouTube. Condiciones 2026: modelo de suscripción (no solo anuncios), categorías Photo & Video / Gaming / Health & Fitness / Utilities, precio alto (RLTV 34,82 $ vs 10,69 $), audiencia norteamericana, y diferenciación real sobre el modelo (RevenueCat: "AI alone won't drive success"). Para la variante "gratuita con anuncios" no se encontró evidencia abierta en ningún sentido.

---

## 4. Programmatic SEO con IA y política de Google

- **Política oficial** (developers.google.com/search/docs/essentials/spam-policies **[ABIERTA]**): "**Scaled content abuse** is when many pages are generated for the primary purpose of manipulating search rankings and not helping users… no matter how it's created. Examples… Using generative AI tools or other similar tools to generate many pages without adding value for users; Scraping feeds, search results, or other content…; Stitching or combining content from different web pages without adding value; Creating multiple sites with the intent of hiding the scaled nature of the content."
- Anuncio 5-mar-2024 (Search Central Blog **[ABIERTA]**): tres políticas nuevas (expired domain abuse, scaled content abuse, site reputation abuse); "Sites that violate our spam policies may rank lower in results or not appear in results at all." blog.google **[ABIERTA]**: objetivo −40 %, resultado declarado −45 % de contenido "low-quality, unoriginal".
- **Originality.ai**, serie temporal de IA en el top-20 de Google **[ABIERTA]** (detector propio, sesgo de herramienta): 2,27 % (feb-2019) → 8,48 % (dic-2023) → **7,43 % tras la actualización de mar-2024** → 19,56 % (jul-2025) → 17,31 % (sep-2025). Es decir, la penalización de 2024 fue un bache: la proporción de contenido IA en los resultados se **duplicó** después.
- **Ahrefs** **[ABIERTA]**: 900.000 páginas nuevas (abr-2025): **74,2 %** contienen contenido generado por IA.
- Casos con cifras de caída de sitios IA (Byword "SEO heist", estudio de desindexaciones de Originality.ai): 404 en todas las URLs probadas; SEJ sirvió un GIF → **NO ENCONTRADO**.
- HN (jun-2026): "Trying to recover from thin content penalty from Google" (6 puntos) **[ABIERTA solo título]**.

Lectura: la política es explícita y la caída de 2024 fue real, pero el contenido IA ha vuelto a crecer en los resultados; lo que se castiga es la falta de valor añadido, no la herramienta. Para quien empieza solo, el problema no es la prohibición sino que compite contra un 74 % de páginas nuevas también generadas con IA y una CTR en caída.

---

## 5. España / español

- **IAB Spain, Estudio de Inversión Publicitaria en Medios Digitales 2026** (con PwC) **[ABIERTA]**: el mercado digital cerró **2025 con 6.211,2 M€ (+11,2 %)**; Search 1.992,6 M€ (+32,1 %); Redes Sociales 1.832,5 M€ (+29,5 %); dentro de Display, Vídeo 535,2 M€ (+7,9 %); CTV 174 M€ (+48,4 %); Clasificados +20,2 %.
- **IAB Spain, 2ª ola 2026** **[ABIERTA]**: previsión 2026 **6.597-6.801 M€** (+6,2 %/+9,5 %); Search 32 % del total; Redes 29,7 % (1.961,6-2.013,2 M€); **Display −1,2 %/+2,5 %**, "impulsado principalmente por la caída de la Publicidad Nativa… −12,7 %/−7,4 %"; CTV +29,3 %/+40,5 %; Audio digital +21,3 %/+27,3 %; Influencers +10,5 %…
  - Lectura para el solitario: el dinero crece en Search, Social, CTV y audio (plataformas); el **display** —que es lo que cobra una web con anuncios— es el único segmento plano o en caída.
- **RPM en español**: la única cifra abierta es la de YouTube (Lenos 2026: CPM 3,00 $ / RPM 1,65 $ frente a 10,26/5,64 $ en inglés; "CPMs are relatively low due to a large portion of the audience coming from Latin American countries"). RPM web en español 2025-2026 con muestra: **NO ENCONTRADO**. Dato indirecto duro: Raptive exige tráfico mayoritario de US/CA/UK/AU/NZ, lo que excluye a casi cualquier web en español.
- Casos hispanos con cifras (webs o canales): **NO ENCONTRADO** (Blogger3cero, Borja Girón: páginas sin ingresos; ADSLZone/Xataka: artículos localizados pero URL no resuelta). Xataka (abr-2026) aporta el contexto "YouTube sabe que tiene un problema con el slop IA para niños".

---

## 6. Conclusión para el analista

1. **Webs con anuncios: CONFIRMADA.** Las cifras abiertas son peores que las del analista en lo central (−85/−94 % en sitios de calidad; CTR −34,5 %/−60 %; Ezoic a 250.000; display plano en España) y mejores en lo accesorio (Journey 1.000 sesiones, Raptive 25.000 PV). No se encontró ni un caso 2025-2026 de sitio nuevo a 1.000 €/mes verificable.
2. **YouTube infantil replicado: CONFIRMADA** (RPM ≤1 $, 9 M vistas/mes, formato literalmente "inauthentic"). **YouTube sin cara original: MATIZADA** (política sin cambios para contenido transformado; viable en inglés/US con 0,8-1,6 M vistas/mes para 100.000 €/año; sin caso verificado abierto).
3. **Apps: MATIZADA.** La distribución es de ley de potencias (verificado), pero 4,6 % a 10.000 $/mes en 24 meses no es "irreal"; es una lotería con odds conocidas y mejores que las del SEO nuevo. Falta por completo evidencia abierta sobre apps *solo con anuncios* (eCPM 2025-2026 NO ENCONTRADO).

Lagunas honestas: RPM web por nicho (Mediavine/Ezoic índices), eCPM in-app por región, casos individuales con pagos (Reddit/Indie Hackers 403), múltiplos Flippa/EF (JS/PNG), The Planet D, conteo de canales infantiles en español.

---

## 7. Tabla de URLs abiertas / intentadas

| # | URL | Estado | Uso |
|---|---|---|---|
| 1 | https://support.google.com/youtube/answer/1311392 | ABIERTA | Política monetización YouTube, literal 15-jul-2025 |
| 2 | https://support.google.com/youtube/answer/72851 | ABIERTA | Requisitos YPP |
| 3 | https://support.google.com/youtube/answer/9527654 | ABIERTA | Made for kids / COPPA |
| 4 | https://developers.google.com/search/docs/essentials/spam-policies | ABIERTA | Scaled content abuse (literal) |
| 5 | https://developers.google.com/search/blog/2024/03/core-update-spam-policies | ABIERTA (navegador) | Anuncio marzo 2024 |
| 6 | https://blog.google/products/search/google-search-update-march-2024/ | ABIERTA | 40 % / 45 % |
| 7 | https://housefresh.com/how-google-decimated-housefresh/ | ABIERTA | −91 %, 4.000→200/día |
| 8 | https://housefresh.com/david-vs-digital-goliaths/ | ABIERTA | Actualización dic-2025 |
| 9 | https://ahrefs.com/blog/ai-overviews-reduce-clicks/ | ABIERTA | −34,5 % CTR, 300k keywords |
| 10 | https://www.semrush.com/blog/ai-overviews-study/ | ABIERTA | 200k keywords |
| 11 | https://www.semrush.com/blog/semrush-ai-overviews-study/ | ABIERTA | 6,49 %→24,61 %→15,69 % |
| 12 | https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/ | ABIERTA | 8 % vs 15 %, n=900 |
| 13 | https://sparktoro.com/blog/2024-zero-click-search-study-... | ABIERTA | 360/374 clics por 1.000 |
| 14 | https://raptive.com/creators/ | ABIERTA | 25.000 PV; tráfico anglosajón; garantía 100k/12.000 $ |
| 15 | https://www.ezoic.com/pricing/ | ABIERTA | Mínimo 250.000 usuarios |
| 16 | https://www.ezoic.com/incubator/ | ABIERTA | 20 sitios/mes; 18-feb-2026 |
| 17 | https://www.journeymv.com/ | ABIERTA | Journey, Grow 30 días |
| 18 | https://ppc.land/mediavine-ceo-addresses-ai-challenges-and-journey-expansion-in-reddit-ama/ | ABIERTA | Journey 1.000 sesiones; Mediavine 50.000 |
| 19 | https://www.mediavine.com/ | ABIERTA | 20.000 publishers, 114 M visitantes |
| 20 | https://www.retrododo.com/google-is-killing-retro-dodo/ | ABIERTA | −85 % |
| 21 | https://www.cnet.com/tech/services-and-software/google-search-changes-are-killing-websites-in-an-age-of-ai-spam/ | ABIERTA | Retro Dodo −90 %, Travel Lemming −94 % |
| 22 | https://www.adexchanger.com/publishers/the-ai-search-reckoning-is-dismantling-open-web-traffic-and-publishers-may-never-recover/ | ABIERTA | Seer, Mail Online, People Inc |
| 23 | https://pressgazette.co.uk/media-audience-and-business-data/ai-overviews-publisher-traffic/ | ABIERTA | Sistrix 27 %→11 %; Healthline −48 %; People Inc −63 % |
| 24 | https://techcrunch.com/2025/06/10/googles-ai-overviews-are-killing-traffic-for-publishers/ | ABIERTA | NYT 44 %→36,5 % |
| 25 | https://techcrunch.com/2025/07/09/youtube-prepares-crackdown-on-mass-produced-and-repetitive-videos-as-concern-over-ai-slop-grows/ | ABIERTA | Ritchie "minor update" |
| 26 | https://kidscreen.com/2025/10/27/how-kids-creators-are-making-youtube-work-again/ | ABIERTA | RPM infantil ≤1 $; −50 % en 2020 |
| 27 | https://www.ftc.gov/news-events/news/press-releases/2019/09/google-youtube-will-pay-record-170-million-alleged-violations-childrens-privacy-law | ABIERTA (curl) | 170 M$ |
| 28 | https://www.lenostube.com/en/youtube-cpm-rpm-rates-by-niche/ | ABIERTA | CPM/RPM por país, idioma, nicho (autodeclarado) |
| 29 | https://en.wikipedia.org/wiki/Cocomelon | ABIERTA | 200 M subs, 3.000 M$ |
| 30 | https://vidiq.com/youtube-stats/channel/UCbCmjCuTUZos6Inko4u57UQ/ | ABIERTA | Est. 2,9 M$/mes, 1,26 B vistas/28 d |
| 31 | https://www.xataka.com/robotica-e-ia/youtube-invierte-millon-contenido-ia-para-ninos-... | ABIERTA | Mohan anti-slop; Animaj 1 M$ |
| 32 | https://www.revenuecat.com/state-of-subscription-apps-2026/ | ABIERTA | 17,3 % / 4,6 %; 14.700 apps/mes; 69 % pre-2020 |
| 33 | https://www.revenuecat.com/state-of-subscription-apps-2025/ | ABIERTA | 400×; 8.880 $ vs 19 $; IA 0,63 $ RPI |
| 34 | https://www.appbrain.com/stats/number-of-android-apps | ABIERTA | 2,04 M apps; 52,4k nuevas/mes |
| 35 | https://sensortower.com/state-of-mobile-2025 | ABIERTA (landing) | 150.000 M$ gasto |
| 36 | https://a16z.com/100-gen-ai-apps-6/ | ABIERTA | Ranking IA consumo mar-2026 |
| 37 | https://hn.algolia.com/api/v1/items/46705676 (Tell HN kids audio app) | ABIERTA | Caso solo dev, cualitativo |
| 38 | https://originality.ai/blog/ai-content-in-google-search-results | ABIERTA | % IA en SERP 2019-2025 |
| 39 | https://ahrefs.com/blog/what-percentage-of-new-content-is-ai-generated/ | ABIERTA | 74,2 % de 900k páginas |
| 40 | https://iabspain.es/estudio-inversion-publicitaria-medios-digitales-2026/ | ABIERTA | 6.211,2 M€ 2025 |
| 41 | https://iabspain.es/2-ola-inversion-publicitaria-digital-espana-2026/ | ABIERTA | Previsión 2026; Display −1,2/+2,5 % |
| 42 | https://iabspain.es/estudio/estudio-de-inversion-publicitaria-en-medios-digitales-2025/ | ABIERTA | Ficha del estudio 2025 |
| 43 | https://empireflippers.com/marketplace/ | ABIERTA | Listado 2,76 M$ / 765k $ beneficio |
| 44 | https://flippa.com/data-insights | FRAGMENTO | Múltiplos no cargan (JS) |
| 45 | https://fatstacksblog.com/niche-site-income-report/ | ABIERTA | Dejó de publicar informes (abr-2026) |
| 46 | https://www.statista.com/statistics/276623/... y /1346823/... y /1269510/... | FRAGMENTO | Cifras ocultas |
| 47 | https://support.google.com/adsense/answer/9902?hl=es | ABIERTA | Sin dato de RPM |
| 48 | https://empireflippers.com/state-of-the-industry-report/ | FRAGMENTO | Redirige a PNG |
| 49 | https://www.theverge.com/24063327/... y /2024/5/2/24147124/... | FRAGMENTO | Sirve otro artículo (paywall/redirección) |
| — | searchengineland.com (2 URLs) | 403 | NO ENCONTRADO |
| — | similarweb.com/blog (2 URLs) | 202/403 | NO ENCONTRADO |
| — | socialblade.com (curl y navegador) | 403 | NO ENCONTRADO |
| — | businessofapps.com (2 URLs, curl y navegador) | 403 | NO ENCONTRADO |
| — | apple.com/newsroom (4 URLs) | 403/404 | NO ENCONTRADO |
| — | reddit.com / old.reddit.com (3 URLs) | 403 | NO ENCONTRADO |
| — | indiehackers.com (3 URLs) | 403 | NO ENCONTRADO |
| — | mediavine.com requisitos / help.mediavine.com (7 URLs) | 404 | NO ENCONTRADO (50.000 solo vía PPC Land) |
| — | appodeal.com, is.com, admob.google.com, tenjin, publift, monetizemore, setupad, adpushup (eCPM/CPM por país) | 404/sin datos | NO ENCONTRADO |
| — | theplanetd.com (2 URLs + búsqueda interna) | 404 | NO ENCONTRADO |
| — | byword.ai/case-studies/seo-heist; originality.ai estudios desindexación (4 URLs); searchenginejournal.com | 404/410/GIF | NO ENCONTRADO |
| — | motioninvest.com (2 URLs) | 100 % JS | NO ENCONTRADO |
| — | Google News RSS (15 consultas) | ABIERTA | Solo titulares; enlaces cifrados, no resueltos |
