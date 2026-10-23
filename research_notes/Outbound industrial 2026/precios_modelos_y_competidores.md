# Prospección B2B externalizada para fabricantes industriales (España): precios, modelos y competidores

Investigación adversarial con páginas abiertas. Fecha de captura: 23-10-2026. Herramienta: `tools/pwfetch.js` (HTTP y Chromium), `curl` y la API de archivo de Reddit (arctic-shift) cuando reddit.com bloqueó. Convenciones: **[ABIERTA]** = página leída entera o en lo relevante; **[FRAGMENTO]** = solo fragmento vía buscador/tercero; **NO ENCONTRADO** = no localizado o bloqueado. Todas las cifras llevan moneda y fecha (fecha de la página si la publica; si no, fecha de captura).

---

## 0. Veredictos

**H1 (modelos de precio) — PARCIALMENTE CONFIRMADA, con dos correcciones importantes.**
- Retainer mensual es el modelo dominante en todas partes, sí. Pero en España *no hay ni una sola agencia de outbound que publique su tarifa*: de ~20 páginas españolas abiertas, solo DevCommX (sede Madrid, web en inglés y dólares) publica "From $6,000/month". El rango 1.500-4.000 €/mes de la hipótesis solo aparece como **estimación de terceros** (SyncGTM estima €1.500-4.000/mes para SalesCaptain y €3.000-8.000 para Gotoclient; Salesforge afirma "la mayoría de agencias de cold email en España cobran entre 1.000 y 4.500 €/mes"; SyncGTM dice que "las agencias GTM españolas cobran €5.000-15.000/mes"). Es decir: el rango es plausible pero **no está publicado por ninguna agencia española**; el mercado español es opaco.
- Pago por reunión: existe sobre todo en EE. UU./RU y en freelancers. Rango publicado en comparativas 2025-2026: 50-500 USD la banda baja (SalesAR, Intelemark, SalesBread), 150-900 USD (Smartlead, Cleverly pyme/mid-market), 300-1.500 USD (SaaSHero, GigRadar), hasta 800-2.500 USD enterprise (Cleverly). La cifra "100-500 €" de la hipótesis es correcta para pymes pero infravalora el segmento mid-market/enterprise. En España no hallé ninguna agencia que publique precio por reunión; sí ofertas en Workana de setters pagados "por reunión agendada" (importe a pactar). Skipcall (vendedor francés de dialers, blog en español) sitúa la mediana interna española en 200-300 € por reunión conseguida.
- "Piloto pagado de 30 días con garantía de reuniones a 500-1.500 €": **NO CONFIRMADA**. Lo que existe es: pilotos de 3-4 meses (Martal, "3 Month Pilot Campaign" y "4 Month Pilot Campaign", precio a consultar; Belkins "custom quotes for 4, 6 and 12 months"); periodos de 4 semanas renovables desde 11.950 USD (SalesRoads); mes a mes (Leadium, CIENCE, Sopro "no minimum contract"). Ninguna agencia abierta ofrece un piloto de 30 días por 500-1.500 €. La garantía habitual no es "X reuniones o te devolvemos el dinero" sino **"si la reunión no cumple los criterios acordados, la repetimos sin coste"** (CustomerTop, España) o "100 guaranteed appointments/year" ligado a un retainer de 8.000 USD/mes (Belkins). Leadium declara explícitamente que *no* da garantías de resultado.
- Comisión por cliente cerrado: **CONFIRMADO que es raro** y además rechazado activamente por las agencias (hilo de r/sales con 29 votos: "They insist on paying us only once deal is closed. We dont do that"). Solo Martal lo ofrece como híbrido ("flat fee per month + sales commission") y Belkins/SaaSHero describen híbridos base + bono por reunión (3.000-5.000 USD + ~150 USD/reunión en el caso de Belkins, según un usuario de Reddit citado por Salesforge).

**H2 (demanda consciente y categoría con nombre) — CONFIRMADA A MEDIAS.**
- La categoría existe y tiene nombre en España, pero el nombre dominante *no* es "SDR externalizado" ni "appointment setting": es **"concertación de visitas comerciales"** (CustomerTop lleva "+21 años" en ello, "+900 empresas" en España/Latam; LCA Contact Center, Barcelona; InfoJobs lista 104 ofertas con la palabra "concertación" y hay ofertas de "Concertador/a de visitas B2B" a 18.000 € brutos/año). "Appointment setting" en España está capturado por el mundo del infoproducto/high-ticket (Forbes España, 2-8-2023, nota de pago: "nueva profesión sin paro", "entre dos mil y siete mil euros netos mensuales"), no por la industria.
- Los fabricantes industriales *sí* contratan: CustomerTop tiene páginas de "Sector Maquinaria" y "Sector Fabricación y Manufactura", con un formulario que pregunta "¿Qué importe mensual estás invirtiendo…?" con tramos "Menos de 1.000 € / 1.000-2.500 € / 2.500-5.000 € / 5.000-10.000 € / Más de 10.000 €"; Durhamlane (RU) publica un caso industrial (RS Industria, IoT industrial, "£700k estimated pipeline"); SalesAR describe un cliente "manufacturing supplier" en la UE que pagaba 80-150 USD por reunión; Intelemark pone como ejemplo "a manufacturer that wants strategic accounts with more than €1M in revenue but receives mostly SMB meetings".
- Pero la demanda es *pequeña y poco digital*: Google Trends no pudo abrirse (HTTP 429 en tres intentos); tecnoempleo devuelve 3 ofertas para "sdr"; la mayoría de las "agencias de generación de leads" españolas que salen en rankings (Marketers Group, Dobuss, BCM, Novicell, Connext, Inbound Emotion, mbudo, Marketinet, Inprofit, WAM) son **agencias de inbound/HubSpot/SEO/Ads**, no de outbound. El propio Salesforge lo reconoce: "Most credible options here are digital marketing agencies with strong lead generation practices rather than pure SDR shops".

Conclusión para el negocio: el hueco real no es "nadie hace outbound para industria" (CustomerTop lo hace por teléfono+LinkedIn desde hace 21 años), sino que **nadie en España publica precio, nadie ofrece un piloto corto con garantía explícita, y casi nadie combina correo frío + LinkedIn dirigido por IA con lenguaje industrial**. El riesgo es el contrario al previsto: el comprador industrial español asocia la categoría con telemarketing y con setters de infoproductos, y desconfía (ver frases en §6).

---

## 1. Agencias en España (y con sede/cobertura española)

