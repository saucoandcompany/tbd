# Outbound industrial 2026 — H3 (garantía 4 reuniones/300 contactos), H4 (dolor de la pyme industrial) y H5 (marca, LSSI y RGPD)

Fecha de la investigación: 23 de octubre de 2026. Método: páginas abiertas con `tools/pwfetch.js` o `curl` desde la sesión; PDFs descargados y convertidos con `pdftotext`. Etiquetas: **[ABIERTA]** = página leída íntegramente o en la sección citada; **[FRAGMENTO]** = sólo visto en resultados de búsqueda (la página devolvió 403/503/Cloudflare); **NO ENCONTRADO** = buscado y no localizado. Cifras siempre con muestra, fecha y definición cuando la fuente las da. Postura adversarial: se intenta destruir cada hipótesis.

---

## 0. Resumen ejecutivo

| Hipótesis | Veredicto | Motivo en una línea |
|---|---|---|
| **H3** — 300 contactos/mes → ≥4 reuniones celebradas de forma fiable | **REFUTADA como garantía** (alcanzable sólo en escenario optimista) | La "tasa de respuesta positiva 2,5-3,5 %" atribuida a Sopro no existe en sus datos: el *Lead %* de Sopro para Maquinaria/Automatización/Ingeniería es 1,9-2,2 % **por empresa contactada**, 0,9-1,3 % por contacto, y sólo ~1/3 de esos "leads" son respuestas positivas (resto: interés diferido y referidos). Los casos documentados de fabricantes dan 0,3-1,5 % de reuniones agendadas por contacto (multicanal, con llamadas). Esperanza base ≈ 2,4 reuniones celebradas por 300 contactos; P(≥4) ≈ 22 %. |
| **H4** — La pyme industrial 20-200 depende de ferias/distribuidores, no tiene SDR, ciclo largo, dispuesta a externalizar | **PARCIALMENTE SOPORTADA / NO VERIFICADA** | Hay datos duros de estructura (≈16.600 empresas industriales con ≥20 asalariados; 34,5 % de las empresas de 10+ usan CRM; ciclo 90-240 días o 12-18 meses según agencias) y señales cualitativas de dolor comercial, pero **ninguna encuesta abierta cuantifica** la dependencia de ferias/distribuidores, la ausencia de SDR ni la disposición a externalizar la prospección. |
| **H5** — Un tercero puede enviar correo frío en nombre del fabricante sin dañar la marca ni infringir LSSI/RGPD | **REFUTADA en su formulación literal (correo frío a direcciones nominativas)**; viable sólo rediseñando el canal | LSSI art. 21.1 prohíbe el correo comercial no solicitado y la AEPD lo aplica a buzones corporativos de directivos y trabajadores (E/02208/2018, A/00031/2019). El art. 19 LOPDGDD legitima *tratar* el dato de contacto profesional, no *enviar* la comunicación: la AEPD (informe 2018-0173) dice que el art. 21 LSSI es norma especial que desplaza al interés legítimo del RGPD. Riesgo sancionador bajo en cuantía (apercibimientos y multas de 200-30.000 €) pero real y reputacional; el remitente formal es el fabricante. |

---

## 1. Benchmarks por sector (bloque 1)

### 1.1 Sopro — resultados en vivo (datos propios de la agencia, 792 campañas activas, actualizado 23/10/2026) [ABIERTA]
Fuente: https://sopro.io/results/interactive-insights/performance-by-industry y https://sopro.io/results/the-state-of-prospecting/ (misma tabla; "Live results").

**Definiciones deducidas de la propia tabla**: *Lead %* = Leads generados / **Empresas** contactadas (no por persona). Comprobación: total 90.600 leads / 4.505.098 empresas = 2,01 % (coincide con el 2,01 % publicado); 90.600 / 9.330.012 prospectos = 0,97 %. En la tabla mensual, *Leads* ≈ *Positive Response* + *Deferred Interest* + *Referral* (sept. 2026: 1.248 + 1.373 + 1.145 = 3.766 ≈ 3.780 leads). Es decir, **la respuesta estrictamente positiva es ~1/3 del "lead" de Sopro**.

| Sector objetivo (Sopro) | Campañas | Empresas | Prospectos | Leads | Lead % publicado (por empresa) | Lead % por prospecto (cálculo propio) |
|---|---|---|---|---|---|---|
| Machinery | 465 | 43.924 | 74.592 | 933 | 2,12 % | **1,25 %** |
| Industrial Automation | 464 | 20.982 | 44.836 | 400 | 1,91 % | **0,89 %** |
| Mechanical or Industrial Engineering | 521 | 84.249 | 145.229 | 1.838 | 2,18 % | **1,27 %** |
| Electrical/Electronic Manufacturing | 519 | 68.009 | 118.749 | 1.237 | 1,82 % | **1,04 %** |
| Construction | 574 | 290.175 | 559.726 | 8.806 | 3,03 % | 1,57 % |
| Civil Engineering | 461 | 36.480 | 86.629 | 1.342 | 3,68 % | 1,55 % |
| Chemicals | 499 | 43.749 | 112.385 | 1.515 | 3,46 % | 1,35 % |
| Oil & Energy | 490 | 48.494 | 129.443 | 1.831 | 3,78 % | 1,41 % |
| Utilities | 515 | 50.247 | 164.923 | 1.917 | 3,82 % | 1,16 % |
| Mining & Metals | 414 | 20.294 | 46.187 | 1.155 | 5,69 % | 2,50 % |
| **Total Sopro** | 792 | 4.505.098 | 9.330.012 | 90.600 | 2,01 % | 0,97 % |
| Objetivo 51-200 empleados | 729 | 1.249.159 | 1.948.374 | 20.455 | 1,64 % | 1,05 % |
| Objetivo 11-50 empleados | 635 | 1.116.354 | 1.424.981 | 15.006 | 1,34 % | 1,05 % |

Tabla mensual (oct 2025 – sep 2026), **respuestas positivas estrictas / prospectos contactados en el mes**: sep 1.248/410.869 = 0,30 %; ago 0,28 %; jul 0,27 %; jun 0,26 %; may 0,22 %; abr 0,30 %; mar 0,32 %; feb 0,33 %; ene 0,35 %; dic 0,29 %; nov 0,30 %; oct 0,28 %. Emails por prospecto y mes: 1,75-1,93. Coste por lead publicado: 396-586 $ (sept. 2026: 434,78 $).

**Consecuencia para H3**: el "2,5-3,5 % de respuesta positiva en ingeniería/construcción/industria según Sopro" de la hipótesis **no se sostiene**. Las cifras de 3-3,8 % son *Lead %* por empresa en Construcción/Civil/Energía (que incluyen interés diferido y referidos); en el ICP núcleo (maquinaria, automatización, ingeniería mecánica, electrónica) el Lead % es 1,8-2,2 % por empresa y 0,9-1,3 % por contacto, y la respuesta positiva estricta ~0,3-0,45 % por contacto.

