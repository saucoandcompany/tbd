# Benchmarks de prospección B2B en frío (H7, H8, H9) — verificación adversarial

Fecha: 22-10-2026. Método: 50+ páginas abiertas con `tools/pwfetch.js` (HTTP directo o Chromium) y `curl` para el PDF de Mailshake. Marcas: **[ABIERTA]** = página leída entera; **[FRAGMENTO]** = sólo extracto o cita indirecta; **NO ENCONTRADO** = buscado y no localizado. La búsqueda web se agotó (cuota de sesión) tras ~25 consultas; todo lo que sigue procede de páginas abiertas.

Advertencia metodológica transversal: casi todos los benchmarks son de proveedores de software/agencias con interés comercial. La cifra "3,43 %" que repiten Woodpecker, lemlist, Martal, Cleverly y Webtonic **es una sola fuente (Instantly 2026) recirculada**, no cinco confirmaciones independientes. Hay que distinguir siempre el denominador: respuestas / correos enviados (Belkins) ≠ respuestas / contactos (Smartlead, Hunter, Saleshandy) ≠ respuestas / aperturas.

---

## H7. Tasa de respuesta 6 % (base) / 2 % / 9 %; apertura 45 %; entregabilidad 95 %

### Datos abiertos, con muestra

| Fuente (año datos) | Muestra | Métrica exacta | Valor |
|---|---|---|---|
| **Belkins, estudio 2026** [ABIERTA] | 7.530.489 correos, 34.393 respuestas, 2025, campañas de clientes (EE. UU. 5,6 M, UK 370 k, Canadá 266 k, Polonia 46 k) | Respuestas únicas ÷ **correos enviados** (sin autorespuestas ni rebotes); tracking de apertura desactivado | **0,45 %** media; 0,54 % feb → 0,35 % dic; fundadores 0,57 %, C-level 0,42 %, VPs 0,32 %; empresas 0-10 empl. 0,72 %, 11-50 0,49 %, 10.000+ 0,22 %; Construcción/Finanzas/Salud/Legal 0,56-0,60 %; Food & Beverage 3,47 %; Banca y Seguros las peores. **1.200 reuniones sobre 7,5 M correos (0,016 % por correo; 3,5 % de las respuestas)** |
| Belkins, follow-up 2026 [ABIERTA] | mismos 7,5 M | Por paso | Paso 1: 0,59 %; los seguimientos aportan el 58,6 % de las respuestas; el paso 3 genera más reuniones que 1+2; 53 % de reuniones desde el paso ≥3 |
| Belkins 2023 [ABIERTA] | 11 M correos, 90+ industrias | Apertura / respuesta por campaña | 36 % apertura, **7 %** respuesta; 1,7 % sin personalizar; campañas de 240-499 personas 10 %; 3 pasos 9,2 % |
| **Smartlead benchmarks** [ABIERTA] | >850 M correos; sólo remitentes con ≥500 envíos; **mediana**, no media | Respuestas ÷ **contactos** | **Mediana 0,74 %** (1 respuesta/135 contactos); top 25 % 1,43 %; top 10 % 2,63 %; top 5 % 3,85 %; bottom 25 % 0,37 %. Por paso: email 1 1,18 %, email 2 0,73 %, email 3 0,56 %, email 7 0,33 %; secuencia de 3 → 25 respuestas/1.000 contactos, de 5 → 33. Campaña mediana 499 leads ≈ 4 respuestas. Rebote mediano 1,54 % (25 % de remitentes >3,21 %). Verificados SPF/DKIM/DMARC 108 contactos/respuesta vs 120 sin verificar |
| **Instantly, informe 2026** [ABIERTA] | "miles de millones de interacciones, miles de workspaces", ene-dic 2025; sin cifra exacta de correos ni definición publicada del denominador (en otra página: "% de correos entregados que reciben respuesta") | Respuesta por campaña | **Media 3,43 %**; top 25 % ≥5,5 %; top 10 % ≥10,7 %; 58 % de respuestas en el paso 1; <80 palabras; secuencia 4-7 pasos; rebote <2 % |
| Hunter, State of Cold Email 2025 [ABIERTA] | 11 M correos 2024 + encuesta a 217 decisores | Respuesta media por campaña | **4,1 %**; campañas ≤50 destinatarios **5,8 %** vs 1.000+ **2,1 %**; con seguimientos 4,9 % vs 3 % sin; Outlook dominio propio 5,9 %; correlación longitud-respuesta −0,09 |
| Saleshandy 2026 [ABIERTA] | 30,31 M correos, 2.906 cuentas, ~39.800 buzones (la página mezcla "ene-jun 2026" y "jul-oct 2026") | Respuesta por campaña | **4,5 %** media; campañas medias 3-10 %; top 5 % 11-15 %; top 1 % 15-30 %; apertura media 21 %; secuencias <200 prospectos ≈2× respuestas; 57 % de respuestas positivas vienen de seguimientos; **2-3 reuniones/100 correos en las mejores campañas** |
| Woodpecker, cuántos correos/día [ABIERTA] | 7.676 buzones con ≥500 envíos en 90 días | Mediana de respuesta según volumen diario del buzón | **1-20/día: 2,0 %**; 21-50: 1,2 %; 51-100: 0,9 %; 101-200: 0,5 %; 201-500: 0,4 % |
| Woodpecker, estadísticas 2026 [ABIERTA] | ">20 M correos" (sin detalle) | Media | Repite el 3,43 % de Instantly; "5,1 % en 2024"; 3-5 pasos 8,3 % vs 4,1 % sin seguimiento; personalización avanzada 17-18 % vs 7-9 %. Atribuye erróneamente a "Belkins 16,5 M" el dato 5,8 %/2,1 % que es de Hunter → señal de reciclaje de cifras |
| **Sopro, Performance by industry** [ABIERTA, Chromium] | 792 campañas, 4.505.098 empresas, 9.330.012 prospectos, 36,4 M "engagements" (agencia UK, actualizado en vivo 22-10-26) | **Lead % = leads ÷ empresas contactadas** (lead = respuesta positiva/interés; definición exacta no publicada en la página) | Global **2,01 %**; **Oil & Energy 3,78 %; Utilities 3,82 %; Renewables & Environment 3,57 %; Construcción 3,03 %; Mining & Metals 5,69 %; Chemicals 3,46 %; Civil Engineering 3,68 %; Manufacturing 1,82 %; Electrical/Electronic Mfg 1,82 %; Industrial Automation 1,91 %; Machinery 2,12 %; Mechanical/Industrial Engineering 2,18 %; Logistics 2,26 %; Automotive 1,97 %**. Por tamaño: 1-10 empl. 1,19 % → 10.001+ 5,79 % (sentido inverso a Belkins; Sopro cuenta por empresa y multihilo) |
| Sopro, State of Prospecting 2026 [FRAGMENTO: landing] | 442 decisores + 151 M touchpoints; benchmarks sobre 30 M mensajes, 82 industrias | — | El PDF requiere registro. Emailchaser (abierta) le atribuye "≈5,1 % respuesta media, mayoría 1-5 %" — no verificable |
| Mailshake, State of Cold Email 2025 [ABIERTA, PDF] | Encuesta a 508 profesionales (no datos de plataforma) | Autodeclarado | **40 % reporta 1-4 %; 21 % <1 %; sólo 16 % >5 %**; apertura declarada mayoritaria 10-30 %; 69 % dice que su rendimiento cayó interanual; 48 % rebote 2-5 % |
| Backlinko/Pitchbox 2019 [ABIERTA] | 12 M correos de **link building**, no ventas | Respuesta | 8,5 % (origen del "8,5 %" que circula; no aplicable a B2B comercial) |
| Snov.io (ES) [ABIERTA] | 44 M correos feb-mar 2025 | Respuesta | Desactivar tracking de aperturas: 1,08 % → 2,36 %; apertura personalizada 20,79 % vs 14,96 % |
| Apollo, guía de benchmarks 2026 [ABIERTA] | Sin muestra (agregación de terceros) | Rangos | Respuesta media 3-5,8 %, buena 8-10 %; apertura 21-28 % "sólo direccional"; inbox placement objetivo ≥85 %; **positivas ≥40 % de las respuestas = verde, <20 % = rojo**; reuniones/1.000 envíos ≥3 verde, <1 rojo; spam <0,1 % |
| Cleverly 2026 [ABIERTA] | Agregado ">100 M" sin detalle | Rangos | Conversión a reunión 0,2-2 %; bien dirigidas 1-3 reuniones/100 correos; positiva→reunión 40-60 %; inbox placement global 83-84 %; cita Mailshake 1,37 M correos → 2,09 % |
| Gong [ABIERTA] | Sin muestra en la página | Reuniones | Lenguaje de ROI −15 %; "interest CTA" mejor que pedir reunión; sin tasa de respuesta |
| Martal, Webtonic, lemlist, SomethingInc [ABIERTAS] | Recopilaciones | — | Reciclan Instantly 3,43 %, Belkins 0,45 %, Woodpecker "mediana 1,5 % en 56.614 campañas" (no verificada en Woodpecker). SomethingInc: la diferencia 0,45 % vs 8,3 % es de denominador, "18×" |

