# Disparadores de mercado 2025-2027 (fin de soporte, cierre, subida de precio, cambio de licencia) y la demanda "alternativa a X"

Fecha: 23-10-2026. Sesión nube (claude.ai/code). Investigador adversarial, fila "disparadores con fecha".
Herramientas: `tools/pwfetch.js` (HTTP y Chromium), `curl`, `r.jina.ai`, API arctic-shift (Reddit), API de pageviews de Wikimedia, autocompletado de Google (`suggestqueries.google.com`), WebSearch (11 consultas).
Marcas: **[ABIERTA]** = página leída en esta sesión; **[FRAGMENTO]** = dato de un resumen de buscador o de fuente secundaria, sin abrir la fuente primaria; **NO ENCONTRADO / sin dato** = no hay cifra verificable. Toda cifra lleva moneda, fecha y URL. Fechas de Microsoft: la web muestra "10/14/2026 6:59:59 AM PT", que equivale al 13-10-2026 en hora del Pacífico; se anota la fecha comercial que usa Microsoft.

**Advertencia de método.** Google Trends devolvió 429 en los dos hosts (trends.google.com y trends.google.es) con Chromium y por API (`/trends/api/explore` devuelve HTML). Las herramientas públicas de volumen y CPC (Semrush, SpyFu, Ahrefs keyword generator, SE Ranking, Ubersuggest, alternativeto.net, SaaSHub) bloquearon la sesión (403/captcha/JS). Por tanto, en esta nota el volumen y el CPC son "sin dato" salvo lo que ya midió Jorge en el Planificador de Google Ads el 4-10-2026 (`research_notes/Dolores en crecimiento con pruebas/search_volume_planner_trends.md`). Como sustitutos medibles se usan: (a) páginas vistas mensuales de Wikipedia (en/es) 2024-2026, (b) número de posts por mes en Reddit vía arctic-shift, (c) número y texto de sugerencias de autocompletado de Google España. Son indicadores de atención, no de búsquedas con intención de compra.

---

## 0) Veredictos H1-H6

| Hipótesis | Veredicto | Resumen con datos |
|---|---|---|
| **H1** ≥6 disparadores con fecha oficial 2026-2027 verificada en la web del fabricante | **CONFIRMADA (9 verificados en fuente primaria)** | Windows 10 ESU consumidor hasta **12-10-2027** (la hipótesis del encargo decía 13-10-2026: Microsoft lo amplió un año); Office 2021 **13-10-2026**; Publisher **13-10-2026**; Windows Server 2012 R2 fin de ESU **13-10-2026**; SQL Server 2016 **14-07-2026**; Windows Server 2016 **12-01-2027**; vSphere 8 fin de soporte general **11-10-2027**; SAP Business Suite 7 fin de mantenimiento estándar **31-12-2027**; verificación de desarrolladores Android **sept-2026** (4 países) y **2027** (global). Más M365 comercial +12-33 % desde **1-07-2026** [FRAGMENTO] y Atlassian Data Center fin de venta a nuevos **30-03-2026** [FRAGMENTO]. Pero: 6 de los 9 son de Microsoft, 5 ya han pasado (oct-2026) y su comprador natural es IT/MSP, no un usuario que compra con tarjeta. |
| **H2** La demanda "alternativa a X" es medible y crece (≥8 incumbentes) | **NO VERIFICABLE con Trends; los sustitutos dicen que NO crece** | Trends: 429 en todas las consultas. Autocompletado ES: hay intención explícita para VMware (10 sugerencias, incl. "proxmox alternativa a vmware"), AutoCAD (10), Photoshop (10), Notion (10, incl. "alternativa europea a notion"), Canva (10), Microsoft 365 (9, incl. "alternativa europea a microsoft 365"), Publisher (10), Skype (10), Google Workspace (3, incl. "alternativa europea"); casi nula para LastPass (1), Mailchimp (2), Zapier (2), Google Analytics (1). Wikipedia 2024→2026: Skype, Google Analytics, Autodesk, Evernote, LastPass, Publisher, Proxmox: todas **a la baja**; solo suben Zorin OS, Linux Mint y Affinity alrededor de su disparador, y vuelven a la base en 3-7 meses. |
| **H3** En mercados grandes las alternativas son productos enormes; el hueco está en satélites | **CONFIRMADA, con matiz incómodo** | Para cada disparador hay sustitutos consolidados y a menudo gratuitos: Proxmox (120-1.100 €/socket/año), XCP-ng, Nutanix, Hyper-V; Windows 11, Linux (campaña End of 10), ESU; BricsCAD, ZWCAD (desde 899 $, perpetua); Affinity gratis desde oct-2025 (1 M de altas en 4 días), GIMP, Photopea; Teams Free; Instapaper, Raindrop; Plausible 9-19 $/mes, Matomo. Matiz: los satélites también tienen incumbente gratuito (asistente de importación ESXi de Proxmox, Nutanix Move, PC Health Check de Microsoft, "guardar como PDF" para Publisher, endoflife.date, Lansweeper Free, RMM de los MSP). El hueco satélite existe solo donde el incumbente no quiere resolverlo: coste de salida de Broadcom, defensa ante auditorías de licencias, radar de renovaciones multi-proveedor. |
| **H4** ≥5 satélites construibles en <8 semanas a 35-50 €/mes | **PARCIAL: 9 candidatos, ninguno pasa el filtro de muerte completo** | Los 3 mejores (sección 4): planificador de salida de VMware/Broadcom (6/10), autoauditoría de licencias Autodesk/Adobe (5/10), radar de renovaciones y fin de soporte para pymes (5/10). Todos fallan en lo mismo: volumen y CPC **sin dato**, comprador IT que espera la herramienta gratis del proveedor, y precio 35-50 €/mes solo plausible si el cliente es un MSP que lo cobra a sus clientes. |
| **H5** CPC ≤3 € en "alternativa a X" y "migrar de X" | **SIN DATO (no verificable en esta sesión)** | Ninguna fuente pública de CPC accesible. Único dato real disponible: Planificador de Jorge (4-10-2026): puja superior rango alto bloque "controles" (verifactu) 4,99 €; iso9001 2,34 €; cecra 15,59 €; gbp 5,56 €. Para IT de infraestructura (VMware, Java) la puja la marcan Nutanix, Red Hat, Azul y Broadcom: lo esperable es >3 €, pero es una expectativa, no un dato. Hay que pasar la lista de la sección 2 por el Planificador. |
| **H6** La ola se agota en 6-12 meses tras la fecha | **CONFIRMADA y peor: 1-2 meses para el incumbente, 3-7 meses para el sustituto** | Wikipedia en: Skype 140 k (mar-2025, anuncio) y 149 k (may-2025, cierre) → 54 k en jun-2025, luego por debajo de la base (28-35 k en 2026). Windows 10: 80 k (sep-2025) → 151 k (oct-2025) → 60 k (nov) → ~40 k en 2026, por debajo de la base previa (70-85 k). Windows 10 es.wikipedia: 22 k (oct-2025) → 6 k (nov). Zorin OS: 23-24 k oct-2025 a ene-2026 → 9 k en jun-2026 (7 meses). Affinity Photo: 16 k (nov-2025) → 6 k (feb-2026). Pocket: 6 k (may-2025) → 2 k (ago-2025). Reddit r/sysadmin, títulos con "ESU": 10 posts en oct-2025, 1-3/mes desde feb-2026. **La excepción es VMware/Broadcom**: 130 posts con "Broadcom" en r/sysadmin desde ene-2024, con picos de 2.669, 2.368 y 1.694 votos (mar-2025, may-2025, dic-2025, cartas de cese y desistimiento) y actividad continua en 2026, porque el disparador no es una fecha sino renovaciones escalonadas y cambios de licencia sucesivos hasta el 11-10-2027. |

**Conclusión de la fila.** El patrón Plausible (herramienta odiada + fecha oficial + ángulo UE + construible solo) no aparece limpio en ningún candidato de esta fila. Lo más parecido es "salida de VMware" (ola larga, odio documentado, fecha 2027, intención de búsqueda explícita), pero su comprador es IT/MSP y la hipótesis de autoservicio sin llamada es la más débil justamente ahí. Si Jorge quiere seguir esta fila, el siguiente paso barato es el Planificador con las 24 palabras clave de la sección 2 (30 minutos) antes de escribir una línea de código.

---

## 1) Tabla de disparadores