### 1.2 Belkins — 7,5 M de correos fríos en 2025 (datos propios de la agencia) [ABIERTA]
- https://belkins.io/blog/cold-email-response-rates : tasa de respuesta media **0,45 %** (respuestas totales, incluidas negativas, / correos enviados; 7.530.489 correos; metodología cambiada en 2025: antes se dividía por aperturas). Febrero 0,54 %, diciembre 0,35 %. Fundadores 0,57 %, C-level 0,42 %, VP 0,32 %. Empresas 11-50 empleados 0,49 %; 10.000+ 0,22 %. Por industria (mín. 20.000 correos): Food & Beverage 3,47 % (atípico); Construction, Financial Services, Healthcare, Legal 0,56-0,60 %; Banking/Insurance las más bajas. **Fila "Manufacturing": NO ENCONTRADO** (no aparece en el texto; el gráfico no se renderiza).
- https://belkins.io/blog/sales-follow-up-statistics : tasa de respuesta por paso: paso 1 0,59 %, paso 3 0,30 %, paso 4 0,34 %, paso 6 0,28 %; los pasos 2-6 suman 58,6 % de las respuestas. **Tasa de cita (appointment) por correo: ~0,1 % en pasos 1-2 y se estabiliza en 0,2 % desde el paso 3**. Reparto de citas por canal en 2025: email 50 %, llamada 33,6 % (46.000+ llamadas, 18,6 % de conexión), LinkedIn el resto (respuesta 7 %+; mensajes a conectados 12,22 %; peticiones de conexión 7,95 %, datos de Expandi).
- "Average industry results" para manufactura que Belkins promete (https://belkins.io/case-studies/industry/manufacturing): 150+ citas/año, 10 % lead-to-appointment, 60 %+ engagement. Son promesas de marketing, sin muestra.

### 1.3 Plataformas (medianas de mercado, no de agencia) [ABIERTA]
- **Smartlead**, 850 M+ correos, remitentes con ≥500 envíos, respuesta/contacto: mediana **0,74 %** (1 respuesta cada 135 contactos); top 25 % 1,43 %; top 10 % 2,63 %; top 5 % 3,85 %; bottom 25 % 0,37 %. "Mide respuestas, no reuniones ni ingresos; no desglosa por industria". https://www.smartlead.ai/benchmarks/average-cold-email-reply-rate
- **Woodpecker** (vía Webtonic y la propia página de Woodpecker, análisis de 26.000 campañas, actualizado ene-2025): mediana de respuesta 1,5 % en 56.614 campañas; apertura mediana 26 %. https://woodpecker.co/blog/cold-email-benchmarks/ ; https://www.webtonic.io/blog/manufacturing-and-industrial-cold-email-outbound-statistics (recopilación "Manufacturing and Industrial Cold Email Data 2026": recomienda planificar con la mediana 1,5 % y tratar 3,43 % como techo).
- **Instantly 2026 Benchmark Report** (vía Cleverly/Webtonic; la página de estadísticas de Instantly abierta sólo contiene consejos de asunto/seguimiento): media de respuesta 3,43 % sobre entregados, "miles de millones" de envíos, sin desglose industrial útil. https://instantly.ai/blog/cold-email-statistics
- **Cleverly** (agencia, 28/07/2026): respuesta positiva = 40-60 % de las respuestas totales; **reuniones agendadas por 1.000 correos: high-ticket/enterprise 3-8 (0,3-0,8 %), mid-market 5-15, SMB 10-25**; manufactura apertura 28-33 %, sin fila de respuesta. https://www.cleverly.co/blog/cold-email-benchmarks-by-industry
- **lemlist** (2026): bandas por industria 2-7 % sin muestra ni fila industrial. https://lemlist.com/blog/cold-email-benchmarks/ ; https://lemlist.com/blog/cold-email-response-rate
- **Cognism/Kaspr por sector: NO ENCONTRADO** (URL de estadísticas devuelve 404).

### 1.4 LinkedIn en industria — Expandi (13.218.869 peticiones de conexión, 13.302 cuentas, may-2025 a abr-2026) [ABIERTA]
https://expandi.io/blog/linkedin-outreach-benchmarks/ (apéndice parseado del HTML). Medias de plataforma: aceptación 28,5 %, respuesta a la nota de conexión 3,0 %, respuesta a mensajes 10,4 %. Filas por **industria del remitente**:

| Industria remitente | Cuentas | Peticiones | Aceptación | Resp. nota conexión | Resp. mensaje |
|---|---|---|---|---|---|
| Mechanical / Industrial Engineering | 87 | 86.407 | 29,5 % | 2,3 % | 10,9 % |
| Electrical / Electronic Manufacturing | 51 | 60.334 | 29,0 % | 2,9 % | 12,1 % |
| Machinery | 56 | 52.233 | 26,8 % | 2,3 % | 9,0 % |
| Industrial Automation | 42 | 48.800 | 31,2 % | 3,2 % | 9,6 % |
| Construction | 119 | 117.715 | 26,9 % | 2,5 % | 11,4 % |
| Oil & Energy | 30 | 41.529 | 28,1 % | 4,1 % | 12,0 % |
| Utilities | 20 | 13.916 | 27,5 % | 3,9 % | 12,5 % |
| Chemicals | 16 | 18.631 | 31,4 % | 3,0 % | 9,5 % |

Lectura: por cada 100 peticiones de conexión en industria, ~27-31 aceptan y ~3 responden a la nota; de los mensajes posteriores responden ~9-12 % (todas las respuestas, no sólo positivas). **HeyReach por sector: NO ENCONTRADO** (404).

### 1.5 Respuesta positiva → reunión agendada → reunión celebrada
- Conversión positiva→agendada: **no existe estudio con muestra**. Cleverly (0,3-0,8 % de reuniones/correo en high-ticket) y Modern Inbound ("1.000 correos → 10-20 positivas → 4-10 reuniones", es decir 40-50 %) son estimaciones de agencias. https://moderninbound.com/blog/cold-email-meeting-show-rate-2026
- **No-show**: RevenueHero cita "20-40 %" como rango de la industria (su estudio de 6.428 reuniones B2B con 6,5 % de no-show, dic-2024, sólo apareció en búsqueda: [FRAGMENTO]) https://www.revenuehero.io/blog/what-is-a-no-show-rate ; Chili Piper: "el no-show estándar en ventas es 20 %", su outbound <5 % con recordatorios; cliente OrderMyGear 20 % → 10 % https://www.chilipiper.com/post/will-aitken-guide-no-shows , https://www.chilipiper.com/customer-story/ordermygear ; Focus Digital (14/09/2026, sin fuente primaria): mezcla 25 %, **outbound SDR 35-45 %, "appointment setting externalizado" 42 %**, agenda el mismo día 7 % https://focus-digital.co/average-no-show-rate-for-booked-sales-meetings-by-booking-channel/ ; Modern Inbound rastrea la única cifra con dataset (Operatix, 500+ empresas): ~80 % de asistencia / 20 % no-show en reuniones de SDR outbound. Belkins/Smartrek: 1 no-show de 15 citas (6,7 %). **Gong, Calendly: NO ENCONTRADO** con muestra.

---

## 2. Casos documentados 2021-2026 de outbound para fabricantes/industriales (bloque 2) — 10 casos abiertos

Todos son casos publicados por las propias agencias (sesgo de selección: sólo publican éxitos; cifras no auditadas). Se extrae el ratio reuniones/contactos cuando la página lo permite.

| # | Caso (agencia, fuente) | Cliente / tamaño | Periodo | Contactos | Respuestas / aperturas | Reuniones agendadas | Ratio reuniones/contacto | Otros |
|---|---|---|---|---|---|---|---|---|
| 1 | Belkins – BAG Corp (bolsas industriales, Texas) https://belkins.io/case-studies/lead-generation-for-bulk-bag-manufacturer | 201-500 empl. | 11 meses | **10.780 contactos** investigados | apertura 41 %, respuesta 7,3 % | **91** (≈8/mes) | **0,84 %** | 22 peticiones de oferta (24 % de las citas); sólo email; 3 citas de una campaña nicho a parques eólicos |
| 2 | Belkins – AMI Global (IoT para fabricantes de bombas, Nevada) https://belkins.io/case-studies/lead-generation-for-industrial-iot-solutions-manufacturer | 11-50 empl. | 18 meses, 14+ campañas | **6.700 contactos** | apertura hasta 81 %, respuesta máx. 17 % | **101** (29 con enterprise) | **1,5 %** (declarado por Belkins) | 15 citas en los 2 primeros meses; "ciclos de venta largos" |
| 3 | Belkins – Sekisui Products (química/plásticos, filial EE. UU.) https://belkins.io/case-studies/lead-generation-for-thermal-management-products-manufacturer | 10.001+ empl. | 4 meses | 800 leads | n/d | **21** (5-6/mes; 6 "dream clients") | 2,6 % | ratio de cierre 15 %; marca global reconocida |
| 4 | Belkins – Smartrek (conectividad inalámbrica industrial) https://belkins.io/case-studies/lead-generation-for-wireless-connectivity-products-manufacturer | pyme | 2 meses | **1.000 leads** (vs 750 estándar) | n/d | **15** | **1,5 %** | **1 no-show de 15**; producto "muy técnico y nicho" |
| 5 | Belkins – fabricante de señalización (EE. UU.) https://belkins.io/case-studies/omnichannel-lead-generation-for-a-signage-manufacturer | 51-100 empl. | 2025 | 6.000+ contactos (campaña "breakout") | n/d | 17 (breakout) + 31 (segmento núcleo); ~4/mes, 50-60/año | **0,28 %** (breakout) | omnicanal: 4 emails + LinkedIn + llamadas; pipeline 2,7 M$; mayor oportunidad 575 k$ |
| 6 | Belkins – Deluxe Modular (construcción modular, NY) https://belkins.io/case-studies/lead-generation-for-prefabricated-building-manufacturer | 11-50 empl. | 3 meses | n/d ("la investigación tardó el doble") | n/d | 30+ (8 el primer mes) | n/d | 2 M$+ cerrados |
| 7 | Belkins – Lion Energy (almacenamiento energético, Utah) https://belkins.io/case-studies/lead-generation-for-clean-energy-storage-manufacturer | 11-50 empl. | 10 meses | n/d | apertura 85 % | 137 (70 en 4 meses) | n/d | objetivo: instaladores solares; pipeline +10 M$ |
| 8 | CIENCE – CB Pacific (automatización industrial, tras fusión con GE) https://www.cience.com/case-studies/cb-pacific | distribuidor industrial | 3 años | 5.000+ emails + 3.000+ llamadas | n/d | 300+ citas presenciales | n/d (base de clientes heredada; no es frío puro) | multicanal con landing pages |
| 9 | Sopro – Coveris (envases, Reino Unido) https://sopro.io/results/case-studies/coveris/ | 4.000+ empl. (fabricante) | n/d | **2.195 prospectos** (1.097 F&B, 695 Food Production, 248 Electrical/Electronic Mfg, 110 Retail, 45 Consumer Goods) | respuestas 222 (10 %) | **97 leads (4,4 %)**; no publica reuniones | lead 4,4 %; **en Electrical/Electronic Mfg 5 leads de 248 = 2 %, 99 £/lead** | coste/lead 26-220 £; empresas 11-50 y 51-200 empl.: lead rate 5 % |
| 10 | Sopro – On Device Research (no industrial, referencia de ritmo) https://sopro.io/results/success-stories/on-device | 51-200 | desde 2022 | n/d | n/d | 725 conversaciones, 34 leads/mes en 2023 | n/d | leads, no reuniones |

Casos negativos/mixtos [FRAGMENTO]: Clutch, fabricante de San Diego (51-200 empl.) sobre Martal Group: "empezaron con 1-2 citas por semana, luego se fue apagando"; coste 3/5 https://clutch.co/go-to-review/martal-group/119026 (bloqueado por Cloudflare). Trustpilot Prospectify: "6 reuniones en 4 meses, sólo 1 encajaba con el perfil acordado" https://www.trustpilot.com/review/weprospectify.com (403). Trustpilot Dealforce: leads "no cualificados ni realmente interesados", cobro por reunión igualmente https://de.trustpilot.com/review/dealforce.io (403).

**Casos españoles con cifras (agencias españolas, posts de fundadores industriales, Indie Hackers): NO ENCONTRADO.** Lo más cercano: Sol Media Solutions (Clutch, 403) afirma "3.500+ reuniones para 55 empresas" sin desglose; listado SyncGTM de agencias en España (ALYS Marketing "industrial B2B", SalesCaptain "120+ reuniones en 12 meses" en SaaS) https://syncgtm.com/blog/best-sales-agencies-in-spain [ABIERTA]; Enginy y DevCommX venden servicios para fabricantes en Sevilla/Bilbao sin resultados publicados.

**Lectura transversal**: en los 4 casos con numerador y denominador (BAG Corp, AMI Global, Smartrek, señalización-breakout) el ratio **reuniones agendadas / contacto está entre 0,28 % y 1,5 %**, con mediana ≈ 1,2 %, usando equipos humanos de SDR, secuencias de 14+ campañas, y en 2 de 4 casos llamadas y LinkedIn además del email. Ninguno es un fabricante español ni opera bajo LSSI.

---

## 3. Cálculo de la garantía "4 reuniones celebradas en 30 días con 300 contactos" (H3)

Supuestos comunes: 300 contactos nominativos del ICP (maquinaria/automatización/ingeniería), secuencia de 3-5 correos (≈1,9 emails/prospecto/mes como Sopro) ± LinkedIn; mes natural de 30 días (la reunión debe *celebrarse* dentro del mes, lo que recorta el embudo: Belkins dice que >53 % de las citas llegan del paso 3 en adelante, y la Sopro sitúa el primer flujo estable de reuniones en "4-6 semanas" https://sopro.io/solutions/appointment-setting-services/).

| Paso | Pesimista | Base | Optimista | Fuente del parámetro |
|---|---|---|---|---|
| Contactos | 300 | 300 | 300 | — |
| Respuesta total (todas) | 0,74 % → 2,2 | 1,5 % → 4,5 | 2,63 % → 7,9 | Smartlead mediana / Woodpecker mediana / Smartlead top-10 % |
| Respuesta positiva estricta | 0,30 % → **0,9** | 0,6 % → **1,8** | 1,3 % → **3,9** | Sopro mensual 0,22-0,35 % por prospecto / ≈40 % de respuestas (Cleverly) / 50 % de top-10 % |
| "Leads" en sentido amplio (positiva + diferida + referido) | 1,0 % → 3,0 | 1,25 % → 3,75 | 2,1 % → 6,4 | Sopro por prospecto: Ind. Automation 0,89 %, Machinery 1,25 %; Lead % por empresa Machinery 2,12 % |
| Reuniones agendadas | 50 % de positivas → **0,45** (o Belkins 0,1-0,2 %/email × 5 pasos → 2,4 si hay llamadas) | casos Belkins mediana **1,0 %** → **3,0** | **2,0 %** → **6,0** (Sekisui 2,6 %, Smartrek/AMI 1,5 %) | Modern Inbound / casos BAG Corp 0,84 %, AMI 1,5 %, Smartrek 1,5 %, señalización 0,28 % |
| Asistencia (1 − no-show) | 60 % (Focus Digital 35-45 % no-show en outbound externalizado) | 80 % (Operatix/Chili Piper 20 %) | 90 % (Smartrek 1/15; Chili Piper <5 % con recordatorios) | sección 1.5 |
| **Reuniones celebradas / mes** | **0,3-1,4** | **2,4** | **5,4** | — |
| P(≥4 celebradas) con Poisson(λ) | λ=1,1 → **≈3 %** | λ=2,4 → **≈22 %** | λ=5,4 → **≈79 %** | cálculo propio |

Para que una garantía de 4 reuniones celebradas se cumpla el 80 % de los meses hace falta λ ≈ 5,5 → con el ratio base (0,8 % celebradas/contacto) **≈ 690 contactos/mes**, o 300 contactos con un ratio del 1,8 % de reuniones celebradas por contacto, que sólo aparece en el mejor caso publicado (Sekisui, marca global, Belkins con SDR humanos y llamadas).

**Veredicto H3: REFUTADA.** (a) La premisa numérica es falsa: Sopro no publica "respuesta positiva 2,5-3,5 %" en industria; su Lead % de 1,8-2,2 % en el ICP núcleo es por empresa, incluye interés diferido y referidos, y la positiva estricta es ~0,3-0,45 % por contacto. (b) La conversión positiva→reunión 40-60 % no tiene fuente con muestra. (c) Con los mejores casos publicados por agencias con SDR humanos y llamadas, 300 contactos producen 1-3 reuniones celebradas; "4 garantizadas en 30 días" exige el percentil 90 del sector o duplicar/triplicar el volumen. (d) Un canal sólo-email dirigido por IA, sin llamadas, está por debajo del escenario base (Belkins obtiene el 33,6 % de sus citas por teléfono).

---

## 4. La pyme industrial española (H4)

### 4.1 Tamaño del universo (INE DIRCE a 1-1-2025, publicado 11-12-2025) [ABIERTA]
https://www.ine.es/dyngs/Prensa/es/DIRCE2025.htm y PDF https://www.ine.es/dyngs/Prensa/DIRCE2025.pdf
- 3.310.824 empresas activas; **Industria 172.765 (5,2 %)**. Industria por asalariados: sin asalariados 55.412; 1-2: 48.803; 3-5: 23.160; 6-9: 14.472; **10-19: 14.341; 20 o más: 16.577 (9,6 % de las industriales, el sector con mayor peso de empresas de ≥20)**. El 32,4 % de las industriales tiene ≥20 años. La estadística pública no desglosa 20-49 / 50-199 ni separa manufactura (sección C) de extractivas/energía en la nota de prensa; **tabla exacta 20-49 y 50-199 de la sección C: NO ENCONTRADO** (el anexo Excel devolvió 404; INEbase no se abrió).
- IPYME, *Retrato de la PYME 2024* (DIRCE 2023) https://ipyme.org/Publicaciones/Retrato%20de%20la%20PYME/Retrato_Pyme_DIRCE_2024.pdf [ABIERTA, PDF]: en industria, microempresas 1-9: 51,5 %; **pequeñas 10-49: 14,4 %; medianas 50-249: 2,6 %; grandes ≥250: 0,6 %**. La industria concentra el 19,0 % de todas las pequeñas y el 22,0 % de todas las medianas de España. Pymes manufactureras −2.428 (−1,56 %) en 2023; alimentación 22.789 pymes, química 3.286.
- IPYME, *Cifras PYME diciembre 2025* https://ipyme.org/Publicaciones/Cifras%20PYME/CifrasPyme_diciembre_2025.pdf [ABIERTA, PDF]: Industria 163.459 empresas con Seguridad Social (−2,54 % anual), 2.332.395 empleados; tamaño medio industrial 13 empleados (vs 6 total). Empleo en industria manufacturera por tramo: 60.397 (autónomos) / 231.415 (1-9) / 503.922 (10-49) / 549.551 (50-249) / 741.970 (≥250) = 2.087.255.
- **Estimación propia del ICP** (20-199 empleados, manufactura): 16.577 industriales con ≥20 asalariados menos las ≥200 (≈1.000-1.500, dado que las ≥250 son el 0,6 %) y menos extractivas/energía/agua (≈5-8 % del sector industrial) → **≈ 13.000-15.000 empresas**. Es un mercado finito: a 300 contactos/mes y ~3 contactos por empresa, un solo cliente agota 100 empresas/mes; 10 clientes del mismo subsector colisionan en pocos meses.

### 4.2 Digitalización comercial [ABIERTA]
- INE, *Encuesta de uso de TIC y comercio electrónico en las empresas 2024 / 1T 2025* (22-10-2025) https://www.ine.es/dyngs/Prensa/es/ETICCE20241T2025.htm y PDF: empresas de 10+ empleados que usan **software CRM: 34,5 %** (total, todos los sectores; Cataluña 43,4 %, Madrid ~alto, Asturias 20,3 %); ERP 63,6 %; en **Industria**: analítica de datos 42,5 %, cloud de pago 40,4 %, IA 17,5 % (vs 25,7 % servicios). Desglose de CRM por sector y por tramo 10-49: NO ENCONTRADO en la nota (está en los resultados detallados, no abiertos). Eurostat 2023 (vía búsqueda, [FRAGMENTO]): CRM 22 % en pequeñas vs 61 % en grandes de la UE.
- Fundación BBVA/Ivie (jul-2025, citado por Aspid [FRAGMENTO]): ~62 % de las manufactureras españolas alcanza nivel básico de digitalización vs 68 % UE.

### 4.3 Función comercial, ferias, distribuidores, externalización
- AMEC (empresas industriales internacionalizadas, 8-4-2025) https://amec.es/en/press-releases/amecs-international-industrial-companies-are-responding-strategically-to-the-challenges-of-the-new-era-of-globalization-and-foresee-growth-through-2025/ [ABIERTA]: exportaciones +5,43 % en 2024; 76,2 % prevé crecer en 2025; 55 % aumentó plantilla; UE 50,2 % de las exportaciones; nota 2026 (vía búsqueda): propensión exportadora media **57 % de la facturación**, 74,1 % prevé exportar más en 2026. AMEC no publica datos sobre canales de venta ni prospección.
- Consejo General de Economistas, *Informe Pyme 2024* (634 pymes) [FRAGMENTO, PDF 403]: la industria es el sector más internacionalizado (13,2 % del negocio en el exterior); *Informe Pyme 2025*: industria destaca en acceso a nuevos mercados (46,5 %).
- HubSpot, informe sobre pymes españolas (ene-2026, vía Autónomos y Emprendedor) https://www.autonomosyemprendedor.es/articulo/pymes/asesorias-explican-que-muchas-pymes-han-logrado-crecer-ni-aumentar-ingresos-2025/20260116105321047816.html [ABIERTA]: los retos están en "la captación de clientes y la actividad comercial"; sólo 4 de cada 10 analizan ambas conjuntamente; visibilidad limitada del recorrido del cliente en el 70 % de las conversaciones; 80 % de fallos de transmisión entre quien genera oportunidades y quien las gestiona. No es específico de industria.
- Aspid (agencia industrial, guía 2025) https://aspid.marketing/marketing-industrial-espana-guia-empresas-b2b/ [ABIERTA]: "una parte significativa de estas empresas depende todavía de la red comercial de toda la vida, de las ferias sectoriales y del boca a boca" — afirmación de proveedor **sin dato**; cita Gartner 2024 (632 compradores B2B): 61 % prefiere comprar sin interacción con un comercial.
- Ferias: AFE (vía búsqueda [FRAGMENTO]): 472 ferias en 2025 (445 en 2024), expositores +6,9 %. Ministerio: ~600 eventos/año. Nada mide qué % de la captación industrial depende de ferias.
- Canales: el único dato cuantitativo hallado es un estudio académico antiguo (Dialnet, sin fecha, [FRAGMENTO]): 83,3 % de fabricantes industriales usan distribuidores independientes en el mercado nacional; venta directa = 46 % de las ventas. Encuesta ESEE 2024 de Fundación SEPI: el servidor rechaza TLS desde la sesión → NO ABIERTA.
- Externalización comercial: GrupoUno CTC (2016, 300 directivos) [FRAGMENTO]: 13 % de lo externalizado son procesos comerciales; Alimarket *Informe 2025 sobre outsourcing comercial* de pago; Grant Thornton: 40 % de medianas externalizó algún servicio tras la pandemia. **Encuesta sobre disposición de la pyme industrial a externalizar la prospección: NO ENCONTRADO.**
- Ciclo de venta: Belkins/AMI "ciclos largos", Sekisui 15 % de cierre; DevCommX (agencia) anuncia "90-240 días" para manufactura; SalesRoads cita 12-18 meses. Son afirmaciones de proveedores.

**Veredicto H4: PARCIALMENTE SOPORTADA / NO VERIFICADA.** Lo que está probado: el segmento existe y es pequeño (≈13-15 k empresas manufactureras de 20-199), tiene 13 empleados de media en industria, baja adopción de CRM (34,5 % en 10+ empleados; menor en pequeñas) y exporta mucho (las de AMEC, 57 % de su facturación). Lo que **no** está probado con páginas abiertas: que dependa de ferias/distribuidores (sólo afirmaciones de agencias y un estudio académico antiguo), que carezca de SDR (ningún dato), ni que esté dispuesta a externalizar la prospección (ningún dato; la externalización comercial medida es de punto de venta/gran consumo). El dolor "captación de clientes" aparece en el informe HubSpot pero para pymes en general.

---

## 5. Legal España (H5) — texto literal del BOE y criterios de la AEPD

### 5.1 LSSI, Ley 34/2002 (texto consolidado, BOE) [ABIERTA] https://www.boe.es/buscar/act.php?id=BOE-A-2002-13758
- **Art. 21.1**: «Queda prohibido el envío de comunicaciones publicitarias o promocionales por correo electrónico u otro medio de comunicación electrónica equivalente que previamente no hubieran sido solicitadas o expresamente autorizadas por los destinatarios de las mismas.»
- **Art. 21.2**: «Lo dispuesto en el apartado anterior no será de aplicación cuando exista una relación contractual previa, siempre que el prestador hubiera obtenido de forma lícita los datos de contacto del destinatario y los empleara para el envío de comunicaciones comerciales referentes a productos o servicios de su propia empresa que sean similares a los que inicialmente fueron objeto de contratación con el cliente. En todo caso, el prestador deberá ofrecer al destinatario la posibilidad de oponerse al tratamiento de sus datos con fines promocionales mediante un procedimiento sencillo y gratuito […] Cuando las comunicaciones hubieran sido remitidas por correo electrónico, dicho medio deberá consistir necesariamente en la inclusión de una dirección de correo electrónico u otra dirección electrónica válida donde pueda ejercitarse este derecho, quedando prohibido el envío de comunicaciones que no incluyan dicha dirección.» (redacción vigente desde 11/05/2014).
- **Art. 20.1 y 20.4**: la comunicación debe ser «claramente identificable como tal» y «la persona física o jurídica en nombre de la cual se realizan también deberá ser claramente identificable»; prohibido «disimular u ocultar la identidad del remitente por cuenta de quien se efectúa la comunicación». → Un tercero que envía *en nombre* del fabricante expone formalmente al fabricante.
- **Art. 38.3.c)** (grave): «El envío masivo de comunicaciones comerciales por correo electrónico […] o su envío insistente o sistemático a un mismo destinatario del servicio cuando en dichos envíos no se cumplan los requisitos establecidos en el artículo 21.» **Art. 38.4.d)** (leve): el envío que incumpla el art. 21 «y no constituya infracción grave». **Art. 39.1**: leves hasta 30.000 €; graves 30.001-150.000 €; muy graves 150.001-600.000 €.
- Anexo f): «comunicación comercial» = «toda forma de comunicación dirigida a la promoción, directa o indirecta, de la imagen o de los bienes o servicios de una empresa, organización o persona que realice una actividad comercial, industrial, artesanal o profesional» (reproducido por la AEPD en PS/00396/2022). La ley habla de «destinatarios» sin excluir a empresas ni a direcciones profesionales.