| # | Agencia | URL | Modelo de precio | Precio publicado / citado | Permanencia | Garantía | Nicho industrial | Tamaño | Estado |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **CustomerTop** (Madrid; España+Latam) | https://customertop.com/ · /sector-maquinaria/ · /concertacion-de-visitas-comerciales/ · /garantias-de-calidad/ | **Tarifa plana mensual** ("mediante una tarifa plana y sin compromiso de permanencia") | No publica. Formulario con tramos de inversión mensual: <1.000 € / 1.000-2.500 € / 2.500-5.000 € / 5.000-10.000 € / >10.000 € (capt. 23-10-2026) | "sin compromiso de permanencia" | "Garantizamos que el 100% de las reuniones cumplen con los criterios de calidad acordados… Si no, las repetimos SIN COSTE" | **Sí**: páginas "Sector Maquinaria", "Fabricación y Manufactura", "Productos Químicos", "Logística" | "+21 años", "+900 empresas", "+800 empresas confían"; casos: Grenke, Coface, Daikin, Midas, Due Corporación | [ABIERTA] |
| 2 | **DevCommX** (Madrid; web en inglés) | https://www.devcommx.com/appointment-setting/madrid · /b2b-lead-generation/bilbao/manufacturing | **Retainer gestionado** | "Managed Appt Setting Engagement **From $6,000/month**" (USD, capt. 23-10-2026); promete "8-15 qualified appointments per setter per month" | No publica | No publica garantía de resultados | Páginas por ciudad y por sector, incluida "Manufacturing Bilbao/Málaga, 90-240 days sales cycle" (SEO programático) | No publica | [ABIERTA] |
| 3 | **SalesCaptain** (Londres/España, outbound SaaS) | https://www.salescaptain.io/ | Retainer, presupuesto a medida | No publica. SyncGTM estima "€1,500–€4,000/month for execution programmes" y en otro post "approximately €3,500/month" (2026) | No publica | No | No (B2B SaaS; "60+ organizations") | "80+ demand generation specialists" (SyncGTM) | [ABIERTA] + [FRAGMENTO] precio |
| 4 | **Gotoclient** (Barcelona) | https://www.gotoclient.com/ | Retainer/programa a medida (LinkedIn Ads, ABM, "Sales Outreach") | No publica. SyncGTM estima "€3,000–€8,000/month" | — | — | Declara verticales "industrial, tech, SaaS" (SyncGTM) | Pequeña ("smaller team") | [ABIERTA] + [FRAGMENTO] |
| 5 | **HighConverting Agency** (Madrid, cold email) | https://www.salesforge.ai/directory/agencies/highconverting | **Pago por lead** ("Pay-per-lead model") | No publica importe | — | — | No | "10-50 employees" | [FRAGMENTO] (ficha de directorio) |
| 6 | **Reachflow** (Gabriel Martínez; cold email España+LATAM) | https://reachflow.io/ · https://lu.ma/ztx91i2b | No publica | No publica | — | — | No (SaaS/servicios) | — | web JS sin texto; [FRAGMENTO] vía Luma/Smartlead y Favikon |
| 7 | **Sales Force Europe** (Madrid; outsourcing de ventas para tech) | https://salesforceeurope.com/ | Equipo gestionado (retainer) | No publica | — | — | No (tech entrando en Europa) | — | [ABIERTA] |
| 8 | **LCA Contact Center** (Cornellà, telemarketing) | https://www.lcacontactcenter.com/ | Telemarketing/concertación de visitas (precio a consultar) | No publica | — | — | Multisector | — | [ABIERTA] |
| 9 | **Callbox** (global, página España) | https://www.callboxinc.com/lead-generation-spain/ | Retainer; Belkins cita "Starts at $15,000 per campaign pod" (2024) | 15.000 USD/pod (cita de tercero) | — | — | No | Grande | [ABIERTA] + [FRAGMENTO] |
| 10 | **Novicell** (Barcelona; "agencia digital para el sector B2B industrial") | https://www.novicell.es/ | Proyecto/retainer inbound (SEO, paid, HubSpot) | No publica | — | — | **Sí** ("60% de nuestros proyectos son de empresas industriales B2B") pero **no outbound** | "+30 especialistas" | [ABIERTA] |
| 11 | **Connext** (Valencia; marketing industrial, HubSpot Platinum) | https://www.connext.es/ | Inbound/HubSpot | No publica | — | — | Sí (industrial), **no outbound** | — | [ABIERTA] |
| 12 | **Inbound Emotion** (Barcelona; industrial/HubSpot) | https://www.inboundemotion.com/ | Proyecto | "rediseño web con CMS… desde los 8.000 €" (capt. 23-10-2026) | — | — | Sí (industrial), **no outbound** | — | [ABIERTA] |
| 13 | **Línea Gráfica** (Barcelona/Madrid/Sevilla) | https://www.lineagrafica.es/ | Retainer marketing | FAQ: "cuotas mensuales de retainer parten habitualmente desde rangos de 1.500 a 4.000 euros" (es para ecommerce, no outbound) | — | — | No | — | [ABIERTA] |
| 14 | **mbudo** (HubSpot Diamond) | https://www.mbudo.com/ | Inbound/CRM | No publica | — | — | No | — | [ABIERTA] |
| 15 | **Marketinet** (Madrid) | https://www.marketinet.com/ | Inbound/automation | No publica | — | — | No | — | [ABIERTA] |
| 16 | **Inprofit** (Valencia/Alicante) | https://www.inprofit.es/ | MarTech/inbound | No publica | — | — | No | — | [ABIERTA] |
| 17 | **WAM** (Madrid) | https://www.wearemarketing.com/ | Consultora digital | No publica | — | — | No | — | [ABIERTA] |
| 18 | **Smart Team**, **ALYS Marketing**, **omnieGTM**, **eXprimeNet**, **Avnza**, **Lead Market**, **Phone Tool Marketing** | smart-team.es · alysmarketing.com · omniegtm.com · exprimenet.com · avnza.com · leadmarket.es · phonetoolmarketing.com | — | — | — | — | ALYS y Avnza se anuncian como "industrial lead generation" (Salesforge/Clutch) | — | NO ENCONTRADO (502 / certificado inválido / caído el 23-10-2026) |
| 19 | **Clarmaj** (Portugal, clientes en España; pymes de moldes, metalurgia, fundición) | https://www.goodfirms.co/company/clarmaj | — | No publica | — | — | **Sí**, industrial; "prospección LinkedIn con contacto directo a decisores" (snippet) | — | [FRAGMENTO] |
| 20 | **Sortlist – "Lead Generation Spain"** | https://www.sortlist.com/s/lead-generation/spain-es | Directorio: **138 companies**; "From €150 / €300 / €500 / €1,000 for Lead Generation" (mínimos de proyecto; Bluecell, Billber, Unlock Management, Nokeon, Digitus, Góbalo, Coco Solution…) | EUR, capt. 23-10-2026 | — | — | Casi todas son agencias de marketing digital | 1-10 a 51-200 | [ABIERTA] |

