# Mercado hispanohablante: ¿hay fundadores solos (1-3) ganando >100.000 €/año con SaaS o infoproductos sin audiencia previa?

**Fecha:** 22-10-2026 · **Rol:** investigador adversarial (refutar al analista) · **Páginas abiertas con contenido (STATUS 200):** 44 · **Fragmentos (snippet de buscador, página no abierta):** 9

**Tesis del analista:** "En el mercado hispanohablante no hay casos verificables relevantes de fundadores solos ganando más de 100.000 €/año con SaaS o infoproductos sin audiencia previa; lo que hay son agencias, consultores y creadores con años de audiencia".

## Veredicto: MATIZADA (no refutada, no confirmada)

- **Refutado en la parte SaaS 1-3 fundadores:** existen al menos 6 casos hispanos verificables (cifras propias en prensa/entrevistas, o estimaciones de terceros concordantes) de equipos de 1-3 fundadores, bootstrapped, sin audiencia previa, que superaron 100.000 €/año: Metricool (ES), Quaderno (ES), Hevy (ES/CA), SumaCRM (ES), Whaticket (PE), Hower (MX), más Freepik (ES, producto digital no SaaS). En todos, el canal de adquisición fue producto gratuito + SEO/boca a boca, tiendas de apps, blog propio o prospección en frío por DM, nunca "años de audiencia".
- **Confirmado en la parte "fundador estrictamente solo":** solo Quaderno (Carlos Hernández, 2014) y Hower (Andrés Quiroz, 22 años) arrancaron con un único fundador; las cifras de Quaderno son estimaciones de terceros (Latka) y las de Hower son autodeclaradas. Nelio Software (3 fundadores, Barcelona, 12 años) y Failory (solo, Argentina) ilustran lo normal: ~90.000 $ y ~9.500 $/año respectivamente.
- **Confirmado en infoproductos:** NO ENCONTRADO ningún infoproductor hispano verificable con >100.000 €/año que haya empezado sin audiencia; las cifras que lo sugieren (Hotmart: "creadores con ≤50.000 seguidores facturan de media 250.000 $") son marketing de la plataforma sin metodología. Los instructores Udemy en español con cientos de miles de alumnos (Fernando Herrera, Álvaro Chirou) obtuvieron distribución de la plataforma, no de audiencia propia, pero sus ingresos no son públicos y los propios instructores declaran caídas de ingresos a niveles de hace 3-4 años (Udemy, 2025).
- **Confirmado en formación técnica/industrial en español:** el mercado (marcado CE, Reglamento 2023/1230, ISO 9001, PRL) lo ocupan TÜV SÜD, TÜV Rheinland, LRQA, INSST, COGITI, Fundación Ingeniero Jorge Juan, Servicios Normativos (350 €), CEV Consultores (150 €). No se encontró ningún formador individual vendiendo a empresas por correo frío con cifras. En el marketplace de Hotmart no hay cursos ISO 9001 en español (solo portugués, 34-147 US$) y la búsqueda "marcado CE" devuelve ruido.
- **Confirmado en cold email con cifras en España:** NO ENCONTRADO ningún caso de fundador español que haya construido un negocio de producto digital >100.000 € vendiendo a desconocidos por correo frío con cifras publicadas. Lo que existe son consultores y agencias que venden el servicio (Rafa Gandía, Overloop, DevCommX) con benchmarks genéricos (reply rate medio 3,43 %, Instantly 2026). El único caso de prospección en frío con cifra es Hower (DMs de Instagram, México).

## Método y limitaciones

- Herramienta: `tools/pwfetch.js` (cliente HTTP de Playwright y Chromium) + WebSearch para localizar URLs. Google, Bing (resultados aleatorios), DuckDuckGo, Brave, Mojeek, Ecosia, Startpage, Yandex bloquearon o devolvieron captcha; Yahoo funcionó unos minutos y después devolvió 500. El presupuesto de WebSearch de la sesión se agotó a mitad de trabajo; desde entonces solo se abrieron URLs ya conocidas o deducidas. Quedaron sin cubrir: Business Insider España, Startupeable, Itnig, Indie Makers España/Bootstrapping.es (no se pudo comprobar si existen), perfiles de Indie Hackers filtrados por país.
- Bloqueos 403: udemy.com (perfiles de instructor, búsqueda por idioma), indiehackers.com, elreferente.es, tuvsud.com, lrqa.com. Para Udemy se usaron espejos (OpenCourser) y la comunidad oficial de instructores.
- Criterio de "verificado": cifra publicada por el propio fundador en un medio o entrevista identificable, o estimación de terceros (GetLatka, Starter Story) coherente con declaraciones propias. "Autodeclarado": cifra solo en blog/vídeo del propio interesado o de la plataforma que lo vende.