### 5.2 LOPDGDD, Ley Orgánica 3/2018 (BOE) [ABIERTA] https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673
- **Art. 19.1**: «Salvo prueba en contrario, se presumirá amparado en lo dispuesto en el artículo 6.1.f) del Reglamento (UE) 2016/679 el tratamiento de los datos de contacto y en su caso los relativos a la función o puesto desempeñado de las personas físicas que presten servicios en una persona jurídica siempre que se cumplan los siguientes requisitos: a) Que el tratamiento se refiera únicamente a los datos necesarios para su localización profesional. b) Que la finalidad del tratamiento sea únicamente mantener relaciones de cualquier índole con la persona jurídica en la que el afectado preste sus servicios.» **19.2**: misma presunción para empresarios individuales y profesionales liberales «cuando se refieran a ellos únicamente en dicha condición».
- Alcance: legitima **tratar** (recopilar, almacenar, enriquecer) nombre, cargo y email profesional para relacionarse con la empresa. **No** deroga el art. 21 LSSI, que regula el **acto de enviar** la comunicación comercial electrónica.

### 5.3 Criterio de la AEPD [ABIERTA, PDFs]
- **Informe del Gabinete Jurídico 2018-0173** https://www.aepd.es/documento/2018-0173.pdf : «resulta de aplicación el principio de especialidad, de forma que las causas legitimadoras para el tratamiento de los datos a las que se refiere el artículo 6 del Reglamento general de protección de datos […] han de ceder ante la regla especial contenida, para estos concretos tratamientos en la Ley 34/2002, toda vez que en caso contrario esta última norma quedaría vaciada de contenido»; «el citado artículo 21 opera como límite al que habrá de estarse en todo caso cuando las acciones de mercadotecnia o publicidad se lleven a cabo a través de medios electrónicos, al establecerse para estos supuestos la regla general del consentimiento expreso del interesado». → **El interés legítimo (RGPD 6.1.f / LOPDGDD 19) no sirve como base para el correo frío.** Cita el informe 195/2017 y la SAN que condenó a un remitente por no tener «consentimiento de sus destinatarios y no constar la existencia de una relación contractual anterior».
- **E/02208/2018** https://www.aepd.es/documento/e-02208-2018.pdf : correos publicitarios de LACOMA, RUEDA Y ASOCIADOS, S.L. a «dos cuentas de correo electrónico, pertenecientes a directivos y trabajadores de la empresa REAL SITIO DE VENTOSILLA SA», sin relación contractual. AEPD: «ha quedado acreditada la remisión […] lo que constituye una infracción del art. 21.1 de la LSSI. Infracción tipificada como leve en el artículo 38.4.d) […] pudiendo ser sancionada con multa de hasta 30.000 euros». Se archiva porque el remitente dio de baja las direcciones al primer aviso (SAN 29/11/2013: si las medidas correctoras ya se adoptaron, procede el archivo). **Confirma que el correo B2B a buzones corporativos nominativos está dentro del art. 21.**
- **A/00031/2019 → RR/00040/2020** https://www.aepd.es/es/documento/reposicion-00031-2019.pdf : despacho YBL Abogados envió publicidad de sus servicios a dos direcciones de otro despacho; ignoró la petición de baja. **Apercibimiento** (art. 39 bis.2 LSSI) con requerimiento de medidas en un mes; recurso desestimado.
- **A/00011/2017** https://www.aepd.es/documento/a-00011-2017.pdf : SEARCH TASK S.L.U. envió 5 correos (jul-ago 2016) ofreciendo «créditos a pymes y solicitudes de ayuda» desde dominios secundarios (responseput1.com, responsegetc.com) con pie de baja; sin consentimiento acreditado → infracción leve 21.1, apercibimiento. **Relevante: usar dominios secundarios y enlace de baja no exime; lo que se castiga es la falta de consentimiento previo.**
- **PS/00396/2022** https://www.aepd.es/documento/ps-00396-2022.pdf : correos comerciales tras solicitar la baja (enlace de baja inactivo) → multa de **200 €** a LA CASA DEL BAMBÚ (empresa extranjera). Resoluciones 2023-2026 específicas sobre correo B2B a direcciones corporativas: **NO ENCONTRADO** (el buscador de resoluciones de la AEPD devolvió 403/503; sólo [FRAGMENTO]: Prodat describe una multa de 20.000 € a una gran textil por art. 21 en contexto B2C https://www.prodat.es/blog/utilizan-los-datos-personales-del-ticket-de-compra-para-el-envio-de-publicidad-sin-consentimiento-previo/ [ABIERTA]; Genbeta (nov-2022) 800 € a una empresa que «hace un recopilatorio de personas que pueden estar interesadas en un sector concreto» [ABIERTA]).
- Circular 1/2023 de la AEPD (llamadas comerciales, nota de Ecija, mayo 2023) https://files.griddo.ecija.com/nota-informativa-circular-12023-vfinal.pdf [ABIERTA, PDF]: la AEPD admite el interés legítimo para **llamadas** a «personas físicas que presten servicios en una persona jurídica o empresarios individuales y profesionales liberales en base al artículo 19 LOPDGDD», con ponderación documentada y consulta previa a los sistemas de exclusión publicitaria (Lista Robinson). Ecija subraya que ni la Circular ni el informe 40/2022 se pronuncian sobre llamadas a *potenciales* clientes. → **El teléfono tiene una vía de interés legítimo que el correo electrónico no tiene.** Garrigues (2019) https://www.garrigues.com/es_ES/noticia/listas-robinson-las-empresas-deben-revisar-sus-procedimientos-internos-para-el-envio-de [ABIERTA]: cuando la base es el interés legítimo, es obligatorio consultar la Lista Robinson (Adigital).
- Fieldfisher, *Bases de datos empresariales bajo la lupa* (resoluciones AEPD 2025) https://www.fieldfisher.com/es-es/locations/spain/insights/bases-datos-empresariales [FRAGMENTO, 403]: el art. 19 LOPDGDD «no ampara el envío de comunicaciones comerciales B2B» y la AEPD considera el art. 21 LSSI norma especial; resoluciones de mayo de 2025 rechazan usar datos censales de autónomos para productos de información empresarial.