Freelance/marketplaces España (demanda de setters, no agencias): Workana "setter para realizar llamadas en frío solo a comisión" y "pago por cada reunión agendada, cantidad a pactar… más comisión si cierra"; otra oferta "fijo 250 USD/mes + comisión por cierre" [FRAGMENTO]; Upwork "Spanish B2B Appointment Setter – Education Sector", precio fijo 75 USD por prueba de 30 llamadas [FRAGMENTO]; Fiverr gig "Spanish B2B cold calling… monthly retainer" (403 al abrir) [FRAGMENTO].

## 2. Agencias internacionales de referencia

| Agencia (país) | URL | Modelo | Precio publicado (moneda, fecha) | Permanencia | Garantía | Nicho industrial | Estado |
|---|---|---|---|---|---|---|---|
| **Belkins** (EE. UU./UA) | https://belkins.io/pricing · /blog/best-appointment-setting-companies | Retainer ("monthly retainer packages") | Pricing page sin cifras; su propio blog: "Starts at **$8,000/month** for 100 guaranteed appointments/year and 3 outreach channels"; Smartlead: "from $5,000/month"; Salesforge recoge Clutch "~$5,500/mo for 10+ meetings, min project $1,000+" y Reddit "$3,000 + $150 per booked meeting" (2024-2026) | "custom quotes for 4, 6, and 12 months" | "100 guaranteed appointments/year" (contadas como booked, no held) | Manufacturing entre sus clusters fuertes (Salesforge) | [ABIERTA] |
| **Martal Group** (Canadá) | https://martal.ca/pricing/ | Flat fee mensual; opción **flat fee + comisión de ventas**; **"3 Month Pilot Campaign" / "4 Month Pilot Campaign"**, luego suscripción mensual | "Inquire about pricing"; Belkins cita "$2,500–$10,500 per month" (2024) | 3-4 meses de piloto | No | No (tech) | [ABIERTA] |
| **CIENCE** (EE. UU.) | https://www.cience.com/pricing | Fee de equipo + plataforma + por SDR + bono | "Campaign team **$2,000/mo**", "graph8 platform **$499/mo**", "Offshore from **$1,750 per SDR/mo**", "US/Europe from **$3,500 per SDR/mo**", ejemplo 5 SDR offshore = **$11,249/mo** + bono; "Month to month, no long contract" (USD, capt. 23-10-2026) | Mes a mes | Bono por objetivo de reuniones | No | [ABIERTA] |
| **SalesRoads** (EE. UU.) | https://salesroads.com/pricing/ | Retainer por periodo de 4 semanas, escalado por nº de SDR | 1 SDR **$11,950 / 4 semanas**; 2 SDR $16,750; 3 SDR $23,500; 6 SDR $43,150 (USD, capt. 23-10-2026); "Does SalesRoads offer long-term contracts? No" | 4 semanas renovables | No | Clientes industriales (Shell, Parker) según Belkins | [ABIERTA] |
| **Cleverly** (EE. UU.) | https://www.cleverly.co/ · /blog/b2b-lead-generation-agency-cost | Suscripción mensual LinkedIn/cold email | "B2B Lead Gen Starting at **$397/Month**" (blog, 16-3-2026); su guía: agencias $2.000-15.000/mes; por reunión SMB $150-500, mid-market $300-900, enterprise $800-2.500+ | — | — | No (SaaS, coaches, finanzas) | [ABIERTA] (pricing page 404) |
| **Sopro** (RU) | https://sopro.io/pricing/ | Retainer | "pricing starts at around **$3.8K per month**", "no minimum contract" (capt. 23-10-2026) | Sin mínimo | No | No | [ABIERTA] |
| **Operatix** (RU/EE. UU., ahora memoryBlue) | https://www.operatix.net/ | SDR outsourcing | No publica | — | — | Software B2B | [ABIERTA] |
| **Leadium** (EE. UU.) | https://www.leadium.com/pricing | Retainer mes a mes | Formulario con tramos "$2,500-3,500 / 3,500-5,000 / 5,000-7,000 / 7,000-10,000 / Above $10,000"; "all of our contracts are month-to-month"; "**we do not provide performance guarantees** for the outcomes of our outbound sales efforts" (capt. 23-10-2026) | Mes a mes | Explícitamente **no** | No | [ABIERTA] |
| **Pearl Lemon Leads** (RU) | https://pearllemonleads.com/ | Retainer por servicio | "Appointment Setting **£4,497 Per Month**", "Cold Email **£2,497+**", "Cold Calling **£2,997+**", "End to End Sales **£6,697+**", "LinkedIn Lead Gen £…497+", "Multi-Channel £3,497+" (GBP, capt. 23-10-2026); también "pay-per-lead services" | — | — | No | [ABIERTA] |
| **The Sales Factory** (Canadá) | https://www.thesalesfactory.com/ | Outsourced sales | No publica ("+2000 Meetings Booked") | — | — | No | [ABIERTA] |
| **Durhamlane** (RU) | https://www.durhamlane.com/ | Retainer | "campaigns can start from a few thousand per month… our average new customer typically invests between **£10-20k per month**"; onboarding 30 días (GBP, capt. 23-10-2026) | — | — | **Sí**: caso "RS Industria: £700k Estimated Pipeline for an Industrial IoT Start-up" | [ABIERTA] |

## 3. Comparativas y directorios con cifras