## Bloque 1 · SaaS bootstrapped de 1-3 fundadores (España y Latinoamérica)

| Producto | Fundadores / inicio | Cifra | Tipo de dato | Canal de adquisición | ¿Audiencia previa? | Fuente |
|---|---|---|---|---|---|---|
| **Metricool** (Madrid) | 2 (Juan Pablo Tejela y su mujer, ambos desarrolladores), 2015-16 | 24.000 € (2016, sin empleados) → 125.000 € (2017, 2 empleados + becario) → 351.000 € (2018) → 1 M$ ARR (2020, 400.000 usuarios, 5.000 clientes) → 11 M$ (2024, 60-104 empleados) | Verificado: cifras propias en Emprendedores.es, Starter Story y Latka (YouTube) | Herramienta gratuita para blogueros → SEO, boca a boca; "casi 100 % marketing digital, sin equipo de ventas" | No. Tejela no dejó su empleo hasta 2017; crédito Enisa 50.000 € y ahorros familiares | [ABIERTA] emprendedores.es, starterstory.com, getlatka.com |
| **Quaderno** (Las Palmas) | 1 (Carlos Hernández), 2014 | Rentable al año de arrancar; 850 clientes en 38 países (2017); 1,2 M$ (2020), 2,8 M$ est. (2023), 3,6 M$ est. (2024); 12 empleados | Mixto: hitos propios (SaaStock); facturación = estimación GetLatka | Producto (facturación/IVA para SaaS), mercado internacional; sin inversores "porque no hay en Gran Canaria" | No | [ABIERTA] saastock.com, getlatka.com |
| **Hevy** (fundada en España; Guillem Ros, catalán) | 2 (Ros y Desmond McNamee), 2019 | "esperamos 2 M$ de ingresos en 2023, el doble que 2021"; 1,5 M usuarios; 2 M descargas con 15.000 $ de ads; 9 personas | Verificado: cofundador en Ottawa Business Journal; podcast RevenueCat. Estimaciones Latka (240 k$) y Starter Story (160 k$/mes) divergen | Orgánico: App Store/Google Play, comunidad, boca a boca | No. Venían de ser empleados en 8fit | [ABIERTA] obj.ca, revenuecat.com |
| **SumaCRM** (Madrid) | 2 (Tomás Santoro, Alfredo Nicolás), 2015 | >30.000 €/mes (mar-2017); 51.432 €/mes (jun-2019); 47.000 € MRR y 906 clientes (El Referente, 403); venta a Efficy por 2,1 M€ | Verificado (cifras propias publicadas en su blog y recogidas por wwwhatsnew, Alicante Plaza, El Referente) | Blog de transparencia ("viaje a la isla del tesoro de los 100.000 €/mes"), llamadas en frío (post "cómo perdí el miedo a las llamadas en frío") | No al inicio; la audiencia la construyó el blog en paralelo al producto | [ABIERTA] wwwhatsnew.com, alicanteplaza.es; [FRAGMENTO] elreferente.es |
| **Whaticket** (Perú/Brasil) | 3 socios (Juan Luis Auccatoma, Raúl, Cassio), 2021-22 | >5.000 $ el primer mes vendiendo solo software de escritorio; >4,5 M$ ARR (ene-2026); +4.500 clientes | Autodeclarado (blog del fundador) + web corporativa | Venta directa de software de escritorio → contenido, comunidad, alianzas, ventas | No; venía de una agencia quebrada en la pandemia | [ABIERTA] fundadorsaas.com, whaticket.com |
| **Hower** (México) | 1 (Andrés Quiroz, 22 años), hoy 5 personas | >10.000 $ MRR (~110.000 €/año) | Autodeclarado, analizado por tercero (Auccatoma) | **Prospección en frío por DM de Instagram con su propio producto**, después anuncios pagados; extensión de Chrome | No | [ABIERTA] fundadorsaas.com |
| **Freepik** (Málaga) – producto digital, no SaaS | 3 (hermanos Sánchez Blanes, FP; Joaquín Cuenca 5 %), 2010 | ~200.000 € en 2012 con 5 empleados; venta a EQT por 250 M€ (2020) | Verificado (historia documentada; chalsarboleya; carballar.com) | SEO (buscador de recursos gratuitos), tráfico de referencia | No | [ABIERTA] carballar.com, chalsarboleya.substack.com |
| **Acumbamail** (Ciudad Real) | 3 fundadores, 2013 | Vendida en 2018 "por varios millones" y revendida en 2022 por 70 M€ junto a otra startup | Verificado parcial (análisis de terceros) | Sin dato | No | [ABIERTA] chalsarboleya.substack.com |
| **FindThatLead** (Barcelona) | 2 (Gerard Compte, Cristian Vitales), 2015 | 11.000 usuarios de la extensión (2016); planes 15-90 $/mes; financiación 150.000 € (StartupTalky); adquirida | Autodeclarado/terceros; facturación NO ENCONTRADA | Extensión Chrome, Product Hunt, cold email (su propio producto) | No | [ABIERTA] woodpecker.co; [FRAGMENTO] startuptalky.com |
| **Nelio Software** (Barcelona) – contraejemplo | 3, 2013 | 59.900 $ (2021) → 91.000 $ est. (2024); 3 personas | Estimación GetLatka | Plugins WordPress, contenido | No | [ABIERTA] getlatka.com, neliosoftware.com |
| **Failory** (Buenos Aires) – contraejemplo | 1 (Nico Cerdeira) | 9.500 $ (2023), 1 persona; newsletter 40.000 suscriptores | Estimación GetLatka + web propia | Contenido/SEO | Construyó la audiencia él mismo | [ABIERTA] getlatka.com, failory.com |
| **Julian Mayorga** (Mendoza, AR) | 1 | "SaaS bootstrapped a 15.000 $ MRR en 3 años" (AMA IH 2021) | Solo título; sin producto ni verificación | — | — | [FRAGMENTO] indiehackers.com |