### 5.4 Cómo lo resuelven las agencias y proveedores
- Overloop, *Cold email B2B en España: guía RGPD + LSSI + AEPD (mayo 2026)* https://overloop.com/es/blog/b2b-cold-email-espana-rgpd-aepd [ABIERTA]: reconoce que «tener una base RGPD-compliant no te autoriza a enviar emails comerciales bajo LSSI»; su receta es «cumplir LSSI Art. 21 vía consentimiento previo o relación contractual previa, opt-out claro en cada email, limitar el tratamiento a contactos en función profesional»; afirma que «la AEPD acepta el interés legítimo para B2B con direcciones de cargo profesional» — afirmación de un proveedor de software que **contradice el informe 2018-0173** de la propia AEPD. Cita 70.000 € por opt-out roto (sin referencia abierta).
- LeadGenius (26-5-2026) https://www.leadgenius.com/resources/best-b2b-data-provider-for-spain-aepd-lssi-ce-and-lista-robinson-compliance [ABIERTA]: «España opera uno de los regímenes de correo comercial más estrictos de la UE bajo LSSI-CE, que en general exige consentimiento previo para el email B2B fuera de una relación comercial preexistente»; vende datos con doble opt-in y cribado de Lista Robinson.
- Práctica estándar de agencias (Danish Lead Co, Smartlead, SmartReach): dominios secundarios y buzones separados «nunca el dominio principal», SPF/DKIM/DMARC, volumen controlado, calentamiento 2-3 semanas, aprobación de copy por el cliente, pago por «reunión cualificada» según criterios pactados https://danishleadco.io/cold-email-blog/before-you-hire-a-cold-email-agency-read-this [ABIERTA]. Esto protege la **entregabilidad** del dominio del cliente, no su exposición legal: LSSI art. 20 exige identificar a la persona «en nombre de la cual» se envía, y la AEPD (A/00011/2017) sancionó envíos desde dominios secundarios.