### Desglose sectorial industria/energía
- Sopro es la **única** fuente abierta con filas industriales y muestra: energía/utilities/renovables 3,6-3,8 % de **empresas** con lead (respuesta positiva, multicanal, multihilo, agencia UK); fabricación/maquinaria/ingeniería industrial 1,8-2,2 %.
- Belkins 2026 sólo publica el sector en gráficos (imágenes): Construcción 0,56-0,60 % por correo; no hay fila de manufactura/energía en texto. **NO ENCONTRADO** desglose energía/industrial en Instantly, Smartlead, Hunter, Saleshandy (SaaS "la más receptiva").
- España: **NO ENCONTRADO** ningún estudio con muestra (Ringover: nada; Snov.io ES es traducción de datos globales; Belkins por país lista Polonia 1,43 %, Canadá 0,63 %, EE. UU. 0,51 %, UK 0,48 %, sin España). Warmy ES repite "5,1 %" sin muestra.

### Apertura y entregabilidad
- Apertura: Belkins **dejó de medirla** en 2025 ("el píxel dañaba la entregabilidad"); Hunter aconseja ignorarla; Apollo "sólo direccional" 21-28 % media; Saleshandy 21 %; Instantly/Martal 27,7 %; Mailshake (encuesta) mayoría 10-30 %. Apple MPP infla (~49 % de aperturas rastreadas según Cleverly). Snov: quitar el píxel **duplica** la respuesta.
- Entregabilidad: Saleshandy "Google Workspace entrega el 97 %" (entrega, no bandeja); Cleverly/Martal "17 % nunca llega a la bandeja", placement global 83-84 %; Apollo objetivo IPR ≥85 %; Smartlead rebote mediano 1,54 %; Warmup Inbox 95-98 % de inbox rate **para correos de warm-up** (no de campaña).