Agregados: GetLatka cuenta 746 empresas SaaS en España (oct-2026) con filtro de ingresos "<1 M$", pero el filtro de tamaño de equipo está bloqueado; no permite aislar fundadores solos. El análisis de chalsarboleya (93 emprendedores; 41 bootstrapped) muestra que el 27 % de los fundadores bootstrapped españoles de éxito no tiene grado universitario y el 29 % eran ingenieros de software en su primer empleo: perfil "constructor", no "creador de audiencia".

## Bloque 2 · Infoproductores hispanos

- **Hotmart (autodeclarado, promocional):** "Black Accounts" = productores con ≥1 M R$ (~170.000 €) en ventas (startups.com.br, 2021). España/Portugal: >1 M de compradores, creadores activos +35 % y ventas +21 % en el último año (Forbes BrandVoice pagado por Hotmart); "en 2024 el número de creadores activos creció un 33 % en Iberia" (entrevista Forbes ES al CEO). LATAM: "los creadores con hasta 50.000 seguidores generaron de media 250.000 $ en 12 meses" y "el 36 % de los productores más avanzados tiene ≤50.000 seguidores" (Expansión MX, feb-2026, fuente: directivos de Hotmart). Sin metodología ni muestra: sesgo de supervivencia evidente (media de los que ya venden). Comisión Hotmart: 9,90 % + 0,10-0,50 €.
- **Casos nominales de Hotmart en prensa:** Daniel Habif (~2.000 alumnos), Marco Antonio Regil (>20.000), Brenvita (120.000 alumnos, 1,1 M seguidores en Instagram): todos con audiencia previa masiva (DPL News, 2023). Hotmart afirma que "primero es necesario crear una comunidad".
- **Udemy en español:** Fernando Herrera (DevTalles) imparte cursos de 6-54 h a "cientos de miles de alumnos" (OpenCourser, Arc); Álvaro Chirou autodeclara ">500.000 estudiantes y 100 formaciones" (OpenCourser); un agregador habla de 2 M de inscripciones. Ingresos: NO PUBLICADOS. Un instructor destacado por Udemy (Carlos, El Salvador) describe cobrar "3 $ por curso vendido"; Pablo Tilotta (17 cursos) declara que en 2025 los ingresos "se derrumbaron a valores de 3 o 4 años atrás" por los planes personales, menor % y un recorte adicional del 5 % desde enero de 2026. Udemy aporta la distribución (no hace falta audiencia) pero a un precio medio de 9,99 $ y con reparto decreciente: para 100.000 € netos harían falta del orden de 30.000-35.000 ventas/año a 3 $ netos.
- **Domestika:** produce los cursos (2-4 h) y los vende a 9,90 € en rebajas; sin estadísticas públicas por profesor. [ABIERTA] domestika.org/es/teachers.
- **Comunidades de pago (Skool):** la búsqueda "español" en Skool devuelve 218 comunidades, pero casi todas son de aprender español para angloparlantes (8.500 miembros a 20 $/mes, 1.600 a 9 $/mes…). La búsqueda "negocios" devuelve 15, en su mayoría <100 miembros a 10-97 $/mes (Oassis Digital 43 × 27 $; RevOS 10 × 97 $). Ranking de dropshipping en español (andreybusiness.com, autopromocional): 5 comunidades de 100-800 miembros a 49-149 $/mes (estimado: 20.000-60.000 $/mes brutos las mayores; cifras no verificadas). Mediana global Skool: 205 miembros a 27 $/mes (RevenueGeeks).
- **Distribución de ingresos de creadores (Cursio, LATAM 2026, agregado sin fuente primaria):** 70 % <500 $/mes; 20 % 500-5.000 $; 8 % 5.000-30.000 $; 2 % >30.000 $. "Udemy reporta que su creador promedio gana 100-500 $/mes".