| Fuente (fecha) | URL | Cifras literales | Estado |
|---|---|---|---|
| Belkins, "B2B appointment setting costs and pricing models" (act. ene-2024) | https://belkins.io/blog/appointment-setting-costs-pricing-models.md | Retainer básico "around $2,000 per month"; completo "$5,000 to $10,000 per month"; proyecto "$1,500 to $3,000" a "$5,000 to $15,000 or more"; hora "around $25"; por lead "$20 to $200"; por lead cualificado "from around $50" | [ABIERTA] |
| Intelemark, guía 2025 | https://www.intelemark.com/blog/b2b-appointment-setting-pricing-guide-models-costs-and-roi-standards-for-2025/ | "Pay-per-appointment runs often cost $50 to $300 per meeting scheduled"; "Retainer models usually hover between $3,000 and $10,000 per month"; "SaaS vendor paying $150 to $400 per booked demo" | [ABIERTA] |
| SalesAR (dic-2025) | https://salesar.io/blog/b2b-appointment-setting-costs-in-2025-pricing-models-explained | "According to Clutch, the average cost per qualified B2B appointment in 2025 is between $550 and $1,700"; pay-per-appointment "$50 to $500"; cliente SaaS "$400 per qualified meeting"; **"manufacturing supplier reaching out to logistics companies across the EU… cost per meeting? Roughly $80–$150"**; "below $100 per meeting, you're usually buying quantity" | [ABIERTA] |
| Instantly (act. nov-2025) | https://instantly.ai/blog/outsourced-appointment-setting-service-guide/ | "pay-per-meeting ($15-100 per appointment), monthly retainer ($3,000-$5,000+ per month)"; setup "$500-$3,000" | [ABIERTA] |
| Smartlead (2026) | https://www.smartlead.ai/blog/appointment-setting-companies | "Monthly retainers… $5,000–$15,000+, with per-meeting pricing running $150–$900+"; SalesRoads "3-month minimum is reported"; CIENCE "one-time GTM setup fee… $5,000" | [ABIERTA] |
| SalesBread (sep-2025 / 2026) | https://salesbread.com/appointment-setting-services-cost/ | "Hourly $16.12/h (US)"; "Subscription $2,000–$4,500/mo"; "Per appointment $100–$500+"; "Pay per qualified lead $50–$250"; "Retainer $2,000–$5,000" | [ABIERTA] |
| Cleverly (16-3-2026) | https://www.cleverly.co/blog/b2b-lead-generation-agency-cost | "$2,000 to $15,000+ per month"; cold email "$2,000–$8,000"; LinkedIn "$3,000–$10,000"; por reunión SMB "$150–$500", mid-market "$300–$900", enterprise "$800–$2,500+" | [ABIERTA] |
| SaaSHero, "Reddit B2B leadgen agency pricing" (ago-2026) | https://www.saashero.net/competitor/reddit-b2b-leadgen-agency-pricing/ | "Monthly Retainer $2,000–$15,000+/month, most… $3,000–$1x,000"; "Hybrid $2,000–$4,000/month base plus performance bonuses"; "Pay-per-meeting rates in 2026 run $300–$1,500"; "Three to six month minimums are common, and some agencies demand 12 months" | [ABIERTA] |
| GigRadar (2026) | https://gigradar.io/blog/b2b-appointment-setting | "$400-$1,500 per BANT-verified meeting"; legal/M&A "$500-$1,500" | [FRAGMENTO] |
| Salesforge, Belkins review (2026) | https://www.salesforge.ai/blog/belkins-review-2026-b2b-lead-generation-appointment-setting-agency | Tabla de 6 fuentes: Clutch "~$5,500/mo for 10+ meetings, min $1,000+"; 100Signals "$3,000–5,000 base + ~$150/meeting, or $5,000–15,000 all-inclusive"; "Setup fees… $2,000 to $5,000 on top"; "Not the right fit if… your budget sits under $3K per month" | [ABIERTA] |
| Salesforge, cold email agencies Spain (2026) | https://www.salesforge.ai/blog/cold-email-agencies-spain | **"Most cold email agencies in Spain charge between 1,000 and 4,500 euros per month… Some work on flat retainers, others on a pay-per-meeting model"** | [ABIERTA] |
| SyncGTM, sales/GTM agencies Spain (may-2026) | https://syncgtm.com/blog/best-sales-agencies-in-spain · /best-gtm-agencies-in-spain | "Spanish GTM agencies charge €5,000–€15,000/month"; "Instead of paying €4,000+/month for someone else to run outbound"; SalesCaptain "€1,500–€4,000/month" / "approximately €3,500/month"; Gotoclient "€3,000–€8,000/month"; ColdIQ "$3,000–$8,000/month" | [ABIERTA] |
| Lessie (ES) | https://lessie.ai/es/blog/sdr-agency | "Las agencias suelen costar entre $5,000 y $15,000 al mes por equipo (pod)"; "Pago por reunión cualificada. Normalmente entre $300 y $800"; "el modelo más común a partir de $8,000 al mes" | [ABIERTA] |
| Techsy (ES) | https://techsy.io/es/blog/agencia-ai-sdr | "Las agencias AI SDR cobran $2–5K/mes tarifa plana"; "Costo por reunión agendada ~$140 (agencia) vs ~$400 (SDR humano)" | [ABIERTA] |
| Skipcall (ES, 2026) | https://skipcall.io/es/blog/contratar-un-sdr · /salario-sdr-espana · /escalar-agencia-prospeccion-sin-contratar | "Un puesto de SDR cuesta de 45 a 65.000 € con cargas en España"; "La mediana del mercado se sitúa en torno a 200-300 € por reunión; el cuartil superior baja a 80-150 €"; "En marcación manual, una reunión cuesta de 400 a 1.200 €"; "Por debajo de 20.000 € de ticket medio, la ecuación rara vez funciona"; SDR junior OTE 28-40K€, confirmado 38-52K€, senior 45-65K€; "Reuniones cualificadas… El más utilizado en España" como KPI | [ABIERTA] |
| Puromarketing (ES, sin fecha) | https://www.puromarketing.com/44/25860/pros-contras-modelos-precios-generacion-leads | "El rango de precios por lead oscila entre los 20€ a 180€"; "precios de mercado por cuenta prospectada oscilan entre los 4€ a 9€"; "coste hora que puede oscilar entre los 12€ a 18€" | [ABIERTA] |
| Upwork (ofertas 2025-2026) | varias /freelance-jobs/ | Tarifas por hora fijadas por clientes: "$30-45", "$20-30", "$10-15", "$6-10"; benchmark Upwork "Beginner $8/h, Intermediate $14/h, Advanced $45/h" | [FRAGMENTO] (upwork.com/hire 403) |
| Clutch (categoría Lead Generation Spain) | https://clutch.co/es/agencies/lead-generation | Cloudflare "Just a moment" en HTTP, Chromium y curl | NO ENCONTRADO |
| GoodFirms (Spain) | /lead-generation-companies/spain | 404 | NO ENCONTRADO |
| G2 Belkins reviews / Trustpilot (Sopro, Belkins, RevNew) | g2.com, trustpilot.com | 403 (Trustpilot Belkins deja ver cabecera: "Reviews 13 • 4.4") | NO ENCONTRADO / [FRAGMENTO] |

## 4. Tabla final: modelo de precio × agencias (España) y rangos