### Veredicto H7
**DESTRUIDA en su cifra base.** 6 % de respuesta como escenario base no lo sostiene ninguna muestra grande: la mediana por contacto es 0,74 % (Smartlead, 850 M), la media por campaña 3,4-4,5 % (Instantly s/muestra; Hunter 11 M; Saleshandy 30 M), y por correo enviado 0,45 % (Belkins 7,5 M). El 6 % sólo aparece como "campaña pequeña y muy segmentada" (Hunter ≤50 destinatarios 5,8 %; Woodpecker buzón a 1-20/día 2,0 % mediana) o en el top 10-25 %.
- **Cifras corregidas (respuestas de cualquier signo ÷ contactos, secuencia completa de 3-4 pasos, lista <200, verificada, buzón a ≤25/día):** pesimista **1 %**, base **2,5-3 %**, optimista **5-6 %** (top-quartile Instantly 5,5 %, Hunter ≤50 destinatarios 5,8 %).
- **Respuesta positiva:** ~40 % de las respuestas (Apollo verde; Saleshandy "57 % de positivas de seguimientos") → base **~1 % de contactos**; Sopro energía/utilities **3,6-3,8 % de empresas** con lead tras campaña multicanal de agencia (techo optimista para positivas).
- **Reuniones:** 0,5-1 por 100 contactos base (Cleverly 0,2-2 %; Saleshandy 2-3/100 sólo en top; Belkins 3,5 % de las respuestas → reunión en volumen alto).
- **Apertura 45 %:** reemplazar por "no medir" (Belkins/Hunter) o, si se mide, base **25-30 %**; 45 % es el umbral "bueno/elite" (Apollo 35-45 % buena).
- **Entregabilidad 95 %:** aceptable como **tasa de entrega** (no rebote) con lista verificada (rebote <2 %); la **colocación en bandeja** real es ~85 %, así que planificar 85 % de correos vistos.

---

## H8. 25 correos/día por buzón; calentamiento 2 semanas; SPF/DKIM/DMARC obligatorios; Google/Yahoo 2024: autenticación y spam <0,3 % para masivos

### Reglas oficiales (texto literal, páginas abiertas)
**Google, Email sender guidelines** (support.google.com/a/answer/81126) [ABIERTA]:
- "Starting February 1, 2024, all email senders who send email to Gmail accounts must meet the requirements in this section": "Set up SPF **or** DKIM"; "valid forward and reverse DNS records"; "Use a TLS connection"; "**Keep spam rates reported in Postmaster Tools below 0.3%**"; RFC 5322; no suplantar From de Gmail.
- "Requirements for sending 5,000 or more messages per day": "Set up SPF **and** DKIM"; "Set up DMARC … Your DMARC enforcement policy can be set to none"; alineación del From con SPF o DKIM; "Marketing messages and subscribed messages must support **one-click unsubscribe**, and include a clearly visible unsubscribe link"; cabeceras `List-Unsubscribe-Post: List-Unsubscribe=One-Click` y `List-Unsubscribe:` (RFC 8058).
- "Increase sending volume slowly"; "Start with a low sending volume to engaged users, and slowly increase the volume over time."
- DKIM ≥1024 bits (recomendado 2048) para enviar a Gmail personal.