## Bloque 3 · Formación técnica e industrial en español (marcado CE, máquinas, ISO, PRL)

| Oferta | Proveedor | Precio | Formato | Fuente |
|---|---|---|---|---|
| Marcado CE: aplicación a máquinas y construcción (100 h) | Servicios Normativos Centro de Formación | 350 € IVA inc., bonificable (gestionan Fundae) | Online | [ABIERTA] emagister.com |
| Marcado CE de embarcaciones (100 h) | Fundación Ingeniero Jorge Juan | 1.001-2.000 € | Online | [ABIERTA] emagister.com |
| Marcado CE de chatarra (30 h) | CEV Consultores | 150 € IVA inc., bonificable | Online | [ABIERTA] emagister.com |
| Curso introducción Reglamento (UE) 2023/1230 | TÜV SÜD España | precio no visible (403), bonificable Fundae | Virtual | [FRAGMENTO] tuvsud.com |
| Diretiva Máquinas + Regulamento 2023/1230 (1 día) | TÜV Rheinland Portugal | 135 € sin IVA / 166,05 € | Virtual classroom | [ABIERTA] tuv.com |
| Machinery Regulation 2023/1230 course | Euronorm (NL) | 175 € + IVA | Online | [ABIERTA] euronorm.net |
| Reglamento 2023/1230: novedades (2 h, 19-11-2026) | INSST (público) | gratuito | Webinario | [ABIERTA] insst.es |
| Directiva Máquinas 2006/42 (16 h) | LRQA | no visible (403) | — | [FRAGMENTO] lrqa.com |
| ISO 9001 en Hotmart | Solo cursos en portugués (auditor interno SGI 34-147 US$, >3.000 alumnos) | 34-147 US$ | Online | [ABIERTA] hotmart.com/es/marketplace |

Emagister lista 23 cursos "marcado CE"; todos son de centros, colegios profesionales o certificadoras. **No se encontró ningún ingeniero individual vendiendo guías/cursos de pago sobre marcado CE, subestaciones o transformadores en español, ni nadie que declare venderlos a empresas por correo frío.** El canal real de esta formación es la bonificación Fundae (el proveedor gestiona el crédito) y el catálogo de las certificadoras.

## Bloque 4 · Tamaño de mercado