### 5.5 Riesgo de marca (bloque 5)
- Evidencia documentada de fabricantes dañados por externalizar prospección: **NO ENCONTRADO** con nombre y cifras; sólo reseñas anónimas [FRAGMENTO] (Prospectify 1/6 reuniones en perfil; Dealforce leads no interesados cobrados; Martal "se fue apagando"; Trustpilot Sopro mixto, contrato de 3 meses discutido) y anécdotas de agencias sobre dominios principales en lista negra (Danish Lead Co: «arreglar un dominio en lista negra lleva meses»; vendedor de EmailListVerify: «100+ correos por buzón al día = dominio entero en lista negra en un mes») [FRAGMENTO].
- Dato duro de deterioro del canal: Belkins −20 % de respuesta entre 1S y 2S de 2025 por «saturación de bandejas y filtrado más estricto» [ABIERTA]; Woodpecker: campañas con <2 % de rebote obtienen 60 % más respuesta que las de >20 % [ABIERTA vía Webtonic].
- Mitigaciones que usan las agencias serias: dominios secundarios + DMARC; aprobación del mensaje por el cliente; criterios de cualificación por escrito y reposición de reuniones no válidas; volumen bajo por buzón (20-40 envíos/día en dominio nuevo); recordatorios SMS/email para reducir no-show (Chili Piper <5 %).