**Google, Email sender guidelines FAQ** (support.google.com/a/answer/14229414) [ABIERTA]:
- "A bulk sender is any email sender that sends **close to 5,000 messages or more to personal Gmail accounts within a 24-hour period**. Messages sent from the same primary domain count toward the 5,000 limit." "Senders who meet the above criteria at least once are **permanently** considered bulk senders."
- "The Email sender guidelines **don't apply to messages sent to Google Workspace accounts**. Sender requirements and Google enforcement apply only when sending email to personal Gmail accounts." (Relevante: destinatarios B2B con dominio corporativo no cuentan.)
- "**Starting November 2025**, Gmail is ramping up its enforcement on non-compliant traffic. Messages that fail … will experience disruptions, including temporary and permanent rejections."
- Spam: "keep your user-reported spam rate **below 0.1%** and prevent it from reaching 0.3% or higher"; "Spam rate is calculated daily"; "Beginning June 2024, bulk senders with a user-reported spam rate greater than 0.3% will be ineligible for mitigation"; elegibles de nuevo tras 7 días consecutivos <0,3 %. Tabla de enforcement: sin SPF+DKIM / sin alineación / sin TLS / sin PTR → "Temporary or Permanent Failure codes, or spam foldering"; spam >0,3 %, sin DMARC, sin one-click → "Delivery support or mitigations unavailable". Bajas deben honrarse en 48 h.

**Google Workspace, Gmail sending limits** (support.google.com/a/answer/166852) [ABIERTA]:
- "Daily sending limit per user account: **2,000**; 1,500 for mail merge; **500 for trial accounts**"; "Recipients per message: 2,000 total (maximum of 500 external)"; "Total recipients per day: 10,000"; "**External recipients per day: 3,000**"; "Unique recipients per day: 3,000 (2,000 external; 500 external for trial accounts)". Los límites de cuenta de prueba suben cuando el dominio ha pagado ≥100 USD acumulados.

**Yahoo, Sender Requirements & Best Practices** (senders.yahooinc.com) [ABIERTA]:
- Todos: "Implement SPF or DKIM at a minimum"; "Keep your spam rate below 0.3%"; DNS directo/inverso; RFC 5321/5322.
- Bulk: "Implement both SPF & DKIM"; "Publish a valid DMARC policy with at least p=none - DMARC must pass"; alineación relajada aceptable; "list-unsubscribe header, which supports one-click unsubscribe for marketing and subscribed messages"; "Honor unsubscribes within 2 days"; spam rate "calculated … based on mail delivered to the inbox".
- FAQ [ABIERTA]: "A 'bulk' sender is classified as an email sender sending a significant volume of mail. **We will not specify a volume threshold.**" Enforcement desde febrero 2024.

### Volumen diario por buzón (datos medidos vs opinión)
| Fuente | Tipo | Dato |
|---|---|---|
| Smartlead [ABIERTA] | **Medido**, 850 M correos | Mediana **14 correos fríos/día por buzón**; 50 % de buzones entre 8 y 24; 10 % más activo ≥42; 5 % ≥70; guía Smartlead ≤50/día; cuenta típica 20 buzones |
| Woodpecker [ABIERTA] | **Medido**, 7.676 buzones | Respuesta mediana cae con el volumen: 1-20/día 2,0 % → 21-50 1,2 % → 51-100 0,9 %; recomienda 25-35/día, nunca >50 |
| Mailreach [ABIERTA ×2] | Opinión de proveedor | Techo ~100/día en Workspace/M365 ("ceiling, not target"); dominios nuevos empezar 20-30/día; SMTP propio 20-50 |
| lemlist help [ABIERTA] | Opinión/config | Buzón nuevo 30-40/día; lemwarm al volumen objetivo; lemlist a 0 durante warm-up |
| Instantly 2026 [ABIERTA] | Opinión | "Starting slow with 5-10 emails per day initially, then gradually increasing over 4-6 weeks" |
| Google [ABIERTA] | Oficial | 2.000/día (500 en prueba) — límite técnico, no de reputación |

### Duración del calentamiento
| Fuente | Tipo | Dato |
|---|---|---|
| Instantly help "When your account is ready" [ABIERTA] | Regla de producto | "**At least 2 weeks of warmup**" (3 para AirMail) y "Health Score above 90 %" (inbox rate de los warm-ups en 7 días). Ajustes por defecto: +1/día hasta límite 10/día, 30 % respuestas |
| lemlist help lemwarm [ABIERTA] | Regla de producto | "Ramp-up takes about **40 days at +1/day, then 14 days of stabilization** … before the first campaign" para buzón nuevo a 30-40/día (≈8 semanas) |
| Smartlead [ABIERTA] | **Medido** | Media observada **8,0 días** de warm-up antes de la primera campaña (9,4 un año antes); "it is what the average sender does, not a proven minimum"; warm-ups llegan a bandeja ~99 % |
| Warmup Inbox "Is email warmup dead" [ABIERTA] | **Medido**, 17.247 buzones | Inbox rate mediano **95,17 % semana 1 → 97,93 % semana 2**; dispersión 6,5 puntos en semana 1 → 1 punto en semana 12; caída detectada <3 días se recupera en 7-9 días; ≥15 días degradado → 57-74 días y ~51 % de probabilidad de recuperación total; Gmail es el primero en marcar spam en 85 % de casos. Enforcement Gmail nov-2025: spam rate se duplicó, 16 semanas de recuperación |
| Warmy [ABIERTA] | Opinión | 5/día días 1-5; 10-15 días 6-14; 50+ días 15-25; "warmed" ~día 45 |
| Cleverly [ABIERTA] | Opinión | 2-4 semanas |
| Mailreach | — | NO ENCONTRADO artículo propio de duración (404) |