| Incumbente | Qué cambia | Fecha oficial | URL (estado) | Estado de la ola a 23-10-2026 |
|---|---|---|---|---|
| Windows 10 Home/Pro | Fin de soporte (22H2 última versión) | 14-10-2025 | https://learn.microsoft.com/en-us/lifecycle/products/windows-10-home-and-pro [ABIERTA] | Pasada. Pico de atención un mes (oct-2025) y caída por debajo de la base. Cuota España sept-2026: Win11 68,22 %, Win10 29,84 % (Statcounter, https://gs.statcounter.com/windows-version-market-share/desktop/spain [ABIERTA]). |
| Windows 10 ESU consumidor | Actualizaciones de seguridad de pago/gratis | **Hasta 12-10-2027** ("Both enrollment options provide extended security updates through October 12, 2027"); gratis con copia de ajustes, o 1.000 puntos Rewards, o pago único 30 USD; hasta 10 dispositivos | https://support.microsoft.com/en-us/windows/windows-10-consumer-extended-security-updates-esu-program-33e17de9-36b3-43bb-874d-6c53d2e4bf42 [ABIERTA] | Viva pero desactivada: la extensión gratuita a 2027 quita la urgencia. Autocompletado ES "windows 10 esu": 10 sugerencias (incl. "windows 10 esu 2027", "windows 10 esu gratis"). |
| Windows 10 ESU empresa | ESU por licencia por volumen | 61 USD/dispositivo año 1, dobla cada año, máx. 3 años (hasta oct-2028) | https://learn.microsoft.com/en-us/windows/whats-new/extended-security-updates [ABIERTA] | Viva para MSP/pymes rezagadas; Reddit r/sysadmin "ESU": 10 posts oct-2025, 7 dic-2025, 1-3/mes en 2026. |
| Office 2016 y 2019; Exchange Server 2016 y 2019 | Fin de soporte extendido | 14-10-2025 | https://learn.microsoft.com/en-us/lifecycle/products/microsoft-office-2016 · .../microsoft-office-2019 · .../exchange-server-2016 · .../exchange-server-2019 [ABIERTAS] | Pasada. Exchange on-prem queda solo en Exchange SE (suscripción). |
| Office 2021 (Home&Business, Home&Student, Professional) | Retiro | 13-10-2026 | https://learn.microsoft.com/en-us/lifecycle/products/office-2021 [ABIERTA] | Acaba de pasar (hace 10 días). Sin señal de ola propia (nadie busca "alternativa a office 2021"). |
| Microsoft Publisher | Fin de vida; se elimina de M365 a partir del 1-10-2026; soporte perpetuo acaba con Office LTSC 2021 | 13-10-2026 | https://support.microsoft.com/en-us/publisher [ABIERTA] | Acaba de pasar. Wikipedia en Publisher estable 8-16 k/mes (pico 16 k en abr-2026), es 1-2 k y bajando. Autocompletado ES "alternativa a publisher" 10 sugerencias. Microsoft recomienda convertir a PDF/Word y usar Word, PowerPoint o Designer. |
| Windows Server 2012 R2 | Fin del ESU año 3 | 13-10-2026 | https://learn.microsoft.com/en-us/lifecycle/products/windows-server-2012-r2 [ABIERTA] | Acaba de pasar; residual. |
| SQL Server 2016 | Fin de soporte extendido; ESU año 1 hasta 13-07-2027 | 14-07-2026 | https://learn.microsoft.com/en-us/lifecycle/products/sql-server-2016 [ABIERTA] | Pasada hace 3 meses; mercado IT puro. |
| Windows Server 2016 | Fin de soporte extendido | 12-01-2027 | https://learn.microsoft.com/en-us/lifecycle/products/windows-server-2016 [ABIERTA] | Por llegar (3 meses). Mercado IT puro. |
| Microsoft 365 comercial | Subida de lista mundial: Business Basic 6→7 USD, Business Standard 12,50→14 USD, Business Premium igual (22), E3 36→39, E5 57→60, F1 2,25→3, F3 8→10 USD/usuario/mes; aplica en la renovación | 1-07-2026 | https://office-watch.com/2025/microsoft-365-price-increase-2026/ [ABIERTA, secundaria]; anuncio de Microsoft citado como imagen, URL primaria NO ENCONTRADA (la del blog devolvió 404) | Viva hasta jul-2027 (renovaciones escalonadas). Autocompletado ES: "alternativa europea a microsoft 365" existe; "coste licencias microsoft 365" 1 sugerencia. |
| Microsoft 365 Personal/Family | +3 USD/mes con Copilot incluido; planes "Classic" sin IA por tiempo limitado | 16-01-2025 | https://www.microsoft.com/en-us/microsoft-365/blog/2025/01/16/copilot-is-now-included-in-microsoft-365-personal-and-family/ [ABIERTA] | Pasada. |
| Google Workspace | Gemini incluido; Business Standard 12→14 USD/usuario/mes ("only $2 more") | ene-2025 | https://workspace.google.com/blog/product-announcements/empowering-businesses-with-AI [ABIERTA] | Pasada. Autocompletado ES "alternativa europea a google workspace" existe (3 sugerencias en total). |
| Skype | Cierre; Skype Number terminados en may-2026; historial de usuarios inactivos borrado tras el 15-06-2026 | may-2025 (cierre) | https://support.microsoft.com/en-us/skype/skype-is-retiring-in-may-2025-what-you-need-to-know-2a7d2501-427f-485e-8be0-2068a9f90472 [ABIERTA] | Agotada. Wikipedia en: 140 k (mar-2025), 149 k (may-2025) → 54 k (jun-2025) → 28-35 k en 2026. es: 15 k (may-2025) → 1-3 k en 2026. |
| VMware (Broadcom) | Fin de licencias perpetuas y paso a suscripción por core (dic-2023); mínimo de 72 cores por pedido anunciado por distribuidores para el 10-04-2025 y luego matizado/retirado; vSphere 7 fin de soporte general oct-2025; **vSphere 8 fin de soporte general 11-10-2027** | 11-10-2027 (vSphere 8.0, ESXi 8.x, vCenter 8.x: "The End of general support for vSphere 8.0 is October 11, 2027") | https://knowledge.broadcom.com/external/article/459135/end-of-general-support-for-vsphere-80.html [ABIERTA vía WebFetch]; https://news.broadcom.com/releases/broadcom-dramatically-simplifies-vmware-offer-lineup-and-licensing-model NO ABIERTA (401); 72 cores [FRAGMENTO: The Register/Licenseware/heise vía WebSearch] | **Viva y larga**: r/sysadmin 130 posts "Broadcom" desde ene-2024; cartas de cese y desistimiento a titulares de perpetuas (2.368 votos 8-05-2025; 1.694 votos 4-12-2025); "Broadcom does not want to renew partial VMware licensing" (373 votos, 19-01-2026). Autocompletado ES "migrar de vmware": 10 sugerencias (proxmox, hyper-v, nutanix, aws, azure). |
| Atlassian Data Center | Fin de ciclo: no se aceptan apps DC nuevas 16-12-2025; fin de venta a nuevos clientes 30-03-2026; fin de venta a existentes 30-03-2028; fin de vida 28-03-2029; Bitbucket excepto | 30-03-2026 / 28-03-2029 | [FRAGMENTO] vía WebSearch (actonic.de, seibert.group, getint.io, utoolity); páginas de atlassian.com devolvieron 401/404 | Viva para empresas medianas; fuera del alcance de un fundador solo (migraciones de Jira con partners). |
| Adobe Creative Cloud | All Apps → "Creative Cloud Pro" 59,99→69,99 USD/mes (anual facturado mensual); nuevo "Standard" 54,99 USD; solo Norteamérica; fuera de NA cambios limitados (Teams Pro Edition) | 17-06-2025 | https://licenseware.io/adobe-licensing-pricing-changes-comprehensive-analysis-of-2025-updates/ y https://petapixel.com/2025/05/20/... [ABIERTAS, secundarias]; https://helpx.adobe.com/creative-cloud/plans-pricing/pricing-update.html NO ABIERTA (403) | Pasada y no aplica a España. **Contra-disparador**: Affinity (Canva) gratis para particulares, "more than one million people have signed up in four days" (https://www.canva.com/newsroom/news/affinity-free/ [ABIERTA]; fecha exacta no en la página; Wikipedia Affinity Photo 16 k en nov-2025 frente a 5-6 k de base). |
| Autodesk | Fin del descuento del 5 % en renovaciones anuales y recorte del multianual (ene-2025); +3,3 % en suscripciones monousuario desde 7-05-2025; planes "Move to Subscription"/"Transition to Named User" +5 % y solo anuales desde 10-05-2025 | 7-05-2025 | [FRAGMENTO] vía WebSearch (Graitec/Microsol Resources, distribuidores); https://www.autodesk.com/support/account/admin/subscription/pricing-changes [ABIERTA pero solo JS/menú, sin texto]; https://www.autodesk.com/in/price-change-terms-conditions [ABIERTA, texto de 2022 para India] | Sin fecha nueva 2026-2027. Señal lateral: autocompletado EN "autodesk license compliance and audit engagement" (auditorías de licencia a clientes); r/AutoCAD "license": 6 posts en jul-2026. |
| Slack | Business+ 12,50→15 USD/usuario/mes (anual); mensual 15→18; renovaciones desde 17-08-2025 | 17-06-2025 | https://slack.com/help/articles/39264531104275-... [ABIERTA; la cifra 15 USD viene del resumen de WebSearch de la misma página] | Pasada. |
| Canva Teams | De 120 USD/año a 500 USD/año por persona en algunos clientes (TechCrunch 3-09-2024) | sept-2024 | [FRAGMENTO] vía DuckDuckGo (https://duckduckgo.com/html/?q=canva+teams+price+increase+2024+per+user [ABIERTA]) | Pasada. |
| Chrome Manifest V2 / uBlock Origin | MV2 desactivado para todos en Chrome 138 (24-07-2025); eliminado en Chrome 139 | 24-07-2025 | https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline [ABIERTA] | Pasada. Autocompletado ES "alternativa a ublock origin": 5 sugerencias. No hay producto de pago posible (uBO Lite, Firefox, Brave gratis). |
| Pocket (Mozilla) | Cierre de la app y extensiones | 2025 ("Pocket has shut down"); fechas exactas de cierre y de exportación NO VERIFICADAS (support.mozilla.org bloqueado por challenge) | https://getpocket.com/farewell [ABIERTA] | Agotada: Wikipedia en 6 k (may-2025) → 1 k en 2026. Autocompletado ES "alternativa a pocket" lo copan Osmo Pocket y Retroid Pocket. |
| Google Analytics / Universal Analytics | UA: datos borrados desde la semana del 1-07-2024 | 1-07-2024 | https://support.google.com/analytics/answer/11583528?hl=en [ABIERTA] | Agotada. Wikipedia en Google Analytics 32 k (ene-2024) → 6-9 k (2026), sin repunte en jul-2024. Autocompletado ES "alternativa a google analytics": 1 sugerencia. Plausible cobra 9/14/19 USD/mes (https://plausible.io/#pricing [ABIERTA]). |
| Oracle Java SE | Suscripción universal por empleado (no por instalación) | desde ene-2023; precios no publicados en la página abierta (PDF de lista 404) | https://www.oracle.com/java/java-se-subscription/ [ABIERTA] | Continua (auditorías), sin fecha. Azul ofrece evaluación y "Java X-Ray Tool" (https://www.azul.com/ [ABIERTA, página 404 interna con menú]). |
| SAP Business Suite 7 (ECC) | Fin de mantenimiento estándar 31-12-2027; extendido opcional hasta 31-12-2030 | 31-12-2027 | https://news.sap.com/2020/02/sap-s4hana-maintenance-2040-clarity-choice-sap-business-suite-7/ [ABIERTA] | Viva, pero el ecosistema es de integradores grandes; descartado para fundador solo. |
| Google Play / Android | Verificación obligatoria de desarrolladores para instalar apps en dispositivos certificados: acceso anticipado oct-2025, abierta a todos mar-2026, obligatoria en Brasil, Indonesia, Singapur y Tailandia sept-2026, resto del mundo 2027 | sept-2026 / 2027 | https://android-developers.googleblog.com/2025/08/elevating-android-security.html [ABIERTA] | Por llegar en la UE (2027). Afecta a desarrolladores, no a pymes; sin producto recurrente claro. |
| Google Domains | Venta a Squarespace | 2023-2024 | https://support.google.com/domains/answer/13689670?hl=en [ABIERTA, sin fechas legibles en el texto] | Agotada. |
| Verifactu (España) | Aplazamiento: sociedades 1-01-2027, autónomos y resto 1-07-2027 (RDL 15/2025, BOE 3-12-2025) | 1-01-2027 / 1-07-2027 | [FRAGMENTO] vía WebSearch (fiscal-impuestos, Billin, ICAM, Consejo de Gestores); https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu.html [ABIERTA, sin la fecha en el texto extraído]; el BOE abierto (BOE-A-2025-26379) resultó ser otra resolución | Viva. Planificador Jorge 4-10-2026: "verifactu" 40.500 búsq./mes ES, −63 % interanual tras el aplazamiento; Trends ES pico 30-11-2025 = 100 y ~14 dos semanas después. Factura electrónica B2B (RD 238/2026: 6-10-2027 / 6-10-2028) NO VERIFICADA. |
| Cookies / AEPD | Guía de cookies actualizada en mayo 2024 (40 páginas); sanciones AEPD 2025: 33,9 M€ en total [FRAGMENTO Lawwwing]; multas por cookies pequeñas (1.200 € medio digital feb-2025; 90.000 € tres dominios en 2024) [FRAGMENTO] | sin fecha nueva 2026-2027 | https://www.aepd.es/guias/guia-cookies.pdf [ABIERTA]; https://www.aepd.es/prensa-y-comunicacion/notas-de-prensa [ABIERTA, sin notas sobre cookies en oct-2026]; Digital Omnibus UE NO ABIERTA (403 CloudFront) | Sin disparador con fecha; riesgo de que el Omnibus digital reduzca la obligación de banner (no verificado). |
| Zapier, Notion, Calendly, Typeform, Mailchimp, Evernote, LastPass, Unity, X API | Precios actuales abiertos: Zapier Team desde 69 USD/mes; Notion Plus 10 / Business 20 USD/asiento/mes; Calendly Standard 10 / Teams 16 USD/asiento/mes | sin fecha de disparador 2026-2027 | https://zapier.com/pricing · https://www.notion.com/pricing · https://calendly.com/pricing · https://www.typeform.com/pricing/ · https://blog.lastpass.com/posts/notice-of-recent-security-incident · https://unity.com/blog/unity-is-canceling-the-runtime-fee · https://developer.x.com/en/portal/products [ABIERTAS]; Mailchimp y Evernote 401/404 | Sin ola. Autocompletado ES: Notion 10 sugerencias ("alternativa europea a notion"), Evernote 5, Slack 3, Zapier 2, Mailchimp 2, LastPass 1. |

---

## 2) Tabla de demanda "alternativa a X" (sustitutos de Trends)

Trends: **sin dato** (429 en todas las consultas, con Chromium y por API). Columnas: sugerencias de autocompletado Google España (hl=es, gl=es, 23-10-2026; máximo 10) con las más reveladoras; páginas vistas en Wikipedia (media mensual en miles, usuarios, todos los accesos) ene-jun 2024 frente a abr-sep 2026; Reddit cuando hay dato.

| Incumbente | Consulta ES | Autocompletado ES (n y ejemplos) | Autocompletado EN (gl=us) | Wikipedia en 2024→2026 | Wikipedia es 2024→2026 | Lectura |
|---|---|---|---|---|---|---|
| VMware | alternativa a vmware / migrar de vmware | 10: "alternativa a vmware vsphere", "alternativa a vmware esxi", "proxmox alternativa a vmware", "alternativa open source vmware"; "migrar de vmware" 10: a proxmox, hyper-v, nutanix, aws, azure | "vmware alternatives 2026", "vmware alternatives enterprise", "proxmox migration from vmware" | Proxmox VE 18 k → 12-14 k (baja) | Proxmox VE 1,3 k → 0,4-0,6 k (baja) | Intención de migración explícita y viva; la atención al sustituto no crece. |
| Windows 10 | alternativa a windows 10 / windows 10 fin de soporte | 10 y 10: "windows 10 fin de soporte extendido", "...que hacer", "...2026", "...europa"; "migrar de windows 10 a linux" | "windows 10 end of support extended to 2026", "windows 10 esu year 2 cost" | Windows 10 87 k → 38-41 k; Zorin OS 6-7 k → 7-16 k; Linux Mint 28 k → 22-31 k | Windows 10 20 k → 3-4 k | Ola de oct-2025 agotada; Linux sube 4-7 meses y vuelve. |
| AutoCAD / Autodesk | alternativa a autocad | 10: "gratis", "en linux", "open source", "online", "2d", "electrical"; "licencias autodesk" 10 ("baratas", "gratis"); "auditoria autodesk" 2 | "autodesk license audit" 5 incl. "autodesk license compliance and audit engagement" | Autodesk 33 k → 13-16 k (baja) | sin dato | Demanda de "gratis", no de pago; la señal de auditoría es pequeña pero con dolor real. |
| Photoshop / Adobe | alternativa a photoshop / alternativa a adobe | 10 y 10: "gratis", "online", "de canva", "open source"; Adobe: "acrobat", "acrobat gratis", "illustrator" | sin medir | Affinity Photo 5 k → 5-7 k con pico 16 k nov-2025 | sin dato | Mercado resuelto por Affinity gratis y Photopea; sin hueco de pago. |
| Skype | alternativa a skype | 10: "para llamadas internacionales", "para llamadas", "gratis" (varias en italiano) | "alternative to skype number", "...for landline calls" | Skype 50 k → 28-33 k | Skype 8 k → 1-3 k | Agotada; residuo en "número virtual/llamadas a fijos". |
| Microsoft 365 / Google Workspace | alternativa a microsoft 365 / a google workspace | 9: "gratis", "mejor", "**alternativa europea a microsoft 365**", "euroffice"; Workspace 3: "**alternativa europea a google workspace**" | sin medir | sin dato (API limitada) | sin dato | Señal "europea/soberanía" real pero pequeña; sustitutos: Nextcloud, Zoho, Infomaniak, Proton. |
| Publisher | alternativa a publisher | 10: "gratis", "online", "para mac", "open source", "google" | 10: "free", "for mac", "for newsletters" | Publisher 11 k → 8-16 k (estable) | 5 k → 1 k (baja) | Demanda estable y de "gratis"; una herramienta de pago choca con Word/Designer/Affinity. |
| Google Analytics | alternativa a google analytics | 1 | sin medir | GA 27 k → 6-9 k; Universal Analytics ≈0 | sin dato | Ola de 2022-2024 totalmente agotada. |
| Notion | alternativa a notion | 10: "open source", "gratis", "de google", "de microsoft", "**alternativa europea a notion**", "outline" | sin medir | sin dato | sin dato | Intención presente, sin disparador con fecha. |
| Canva | alternativa a canva | 10: "gratis", "con inteligencia artificial", "pro gratis", "de microsoft", "de google" | sin medir | sin dato | sin dato | Demanda de gratis. |
| Pocket | alternativa a pocket | 10 pero 8 son Osmo/Retroid/DJI Pocket | "alternative to pocket app" 1 de 10 | Pocket 2-3 k → 1 k | sin dato | Agotada. |
| Evernote / LastPass / Mailchimp / Zapier / Slack / Jira / uBlock | alternativa a ... | 5 / 1 / 2 / 2 / 3 / 3 / 5 | sin medir | Evernote 7 k → 3-5 k; LastPass 6 k → 2-3 k | sin dato | Sin ola. |
| Broadcom precio / cookies / coste M365 | broadcom vmware precio / gestion de cookies web / coste licencias microsoft 365 | 0 / 0 / 1 | sin medir | Broadcom 40 k → 25-37 k | sin dato | Las consultas "satélite" en español casi no existen en autocompletado. |

**Lista para el Planificador de Google Ads (Jorge, 30 minutos, ES + "todas las ubicaciones"):** alternativa a vmware · vmware alternative · migrar de vmware a proxmox · proxmox vs vmware · broadcom vmware licencias · windows 10 esu · windows 10 fin de soporte · migrar de windows 10 a linux · alternativa a autocad · autodesk license audit · auditoria licencias software · alternativa a photoshop · alternativa a microsoft 365 · alternativa europea a microsoft 365 · alternativa europea a google workspace · coste licencias microsoft 365 · gestión de suscripciones saas · alternativa a publisher · convertir pub a pdf · alternativa a skype para llamadas internacionales · alternativa a google analytics · verifactu software · banner cookies rgpd · gestor de consentimiento cookies.

---

## 3) Herramientas satélite candidatas

Puntuación 0-10 = media ponderada de: disparador con fecha (0-2), intención de búsqueda demostrada (0-2), capacidad de pago 35-50 €/mes sin llamada (0-2), ausencia de incumbente gratuito (0-2), construible <8 semanas por una persona con IA (0-2). Volumen y CPC: **sin dato** salvo indicación.

| # | Herramienta (qué hace) | Quién paga | Precio plausible | Keyword de entrada (señal) | Volumen / CPC | Competidores | Complejidad | Puntos |
|---|---|---|---|---|---|---|---|---|
| S1 | **Planificador de salida de VMware/Broadcom**: importa RVTools/CSV de vCenter, calcula cores a licenciar y coste de renovación VVF/VCF frente a Proxmox (120/370/550/1.100 €/socket/año), XCP-ng, Hyper-V; genera plan de migración por oleadas, checklist y PDF para dirección | MSP y responsable IT de pyme con 2-10 hosts; MSP lo reutiliza por cliente | 49 €/mes (MSP, clientes ilimitados) o 149 € por informe | "alternativa a vmware", "migrar de vmware a proxmox", "vmware alternatives 2026" (10/10 sugerencias ES y EN) | sin dato / sin dato (puja esperada >3 € por Nutanix, Red Hat, Broadcom: no verificado) | Calculadoras gratuitas de Nutanix, Scale, Vates; RVTools (gratis); asistente de importación ESXi de Proxmox (gratis, https://pve.proxmox.com/wiki/Migrate_to_Proxmox_VE [ABIERTA]); Nutanix Move (gratis, [ABIERTA]); consultoras | Media: parser de RVTools (xlsx), tabla de precios Proxmox (pública) y VMware (opaca: Broadcom no publica lista), PDF | **6** |
| S2 | **Autoauditoría de licencias Autodesk/Adobe**: script/agente que inventaría instalaciones y versiones en los equipos, las cruza con el CSV de suscripciones del portal y señala instalaciones sin asiento, asientos sin uso y duplicados; genera el paquete de respuesta a la carta de "License Compliance and Audit engagement" | Estudios de arquitectura/ingeniería/diseño 10-100 puestos; su responsable IT o gerente al recibir la carta | 39 €/mes o 249 € por auditoría | "autodesk license audit" (5 sugerencias EN, incl. la frase exacta de la carta), "auditoria autodesk" (2 ES), "licencias autodesk" (10 ES, pero con "baratas/gratis") | sin dato / sin dato | Flexera, Snow, Open iT, Licenseware (empresa, precio alto); informes de uso del propio portal Autodesk; abogados de licencias | Media-alta: agente Windows/macOS, registro, firma de código; soporte | **5** |
| S3 | **Radar de renovaciones y fin de soporte para pymes**: carga del inventario de software y suscripciones (CSV, conectores M365/Workspace), calendario de fin de soporte (Office 2021, Server 2016, SQL 2016, vSphere 8, SAP 2027) y de subidas (M365 jul-2026, Slack, Atlassian), coste por asiento y "alternativa europea" sugerida | Responsable IT/administración de pymes 20-200 empleados; MSP | 35 €/mes | "coste licencias microsoft 365" (1 sugerencia), "alternativa europea a microsoft 365" (existe), "gestión de suscripciones saas" (sin medir) | sin dato / sin dato | endoflife.date (gratis); Cledara desde 75 £/mes (https://www.cledara.com/pricing [ABIERTA]); Substly; Torii, Zluri, Vendr (empresa) | Baja-media | **5** |
| S4 | **Verifactu-ready checker**: valida que las facturas/registros cumplen RD 1007/2023 (QR, huella, encadenado), simula el envío a la AEAT y genera la declaración responsable del SIF | Autónomos y micropymes que facturan con Excel/Word o software antiguo; asesorías | 29-39 €/mes; o 99 € por auditoría | "verifactu" | **40.500 búsq./mes ES, −63 % interanual (Planificador Jorge 4-10-2026)** / puja superior rango alto bloque "controles" **4,99 €** (>3 €) | Todos los ERP (Holded, Billin, Quipu, Sage, a3, Wolters); app gratuita de la AEAT; ya evaluado en `reports/Dolores en crecimiento con pruebas.md` (7/15) | Media (especificación técnica AEAT, firma) | **5** |
| S5 | **Inventario Windows 10 ESU / preparación Windows 11 para MSP**: script sin agente que recoge TPM, CPU, UEFI y estado de inscripción en ESU de la flota y produce presupuesto (ESU 61/122/244 USD empresa; 30 USD consumidor hasta 2027) e informe para el cliente | MSP | 39 €/mes | "windows 10 esu" (10/10 ES y EN), "windows 10 fin de soporte que hacer" | sin dato / sin dato | PC Health Check y Intune (Microsoft, gratis/incluido), WhyNotWin11 (gratis), Lansweeper plan Free ([ABIERTA], límites no extraídos), PDQ 12 USD/dispositivo/año con mínimo 100 ([ABIERTA]), RMM que el MSP ya paga | Media | **4** |
| S6 | **CMP mínimo AEPD para pymes españolas**: banner, escaneo, registro de consentimientos y textos según Guía AEPD mayo 2024 | Pymes y agencias web | 10-20 €/mes (35-50 solo plan agencia) | "gestion de cookies web" (0 sugerencias), "banner cookies rgpd" (sin medir) | sin dato / sin dato | Cookiebot, iubenda, CookieYes, Complianz, Usercentrics, Didomi, Cookie Script, Lawwwing | Baja-media | **4** |
| S7 | **Calculadora de exposición Java y plan de migración a OpenJDK**: detecta JDK de Oracle en servidores y puestos, calcula coste por empleado y propone Temurin/Azul | IT de empresas 50-500 empleados | 39 €/mes | "oracle java licencia por empleado" (sin medir) | sin dato / sin dato (Azul puja) | Azul (evaluación y Java X-Ray gratis), Red Hat, Licenseware | Media | **4** |
| S8 | **Rescate de Publisher**: conversión por lotes .pub → PDF/Word/IDML/Canva y archivo con búsqueda | Parroquias, colegios, imprentas, pymes con décadas de .pub | pago único 9-29 € (no recurrente) | "alternativa a publisher" (10/10), "convertir pub a pdf" | sin dato / sin dato | Microsoft: "guardar como PDF" antes del 13-10-2026; LibreOffice Draw (importa .pub), Zamzar/CloudConvert (gratis), Affinity Publisher (gratis) | Alta (formato .pub cerrado; libmspub incompleto) | **3** |
| S9 | **Asistente de verificación de desarrollador Android** (D-U-N-S, identidad, consola) | Desarrolladores indie | pago único | "android developer verification" (sin medir) | sin dato | Documentación de Google (gratis) | Baja | **2** |

---

## 4) Fichas de los 3 mejores

### S1. Planificador de salida de VMware/Broadcom (6/10)
- **Disparador**: continuo desde dic-2023 (fin de perpetuas, suscripción por core) con fecha dura el **11-10-2027** (fin de soporte general de vSphere 8.0/ESXi 8.x/vCenter 8.x, KB 459135 de Broadcom [ABIERTA]). Las renovaciones de 1 y 3 años firmadas en 2024 vencen en 2025-2027. Cartas de cese y desistimiento a clientes con perpetuas: hilos de 2.368 votos (8-05-2025) y 1.694 votos (4-12-2025) en r/sysadmin [ABIERTA vía arctic-shift].
- **Odio**: "Broadcom is officially the mafia now" 2.669 votos y 528 comentarios (20-03-2025). 130 posts con "Broadcom" en el título en r/sysadmin desde ene-2024, 1-2/mes todavía en 2026.
- **Demanda**: autocompletado ES "alternativa a vmware" 10/10 ("proxmox alternativa a vmware", "alternativa open source vmware"); "migrar de vmware" 10/10. EN "vmware alternatives 2026", "vmware alternatives enterprise". Volumen y CPC: **sin dato** (pendiente de Planificador).
- **Quién paga y cómo**: MSP (cobra la migración a sus clientes) y responsable IT de pyme con 2-10 hosts. 49 €/mes con clientes ilimitados o 149 € por informe. Autoservicio plausible porque el usuario ya tiene el export de RVTools y quiere un número para la dirección.
- **Competencia**: calculadoras de proveedores interesados (Nutanix, Scale, Vates), RVTools gratis, asistente de importación ESXi en Proxmox 8.2+ gratis, Nutanix Move gratis, consultoras. Nadie neutral y barato que combine "cuánto me va a costar renovar" con "cuánto cuesta irme y en qué orden".
- **Riesgos**: Broadcom no publica precios (hay que estimar con cotizaciones de usuarios; riesgo de error); el comprador IT desconfía de SaaS de un desconocido con su inventario (resolver con procesado local en navegador); ola decreciente (posts 2024 ~8/mes → 2026 ~1,5/mes); marca de 35-50 €/mes solo cuadra con MSP.
- **Siguiente paso barato**: Planificador para 6 términos (ES y mundo); landing con calculadora gratuita (cores → coste Proxmox) y captura de correo; medir conversión antes de construir el parser.

### S2. Autoauditoría de licencias Autodesk/Adobe (5/10)
- **Disparador**: sin fecha única; Autodesk cambió descuentos (ene-2025) y subió ~3,3 % (7-05-2025) [FRAGMENTO distribuidores]; modelo de usuario nominativo desde 2021; auditorías de cumplimiento activas (autocompletado EN "autodesk license compliance and audit engagement" es literal de las cartas). Adobe: subida en Norteamérica 17-06-2025 [FRAGMENTO]; en España no hay subida verificada.
- **Demanda**: pequeña pero con dolor agudo y fecha de respuesta (30 días típicos de la carta): "autodesk license audit" 5 sugerencias EN, "auditoria autodesk" 2 ES; r/AutoCAD "license" 6 posts en jul-2026. Volumen/CPC: sin dato.
- **Quién paga**: gerente o IT de estudio de arquitectura/ingeniería que recibe la carta; 249 € por auditoría es más natural que 39 €/mes.
- **Competencia**: Flexera/Snow/Open iT (grandes), Licenseware (medio), portal de Autodesk (informes de uso solo de asientos legítimos), abogados.
- **Riesgos**: necesita agente en equipos (firma de código, soporte Windows/macOS), mercado pequeño en España, el cliente puede preferir pagar la regularización y callar. No cumple "herramienta que la gente use a diario".

### S3. Radar de renovaciones y fin de soporte para pymes (5/10)
- **Disparador**: suma de fechas verificadas: M365 comercial +12-33 % en cada renovación desde el **1-07-2026** [FRAGMENTO]; Office 2021 y Publisher **13-10-2026**; Windows Server 2016 **12-01-2027**; vSphere 8 **11-10-2027**; SAP **31-12-2027**; Atlassian DC fin de venta a existentes **30-03-2028** [FRAGMENTO]; subidas Slack (17-06-2025), Workspace (ene-2025), Canva Teams (sept-2024).
- **Ángulo UE barato**: el autocompletado español ya contiene "alternativa europea a microsoft 365", "alternativa europea a google workspace", "alternativa europea a notion". El producto sugiere la alternativa europea por partida y calcula el ahorro.
- **Demanda**: la consulta satélite en español casi no existe ("coste licencias microsoft 365" 1 sugerencia; "gestión de suscripciones saas" sin medir). Volumen/CPC: sin dato.
- **Quién paga**: administración/IT de pyme 20-200 empleados a 35 €/mes; MSP como herramienta de venta.
- **Competencia**: endoflife.date gratis (fechas), Cledara desde 75 £/mes, Substly, Torii/Zluri/Vendr (empresa). Hueco: ninguno junta fechas de fin de soporte on-prem con renovaciones SaaS y alternativas UE para pyme española.
- **Riesgos**: producto "agradable de tener", sin dolor agudo; keyword casi inexistente; depende de SEO de contenido (una página por disparador), lo que tarda 6-12 meses.

---

## 5) Duración de la ola (datos)

Páginas vistas mensuales en Wikipedia (usuarios, todos los accesos; API Wikimedia [ABIERTA]; miles):

| Artículo | Base previa | Mes de anuncio / fecha | Pico | +1 mes | +3 meses | +6 meses | Duración estimada |
|---|---|---|---|---|---|---|---|
| en Skype | 47-55 k (2024) | anuncio 28-02-2025; cierre 5-05-2025 | 140 k (mar-2025), 149 k (may-2025) | 63 k (abr), 54 k (jun) | 50 k (ago) | 35 k (nov) | **1 mes por evento**; después queda por debajo de la base (28-33 k en 2026) |
| es Skype | 4-8 k | ídem | 15 k (may-2025) | 6 k (jun) | 4 k (sep) | 2 k (nov) | 1 mes |
| en Windows 10 | 66-89 k (2024) | fin de soporte 14-10-2025 | 151 k (oct-2025) | 60 k (nov) | 48 k (ene-2026) | 41 k (abr-2026) | **1 mes**; la base cae a la mitad (38-41 k) |
| es Windows 10 | 10-20 k | ídem | 22 k (oct-2025) | 6 k (nov) | 5 k (ene) | 4 k (abr) | 1 mes |
| en Zorin OS (sustituto) | 6-8 k | ídem | 24 k (nov-2025) | 20 k (dic) | 17 k (feb) | 16 k (abr); 9 k (jun) | **~7 meses** elevado |
| en Linux Mint (sustituto) | 23-30 k | ídem | 40 k (oct-2025) | 32 k (nov) | 38 k (ene) | 31 k (abr); 23 k (jun) | ~4-8 meses |
| en Affinity Photo (sustituto) | 5-6 k | Affinity gratis (anuncio oct-2025) | 16 k (nov-2025) | 9 k (dic) | 6 k (feb) | 6 k (may) | ~2-3 meses |
| en Pocket (service) | 2-3 k | cierre 2025 | 6 k (may-2025) | 4 k (jun) | 2 k (ago) | 2 k (nov); 1 k en 2026 | 2-3 meses |
| en Google Analytics | 27-32 k (ene-abr 2024) | borrado UA 1-07-2024 | sin pico (19 k jul-2024) | 18 k | 16 k | 13 k | sin ola; declive continuo hasta 6-9 k en 2026 |
| en Proxmox VE (sustituto VMware) | 17-20 k (ene-mar 2024) | cambios Broadcom dic-2023 en adelante | sin pico claro (19 k ene-2025) | – | – | – | declive suave a 11-14 k en 2026: la atención al sustituto no acompaña al odio al incumbente |
| en Broadcom | 33-61 k | cartas may-2025 / dic-2025 | 75 k (dic-2024, otras noticias), 61 k (ene-2025), 56 k (sep-2025) | – | – | – | ruido corporativo; no sirve de medida |
| es Verifactu | 89 (oct-2025, artículo nuevo) | aplazamiento 3-12-2025 | 390 (dic-2025) | 258 (ene-2026) | 91 (mar) | 62 (jun); 170 (sep-2026) | 2-3 meses; repunte en sep-2026 al acercarse 2027 |

Reddit (arctic-shift, títulos, r/sysadmin [ABIERTA]):
- "ESU": 2025-09: 5 · 10: **10** · 11: 5 · 12: 7 · 2026-01: 3 · 02: 1 · 03: 2 · 04: 1 · 06: 1 · 08: 1 · 09: 3 · 10: 1. Ola de **4 meses**; hilo representativo "Sysadmins with Windows 10 holdouts: what are you actually doing in 2026" (13-03-2026, 58 comentarios).
- "Broadcom": 2024 ene-sep media ~8/mes; 2025 ~3-5/mes con picos de votos (2.669, 2.368, 1.694); 2026 1-2/mes. Ola de **más de 30 meses**, decreciente pero sostenida por renovaciones y nuevos cambios (72 cores abr-2025, renovaciones parciales ene-2026).
- "Publisher": 2026-04: 2 · 05: 2 · 08: 1 · 09: 3 · 10: 2. Sin ola apreciable pese a la fecha.
- "license" en r/AutoCAD: 1-2/mes con pico de 6 en jul-2026.

Trends medido por Jorge el 4-10-2026 (sesión local): "verifactu" pico 30-11-2025 = 100 en España y ~14 dos semanas después.

**Lectura.** Cuando el disparador es una fecha única (cierre, fin de soporte), la atención al incumbente dura un mes y la del sustituto 2-7 meses; después el mercado queda más pequeño que antes. Solo un disparador escalonado (renovaciones por contrato, cartas de auditoría, cambios de licencia sucesivos) mantiene demanda 24 meses o más. Para un micro-SaaS de 35-50 €/mes que necesita 12-18 meses para madurar SEO, solo valen los disparadores escalonados (VMware/Broadcom, M365 por renovación, auditorías Autodesk/Oracle, Verifactu si no vuelve a aplazarse).

---

## 6) Tabla de URLs abiertas con estado

151 intentos de apertura con `pwfetch.js`/`r.jina.ai` (79 con contenido legible), más 5 lecturas con WebFetch, 11 consultas WebSearch, 36 consultas de autocompletado, 29 series de Wikipedia y 12 consultas arctic-shift. "jina" = vía r.jina.ai; "browser" = Chromium; "http" = cliente HTTP directo. Estado: ABIERTA = texto leído; BLOQUEADA = captcha/anti-bot; FALLO = 401/403/404/vacía/timeout.

| URL | Vía | HTTP | Estado |
|---|---|---|---|
| https://learn.microsoft.com/en-us/lifecycle/products/windows-10-home-and-pro | http | 200 | ABIERTA |
| https://support.microsoft.com/en-us/windows/windows-10-consumer-extended-security-updates-esu-program-33e17de9-36b3-43bb-874d-6c53d2e4bf42 | http | 200 | ABIERTA |
| https://learn.microsoft.com/en-us/windows/whats-new/extended-security-updates | http | 200 | ABIERTA |
| https://learn.microsoft.com/en-us/lifecycle/products/exchange-server-2019 | http | 200 | ABIERTA |
| https://learn.microsoft.com/en-us/lifecycle/products/office-2019 | http | 404 | FALLO/404/403/vacía |
| https://learn.microsoft.com/en-us/lifecycle/products/office-2021 | http | 200 | ABIERTA |
| https://learn.microsoft.com/en-us/lifecycle/products/windows-server-2012-r2 | http | 200 | ABIERTA |
| https://learn.microsoft.com/en-us/lifecycle/products/windows-server-2016 | http | 200 | ABIERTA |
| https://learn.microsoft.com/en-us/lifecycle/products/sql-server-2016 | http | 200 | ABIERTA |
| https://support.microsoft.com/en-us/office/microsoft-publisher-will-no-longer-be-supported-after-october-2026-ab9f2fed-4b31-4d8f-a6c2-cfdc6fad0d4c | http | 404 | FALLO/404/403/vacía |
| https://support.microsoft.com/en-us/skype/skype-is-retiring-in-may-2025-what-you-need-to-know-2a7d2501-427f-485e-8be0-2068a9f90472 | http | 200 | ABIERTA |
| https://www.microsoft.com/en-us/microsoft-365/blog/2025/12/04/microsoft-365-pricing-update-effective-july-1-2026/ | http | 404 | FALLO/404/403/vacía |
| https://www.microsoft.com/en-us/microsoft-365/blog/2025/01/16/copilot-is-now-included-in-microsoft-365-personal-and-family/ | http | 200 | ABIERTA |
| https://workspace.google.com/blog/product-announcements/empowering-businesses-with-AI | http | 200 | ABIERTA |
| https://support.mozilla.org/en-US/kb/future-of-pocket | http | 200 | BLOQUEADA (bot/captcha) |
| https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline | http | 200 | ABIERTA |
| https://news.sap.com/2020/02/sap-s4hana-maintenance-2040-clarity-choice-sap-business-suite-7/ | http | 200 | ABIERTA |
| https://support.google.com/analytics/answer/11583528?hl=en | http | 200 | ABIERTA |
| https://www.oracle.com/java/java-se-subscription/ | http | 200 | ABIERTA |
| https://android-developers.googleblog.com/2025/08/elevating-android-security.html | http | 200 | ABIERTA |
| https://www.microsoft.com/en-us/microsoft-365/blog/ | http | 200 | ABIERTA |
| https://www.bing.com/search?q=microsoft+365+pricing+update+july+1+2026+site%3Amicrosoft.com | http | 200 | ABIERTA |
| https://learn.microsoft.com/en-us/lifecycle/products/microsoft-office-2019 | http | 200 | ABIERTA |
| https://support.microsoft.com/en-us/office/microsoft-publisher-will-no-longer-be-supported-after-october-2026-ab9f2fed-4b31-4d8f-a6c2-cfdc6fad0d4c | browser | 404 | FALLO/404/403/vacía |
| https://support.mozilla.org/en-US/kb/future-of-pocket | browser | 200 | FALLO/404/403/vacía |
| https://news.broadcom.com/releases/broadcom-dramatically-simplifies-vmware-offer-lineup-and-licensing-model | http | 200 | FALLO/404/403/vacía |
| https://support.broadcom.com/group/ecx/productlifecycle | browser | 403 | BLOQUEADA (bot/captcha) |
| https://knowledge.broadcom.com/external/article/318697 | browser | 200 | ABIERTA |
| https://www.autodesk.com/support/account/admin/subscription/pricing-changes | browser | 403 | FALLO/404/403/vacía |
| https://www.autodesk.com/campaigns/new-buying-experience | browser | 403 | FALLO/404/403/vacía |
| https://helpx.adobe.com/creative-cloud/plans-pricing/pricing-update.html | browser | 403 | FALLO/404/403/vacía |
| https://affinity.serif.com/ | browser | 200 | ABIERTA |
| https://slack.com/blog/news/pricing-and-packaging-updates | browser | 404 | FALLO/404/403/vacía |
| https://www.atlassian.com/licensing/future-pricing/cloud-pricing-changes | browser | 404 | FALLO/404/403/vacía |
| https://www.atlassian.com/blog/announcements/data-center-end-of-life | browser | 404 | FALLO/404/403/vacía |
| https://zapier.com/pricing | browser | 200 | ABIERTA |
| https://www.canva.com/pricing/ | browser | 403 | FALLO/404/403/vacía |
| https://www.notion.com/pricing | browser | 200 | ABIERTA |
| https://help.evernote.com/hc/en-us/articles/23272082432403 | browser | 403 | BLOQUEADA (bot/captcha) |
| https://support.google.com/domains/answer/13689670?hl=en | http | 200 | ABIERTA |
| https://www.autodesk.com/support/account/admin/subscription/pricing-changes | jina | 200 | ABIERTA |
| https://www.autodesk.com/campaigns/new-buying-experience | jina | 200 | ABIERTA |
| https://helpx.adobe.com/creative-cloud/plans-pricing/pricing-update.html | jina | 200 | ABIERTA |
| https://www.canva.com/help/teams-pricing-changes/ | jina | 200 | BLOQUEADA (bot/captcha) |
| https://help.evernote.com/hc/en-us/articles/23272082432403 | jina | 200 | BLOQUEADA (bot/captcha) |
| https://news.broadcom.com/releases/broadcom-dramatically-simplifies-vmware-offer-lineup-and-licensing-model | jina | 401 | BLOQUEADA (bot/captcha) |
| https://knowledge.broadcom.com/external/article/318697 | jina | 200 | ABIERTA |
| https://support.mozilla.org/en-US/kb/future-of-pocket | jina | 200 | BLOQUEADA (bot/captcha) |
| https://support.microsoft.com/en-us/office/microsoft-publisher-will-no-longer-be-supported-after-october-2026-ab9f2fed-4b31-4d8f-a6c2-cfdc6fad0d4c | jina | 200 | ABIERTA |
| https://slack.com/intl/en-gb/pricing | jina | 200 | ABIERTA |
| https://www.atlassian.com/licensing/future-pricing | jina | 200 | ABIERTA |
| https://mailchimp.com/pricing/marketing/ | jina | 401 | BLOQUEADA (bot/captcha) |
| https://www.typeform.com/pricing/ | jina | 200 | ABIERTA |
| https://calendly.com/pricing | jina | 200 | ABIERTA |
| https://unity.com/blog/unity-is-canceling-the-runtime-fee | jina | 200 | ABIERTA |
| https://developer.x.com/en/portal/products | jina | 200 | ABIERTA |
| https://blog.lastpass.com/posts/notice-of-recent-security-incident | jina | 200 | ABIERTA |
| https://endof10.org/ | jina | 200 | ABIERTA |
| https://gs.statcounter.com/windows-version-market-share/desktop/worldwide | jina | 401 | BLOQUEADA (bot/captcha) |
| https://gs.statcounter.com/windows-version-market-share/desktop/spain | jina | 200 | ABIERTA |
| https://trends.google.com/trends/explore?geo=ES&date=today%2024-m&q=alternativa%20a%20skype | browser | 429 | BLOQUEADA (bot/captcha) |
| https://www.spyfu.com/overview/keyword?query=vmware%20alternative | browser | 403 | BLOQUEADA (bot/captcha) |
| https://alternativeto.net/software/vmware-vsphere/ | jina | 401 | BLOQUEADA (bot/captcha) |
| https://alternativeto.net/software/windows-10/ | jina | 200 | BLOQUEADA (bot/captcha) |
| https://alternativeto.net/software/autocad/ | jina | 200 | BLOQUEADA (bot/captcha) |
| https://alternativeto.net/software/adobe-photoshop/ | jina | 401 | BLOQUEADA (bot/captcha) |
| https://alternativeto.net/software/skype/ | jina | 200 | BLOQUEADA (bot/captcha) |
| https://alternativeto.net/software/pocket/ | jina | 200 | BLOQUEADA (bot/captcha) |
| https://alternativeto.net/software/google-analytics/ | jina | 200 | BLOQUEADA (bot/captcha) |
| https://alternativeto.net/software/evernote/ | jina | 200 | BLOQUEADA (bot/captcha) |
| https://alternativeto.net/software/lastpass/ | jina | 200 | BLOQUEADA (bot/captcha) |
| https://alternativeto.net/software/microsoft-office-publisher/ | jina | 200 | BLOQUEADA (bot/captcha) |
| https://web.archive.org/web/2025id_/https://helpx.adobe.com/creative-cloud/plans-pricing/pricing-update.html | jina | 403 | BLOQUEADA (bot/captcha) |
| https://web.archive.org/web/2025id_/https://support.mozilla.org/en-US/kb/future-of-pocket | jina | 403 | BLOQUEADA (bot/captcha) |
| https://web.archive.org/web/2025id_/https://support.microsoft.com/en-us/office/microsoft-publisher-will-no-longer-be-supported-after-october-2026-ab9f2fed-4b31-4d8f-a6c2-cfdc6fad0d4c | jina | 401 | BLOQUEADA (bot/captcha) |
| https://www.aepd.es/informes-y-resoluciones/resoluciones | jina | 401 | BLOQUEADA (bot/captcha) |
| https://www.aepd.es/guias/guia-cookies.pdf | jina | 200 | ABIERTA |
| https://digital-strategy.ec.europa.eu/en/library/digital-omnibus | jina | 200 | BLOQUEADA (bot/captcha) |
| https://www.boe.es/diario_boe/txt.php?id=BOE-A-2025-26379 | jina | 200 | ABIERTA |
| https://quickbooks.intuit.com/learn-support/en-us/help-article/service-discontinuation/quickbooks-desktop-service-discontinuation-policy/L1lLgAwJB_US_en_US | jina | 200 | ABIERTA |
| https://alternativeto.net/software/vmware-vsphere/ | browser | 403 | BLOQUEADA (bot/captcha) |
| https://alternativeto.net/software/skype/ | browser | 403 | BLOQUEADA (bot/captcha) |
| https://alternativeto.net/software/microsoft-office-publisher/ | browser | 403 | BLOQUEADA (bot/captcha) |
| https://web.archive.org/web/20250601000000*/https://support.mozilla.org/en-US/kb/future-of-pocket | browser | 502 | FALLO/404/403/vacía |
| https://web.archive.org/web/20250701id_/https://support.mozilla.org/en-US/kb/future-of-pocket | http | https://web.archive.org/web/20250701id_/https://support.mozilla.org/en-US/kb/future-of-pocket | FALLO/404/403/vacía |
| https://web.archive.org/web/20250701id_/https://helpx.adobe.com/creative-cloud/plans-pricing/pricing-update.html | http | https://web.archive.org/web/20250701id_/https://helpx.adobe.com/creative-cloud/plans-pricing/pricing-update.html | FALLO/404/403/vacía |
| https://web.archive.org/web/20250601id_/https://support.microsoft.com/en-us/office/microsoft-publisher-will-no-longer-be-supported-after-october-2026-ab9f2fed-4b31-4d8f-a6c2-cfdc6fad0d4c | http | https://web.archive.org/web/20250601id_/https://support.microsoft.com/en-us/office/microsoft-publisher-will-no-longer-be-supported-after-october-2026-ab9f2fed-4b31-4d8f-a6c2-cfdc6fad0d4c | FALLO/404/403/vacía |
| https://web.archive.org/web/20250901id_/https://www.autodesk.com/support/account/admin/subscription/pricing-changes | http | https://web.archive.org/web/20250901id_/https://www.autodesk.com/support/account/admin/subscription/pricing-changes | FALLO/404/403/vacía |
| https://web.archive.org/web/20240201id_/https://news.broadcom.com/releases/broadcom-dramatically-simplifies-vmware-offer-lineup-and-licensing-model | http | https://web.archive.org/web/20240201id_/https://news.broadcom.com/releases/broadcom-dramatically-simplifies-vmware-offer-lineup-and-licensing-model | FALLO/404/403/vacía |
| https://knowledge.broadcom.com/external/article/390209 | browser | 200 | ABIERTA |
| https://office-watch.com/2025/microsoft-365-price-increase-2026/ | jina | 200 | ABIERTA |
| https://www.atlassian.com/blog/announcements/data-center-end-of-life-announcement | jina | 401 | BLOQUEADA (bot/captcha) |
| https://www.atlassian.com/migration | jina | 401 | BLOQUEADA (bot/captcha) |
| https://ec.europa.eu/commission/presscorner/detail/en/ip_25_2718 | jina | 401 | BLOQUEADA (bot/captcha) |
| https://www.aepd.es/prensa-y-comunicacion/notas-de-prensa | jina | 200 | ABIERTA |
| https://blog.zorin.com/ | jina | 200 | ABIERTA |
| https://workspace.google.com/blog/product-announcements/empowering-businesses-with-AI | jina | 200 | ABIERTA |
| https://www.oracle.com/java/technologies/javase/jdk-faqs.html | jina | 401 | BLOQUEADA (bot/captcha) |
| https://trends.google.es/trends/explore?geo=ES&date=today%2024-m&q=alternativa%20a%20skype | browser | 429 | BLOQUEADA (bot/captcha) |
| https://explodingtopics.com/topic/proxmox | jina | 200 | ABIERTA |
| https://explodingtopics.com/topic/end-of-10 | jina | 200 | ABIERTA |
| https://ahrefs.com/keyword-generator/?country=es&input=alternativa%20a%20vmware | browser | 200 | ABIERTA |
| https://seranking.com/keyword-suggestion-tool.html?keyword=vmware%20alternative&source=es | browser | 200 | ABIERTA |
| https://www.proxmox.com/en/products/proxmox-virtual-environment/pricing | http | 200 | ABIERTA |
| https://vates.tech/pricing/ | jina | 200 | ABIERTA |
| https://www.bricsys.com/en-eu/shop | jina | 200 | ABIERTA |
| https://www.zwsoft.com/product/zwcad | jina | 200 | ABIERTA |
| https://raindrop.io/pro | jina | 200 | ABIERTA |
| https://www.instapaper.com/premium | jina | 200 | ABIERTA |
| https://plausible.io/#pricing | http | 200 | ABIERTA |
| https://www.lansweeper.com/pricing/ | jina | 200 | ABIERTA |
| https://www.pdq.com/pricing/ | jina | 200 | ABIERTA |
| https://www.substly.com/pricing | jina | 200 | ABIERTA |
| https://www.cledara.com/pricing | jina | 200 | ABIERTA |
| https://pve.proxmox.com/wiki/Migrate_to_Proxmox_VE | http | 200 | ABIERTA |
| https://www.azul.com/products/components/azul-intelligence-cloud/ | jina | 200 | BLOQUEADA (bot/captcha) |
| https://www.scribus.net/ | jina | 200 | ABIERTA |
| https://github.com/rcmaehl/WhyNotWin11 | jina | 403 | BLOQUEADA (bot/captcha) |
| https://getpocket.com/farewell | jina | 200 | ABIERTA |
| https://blog.mozilla.org/en/mozilla/pocket-shutting-down/ | jina | 200 | ABIERTA |
| https://support.microsoft.com/en-us/publisher | http | 200 | ABIERTA |
| https://www.oracle.com/a/ocom/docs/corporate/pricing/java-se-subscription-pricelist-070621.pdf | http | 404 | FALLO/404/403/vacía |
| https://digital-strategy.ec.europa.eu/en/policies/digital-omnibus | browser | 403 | BLOQUEADA (bot/captcha) |
| https://www.theverge.com/2024/9/3/24234904/canva-teams-price-increase-ai | jina | 403 | BLOQUEADA (bot/captcha) |
| https://slack.com/blog/news/slack-business-plus-plan-pricing-update | jina | 401 | BLOQUEADA (bot/captcha) |
| https://www.theregister.com/2025/04/10/broadcom_vmware_72_cores/ | jina | 200 | ABIERTA |
| https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu.html | jina | 200 | ABIERTA |
| https://www.microsoft.com/en-us/windows/windows-11-specifications | http | 200 | ABIERTA |
| https://www.nutanix.com/products/move | jina | 200 | ABIERTA |
| https://www.starwindsoftware.com/starwind-v2v-converter | jina | 401 | BLOQUEADA (bot/captcha) |
| https://slack.com/help/articles/39264531104275-Updates-to-feature-availability-and-pricing-for-Slack-plans | jina | 200 | ABIERTA |
| https://duckduckgo.com/html/?q=canva+teams+price+increase+2024+per+user | jina | 200 | ABIERTA |
| https://www.autodesk.com/in/price-change-terms-conditions | jina | 200 | ABIERTA |
| https://www.semrush.com/website/proxmox.com/overview/ | jina | 401 | BLOQUEADA (bot/captcha) |
| https://www.saashub.com/vmware-vsphere-alternatives | jina | 200 | BLOQUEADA (bot/captcha) |
| https://www.saashub.com/skype-alternatives | jina | 200 | BLOQUEADA (bot/captcha) |
| https://www.saashub.com/pocket-alternatives | jina | 200 | BLOQUEADA (bot/captcha) |
| https://www.saashub.com/microsoft-publisher-alternatives | jina | 200 | BLOQUEADA (bot/captcha) |
| https://www.saashub.com/autocad-alternatives | jina | 200 | BLOQUEADA (bot/captcha) |
| https://www.saashub.com/google-analytics-alternatives | jina | 200 | BLOQUEADA (bot/captcha) |
| https://www.saashub.com/microsoft-365-alternatives | jina | 200 | BLOQUEADA (bot/captcha) |
| https://www.saashub.com/lastpass-alternatives | jina | 200 | BLOQUEADA (bot/captcha) |
| https://learn.microsoft.com/en-us/lifecycle/products/microsoft-office-2016 | http | 200 | ABIERTA |
| https://learn.microsoft.com/en-us/lifecycle/products/exchange-server-2016 | http | 200 | ABIERTA |
| https://www.oracle.com/a/ocom/docs/corporate/pricing/java-se-subscription-pricelist.pdf | http | 404 | FALLO/404/403/vacía |
| https://www.adobe.com/products/catalog.html | jina | 200 | ABIERTA |
| https://licenseware.io/adobe-licensing-pricing-changes-comprehensive-analysis-of-2025-updates/ | jina | 200 | ABIERTA |
| https://petapixel.com/2025/05/20/if-you-have-adobe-creative-cloud-your-price-could-increase-next-month/ | jina | 200 | ABIERTA |
| https://www.canva.com/newsroom/news/affinity-free/ | jina | 200 | ABIERTA |
| https://www.autodesk.com/company/license-compliance | jina | 401 | BLOQUEADA (bot/captcha) |
| https://managewp.com/pricing | jina | 401 | BLOQUEADA (bot/captcha) |
Otras lecturas (no pwfetch):
| Fuente | Método | Estado |
|---|---|---|
| https://knowledge.broadcom.com/external/article/459135/end-of-general-support-for-vsphere-80.html | WebFetch | ABIERTA (cita literal de la fecha 11-10-2027) |
| https://helpx.adobe.com/creative-cloud/plans-pricing/pricing-update.html | WebFetch | FALLO 403 |
| https://www.autodesk.com/support/account/admin/subscription/pricing-changes | WebFetch | FALLO 403 |
| https://support.mozilla.org/en-US/kb/future-of-pocket | WebFetch | BLOQUEADA (challenge) |
| https://support.microsoft.com/en-us/office/microsoft-publisher-...ab9f2fed... | WebFetch | FALLO 404 (la URL vigente es https://support.microsoft.com/en-us/publisher, ABIERTA) |
| https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/... (29 series en/es) | curl | ABIERTA (en VMware y Microsoft_365 fallaron por límite de peticiones) |
| https://arctic-shift.photon-reddit.com/api/posts/search?subreddit=sysadmin&title=... | curl | ABIERTA (r/vmware, r/msp, r/skype, r/Pocket, r/Autodesk devolvieron 0 posts con el filtro `title`) |
| https://suggestqueries.google.com/complete/search?client=firefox&hl=es&gl=es&q=... (36 consultas) | curl | ABIERTA |
| https://trends.google.com/trends/api/explore (API) | curl | FALLO (devuelve HTML) |
| WebSearch (11): M365 jul-2026; vSphere 8 EoGS; Atlassian DC EOL; Adobe CC Pro; Publisher; Autodesk 2025; AEPD cookies; CPC "alternativa a"; Verifactu RDL 15/2025; Broadcom 72 cores; Slack/Canva | WebSearch | FRAGMENTO (resúmenes con enlaces; no sustituyen a la fuente primaria) |

Datos no verificados que conviene cerrar en una sesión local con Chrome: URL primaria del anuncio de precios de Microsoft 365 del 1-07-2026; nota de Broadcom de dic-2023 (news.broadcom.com); FAQ oficial de Atlassian sobre Data Center; página de Adobe sobre precios; fechas exactas de cierre y exportación de Pocket; texto del RDL 15/2025 en el BOE (BOE-A-2025-24446 según Invoo, sin verificar); propuesta Digital Omnibus de la Comisión (cookies); volumen y CPC de las 24 palabras clave en el Planificador.