**Veredicto H5: REFUTADA tal como está formulada.** El correo frío a direcciones corporativas nominativas sin consentimiento es, según el BOE y la práctica de la AEPD, una infracción del art. 21.1 LSSI (leve: hasta 30.000 €; grave si es masivo o insistente: 30.001-150.000 €), imputable al prestador y con el fabricante identificado como anunciante (art. 20). El art. 19 LOPDGDD cubre el fichero, no el envío; la AEPD lo ha dicho por escrito (2018-0173) y lo ha aplicado a buzones de directivos y trabajadores (E/02208/2018). La probabilidad de sanción por campaña es baja (procedimientos iniciados por denuncia; primer caso suele acabar en apercibimiento o archivo si se da de baja al instante; multas vistas: 200-20.000 €), pero el riesgo reputacional recae en la marca del fabricante, cuyo mercado son ≈13-15 k empresas que se conocen entre sí. El modelo sólo es defendible si (1) el email se limita a destinatarios con consentimiento o relación previa (clientes, visitantes de feria que aceptaron, descargas con opt-in), (2) la prospección fría se hace por **teléfono** (interés legítimo admitido por la AEPD con ponderación + Lista Robinson) y **LinkedIn** (zona gris: mensajería en plataforma donde el destinatario acepta la conexión; no hay resolución AEPD abierta al respecto — NO ENCONTRADO), y (3) el contrato con el fabricante documenta la ponderación, el opt-out y la responsabilidad del encargado.