### Veredicto H8
**CONFIRMADA con matices.**
- **25/día por buzón: CONFIRMADO y conservador.** La mediana real es 14/día (Smartlead, 850 M); la respuesta mediana se mantiene en 2 % hasta 20/día y cae a 1,2 % en 21-50 (Woodpecker, 7.676 buzones). Recomendación corregida: **15-25 nuevos/día por buzón, ≤50 como techo absoluto**, y escalar con buzones, no con volumen.
- **2 semanas de calentamiento: es el mínimo de producto (Instantly), no un dato medido.** El único dato medido (Warmup Inbox) muestra mejora hasta la semana 2 y convergencia hacia la 12; lemlist pide ~8 semanas para un buzón nuevo; la media observada en Smartlead es 8 días (sin prueba de suficiencia). Corregido: **3 semanas mínimo para dominio nuevo + warm-up continuo** (lemwarm residual 10/día), con la primera semana de campaña a 5-10/día.
- **SPF/DKIM/DMARC "obligatorios":** literalmente Google exige SPF **o** DKIM a todos y SPF+DKIM+DMARC(p=none)+one-click sólo a ≥5.000/día a **Gmail personal** (Yahoo: sin umbral numérico). Con 25/día a dominios corporativos **no se es remitente masivo**; pero los tres son necesarios en la práctica (Smartlead: 108 vs 120 contactos/respuesta; tabla de enforcement de Google trata la falta de alineación como rechazo). Mantener.
- **Spam <0,3 %:** correcto, pero el objetivo operativo de Google es **<0,1 %**; a 25/día una sola queja = 4 % de un día → la métrica diaria es muy ruidosa en volumen bajo. One-click unsubscribe sólo es exigible a marketing/suscripción masiva; aun así, incluir enlace de baja. Fecha "2024" correcta; añadir **enforcement duro desde noviembre 2025**.
- Cuenta de prueba de Workspace: 500/día y 500 externos únicos/día; irrelevante para 25/día pero conviene saldar los 100 USD antes de escalar buzones.

---

## H9. LinkedIn: aceptación 20-30 %; respuesta a mensaje 5-10 %; límites semanales

| Fuente | Muestra | Métrica | Valor |
|---|---|---|---|
| **Expandi, State of LinkedIn Outreach H2 2026** [ABIERTA ×2] | **13.218.869 invitaciones, 6.730.447 mensajes, 3.766.161 aceptaciones, 13.302 cuentas, may-2025 → abr-2026** | Aceptación / respuesta a nota de invitación / respuesta a mensaje (a conexiones aceptadas) | **28,5 % / 3,0 % / 10,4 %**. Por industria (≥50 cuentas): 21,8 % (Telecom) a 36,5 % (Staffing); Facilities Services 23,2 %; Software 2,8 % / 8,8 %; Civil Engineering 39,9 % y 25,5 % pero **sólo 13 cuentas**. Secuencias de 3 mensajes 9,8 %; ≥5 mensajes 5,0 %; envío 7-11 h ~32 % vs 24 % tarde; mensajes 150-200 caracteres 8,5 %; IA hiperpersonalizada −12 % aceptación. H1: 29,6 % en 70.130 campañas |
| SmartReach, State of LinkedIn Outreach 2026 [ABIERTA] | 1.800+ campañas, 160+ empresas, 480+ reps, **500 k+ invitaciones, 460 k+ mensajes**, ene-jun 2026 | Aceptación | **26 %** media; top cuartil 40 %+; **80 % de los que aceptan nunca responden**; **1,3 % de los aceptados → reunión**; cita HeyReach 21 % (96 k campañas) y Belkins 18,7 % (14 k contactos); "~100/week LinkedIn's invitation allowance for every account type" |
| Belkins follow-up 2026 [ABIERTA] | Datos Expandi "15 M contactos" | Respuesta LinkedIn como canal de seguimiento | 7 %+ estable todo 2025; Messenger 12,22 %, Connector 7,95 %, Builder 5,37 %; 26,4 % aceptación (estudio 2025, citado) |
| Waalaxy [ABIERTA] | Caso de 483 prospectos (2022) | — | 51 % aceptación/14,5 % respuesta: caso aislado, no benchmark; límite "~200/semana" (2022, obsoleto) |
| Dripify | — | NO ENCONTRADO dato con muestra (sólo claims comparativos) |
| LinkedIn Sales Solutions | — | NO ENCONTRADO benchmark propio de aceptación |