| Modelo | Agencias españolas que lo usan (de las abiertas) | Nº | Rango publicado/citado España | Rango internacional (2025-26) |
|---|---|---|---|---|
| **Retainer / tarifa plana mensual** | CustomerTop (tarifa plana, sin permanencia), DevCommX ($6.000/mes), SalesCaptain, Gotoclient, Sales Force Europe, Callbox ES, Línea Gráfica, Novicell, Connext, Inbound Emotion, mbudo, Marketinet, Inprofit, WAM (las 8 últimas son inbound/marketing con retainer, no outbound) | 14 (6 outbound) | Ninguna agencia outbound española publica cifra salvo DevCommX (6.000 USD). Estimaciones de terceros: 1.000-4.500 €/mes (Salesforge), 1.500-4.000 €/mes SalesCaptain y 3.000-8.000 €/mes Gotoclient (SyncGTM), 5.000-15.000 €/mes "agencias GTM" (SyncGTM); mínimos Sortlist 150-1.000 € | 2.000-15.000 USD/mes; mediana 3.000-10.000 USD; RU 2.500-4.500 £ (Pearl Lemon), 3.800 USD (Sopro), 10-20k £ (Durhamlane) |
| **Pago por reunión** | Ninguna agencia española lo publica. Freelancers en Workana ("pago por cada reunión agendada, a pactar") | 0 agencias | Sin cifra publicada; benchmark interno Skipcall 200-300 €/reunión (mediana), 80-150 € (cuartil superior) | 50-500 USD pyme; 150-900 USD mid-market; 300-1.500 USD (SaaSHero/GigRadar); 800-2.500 USD enterprise; Clutch vía SalesAR 550-1.700 USD |
| **Pago por lead / por cuenta prospectada** | HighConverting (Madrid, pay-per-lead); Pearl Lemon (RU) también | 1 | 20-180 €/lead; 4-9 €/cuenta prospectada; 12-18 €/hora (Puromarketing) | 20-200 USD/lead; 50-800 USD/lead cualificado |
| **Piloto pagado corto con garantía** | Ninguna española. (CustomerTop: "sin permanencia" + repetición gratis de reuniones no válidas, que funciona de facto como entrada de bajo riesgo) | 0 | — | Martal 3-4 meses; SalesRoads bloques de 4 semanas desde 11.950 USD; Belkins 4/6/12 meses; Leadium/CIENCE/Sopro mes a mes sin garantía |
| **Híbrido base + variable por reunión** | Ninguna española publicada | 0 | — | 2.000-4.000 USD base + bono (SaaSHero); Belkins 3.000-5.000 + ~150 USD/reunión (Reddit vía Salesforge); CIENCE fee + bono por SDR |
| **Comisión sobre venta cerrada** | Ninguna agencia; solo setters freelance "solo a comisión" (Workana) | 0 | — | Martal "flat fee + sales commission" (única); el sector lo rechaza (r/sales) |

## 5. Demanda

- **Empleo (proxy de que las empresas internalizan la función):**
  - LinkedIn Jobs: "**5000+ empleos de Sales Development Representative en España**" (es.linkedin.com, capt. 23-10-2026; cifra inflada por LinkedIn, pero indica categoría activa) [ABIERTA].
  - Tecnoempleo: "**3 Ofertas Trabajo de sdr**" (capt. 23-10-2026) [ABIERTA]: en portales tech españoles la palabra "SDR" casi no existe.
  - InfoJobs: la web bloquea (405/página genérica); vía snippets de buscador: "**104 ofertas de concertacion**", "5 ofertas de teleconcertacion", "654 ofertas de visitas empresas"; oferta "Concertador/a de Visitas B2B… **18.000 € brutos anuales más incentivos**" (Barro, Pontevedra); "Concertador/a de visitas comerciales" (Burjassot, vía Adecco) [FRAGMENTO].
  - Salarios SDR España: join.com "salario mediano 26.000 € brutos; P25 22.000 €, P75 32.000 €; variable OTE 9.400-14.000 €" [ABIERTA]; oferta Page Personnel Madrid "22.000-28.000 € bruto/año" (21-3-2026) [ABIERTA]; Skipcall "coste empresa 45-65K€", "coste oculto de contratar 20-38K€" [ABIERTA]. → Un fabricante de 20-200 empleados compara la agencia contra ~45-65 k€/año de un SDR interno que, según Skipcall, "necesita generar un mínimo de 50 reuniones/año solo para cubrir su coste".
- **Búsquedas:** Google Trends devolvió HTTP 429 en tres intentos (trends.google.es y .com, Chromium) → NO ENCONTRADO. Keyword Planner no accesible.
- **Directorios:** Sortlist "Lead Generation Spain: **138 companies**" [ABIERTA]; Clutch España bloqueado → NO ENCONTRADO.
- **Prensa económica:** Emprendedores (8-7-2025) "Top 10 mejores agencias de marketing industrial de España 2025" (ranking de la Escuela Europea de Empresa: Marketers Group, Dobuss, BCM Marketing; canales "LinkedIn Ads, Google Ads y email automatizado") [ABIERTA]; Merca2 (28-7-2025) mismo ranking [ABIERTA]; Forbes España (2-8-2023, contenido remitido) "Appointment setting… nueva profesión sin paro… salarios entre dos mil y siete mil euros netos mensuales" [ABIERTA]; Emprendedores "Outsourcing comercial en España: las empresas B2B recurren a equipos comerciales externos" (snippet: "ha pasado de ser una solución táctica a convertirse en una herramienta de diseño organizativo"; la URL devuelve 404) [FRAGMENTO]; Alimarket (snippet): "la parte relativa a fuerza de ventas es la más reacia a ser externalizada" [FRAGMENTO]; Salesdorado (ES) "Fuerza de ventas externalizada": riesgos "Gastos imprevistos y costes ocultos, Seguridad de los datos, Retrasos constantes… Falta de conocimientos en el ámbito del cliente" [ABIERTA]. No apareció ningún artículo de Expansión/Cinco Días/El Economista sobre externalización comercial industrial → NO ENCONTRADO.
- **Eventos/comunidad:** Luma: "Inside the #1 B2B Outbound Agency in Spain+LATAM: Gabriel Martínez (Reachflow)", 242 asistentes (Smartlead) [ABIERTA]; WaLead (Barcelona) "Cómo usar LinkedIn Automation + IA para crear una máquina de generación de reuniones", 31 asistentes, entrada 12,10 € [ABIERTA].
- **Marco legal citado por los vendedores (relevante para la oferta):** SyncGTM: "AEPD issued €51 million in GDPR fines in 2023"; Overloop: cold email B2B legal bajo RGPD + art. 21 LSSI con baja en cada correo; Skipcall cita la Orden TDF/149/2025 para llamadas [FRAGMENTO].

## 6. Casos, testimonios y frases literales de compradores