---

## 6. Lo que no se encontró (para que nadie lo dé por hecho)
- Tasa de respuesta positiva de Sopro para industria del 2,5-3,5 %: **no existe**; sus cifras son Lead % por empresa (1,8-3,8 %) con ~1/3 de positivas.
- Fila "Manufacturing" en Belkins 2025 con cifra: NO ENCONTRADO. Cognism/Kaspr/HeyReach por sector: NO ENCONTRADO.
- Estudio con muestra de conversión respuesta positiva → reunión celebrada: NO ENCONTRADO (sólo estimaciones 40-60 % de agencias). No-show con muestra: RevenueHero 6,5 % (6.428 reuniones, dic-2024, [FRAGMENTO]); Operatix ~20 % outbound (citado, no abierto).
- Casos españoles de outbound para fabricantes con cifras: NO ENCONTRADO (8 casos exigidos: se abren 10, todos EE. UU./UK).
- Encuesta sobre % de pymes industriales españolas con departamento comercial estructurado, dependencia de ferias, o disposición a externalizar prospección: NO ENCONTRADO. ESEE 2024 (Fundación SEPI) no abierta (TLS). Informe Pyme 2024/2025 del Consejo General de Economistas: PDF 403.
- Tabla INE de manufactura por tramos 20-49 / 50-199: NO ENCONTRADO (estimado a partir de DIRCE 2025 e IPYME).
- Resoluciones AEPD 2023-2026 sobre correo B2B a direcciones corporativas: NO ENCONTRADO (buscador AEPD 403/503); las resoluciones abiertas son 2017-2022 y todas aplican el art. 21 a empresas.
- Pronunciamiento de la AEPD sobre mensajes de LinkedIn como «medio de comunicación electrónica equivalente»: NO ENCONTRADO.

---

## 7. Tabla de URLs