- **Fundae, Balance de situación 2024 (PDF oficial):** 5.824.016 participantes en formación programada por 347.442 empresas; 77 M de horas; 13,3 h de media por participante; +3,5 % participantes y +1 % empresas vs 2023; 6,5 M participantes en total (bonificada + subvencionada); 644,6 M€ de crédito usado (fragmento Factorial). Forman el 15,3 % de las microempresas, 48,9 % de las pequeñas, 80 % de las medianas y 91,8 % de las grandes.
- **ANCYPEL vía Stripe:** el sector de formación online en España generó 2.900 M€ en 2024 (+8,5 %); previsión 7.400 M€ en 2026 (cifra poco creíble por el salto). Eurostat: el 27 % de los españoles hizo cursos online en 2025 (4.º de la UE). Hotmart: España es su "segundo mercado más activo tras Brasil" (Stripe) — otra fuente dice que Brasil vale ~50 M$ y México va "siete años por detrás" (DPL News).
- **Hotmart global (autodeclarado):** +15 años, 10.000 M$ en ventas acumuladas, +35 M de compradores, +200.000 creadores con ventas, 188 países; LATAM crece 27,8 %/año hasta 98.000 M$ en 2033 (Expansión).
- **Udemy en español:** NO ENCONTRADO un recuento actual; la única cifra es antigua (>600 cursos en español cuando el catálogo internacional tenía 1.500). Catálogo total 200.000-240.000 cursos. udemy.com devolvió 403 a la búsqueda por idioma.
- **Ken Research:** e-learning y formación digital España 2.780 M$ (2025), CAGR 9,2 % hasta 4.710 M$ (2031) [FRAGMENTO].

## Bloque 5 · Venta a desconocidos por correo frío en España

- **Rafa Gandía (consultor, guía 2026):** reply rate medio 3,43 %, cuartil superior 5,5 %, top 10 % 10,7 % (Instantly Benchmark 2026); 58 % de respuestas en el primer email; 4-7 toques. Aritmética que propone: 12.000 emails/mes → 360 respuestas → 80-100 reuniones. Sin casos propios con facturación.
- **Overloop (vendedor):** "1,2 M de secuencias B2B España, reply rate medio 6,8 %" [FRAGMENTO]. DevCommX y Salesforge: páginas SEO por ciudad sin casos reales [FRAGMENTO].
- **Casos con cifras:** SumaCRM (llamadas en frío + blog, 51.000 €/mes en 2019, 2 fundadores); Hower (DMs en frío por Instagram, 10.000 $ MRR, México); FindThatLead (vendía cold email, sin cifras). **Ningún fundador español que haya pasado de 0 a >100.000 € solo con correo frío y lo documente**: NO ENCONTRADO.
- Podcast "Ventas B2B" (iVoox): página abierta, sin episodios identificables sobre casos con cifras.

## Los 10 casos hispanos más relevantes (cifra y canal)

1. **Metricool (ES)** – 2 fundadores; 125.000 € en el 2.º año, 351.000 € en el 3.º, 11 M$ en 2024 – herramienta gratuita + SEO + boca a boca – verificado.
2. **Quaderno (ES)** – 1 fundador; rentable en 1 año, 1,2-3,6 M$ – producto internacional, bootstrapped en Gran Canaria – hitos propios, cifras estimadas.
3. **Hevy (ES/CA)** – 2 fundadores; ~2 M$ en 2023 con 9 personas – orgánico en tiendas de apps – verificado por cofundador.
4. **SumaCRM (ES)** – 2 fundadores; 51.000 €/mes (2019), exit 2,1 M€ – blog de transparencia + llamadas en frío – verificado.
5. **Whaticket (PE)** – 3 socios; >4,5 M$ ARR, 4.500 clientes – venta directa de software, contenido, alianzas – autodeclarado.
6. **Hower (MX)** – 1 fundador, 5 personas; >10.000 $ MRR – prospección en frío por Instagram → ads – autodeclarado.
7. **Freepik (ES)** – 3 fundadores; 200.000 € en 2012, 250 M€ exit – SEO – verificado (no SaaS).
8. **Acumbamail (ES)** – 3 fundadores; exit "varios millones" 2018 – sin dato de canal – terceros.
9. **Álvaro Chirou / Fernando Herrera (AR/–, Udemy)** – instructores solos con 500.000+ alumnos – distribución de Udemy – alumnos autodeclarados, ingresos no públicos.
10. **Nelio Software (ES) y Failory (AR)** – contraejemplos: 3 personas / 91.000 $ y 1 persona / 9.500 $ – contenido y plugins – estimado.