**Casos con cifras (industria):**
- CustomerTop / Grenke Renting (España): "casi hemos duplicado la activación de clientes… Logramos más de **30 reuniones semanales**"; "El número de distribuidores activados cada semana aumentó de 4 a 7" [ABIERTA].
- Durhamlane / RS Industria (IoT industrial, RU): "**£700k Estimated Pipeline**… multichannel sales strategy in the Industrial IoT sector" [ABIERTA].
- SalesAR: "a manufacturing supplier reaching out to logistics companies across the EU… cost per meeting? Roughly **$80–$150**" vs. SaaS a CFOs "$400 per qualified meeting" [ABIERTA].
- devlo.ch (Suiza, "B2B prospecting agency Madrid"): "120 qualified appointments · 7,000 decision-makers targeted · Virtually no show" (Monizze); "80+ meetings · €200K revenue" (Horus) [ABIERTA].
- SalesCaptain: "One client generated $1.5M in new revenue with 120+ booked meetings over 12 months" [FRAGMENTO SyncGTM].

**Frases literales — inglés (r/sales vía archivo arctic-shift; reddit.com bloqueado):**
- "**Done for you lead gen agencies are trash and rarely ever deliver quality leads.** Implement a lead gen engine that you own… Startup costs are usually cheaper than hiring glorified email pushers" (hilo "B2B Lead Gen Agencies?", 2025).
- "The biggest difference we saw was when the agency handled lead generation appointment setting **instead of just giving us leads**… The key is finding one that builds a pipeline instead of just delivering contacts."
- "So many lame lead gen agencies out there that **promise the moon and stars but are totally mediocre**… Unless your lead gen is hyper focused on one specific industry with a specific segment of the market, telling me you book meetings with CEOs and business owners says a whole lot of nothing" (43 votos, hilo "client tells me I pay only commission based", 2025).
- "**99.999% of these LinkedIN lead generators are pure scammers.** They bring in garbage leads who have no idea what they are even on a call for… If you are providing me with genuine, hot, or even warm leads… why would you NOT accept [commission]?"
- "They insist on paying us only once deal is closed. We dont do that. I suggest a base fee but they decline." (la agencia, 29 votos).
- "what if you offer a guarantee so they can get the expected return of investment… you need to cover your risk too".
- "many split their reps across multiple clients, meaning they're not fully focused on your business" / "why can't I have the Agency give me the SDR's full-time attention, and have them follow my scripts exactly?"
- "I have a LOT of time every day to prospect, **I just HATE it. It drains energy from me**" (fundador que valora agencia vs. contratar).
- Red flags (Fuzzy AI, 22-3-2026): "They promise guaranteed lead volumes without knowing your ICP", "They won't show you the actual messaging they'll send", "Long lock-in contracts with no performance clauses", "Then three months pass. You've spent £15k+. Your pipeline looks the same. Your LinkedIn account got restricted."
- SaaSHero (resumen de Reddit, 2026): "General agencies rely on recycled lists and basic scraping", "Percentage-of-spend pricing is a trap", "reporting that celebrates form fills while revenue stalls".
- Clutch sobre Belkins (vía buscador): "A few clients experienced challenges with Belkins not meeting the promised number of meetings or leads" [FRAGMENTO]. Trustpilot RevNew (1/5): "poor lead quality, repeated no-shows, and a difficult refund" [FRAGMENTO].

**Frases literales — español:**
- CustomerTop (posicionamiento contra el dolor): "**No somos telemarketing**", "¡Al cliente potencial no les sonamos como un robot!", "Tu equipo comercial no debería perder tiempo con empresas sin necesidad, sin presupuesto o sin capacidad de decisión", "No somos una firma de marketing digital que genera leads fríos", "Personas que hablan con personas. Algunos basan su discurso en la automatización y la IA…".
- Grenke (cliente): "Destacada la flexibilidad, la capacidad de reacción y la capacidad de entender nuestras necesidades".
- Salesdorado: "la externalización tradicionalmente se reserva para actividades 'no críticas', y es muy complicado vender sin diferenciación"; "sólo puede funcionar si ya dispone de un proceso comercial establecido".
- Skipcall: "Por debajo de 20.000 € de ticket medio, el coste por reunión calificada se come el margen"; "El salario no es la primera razón de fuga [de SDR]… herramientas inadecuadas, objetivos irrealistas y falta de perspectivas".
- Lessie: "Comprar volumen de agencia antes de validar el mensaje es cómo las empresas gastan $60,000 para descubrir que su posicionamiento era incorrecto".
- Workana (compradores pyme): "setter para realizar llamadas en frío **solo a comisión**"; "pago por cada reunión agendada, cantidad a pactar al inicio, más una comisión extra si la venta se cierra".
- Alimarket (directivo): "la parte relativa a fuerza de ventas es la más reacia a ser externalizada por las empresas".

## 7. Formadores y creadores de outbound B2B en español