**Límites de invitaciones (2025-2026):**
- LinkedIn Help "Types of restrictions for sending invitations" (answer/4800) [ABIERTA]: "All LinkedIn members (Basic and Premium) are subject to invitation limits and restrictions"; causas: "many invitations within a short amount of time", "ignored, left pending, or marked as spam", sospecha de automatización; red máx. 30.000; tras retirar una invitación no se puede reenviar en 3 semanas. **No publica ningún número semanal.**
- LinkedIn Help "Invitation limit reached" (billing/answer/a550555) [ABIERTA]: "This restriction typically lasts one week"; retirar pendientes no la levanta; soporte no revela el motivo.
- LinkedIn Help "Connecting with other members" (answer/62928) [ABIERTA]: reincidencia → exigir e-mail del destinatario permanentemente.
- Cifra observada (no oficial): **~100/semana en ventana móvil de 7 días** (Hublead, Cleverly, Overloop, SmartReach — todas [ABIERTAS]); cuentas nuevas 50-80; Sales Navigator/SSI alto 150-250 según Cleverly (sin fuente); Overloop: "Premium y Sales Navigator no suben significativamente el tope". Mantener <500 pendientes (Cleverly) / <300 (Hublead); invitaciones con nota personalizada limitadas a ~5-10/mes en cuentas gratuitas (Cleverly, sin fuente oficial).

### Veredicto H9
**CONFIRMADA.** Aceptación 20-30 %: centro **26-28,5 %** (Expandi 13,2 M; SmartReach 500 k), rango por industria 20-36 %; para industria/energía no hay fila fiable (Civil Engineering 39,9 % con 13 cuentas no vale). Respuesta a mensaje 5-10 %: la media de Expandi es **10,4 % por mensaje enviado a conexiones aceptadas** (6,7 M), pero la nota de invitación sólo obtiene 3,0 % y el 80 % de aceptados no responde nunca; **por invitación enviada ≈ 28,5 % × 10,4 % ≈ 3 % de conversaciones**, y 1,3 % de aceptados → reunión (SmartReach). Corregido: aceptación **25 %** base, respuesta **8 %** por mensaje post-aceptación, **~2-3 % de invitaciones acaban en conversación**. Límite: planificar **≤80 invitaciones/semana** (margen bajo el ~100 observado; LinkedIn no publica cifra y bloquea ~1 semana).

---

## Resumen de cifras corregidas para el plan

| Parámetro | Hipótesis | Corregido | Fuente principal (muestra) |
|---|---|---|---|
| Respuesta (cualquier signo) ÷ contactos, secuencia 3-4 pasos | 6 % / 2 % / 9 % | **2,5-3 % / 1 % / 5-6 %** | Smartlead mediana 0,74 % (850 M); Hunter 4,1 %, ≤50 dest. 5,8 % (11 M); Instantly 3,43 % (s/muestra); Belkins 0,45 %/correo (7,5 M) |
| Respuesta positiva | — | **~1 % de contactos** (40 % de respuestas) | Apollo (umbral), Sopro energía/utilities 3,6-3,8 % de empresas (4,5 M empresas) |
| Reuniones | — | **0,5-1 / 100 contactos** | Cleverly 0,2-2 %; Saleshandy 2-3/100 top (30 M) |
| Apertura | 45 % | **No medir**; si se mide, 25-30 % | Belkins (tracking off), Apollo 21-28 %, Snov 44 M |
| Entregabilidad | 95 % | **95-98 % entrega; ~85 % bandeja** | Smartlead rebote 1,54 %; Cleverly/Apollo IPR 83-85 % |
| Envíos/día/buzón | 25 | **15-25, techo 50** | Smartlead mediana 14 (850 M); Woodpecker 7.676 buzones |
| Calentamiento | 2 semanas | **3 semanas mínimo + continuo** | Instantly ≥2 sem (regla); Warmup Inbox 17.247 buzones; lemlist ~8 sem |
| Autenticación | SPF+DKIM+DMARC obligatorios | Obligatorio legalmente sólo SPF o DKIM (<5.000/día a Gmail personal); **hacer los tres igualmente** | Google 81126 / 14229414 |
| Spam | <0,3 % | **<0,1 % objetivo, 0,3 % tope** | Google FAQ |
| LinkedIn aceptación | 20-30 % | **25 %** | Expandi 13,2 M; SmartReach 500 k |
| LinkedIn respuesta | 5-10 % | **8 % por mensaje post-aceptación; 2-3 % por invitación** | Expandi 6,7 M mensajes |
| LinkedIn invitaciones/semana | — | **≤80** (100 observado, no oficial) | LinkedIn Help 4800/a550555 (sin cifra) |