## Patrones comunes

1. **Equipo mínimo de 2, no de 1.** Casi todos los que superan 100.000 € tienen 2-3 fundadores complementarios (técnico + comercial/marketing). Los casos de un solo fundador o escalan equipo pronto (Quaderno 12, Hower 5) o se quedan por debajo (Failory, Nelio).
2. **Sin audiencia previa, pero con distribución estructural:** herramienta gratuita indexable (Metricool, Freepik), tiendas de apps (Hevy), marketplaces (Udemy, Hotmart) o extensión de Chrome (FindThatLead, Hower). La "audiencia" se construye en paralelo al producto (blog SumaCRM), no antes.
3. **El correo frío no aparece como motor de ningún caso hispano con cifras**; sí la prospección en frío por DM (Hower) y las llamadas (SumaCRM). Quienes publican sobre cold email en España venden el servicio.
4. **Tiempo:** 2-4 años hasta las seis cifras en todos los casos verificados (Metricool 2 años para 125.000 €; Quaderno 1 año para rentabilidad; Hevy 4 años; SumaCRM 4 años para 47.000 € MRR).
5. **Infoproductos: la plataforma sustituye a la audiencia, pero captura el margen.** Udemy fija precios de 9,99 $ y recorta el reparto; Hotmart cobra 9,9 % y presenta medias sesgadas. Los casos con nombre y cifra en Hotmart tienen millones de seguidores.
6. **Formación técnica regulada en español = negocio institucional** apoyado en la bonificación Fundae (5,8 M de participantes, 644 M€); el individuo que quiera entrar compite con TÜV, LRQA, INSST (gratis) y colegios profesionales, y debe ofrecer la gestión de la bonificación.
7. **Verificabilidad:** las cifras públicas de fundadores hispanos son escasas; abundan estimaciones de GetLatka/Starter Story y autodeclaraciones en blogs/YouTube. Donde hay cifra propia (Metricool, SumaCRM, Hevy) la empresa ya había pasado a 5-10 empleados.

## Tabla de URLs