| Nombre | URL | Qué enseña | Hueco que deja | Estado |
|---|---|---|---|---|
| **Gabriel Martínez (Reachflow)** | https://lu.ma/ztx91i2b · https://reachflow.io/ | Cold email para España+LATAM, "the leading voice in Spanish-language outbound" (Smartlead) | SaaS/servicios; nada de industria ni de ciclos de venta de maquinaria | [ABIERTA]/[FRAGMENTO] |
| **Samuel Santiago** (Sniper Call Center) | https://www.ivoox.com/en/secretos-venta-telefonica-samuel-santiago-audios-mp3_rf_113263956_1.html · Favikon #16 | Venta telefónica, appointment setting, high-ticket; "autor de cuatro bestsellers" | Orientado a high-ticket/infoproducto; no B2B industrial ni email/LinkedIn | [FRAGMENTO] (sin web oficial localizada) |
| **Alfonso Bastida** (+ Christian Helmut, Escuela A&C, Benidorm) | https://www.que.es/2021/10/26/escuela-de-preparacion-ac-para-convertirse-en-closer-de-ventas-de-la-mano-de-los-expertos-alfonso-y-christian/ | Formación de "closers de ventas" (notas de pago 2021) | Cierre high-ticket, no prospección industrial | [FRAGMENTO] |
| **Rafa Gandía** | — | — | — | NO ENCONTRADO (dos búsquedas sin resultado) |
| **Carlos Sogorb / "Ventas B2B podcast"** | — | — | — | NO ENCONTRADO (dos búsquedas) |
| **Favikon "Top 20 influencers de ventas en España 2026"** | https://www.favikon.com/es/blog/top-sales-influencers-spain | #1 Félix Fernández Sánchez (cold calling y outbound), #5 Sergi Ramo (ventas híbridas + IA), #7 Toni Gómez ("sistemas de prospección impulsados por IA y automatización en LinkedIn"), #11 **Luis Hernando Berasaluce** ("Director Comercial e Interim Manager con más de 20 años en sectores industriales B2B"), #15 Regina Lara (Matcheando, "Warmbound"), #19 Gisela Moreno (fractional sales manager pymes) | Solo Berasaluce toca industria y es interim manager, no outbound; nadie une "IA + cold email + LinkedIn + fabricantes" | [ABIERTA] |
| **WaLead** (Barcelona; Walid Amarir, Jacob Domínguez) | https://luma.com/zshkfshy | LinkedIn Automation + IA, eventos presenciales con Marketers Group, LaMalcriada, LinkedScope | Freelances/agencias/pymes genéricas | [ABIERTA] |
| **La Growth Machine (blog ES)** | https://lagrowthmachine.com/es/prospeccion-b2b-2/ | Prospección multicanal, herramienta | Genérico | [ABIERTA] |
| **Overloop (blog ES)** | https://overloop.com/blog/es/b2b-cold-email-espana-rgpd-aepd | Cold email legal en España (RGPD/LSSI) | Legal, no sectorial | [FRAGMENTO] |
| **Skipcall (blog ES)** | https://skipcall.io/es/blog/salario-sdr-espana | Economía del SDR en España | Vende dialer; enfoque SaaS | [ABIERTA] |
| **Lessie / Techsy (blogs ES)** | https://lessie.ai/es/blog/sdr-agency · https://techsy.io/es/blog/agencia-ai-sdr | Agencia vs SDR vs IA | SaaS | [ABIERTA] |
| **El ABC de las Ventas B2B** (podcast, Smart Tap Group, Orlando Salamanca) | https://rephonic.com/podcasts/el-abc-de-las-ventas-b2b | Proceso de venta B2B (7 episodios, 2020-2022, LATAM) | Inactivo | [ABIERTA] |
| lemlist / Instantly / Sopro en español | — | Instantly y Smartlead publican en inglés; Sopro sin contenido ES localizado | — | NO ENCONTRADO |

**Hueco de contenido:** nadie en español habla de outbound para fabricantes (lenguaje de ingeniería de aplicación, ciclos de 90-240 días, decisor = director técnico/compras, ferias como Subcontratación Bilbao/BIEMH). El único actor que lo nombra (CustomerTop, "Sector Maquinaria") lo hace por teléfono y con discurso anti-IA ("Personas que hablan con personas").

## 8. Cinco competidores más relevantes para un fabricante industrial español

1. **CustomerTop** — https://customertop.com/sector-maquinaria/ — el incumbente: 21 años, páginas por sector industrial, tarifa plana sin permanencia, garantía de repetición gratis; discurso anti-automatización.
2. **DevCommX** — https://www.devcommx.com/b2b-lead-generation/bilbao/manufacturing — única con precio publicado (desde 6.000 USD/mes) y páginas "Manufacturing" por ciudad española; competidor en SEO más que en operación.
3. **Novicell** (y Connext / Inbound Emotion como sustitutos inbound) — https://www.novicell.es/ — la alternativa que el fabricante ya conoce: "60% de nuestros proyectos son de empresas industriales B2B", pero inbound, no outbound.
4. **Gotoclient** — https://www.gotoclient.com/ — Barcelona, ABM + LinkedIn + "Sales Outreach", declara vertical industrial; precio estimado 3.000-8.000 €/mes.
5. **Belkins / Martal** (entrada internacional) — https://belkins.io/pricing · https://martal.ca/pricing/ — fijan el ancla de precio (5.000-8.000 USD/mes; piloto 3-4 meses) que el comprador ve al googlear en inglés; Martal es la única con "flat fee + comisión".

Competidor indirecto más peligroso: el **SDR interno + IA** (Fuzzy, Lessie, Techsy, SyncGTM venden "sin retainer de agencia" como argumento central) y el **telemarketing clásico** (LCA, Callbox).

---

## 9. Tabla de URLs y estado