---

## URLs abiertas

| # | Fuente | URL | Estado |
|---|---|---|---|
| 1 | Google — Email sender guidelines | https://support.google.com/a/answer/81126?hl=en | ABIERTA |
| 2 | Google — Sender guidelines FAQ (bulk sender, spam rate, enforcement nov-2025) | https://support.google.com/a/answer/14229414?hl=en | ABIERTA |
| 3 | Google — Gmail sending limits in Google Workspace | https://support.google.com/a/answer/166852?hl=en | ABIERTA |
| 4 | Yahoo — Sender Requirements & Best Practices | https://senders.yahooinc.com/best-practices/ | ABIERTA |
| 5 | Yahoo — Sender FAQ | https://senders.yahooinc.com/faqs/ | ABIERTA |
| 6 | Belkins — Cold email response rates, estudio 2026 (7,5 M) | https://belkins.io/blog/cold-email-response-rates (versión .md) | ABIERTA |
| 7 | Belkins — Sales follow-up statistics 2026 | https://belkins.io/blog/sales-follow-up-statistics | ABIERTA |
| 8 | Belkins — B2B cold email benchmarks 2023 (11 M) | https://belkins.io/resources/b2b-cold-email-benchmarks | ABIERTA |
| 9 | Instantly — Cold Email Benchmark Report 2026 | https://instantly.ai/cold-email-benchmark-report-2026 | ABIERTA |
| 10 | Instantly — report page (misma edición) | https://instantly.ai/report-page | ABIERTA |
| 11 | Instantly — Cold email reply rate benchmarks | https://instantly.ai/blog/cold-email-reply-rate-benchmarks | ABIERTA |
| 12 | Instantly — Cold email statistics | https://instantly.ai/blog/cold-email-statistics | ABIERTA |
| 13 | Instantly Help — When your email account is ready for campaigns | https://help.instantly.ai/en/articles/13938078-when-your-email-account-is-ready-for-campaigns | ABIERTA |
| 14 | Instantly Help — Warmup settings | https://help.instantly.ai/en/articles/7988514-warmup-settings-explained | ABIERTA |
| 15 | Smartlead — Reply rate benchmark (850 M) | https://www.smartlead.ai/benchmarks/average-cold-email-reply-rate | ABIERTA |
| 16 | Smartlead — State of Cold Email 2026 | https://www.smartlead.ai/benchmarks | ABIERTA |
| 17 | Smartlead — Cold emails per day per mailbox | https://www.smartlead.ai/benchmarks/how-many-cold-emails-per-day-per-mailbox | ABIERTA |
| 18 | Smartlead — How long to warm up | https://www.smartlead.ai/benchmarks/how-long-to-warm-up-email-before-cold-outreach | ABIERTA |
| 19 | Smartlead — Do follow-ups work | https://www.smartlead.ai/benchmarks/do-cold-email-follow-ups-work | ABIERTA |
| 20 | Smartlead — Campaign size | https://www.smartlead.ai/benchmarks/average-cold-email-campaign-size | ABIERTA |
| 21 | Smartlead — Bounce rate | https://www.smartlead.ai/benchmarks/cold-email-bounce-rate | ABIERTA |
| 22 | Woodpecker — Cold email statistics 2026 | https://woodpecker.co/blog/cold-email-statistics/ | ABIERTA |
| 23 | Woodpecker — How many cold emails per day (7.676 buzones) | https://woodpecker.co/?p=14453 | ABIERTA |
| 24 | Woodpecker — Cold email reply rate | https://woodpecker.co/blog/cold-email-reply-rate/ | ABIERTA |
| 25 | lemlist — Cold email benchmarks 2026 | https://www.lemlist.com/blog/cold-email-benchmarks | ABIERTA |
| 26 | lemlist Help — How to set up and use lemwarm | https://help.lemlist.com/en/articles/14653207-how-to-set-up-and-use-lemwarm | ABIERTA |
| 27 | Mailreach — How many cold emails per day | https://www.mailreach.co/blog/how-many-cold-emails-to-send-per-day | ABIERTA |
| 28 | Mailreach — Email frequency best practices | https://www.mailreach.co/blog/email-frequency-best-practices | ABIERTA |
| 29 | Warmup Inbox — Is email warmup dead (17.247 buzones) | https://www.warmupinbox.com/blog/uncategorized/is-email-warmup-dead/ | ABIERTA |
| 30 | Warmup Inbox — Gmail policy change | https://www.warmupinbox.com/blog/uncategorized/gmail-policy-change/ | ABIERTA |
| 31 | Warmy — How long to warm up | https://www.warmy.io/blog/how-long-does-it-take-to-warm-up-email-or-domain/ | ABIERTA |
| 32 | Hunter — State of Cold Email 2025 (11 M) | https://hunter.io/the-state-of-cold-email-2025 | ABIERTA |
| 33 | Saleshandy — Cold email statistics 2026 (30,31 M) | https://saleshandy.com/blog/cold-email-statistics/ | ABIERTA |
| 34 | Mailshake — State of Cold Email 2025 (PDF, 508 encuestados) | https://assets.mailshake.com/wp-content/uploads/2025/04/16091740/Cold-Email-Report-2025-Mailshake.pdf | ABIERTA (curl) |
| 35 | Backlinko/Pitchbox — 12 M outreach emails (2019) | https://backlinko.com/email-outreach-study | ABIERTA |
| 36 | Sopro — Performance by industry (datos vivos) | https://sopro.io/results/interactive-insights/performance-by-industry | ABIERTA (Chromium) |
| 37 | Sopro — State of Prospecting 2026 (landing) | https://sopro.io/the-state-of-prospecting/ | FRAGMENTO (PDF tras registro) |
| 38 | Sopro — Whitepaper 2022 landing | https://sopro.io/resources/whitepapers/the-state-of-prospecting | FRAGMENTO |
| 39 | Apollo — How to benchmark outbound open and reply rates | https://www.apollo.io/insights/how-do-i-benchmark-my-outbound-email-open-and-reply-rates-against-industry-standards | ABIERTA |
| 40 | Gong — Cold email stats | https://www.gong.io/blog/cold-email-stats | ABIERTA |
| 41 | Cleverly — Cold email statistics 2026 | https://cleverly.co/blog/cold-email-statistics | ABIERTA |
| 42 | Cleverly — LinkedIn weekly invitation limit | https://www.cleverly.co/blog/bypass-linkedin-weekly-invitation-limit | ABIERTA |
| 43 | Martal — Cold emailing statistics 2026 | https://www.martal.ca/cold-emailing-statistics | ABIERTA |
| 44 | Webtonic — Manufacturing and industrial cold email data 2026 | https://www.webtonic.io/blog/manufacturing-and-industrial-cold-email-outbound-statistics | ABIERTA |
| 45 | SomethingInc — Why reply-rate studies disagree 18× | https://somethinginc.com/blog/cold-email-reply-rate-benchmark-contradiction/ | ABIERTA |
| 46 | SomethingInc — Cold email response rates 2026 data | https://somethinginc.com/blog/cold-email-response-rates-2026-data/ | ABIERTA |
| 47 | Emailchaser — Cold email statistics (cita Sopro 2026) | https://www.emailchaser.com/learn/cold-email-statistics | ABIERTA |
| 48 | Snov.io (ES) — Estadísticas de correo en frío 2026 | https://snov.io/blog/es/estadisticas-de-correos-electronicos-no-solicitados/ | ABIERTA |
| 49 | Expandi — LinkedIn outreach benchmarks 2026 (13,2 M) | https://expandi.io/blog/linkedin-outreach-benchmarks | ABIERTA |
| 50 | Expandi — State of LinkedIn Outreach H2 2026 | https://expandi.io/state-of-linkedin-outreach-h2-2026/ | ABIERTA |
| 51 | SmartReach — State of LinkedIn Outreach 2026 | https://smartreach.io/reports/state-of-linkedin-outreach/ | ABIERTA |
| 52 | Hublead — LinkedIn invitation limit 2026 | https://www.hublead.io/linkedin-invitation-limit | ABIERTA |
| 53 | Overloop — LinkedIn limits 2026 | https://overloop.com/blog/linkedin-limits | ABIERTA |
| 54 | Waalaxy — Weekly limit on invitations (2022) | https://blog.waalaxy.com/en/bypass-linkedin-limit/ | ABIERTA |
| 55 | LinkedIn Help — Types of restrictions for sending invitations | https://www.linkedin.com/help/linkedin/answer/4800 | ABIERTA |
| 56 | LinkedIn Help — Invitation limit reached | https://www.linkedin.com/help/billing/answer/a550555 | ABIERTA |
| 57 | LinkedIn Help — Connecting with other members, best practices | https://www.linkedin.com/help/linkedin/answer/62928 | ABIERTA |

NO ENCONTRADO (404 o inexistente): Apollo "State of Outbound" (no existe como informe; sólo la guía #39); Cognism cold-email statistics (404 en dos rutas); Reply.io benchmarks (404); Outreach/Salesloft/HubSpot benchmark con muestra de correo frío; Mailreach artículo de duración de warm-up; Dripify dato con muestra; LinkedIn Sales Solutions benchmark de aceptación; Ringover estudio España; cualquier estudio español o europeo industrial con muestra (lo más cercano: Sopro, agencia UK, y Belkins por país sin España).