| Estado | URL | Uso |
|---|---|---|
| ABIERTA | https://emprendedores.es/startups/metricool-redes | Metricool: 24.000 € (2016), 125.000 € (2017), 351.000 € (2018), Enisa 50.000 € |
| ABIERTA | https://www.starterstory.com/social-media-planner-analytics | Metricool: 1 M$ ARR 2020, 3.000 $ MRR a los 6 meses, sin equipo de ventas |
| ABIERTA | https://getlatka.com/companies/metricool | Metricool 11 M$ 2024, 104 empleados |
| ABIERTA | https://saastock.com/blog/bootstrapping-a-saas-business-from-gran-canaria | Quaderno: 850 clientes/38 países, rentable en 1 año, 25 h/semana |
| ABIERTA | https://getlatka.com/companies/quaderno | Quaderno 1,2 M$ (2020) – 3,6 M$ est. (2024), 12 empleados |
| ABIERTA | https://obj.ca/fitness-app-entrepreneur-pumped-by-hevys-progress-to-2m-in-annual-revenue/ | Hevy: 2 M$ 2023, bootstrapped, fundada en España |
| ABIERTA | https://www.revenuecat.com/blog/growth/guillem-ros-hevy-podcast | Hevy: 2 M descargas con 15.000 $ de ads |
| ABIERTA | https://wwwhatsnew.com/?p=285755 | SumaCRM >30.000 €/mes (2017), objetivo 100.000 €/mes |
| ABIERTA | https://alicanteplaza.es/alicanteplaza/Larentabilidaddelatransparenciaempresarial | SumaCRM 51.432 €/mes (2019), oferta de compra 1 M€ |
| FRAGMENTO | https://elreferente.es/tecnologicos/efficy-compra-sumacrm-por-21-millones-de-euros/ | 47.000 € MRR, 906 clientes, exit 2,1 M€ (403) |
| ABIERTA | https://fundadorsaas.com/como-llegamos-4-millones-arrr-con-saas-whaticket/ | Whaticket 4,5 M$ ARR, 5.000 $ primer mes |
| ABIERTA | https://whaticket.com/ | +4.500 clientes |
| ABIERTA | https://fundadorsaas.com/analizando-saas-10k-mrr/ | Hower: 10.000 $ MRR, 5 personas, prospección en frío por Instagram |
| ABIERTA | https://carballar.com/en/the-freepik-story | Freepik ~200.000 € en 2012, 5 empleados, SEO |
| ABIERTA | https://chalsarboleya.substack.com/p/bootstrapers | Mayores bootstrappers de España: Freepik, Acumbamail, Erasmusu, Hevy… perfiles |
| ABIERTA | https://woodpecker.co/blog/findthatlead/ | FindThatLead: Barcelona, 11.000 usuarios, planes 15-90 $ |
| ABIERTA | https://www.getlatka.com/companies/nelio-software | Nelio 91.000 $ est., 3 personas |
| ABIERTA | https://neliosoftware.com/es/blog/ | Nelio: resúmenes anuales (sin cifras en portada) |
| ABIERTA | https://getlatka.com/companies/Failory | Failory 9.500 $ 2023, 1 persona |
| ABIERTA | https://www.failory.com/about | Failory: side-project, Buenos Aires |
| ABIERTA | https://getlatka.com/companies/countries/spain | 746 SaaS en España (oct-2026) |
| ABIERTA | https://trustmrr.com/ | Marketplace de ingresos verificados; sin filtro por país visible |
| ABIERTA | https://solofundador.com/sobre | Blog anónimo de fundador solo en Madrid (sin cifras) |
| ABIERTA | https://q2bstudio.com/en/our-blog/20284/la-brutal-y-gratificante-realidad-del-fundador-de-saas-en-solitario | Opinión, sin cifras |
| ABIERTA | https://startups.com.br/negocios/exclusivo-hotmart-lanca-cartao-de-credito-proprio-e-integracao-com-whatsapp/ | Hotmart Black = ≥1 M R$ en ventas |
| ABIERTA | https://forbes.es/?p=528813 | Hotmart Iberia: >1 M compradores, creadores +35 %, ventas +21 %, comisión 9,9 % |
| ABIERTA | https://forbes.es/?p=611606 | Entrevista CEO Hotmart: creadores activos +33 % en Iberia 2024 |
| ABIERTA | https://expansion.mx/tecnologia/2026/02/05/creadores-sin-millones-de-fans-ya-facturan-hasta-250-000-dolares-al-ano | Hotmart: media 250.000 $ con ≤50.000 seguidores; 36 % de top productores |
| ABIERTA | https://www.cronista.com/mexico/finanzas-economia/no-necesitas-millones-de-seguidores-el-negocio-que-se-multiplicara-por-9-en-latinoamerica-hotmart/ | Hotmart LATAM x9 hasta 2033 |
| ABIERTA | https://dplnews.com/?p=187547 | Hotmart LATAM: casos Habif, Regil, Brenvita; Brasil ~50 M$ |
| ABIERTA | https://hotmart.com/es | Hotmart: 10.000 M$ ventas, 35 M compradores |
| ABIERTA | https://hotmart.com/es/marketplace/busca?q=iso%209001 | Solo cursos ISO en portugués, 34-147 US$ |
| ABIERTA | https://hotmart.com/es/marketplace/busca?q=marcado%20CE | Sin cursos de marcado CE |
| ABIERTA | https://stripe.com/mx/resources/more/selling-online-courses-in-spain | ANCYPEL 2.900 M€ 2024; Eurostat 27 %; Hotmart 2.º mercado España |
| ABIERTA | https://www.fundae.es/docs/default-source/publicaciones-y-evaluaciones/informes-y-balances/balance-de-situaci%C3%B3n-2024-(1).pdf | Fundae 2024: 5.824.016 participantes, 347.442 empresas, 77 M horas |
| ABIERTA | https://cursio.app/blog/cuanto-ganar-vendiendo-cursos-online-latam-datos-reales | Distribución 70/20/8/2 % de ingresos de creadores |
| ABIERTA | https://community.udemy.com/es/discussion/162277/tu-repaso-como-instructor-de-2025 | Tilotta: ingresos 2025 caídos a niveles de hace 3-4 años; -5 % desde 2026 |
| ABIERTA | https://community.udemy.com/es/discussion/132586/campeon-destacado-de-la-comunidad | Instructor: "3 $ por curso vendido" |
| ABIERTA | https://opencourser.com/course/of7opf/seguridad-informatica-ingenieria-social-el-arte-del-engano | Chirou: >500.000 estudiantes autodeclarados |
| ABIERTA | https://opencourser.com/search?q=fernando%20herrera | Catálogo de cursos de Fernando Herrera (6-54 h, español) |
| ABIERTA | https://www.freecodecamp.org/espanol/news/fernando-herrera-la-pasion-por-la-programacion-y-la-ensenanza-s3-ep/ | Herrera: trayectoria, sin cifras |
| ABIERTA | https://arc.net/blog/a-conversation-w-fernando-herrera | Herrera: "cientos de miles de alumnos" |
| ABIERTA | https://www.domestika.org/es/teachers | Domestika produce los cursos; sin cifras por profesor |
| ABIERTA | https://formaciononline.eu/cursos-mas-vendidos-domestika/ | Cursos a 9,90 € en rebajas |
| ABIERTA | https://www.skool.com/discovery?q=espa%C3%B1ol | 218 comunidades "español" (casi todas de aprender español) |
| ABIERTA | https://www.skool.com/discovery?q=negocios | 15 comunidades, <100 miembros, 10-97 $/mes |
| ABIERTA | https://revenuegeeks.com/software/skool/best-communities | Mediana Skool 205 miembros, 27 $/mes |
| ABIERTA | https://www.andreybusiness.com/blog/comunidades-skool-dropshipping-espanol-ranking-2026 | Comunidades dropshipping ES 49-149 $/mes, 100-800 miembros (estimado) |
| ABIERTA | https://www.emagister.com/marcado-ce-tps-1589664.htm | 23 cursos marcado CE; 350 €, 150 €, 1.001-2.000 € |
| ABIERTA | https://www.tuv.com/portugal/pt/landingpages/tuv-rheinland-academy/diretiva-m%C3%A1quinas-%E2%80%93-decreto-lei-103-2008-online.html | TÜV PT 135 € sin IVA |
| ABIERTA | https://www.euronorm.net/en/products/machinery-regulation-eu-2023-1230-course | Euronorm 175 € |
| ABIERTA | https://www.insst.es/formacion/cnvm-bizkaia/reglamento-europeo-ue-2023/1230-relativo-a-las-m%C3%A1quinas.-novedades | INSST webinario 2 h gratuito |
| FRAGMENTO | https://www.tuvsud.com/es-es/store/academy-es/seguridad/seguridad-maquinas/2053-curso-reglamento-seguridad-maquinas | TÜV SÜD bonificable (403) |
| FRAGMENTO | https://www.lrqa.com/es-es/formacion/directiva-maquinas-2016-42-ce/ | LRQA 16 h bonificable (403) |
| ABIERTA | https://rafagandia.com/blog/guia-cold-email-saas-b2b-espana/ | Benchmarks cold email 3,43 % / 5,5 % / 10,7 % |
| ABIERTA | https://www.ivoox.com/podcast-ventas-b2b_sq_f1850733_1.html | Podcast Ventas B2B (sin casos con cifras) |
| FRAGMENTO | https://overloop.com/es/blog/plantilla-correo-electronico-ventas | Overloop: reply rate 6,8 % España (vendedor) |
| FRAGMENTO | https://startuptalky.com/findthatlead-tool/ | FindThatLead financiación 150.000 € |
| FRAGMENTO | https://www.indiehackers.com/post/f7ccINEtSYC74PsaFH5i | Motionvid/Sally POS: fundador en Chipre, no hispano (descartado) |
| FRAGMENTO | https://www.kenresearch.com/industry-reports/spain-e-learning-digital-training-market | 2.780 M$ 2025 |
| FRAGMENTO | https://factorial.es/blog/fundae-empresas-formaciones/ | 644,6 M€ crédito usado 2024 |
| NO ENCONTRADO | Business Insider España / Xataka / Startupeable / Itnig | Sin artículos localizados sobre fundadores solos con cifras |
| NO ENCONTRADO | Indie Makers España, Bootstrapping.es, SaaS Bootstrapped España | No se pudo comprobar su existencia (sin buscador) |
| NO ENCONTRADO | Caso español de 0 a >100.000 € solo con correo frío y cifras publicadas | — |
| NO ENCONTRADO | Formador individual de marcado CE / subestaciones / ISO vendiendo a empresas por correo frío | — |