| URL | Estado |
|---|---|
| https://belkins.io/pricing | [ABIERTA] 200 |
| https://belkins.io/blog/appointment-setting-costs-pricing-models.md | [ABIERTA] 200 |
| https://belkins.io/blog/best-appointment-setting-companies | [ABIERTA] 200 |
| https://martal.ca/pricing/ | [ABIERTA] 200 |
| https://www.cience.com/pricing | [ABIERTA] 200 |
| https://salesroads.com/pricing/ | [ABIERTA] 200 |
| https://www.cleverly.co/ | [ABIERTA] 200 (/pricing 404) |
| https://www.cleverly.co/blog/b2b-lead-generation-agency-cost | [ABIERTA] 200 |
| https://sopro.io/pricing/ | [ABIERTA] 200 |
| https://www.operatix.net/ | [ABIERTA] 200 |
| https://www.leadium.com/pricing | [ABIERTA] 200 |
| https://pearllemonleads.com/ | [ABIERTA] 200 (/pricing 404) |
| https://www.thesalesfactory.com/ | [ABIERTA] 200 |
| https://www.durhamlane.com/ | [ABIERTA] 200 |
| https://www.intelemark.com/blog/b2b-appointment-setting-pricing-guide-models-costs-and-roi-standards-for-2025/ | [ABIERTA] 200 |
| https://salesar.io/blog/b2b-appointment-setting-costs-in-2025-pricing-models-explained | [ABIERTA] 200 |
| https://instantly.ai/blog/outsourced-appointment-setting-service-guide/ | [ABIERTA] 200 |
| https://www.smartlead.ai/blog/appointment-setting-companies | [ABIERTA] 200 |
| https://salesbread.com/appointment-setting-services-cost/ | [ABIERTA] 200 |
| https://gigradar.io/blog/b2b-appointment-setting | [ABIERTA] 200 (fragmento útil) |
| https://www.saashero.net/competitor/reddit-b2b-leadgen-agency-pricing/ | [ABIERTA] 200 |
| https://www.saashero.net/uncategorized/lead-generation-agency-reviews-reddit/ | [ABIERTA] 200 |
| https://getfuzzy.ai/blog/red-flags-hiring-b2b-lead-generation-agency | [ABIERTA] 200 |
| https://www.salesforge.ai/blog/belkins-review-2026-b2b-lead-generation-appointment-setting-agency | [ABIERTA] 200 |
| https://www.salesforge.ai/blog/best-outbound-sales-agencies-in-spain | [ABIERTA] 200 |
| https://www.salesforge.ai/blog/lead-generation-agencies-spain | [ABIERTA] 200 |
| https://www.salesforge.ai/blog/cold-email-agencies-spain | [ABIERTA] 200 |
| https://www.salesforge.ai/directory/agencies/highconverting | [ABIERTA] 200 |
| https://www.salesforge.ai/blog/salesgent-review | [ABIERTA] 200 |
| https://syncgtm.com/blog/best-sales-agencies-in-spain | [ABIERTA] 200 |
| https://syncgtm.com/blog/best-gtm-agencies-in-spain | [ABIERTA] 200 |
| https://syncgtm.com/directory/agency/customertop | [ABIERTA] 200 |
| https://customertop.com/ · /sector-maquinaria/ · /concertacion-de-visitas-comerciales/ · /garantias-de-calidad/ · /casos-de-exito/ | [ABIERTA] 200 (5 páginas) |
| https://www.devcommx.com/appointment-setting/madrid · /b2b-lead-generation/bilbao/manufacturing | [ABIERTA] 200 |
| https://www.salescaptain.io/ | [ABIERTA] 200 |
| https://www.gotoclient.com/ | [ABIERTA] 200 |
| https://salesforceeurope.com/ | [ABIERTA] 200 |
| https://www.lcacontactcenter.com/ | [ABIERTA] 200 |
| https://www.callboxinc.com/lead-generation-spain/ | [ABIERTA] 200 |
| https://www.novicell.es/ · https://www.connext.es/ · https://www.inboundemotion.com/ · https://www.lineagrafica.es/ · https://www.mbudo.com/ · https://www.marketinet.com/ · https://www.inprofit.es/ · https://www.wearemarketing.com/ | [ABIERTA] 200 (8 páginas) |
| https://devlo.ch/en/b2b-prospecting-agency-madrid | [ABIERTA] 200 |
| https://www.sortlist.com/s/lead-generation/spain-es | [ABIERTA] 200 (Chromium) |
| https://www.sortlist.es/lead-generation · https://sortlist.co.uk/agency/sales-force-europe | NO ENCONTRADO 403 |
| https://clutch.co/es/agencies/lead-generation · /profile/avnza · /go-to-review/belkins/274343 | NO ENCONTRADO (Cloudflare) |
| https://www.goodfirms.co/lead-generation-companies/spain · /directory/country/top-lead-generation-companies/spain | NO ENCONTRADO 404 |
| https://www.goodfirms.co/company/clarmaj | [ABIERTA] 200 (poco texto) |
| https://www.designrush.com/agency/lead-generation/es | NO ENCONTRADO 403 |
| https://www.g2.com/products/belkins/reviews | NO ENCONTRADO 403 |
| https://www.trustpilot.com/review/belkins.io · /review/sopro.io · https://ca.trustpilot.com/review/revnew.com | NO ENCONTRADO 403 (Belkins: cabecera "13 reviews • 4.4") |
| https://trends.google.es/trends/explore?geo=ES&q=… (3 variantes, Chromium) | NO ENCONTRADO 429 |
| https://es.linkedin.com/jobs/sales-development-representative-empleos | [ABIERTA] 200 ("5000+ empleos") |
| https://www.tecnoempleo.com/busqueda-empleo.php?te=sdr | [ABIERTA] 200 ("3 Ofertas") |
| https://www.infojobs.net/ofertas-trabajo/sdr (y 5 variantes) | NO ENCONTRADO 405/página genérica; conteos vía snippets |
| https://es.indeed.com/jobs?q=sales+development+representative | NO ENCONTRADO 403 |
| https://join.com/es/guias-de-puesto/sales-development-representative | [ABIERTA] 200 |
| https://asaja.iberempleos.es/oferta-empleo/madrid/sales-development-representative-sdr-7667770 | [ABIERTA] 200 |
| https://skipcall.io/es/blog/salario-sdr-espana · /contratar-un-sdr · /escalar-agencia-prospeccion-sin-contratar | [ABIERTA] 200 |
| https://lessie.ai/es/blog/sdr-agency · https://techsy.io/es/blog/agencia-ai-sdr | [ABIERTA] 200 |
| https://www.puromarketing.com/44/25860/pros-contras-modelos-precios-generacion-leads | [ABIERTA] 200 |
| https://salesdorado.com/es/?p=51508 | [ABIERTA] 200 |
| https://emprendedores.es/notas-de-prensa/top-10-las-mejores-agencias-de-marketing-industrial-de-espana-en-2025/ | [ABIERTA] 200 |
| https://www.merca2.es/2025/07/28/mejores-agencias-marketing-industrial-en-espana-2217828/ | [ABIERTA] 200 |
| https://emprendedores.es/gestion/me-interesa-externalizar-todo-o-parte-de-mi-equipo-comercial/ · /uncategorized/outsourcing-comercial-en-espana-… | NO ENCONTRADO 404 (snippets) |
| https://forbes.es/ultima-hora/321092/appointment-setting-los-expertos-opinan-sobre-esta-nueva-profesion-sin-paro/ | [ABIERTA] 200 |
| Reddit r/sales hilos 1nkpw8t, 1j19daj, 1j8r16v (vía https://arctic-shift.photon-reddit.com/api/…) | [ABIERTA] (reddit.com y old.reddit.com devolvieron HTML de bloqueo; pullpush.io rate-limited) |
| https://lu.ma/ztx91i2b · https://luma.com/zshkfshy | [ABIERTA] 200 |
| https://www.favikon.com/es/blog/top-sales-influencers-spain | [ABIERTA] 200 (/blog/top-sales-experts-spain vacío) |
| https://www.ivoox.com/en/secretos-venta-telefonica-samuel-santiago-audios-mp3_rf_113263956_1.html | [ABIERTA] 200 |
| https://rephonic.com/podcasts/el-abc-de-las-ventas-b2b | [ABIERTA] 200 |
| https://lagrowthmachine.com/es/prospeccion-b2b-2/ | [ABIERTA] 200 |
| https://reachflow.io/ | 200 pero sin texto (JS); [FRAGMENTO] |
| smart-team.es · alysmarketing.com · omniegtm.com · exprimenet.com · avnza.com · leadmarket.es · phonetoolmarketing.com · snipercallcenter.com · outbounders.mumbler.io | NO ENCONTRADO (502 / certificado) |
| https://www.upwork.com/hire/appointment-setters/ · fiverr.com gig | NO ENCONTRADO 403 (cifras vía snippets) |

Páginas abiertas con contenido útil: ~60 (≥35 exigidas). Fuentes crudas en `/tmp/claude-0/-home-user-tbd/637262f0-646e-586f-83ef-8ef9d5653ca7/scratchpad/outb_a/pages/`.