| # | URL | Estado | Qué aporta |
|---|---|---|---|
| 1 | https://sopro.io/results/interactive-insights/performance-by-industry | ABIERTA | Tabla viva por industria y tamaño (792 campañas, 23/10/2026) |
| 2 | https://sopro.io/results/the-state-of-prospecting/ | ABIERTA | Misma tabla + tabla mensual con Positive Response / Deferred / Referral / Leads / coste por lead |
| 3 | https://sopro.io/results/the-state-of-prospecting/whitepaper/ | ABIERTA | State of Prospecting 2022: 25 M emails, 82 industrias (sin datos en página) |
| 4 | https://sopro.io/results/case-studies/coveris/ | ABIERTA | Caso Coveris: 2.195 prospectos, 222 respuestas, 97 leads; EEM 2 % |
| 5 | https://sopro.io/results/success-stories/on-device | ABIERTA | 34 leads/mes, 725 conversaciones |
| 6 | https://sopro.io/solutions/appointment-setting-services/ | ABIERTA | "flujo de reuniones en 4-6 semanas"; sin show rate |
| 7 | https://belkins.io/blog/cold-email-response-rates | ABIERTA | 7,5 M emails 2025, 0,45 % respuesta, por tamaño/seniority/industria, metodología |
| 8 | https://belkins.io/blog/sales-follow-up-statistics | ABIERTA | Respuesta y cita por paso; email 50 % / llamadas 33,6 % de citas; LinkedIn 7 %+ |
| 9 | https://belkins.io/case-studies/industry/manufacturing | ABIERTA | 11 casos manufactura y promesas medias |
| 10 | https://belkins.io/case-studies/lead-generation-for-bulk-bag-manufacturer | ABIERTA | BAG Corp: 10.780 contactos → 91 citas (0,84 %) |
| 11 | https://belkins.io/case-studies/lead-generation-for-industrial-iot-solutions-manufacturer | ABIERTA | AMI Global: 6.700 contactos → 101 citas (1,5 %) |
| 12 | https://belkins.io/case-studies/lead-generation-for-thermal-management-products-manufacturer | ABIERTA | Sekisui: 800 leads → 21 citas |
| 13 | https://belkins.io/case-studies/lead-generation-for-wireless-connectivity-products-manufacturer | ABIERTA | Smartrek: 1.000 leads → 15 citas, 1 no-show |
| 14 | https://belkins.io/case-studies/omnichannel-lead-generation-for-a-signage-manufacturer | ABIERTA | Señalización: 6.000+ contactos → 17 citas; 4 citas/mes |
| 15 | https://belkins.io/case-studies/lead-generation-for-prefabricated-building-manufacturer | ABIERTA | Deluxe Modular: 30+ citas en 3 meses |
| 16 | https://belkins.io/case-studies/lead-generation-for-clean-energy-storage-manufacturer | ABIERTA | Lion Energy: 137 citas en 10 meses |
| 17 | https://www.cience.com/case-studies | ABIERTA | Listado (3 casos Industrial Automation) |
| 18 | https://www.cience.com/case-studies/cb-pacific | ABIERTA | CB Pacific: 5.000 emails + 3.000 llamadas → 300+ citas en 3 años |
| 19 | https://martal.ca/case-studies/ | ABIERTA | Sin caso industrial con cifras |
| 20 | https://clutch.co/go-to-review/martal-group/119026 | FRAGMENTO (Cloudflare) | Fabricante 51-200: "1-2 citas/semana, luego se apagó" |
| 21 | https://www.salesforge.ai/blog/martal-group-review | ABIERTA | Crítica: casos miden prospectos, no ventas; calibración 2-3 semanas |
| 22 | https://www.smartlead.ai/benchmarks/average-cold-email-reply-rate | ABIERTA | 850 M emails: mediana 0,74 %, percentiles |
| 23 | https://www.webtonic.io/blog/manufacturing-and-industrial-cold-email-outbound-statistics | ABIERTA | Recopila Instantly 3,43 %, Woodpecker 1,5 %, Belkins 0,45 % para industria |
| 24 | https://woodpecker.co/blog/cold-email-benchmarks/ | ABIERTA | 26.000 campañas; personalización ≈ 2x respuesta |
| 25 | https://www.cleverly.co/blog/cold-email-benchmarks-by-industry | ABIERTA | Positiva = 40-60 % de respuestas; reuniones/1.000 emails por tipo de deal |
| 26 | https://lemlist.com/blog/cold-email-benchmarks/ | ABIERTA | Bandas por industria sin muestra |
| 27 | https://lemlist.com/blog/cold-email-response-rate | ABIERTA | Bandas "bueno/excelente" |
| 28 | https://instantly.ai/blog/cold-email-statistics | ABIERTA | Estadísticas de asunto/seguimiento; sin industria |
| 29 | https://expandi.io/blog/linkedin-outreach-benchmarks/ | ABIERTA | 13,2 M peticiones; filas industriales (tabla 1.4) |
| 30 | https://expandi.io/blog/linkedin-outreach-benchmarks-2026/ | ABIERTA | Misma versión 2026 |
| 31 | https://www.chilipiper.com/post/will-aitken-guide-no-shows | ABIERTA | "no-show estándar 20 %"; outbound <5 % con recordatorios |
| 32 | https://www.chilipiper.com/customer-story/ordermygear | ABIERTA | No-show 20 % → 10 % |
| 33 | https://www.chilipiper.com/blog/improve-your-show-rates | ABIERTA | Consejos; sin muestra |
| 34 | https://www.revenuehero.io/blog/what-is-a-no-show-rate | ABIERTA | "20-40 %" rango de industria (estudio 6.428 reuniones sólo en búsqueda) |
| 35 | https://focus-digital.co/average-no-show-rate-for-booked-sales-meetings-by-booking-channel/ | ABIERTA | Outbound SDR 35-45 %; appointment setting externo 42 % (sin fuente primaria) |
| 36 | https://moderninbound.com/blog/cold-email-meeting-show-rate-2026 | ABIERTA | Operatix ~80 % asistencia; embudo 1.000 → 4-10 reuniones |
| 37 | https://www.ine.es/dyngs/Prensa/es/DIRCE2025.htm | ABIERTA | DIRCE 1-1-2025: industria 172.765; ≥20 asalariados 16.577 |
| 38 | https://www.ine.es/dyngs/Prensa/DIRCE2025.pdf | ABIERTA (PDF) | Tabla industria por tramos de asalariados |
| 39 | https://ipyme.org/Publicaciones/Retrato%20de%20la%20PYME/Retrato_Pyme_DIRCE_2024.pdf | ABIERTA (PDF) | % pequeñas 14,4 % y medianas 2,6 % en industria; pymes manufactureras por CNAE |
| 40 | https://ipyme.org/Publicaciones/Cifras%20PYME/CifrasPyme_diciembre_2025.pdf | ABIERTA (PDF) | 163.459 empresas industriales; empleo manufacturero por tramo; tamaño medio 13 |
| 41 | https://www.ine.es/dyngs/Prensa/es/ETICCE20241T2025.htm | ABIERTA (+PDF) | CRM 34,5 % en empresas 10+; industria: analítica 42,5 %, cloud 40,4 %, IA 17,5 % |
| 42 | https://amec.es/en/press-releases/amecs-international-industrial-companies-are-responding-strategically-to-the-challenges-of-the-new-era-of-globalization-and-foresee-growth-through-2025/ | ABIERTA | Exportaciones +5,43 %, 76,2 % prevé crecer, 55 % aumentó plantilla |
| 43 | https://amec.es/amecnews/notas-de-prensa/ | ABIERTA | Índice de notas; propensión exportadora 57 % (2026) |
| 44 | https://www.autonomosyemprendedor.es/articulo/pymes/asesorias-explican-que-muchas-pymes-han-logrado-crecer-ni-aumentar-ingresos-2025/20260116105321047816.html | ABIERTA | Informe HubSpot: captación y actividad comercial como retos |
| 45 | https://aspid.marketing/marketing-industrial-espana-guia-empresas-b2b/ | ABIERTA | Afirmación "ferias y boca a boca" sin dato; DESI 62 % vs 68 % |
| 46 | https://asest.es/story/b2b-empresarial-de-la-industria-manufacturera-de-exportacion/ | ABIERTA | Sin datos útiles |
| 47 | https://syncgtm.com/blog/best-sales-agencies-in-spain | ABIERTA | Agencias en España; ninguna con caso industrial cifrado |
| 48 | https://www.economistas.es/Contenido/Consejo/Estudios%20y%20trabajos/2025/Informe%20pyme%202025.pdf | FRAGMENTO (403) | Industria 46,5 % acceso a nuevos mercados; 13,2 % negocio exterior (2024) |
| 49 | https://www.fundacionsepi.es/wp-content/uploads/2026/02/LasEmpresasIndustriales2024.pdf | NO ABIERTA (TLS) | ESEE 2024, indicador de comercialización |
| 50 | https://www.boe.es/buscar/act.php?id=BOE-A-2002-13758 | ABIERTA | LSSI arts. 19-22, 38, 39 (texto literal) |
| 51 | https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673 | ABIERTA | LOPDGDD art. 19 (texto literal) |
| 52 | https://www.aepd.es/documento/2018-0173.pdf | ABIERTA (PDF) | Informe jurídico: art. 21 LSSI desplaza al interés legítimo |
| 53 | https://www.aepd.es/documento/e-02208-2018.pdf | ABIERTA (PDF) | Correos a directivos/trabajadores de una empresa = infracción 21.1; archivo por baja inmediata |
| 54 | https://www.aepd.es/es/documento/reposicion-00031-2019.pdf | ABIERTA (PDF) | Despacho → despacho: apercibimiento |
| 55 | https://www.aepd.es/documento/a-00011-2017.pdf | ABIERTA (PDF) | Créditos a pymes desde dominios secundarios: apercibimiento |
| 56 | https://www.aepd.es/documento/ps-00396-2022.pdf | ABIERTA (PDF) | Envíos tras baja: multa 200 €; definición de comunicación comercial |
| 57 | https://files.griddo.ecija.com/nota-informativa-circular-12023-vfinal.pdf | ABIERTA (PDF) | Circular 1/2023: interés legítimo para llamadas a personal de personas jurídicas (art. 19) + Lista Robinson |
| 58 | https://www.garrigues.com/es_ES/noticia/listas-robinson-las-empresas-deben-revisar-sus-procedimientos-internos-para-el-envio-de | ABIERTA | Obligación de consultar Lista Robinson bajo interés legítimo |
| 59 | https://www.prodat.es/blog/utilizan-los-datos-personales-del-ticket-de-compra-para-el-envio-de-publicidad-sin-consentimiento-previo/ | ABIERTA | Multa 20.000 € art. 21 (textil, B2C) |
| 60 | https://www.genbeta.com/actualidad/que-te-envien-correos-publicidad-que-te-dejen-rechazarlos-puede-salir-caro-a-quien-envia-aepd-multa | ABIERTA | Multa 800 € a recopilador sectorial (2022) |
| 61 | https://www.fieldfisher.com/es-es/locations/spain/insights/bases-datos-empresariales | FRAGMENTO (403) | Art. 19 no ampara envíos B2B; resoluciones 2025 sobre censos |
| 62 | https://overloop.com/es/blog/b2b-cold-email-espana-rgpd-aepd | ABIERTA | Guía de proveedor: RGPD ≠ permiso LSSI; receta de cumplimiento |
| 63 | https://www.leadgenius.com/resources/best-b2b-data-provider-for-spain-aepd-lssi-ce-and-lista-robinson-compliance | ABIERTA | "Uno de los regímenes más estrictos de la UE"; doble opt-in |
| 64 | https://danishleadco.io/cold-email-blog/before-you-hire-a-cold-email-agency-read-this | ABIERTA | Dominios secundarios, volumen, cualificación, qué preguntar a una agencia |
| 65 | https://www.trustpilot.com/review/sopro.io ; https://www.trustpilot.com/review/weprospectify.com ; https://de.trustpilot.com/review/dealforce.io | FRAGMENTO (403) | Reseñas negativas sobre cualificación y cobro por reunión |
| 66 | https://clutch.co/profile/sol-media-solutions | FRAGMENTO (403) | Agencia española: "3.500+ reuniones para 55 empresas", dominios dedicados |
