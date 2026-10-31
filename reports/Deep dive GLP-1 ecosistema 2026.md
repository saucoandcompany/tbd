# Deep dive: ecosistema GLP-1 como negocio para Jorge (31-10-2026)

Pregunta de Jorge: "Me gusta la del GLP y yo uso Mounjaro. Deep dive ahí."
Contexto fijo: sin capital, sin reuniones de venta, sin LinkedIn, lo que importa es el CAC, horizonte medio-largo, que no se comoditice con la IA, sin título sanitario ni de CAFyD, España, objetivo 60-100 k€ netos/año.

Base: cinco notas adversariales en `research_notes/GLP-1 ecosistema 2026/` (demanda y tamaño; evidencia clínica; competencia, precios y casos; legal y canales; monetización y CAC), unas 270 páginas abiertas en total, más los datos [INTERNO] del Planificador de Google Ads de tu sesión local. Marcas: [ABIERTA] página leída, [FRAGMENTO] solo extracto, [INTERNO] Planificador, [INTERPRETACIÓN] lectura propia, NO ENCONTRADO buscado sin resultado.

---

## 0. Veredicto en diez líneas

1. **El mercado es real y enorme en dinero, pero no en España ni en español.** Lilly facturó 10.723 M$ de Mounjaro solo en el tercer trimestre de 2026 [ABIERTA, 8-K SEC]. En España hay unos 500.000 usuarios para adelgazar (estimación de consultora, metodología no publicada) y la demanda de búsqueda en español es el 0,5-3 % de la inglesa [INTERNO + ABIERTA].
2. **Las dos cifras del texto externo son ciertas pero de una sola encuesta**: el 21 % de hogares de EE. UU. y el 85 % de usuarios que dicen que el apoyo es deficiente salen del estudio PwC/Numerator de mayo de 2026 (n=3.089) [ABIERTA vía eMarketer; el PDF de PwC dio 403].
3. **El "ángulo muerto" del músculo no existe desde junio de 2026.** Noom regala un GLP-1 Companion con módulo de fuerza, MyFitnessPal añadió soporte GLP-1 gratis en abril y hay más de 25 apps "GLP-1 muscle" lanzadas en 2026 en el App Store de EE. UU., todas con 0-9 valoraciones. Preserve tiene 0 valoraciones en EE. UU. y en España [ABIERTA, API iTunes].
4. **El hueco verificado es otro: salida del fármaco y mantenimiento sin fármaco.** Ningún grande publica un plan de salida. En español el autocompletado de Google ya pide "cómo dejar mounjaro sin efecto rebote" y "dieta mounjaro pdf español" [ABIERTA].
5. **La ciencia no te deja vender lo que el texto externo proponía.** No existe ningún ensayo aleatorizado de fuerza o proteína con semaglutida o tirzepatida; el único de tirzepatida y ejercicio fue retractado en 2025. La fuerza de agarre no cae a 12 meses. No puedes decir "pierdes músculo rápido", "el ejercicio lo evita" ni "dejarás el fármaco sin recuperar peso" [ABIERTA, PubMed/Europe PMC].
6. **Legalmente es el nicho más regulado del fitness.** Personas con obesidad o diabetes tratadas con fármaco son "población especial": en Madrid y Valencia su entrenamiento individual está reservado al Preparador Físico con grado CAFyD, y la pauta de proteína individualizada es acto propio del dietista-nutricionista (Ley 44/2003 art. 7.2.g, Código Penal art. 403) [ABIERTA, BOE].
7. **La captación de pago está cerrada en España.** Google Ads prohíbe nombrar Mounjaro, Ozempic, semaglutida o tirzepatida en anuncios y en la página de destino fuera de EE. UU., Canadá y Nueva Zelanda. Meta bloquea remarketing y Customer Match sobre audiencias de salud y bloquea el evento de compra a dominios de salud. TikTok España: medicamento con receta "Not allowed" [ABIERTA].
8. **Las tasas base de ingresos son malas.** Solo una fundadora sola ha pasado de 1 M$ ARR (Shotsy, EE. UU., Reddit como lanzadera, 2024-25, luego capital riesgo). Los casos verificados hoy en TrustMRR están en 631 y 1.813 $ MRR. Ningún caso entre 5 y 50 k$ MRR [ABIERTA].
9. **Por CAC, solo la comunidad de pago sale con LTV/CAC mayor que 1** (1,5-2,8 con vida media supuesta de 4 meses). Con 2.000 €/mes de anuncios su techo es 11-43 k€/año netos. La app pierde dinero en todos los escenarios (LTV/CAC 0,28) [cálculo propio sobre RevenueCat 2026 y LocaliQ 2026, ABIERTA].
10. **Conclusión**: tu ventaja de usuario de Mounjaro y deportista es real como credibilidad, pero no resuelve ninguno de los tres problemas que matan el negocio: tamaño en español, canal de pago cerrado y reserva legal de la actividad. Es un contenido comoditizable por la IA (la pauta está publicada por las sociedades científicas) cuyo único foso posible es una cara con años de audiencia. Choca con tus cuatro restricciones.

---

## 1. Qué decía el texto externo y qué hay

| Afirmación del "Feedback" | Veredicto | Dato |
|---|---|---|
| "21 % de hogares EE. UU. con usuario GLP-1" | CONFIRMADA, una sola fuente | PwC/Numerator, encuesta 4-9 mayo 2026, n=3.089; 9 % en enero de 2025; Numerator 22 % en agosto de 2026 [FRAGMENTO] |
| "85 % dice que el apoyo es deficiente" | CONFIRMADA como dato de esa misma encuesta | Redacción exacta de la pregunta desconocida (PDF 403); 77 % dice que apps y suscripciones no le ayudan |
| "Las apps actuales solo cuentan calorías" | FALSA | MyFitnessPal GLP-1 Support gratis (28-04-2026), MyNetDiary (05-05-2026), Noom Companion con Muscle Defense gratis (24-06-2026), WW con proteína, Shotsy con proteína |
| "Ángulo muerto: mantener músculo con GLP-1" | FALSA como hueco; sin tracción como mercado | ≥25 apps "GLP-1 muscle" lanzadas feb-oct 2026, todas 0-9 valoraciones; KDP "GLP-1 muscle" líder 115 reseñas, mayoría 0 |
| "Plantilla Notion o KDP a 19 $ con 5 tarjetas" | Formato saturado | Cookbooks GLP-1 en Amazon.com líder 339 reseñas; Hotmart en español 2-69 $, ninguno de fuerza con fármaco |
| "Dejar el fármaco sin recuperar peso" como promesa | PROHIBIDA por la evidencia | STEP 1 extensión: se recupera 2/3 del peso al año; SURMOUNT-4: +14 % en 52 semanas tras retirar tirzepatida |
| El hueco | CORREGIDO | Salida del fármaco y mantenimiento sin fármaco, más idioma español; pequeño y de retención dudosa |

---

## 2. Demanda: tamaño y tendencia

### 2a. Dinero y usuarios

| Geografía | Dato | Fecha | Estado |
|---|---|---|---|
| Global, Lilly | Mounjaro 10.723 M$ en Q3-2026 (+65 %); fuera de EE. UU. 5.700 M$ (+93 %); Zepbound 5.352 M$ (+49 %) | 29-10-2026 | [ABIERTA, 8-K SEC] |
| Global, Novo | Wegovy 79.106 M DKK en 2025 (+36 %); Wegovy pastilla >5 M recetas en EE. UU. hasta Q2-2026 | 2026 | [ABIERTA, 6-K SEC] |
| España | ~500.000 usuarios para adelgazar a cierre de 2025 (+16 % interanual), 1,2 % de adultos; ventas de análogos GLP-1 >840 M€ en 2025 (+75 %) | 23-04-2026 | Lantern vía Alimarket [ABIERTA]; metodología no publicada |
| España | Semaglutida financiada (solo diabetes): 403,9 M€ en receta SNS 2024, primer principio activo por importe | 2024 | Ministerio de Sanidad [ABIERTA] |
| España | Wegovy: financiación rechazada 3 veces en 2025; Mounjaro: sin solicitud inicial; genérico de semaglutida en la UE no antes de 2031 | 2025-26 | Redacción Médica, RX Index [ABIERTA] |
| EE. UU. | 12 % de adultos tomando GLP-1 actualmente, 18 % alguna vez; 56 % lo encuentra difícil de pagar | nov-2025 | KFF [ABIERTA] |

Cálculo del tamaño relativo: 500.000 usuarios en España frente a unos 31 M en EE. UU. (12 % de ~260 M adultos) da un 1,6 %. El Planificador [INTERNO] da ratios de 0,5 % ("ozempic dieta" 30/mes frente a "glp 1 diet plan" 6.600/mes) y 6,9 % ("mounjaro efectos" 90/mes frente a "ozempic muscle loss" 1.300/mes). La demanda en español es del orden del 1-3 % de la inglesa.

### 2b. Precio que ya paga el usuario español

| Producto | PVP farmacia por mes | Fuente |
|---|---|---|
| Mounjaro 2,5 mg | 207,91 € | OCU [ABIERTA] |
| Mounjaro 5 mg | 271,35 € | OCU [ABIERTA] |
| Mounjaro 7,5 y 10 mg | 358,71 € | OCU [ABIERTA] |
| Mounjaro 12,5 y 15 mg | 446,07 € | OCU [ABIERTA] |
| Wegovy 0,25 a 2,4 mg | 179,89 a 292,03 € | prensa lanzamiento 2024 [ABIERTA] |
| Consulta telemedicina con receta (ZAVA) | 25 € | zavamed.com/es [ABIERTA] |
| Acompañamiento sin fármaco (Juniper ES) | 40 a 55 €/mes | juniper [ABIERTA] |

Lectura: el fármaco absorbe 200-450 €/mes del presupuesto del usuario. Un acompañamiento tuyo compite por lo que queda contra clínicas que lo incluyen con médico.

### 2c. Tendencia de interés

- Reddit, cinco subreddits principales en inglés: posts al mes 14.280 (mar-2025) → 6.294 (sep-2026), **−41 % interanual** [ABIERTA, arctic-shift]. Las ventas suben y la conversación cae: el fármaco se normaliza.
- Temas que el texto externo llamaba "ángulo muerto" en los títulos de Reddit (sep-2026): músculo, proteína, mantenimiento, dejar el fármaco suman el 2,5 % de los posts en r/Zepbound (81 de 3.213) y el 3,8 % en r/Mounjaro (51 de 1.327). Náuseas y estreñimiento pesan parecido. "Stopping" en r/Mounjaro es el único tema que sube: 8 → 16 hilos al mes [ABIERTA, arctic-shift].
- Planificador [INTERNO]: ES "ozempic dieta" −33 %, "mounjaro efectos" −22 %, US "glp 1 diet plan" −18 % interanual.
- Comunidades en español en Reddit: r/OzempicEspana 6 suscriptores, r/GLP1espanol 1. Facebook, Telegram y Forocoches: existen según autocompletado, NO VERIFICADO (sin acceso).
- YouTube en español: ningún canal específico GLP-1 con más de 1.000 suscriptores salvo diarios personales (Alba Arranz 10,9k); vídeos de 20-65k vistas. Vídeos sobre músculo o proteína con GLP-1 en español: prácticamente inexistentes. En inglés hay decenas de médicos y entrenadores con 40k a 2,3 M de vistas.

### 2d. Lo que la gente pide en español (autocompletado de Google, 31-10-2026) [ABIERTA]

| Semilla | Sugerencias relevantes | Lectura |
|---|---|---|
| "mounjaro " | precio, efectos secundarios, comprar, pastillas, precio farmacia España | 7 de 15 son precio o compra |
| "dejar mounjaro" | de golpe, poco a poco, sin efecto rebote, sin engordar, después de dejar | Demanda de transición clara |
| "mounjaro dieta" | dieta pdf, dieta pdf español, proteica | Piden un PDF |
| "mounjaro masa muscular" | pérdida masa muscular, pierdes, afecta | Existe, cola corta |
| "mounjaro proteina" | Todas las sugerencias en portugués | El tema casi no existe en español de España |
| "mounjaro acompa" | 1 en español, 14 en portugués ("acompanhamento") | Brasil domina la categoría |

Contraste en inglés: "zepbound protein" → calculator, intake, shake, goal; "coming off mounjaro" → success stories, keeping weight off. La cola inglesa es de producto; la española, de precio y efectos.

### 2e. Multiplicadores 2027-2028

Wegovy pastilla y Foundayo (orforglipron, Lilly) tienen opinión positiva del CHMP (mayo y octubre de 2026); su lanzamiento en España depende de la resolución de precio, sin fecha [ABIERTA, EMA]. Más usuarios y más baratos de administrar, pero sin genéricos ni financiación pública en España hasta 2031. El mercado español de usuarios crece al 16 % anual, no al 75 % de la facturación.

---

## 3. Evidencia clínica: qué puedes afirmar y qué no

| Afirmación | Evidencia | Veredicto |
|---|---|---|
| "Pierdes mucho músculo con GLP-1" | STEP 1 DXA (n=140): 40 % del peso perdido fue masa magra; SURMOUNT-1 DXA (n=160): 25 %. Metaanálisis Eisa 2026 (20 ensayos, n=15.782): semaglutida 35 %, tirzepatida 25 %, estilo de vida 26 %, estilo de vida con fuerza 17,5 %. Masa magra no es músculo (CT/RM ≈25 %). Handgrip con semaglutida: −0,16 kgf, certeza muy baja; SEMALEAN (n=106): +4,5 kg de agarre a 12 meses | Matizar: no puedes decir "rápido" ni "más que con dieta" sin contradecir metaanálisis |
| "El ejercicio de fuerza lo evita" | Ningún ensayo aleatorizado de fuerza o proteína con semaglutida o tirzepatida. El único de tirzepatida y ejercicio (2024) fue RETRACTADO en 2025. Solo S-LiTE (liraglutida y aeróbico). ACSM 2026: esa afirmación excede la evidencia | No afirmable |
| "Podrás dejarlo sin recuperar peso" | STEP 1 extensión (n=327): recuperan 11,6 de 17,3 puntos (2/3) en 1 año. SURMOUNT-4 (n=670): +14 % en 52 semanas tras retirar tirzepatida frente a −5,5 % si continúan | Prohibido como promesa |
| "La mayoría abandona" | Rodriguez 2025 (JAMA Netw Open, n=125.474): 64,8 % abandono a 1 año sin diabetes; Prime (claims): persistencia 31,5 / 15,1 / 8,1 % a 1, 2 y 3 años [FRAGMENTO] | Confirmado: tu cliente deja de pagar cuando deja el fármaco |
| "Los fármacos para preservar músculo llegan en 2027" | Bimagrumab, apitegromab, enobosarm, trevogrumab: fase 2 positivas, ninguno con fase 3 registrada; aprobación improbable antes de 2029 | El hueco no se cierra en 2027-28, pero tampoco lo llenas tú |
| "Hay conocimiento propietario en la pauta" | ≥1,2 g/kg de proteína, fuerza progresiva 2-3 días por semana, manejo digestivo, cribado de trastornos alimentarios: ya publicado por TOS/OMA/ASN/ACLM 2025, EASO 2026 (Lancet), EASD 2025, OMS 2025, GIRO/SEEDO 2024 | No hay conocimiento propio: cualquier IA lo resume igual |

La ficha técnica de Mounjaro y Wegovy (EMA, texto en español) tiene 13 situaciones que remiten al médico: pancreatitis, hipoglucemia con insulina o sulfonilureas, deshidratación con fallo renal, gastroparesia, retinopatía, anestesia, pérdida de visión, colelitiasis, embarazo (suspender 1-2 meses antes), lactancia, interacciones con anticoagulantes, indicación por IMC y posología. Un producto no sanitario no puede interpretar ninguna de ellas ni aconsejar "quédate en 5 mg".

---

## 4. Competencia: quién ocupa qué

| Segmento | Quién | Precio | Músculo | Salida del fármaco |
|---|---|---|---|---|
| Grandes EE. UU. con fármaco | Noom Med 149 $/mes; WW Med+ 74 $/mes; Ro Body 74-149 $/mes; Hims 149 $/mes; Calibrate 199 $/mes; Found 99-169 $/mes | 74-199 $/mes sin fármaco | Noom gratis, Omada (B2B), Found con Obé 2024, Equinox PT | Ninguno publica plan |
| Farmacéuticas | Lilly Health app (5.141 valoraciones), Novo WeGoTogether (62 valoraciones, 3,0) | Gratis | No | No |
| Trackers independientes | Shotsy 34.292 valoraciones en EE. UU., 363 en España; ≥25 apps "GLP-1 muscle" 2026 con 0-9 valoraciones; Preserve 0 | 9,99 $/mes o 20-50 $/año | Marketing sí, tracción no | Micro-comunidades de 2-17 miembros |
| Comunidades Skool | 170 comunidades "glp-1"; GLP1 Enhanced HUB 4.100 miembros × 12 $/mes; Shape & Strength Club 827 × 47 $/mes | 9-47 $/mes | Alguna | "weaning off" en una |
| Creadores con cara (inglés) | Dr. Dan 62,6K subs; The Betty Method 21,4K (Skool 39 $/mes); Astrid Naranjo 5,35K (challenge 550 $) | 39-97 $/mes o 550-797 $/programa | Sí | Guía gratis de Astrid |
| España | ZAVA (consulta 25 €), Santé Clinics, Juniper 40-55 €/mes, Dorsia, 5 libros KDP con 0-24 reseñas, 4 productos Hotmart de 2-69 $, Di Trainer (349 subs) | — | Ninguno de fuerza con fármaco | Ninguno |

No existe un "Greg Doucette del GLP-1" ni en inglés ni en español. En inglés el nicho de creadores es pequeño (máximo 62,6K). En español no hay ningún canal específico por encima de 1.000 suscriptores.

---

## 5. Legal: qué puedes vender tú en España

Las tres restricciones duras [ABIERTA, BOE y políticas de plataforma]:

1. **Captación de pago cerrada**: Google Ads fuera de EE. UU., Canadá y Nueva Zelanda prohíbe términos de medicamentos con receta en anuncio y en página de destino. Palabras clave de medicamentos solo para farmacias y telesalud certificadas. "Health" y "Restricted drug terms" son categorías sin audiencias propias (sin remarketing ni Customer Match). Meta: medicamentos con receta solo con LegitScript y solo en EE. UU., Canadá y Nueva Zelanda; audiencias con condiciones de salud bloqueadas; Core Setup bloquea el evento Purchase a dominios de salud. TikTok España: "Prescription medicine: Not allowed". Quedan SEO, YouTube y TikTok orgánicos y email.
2. **Población especial**: Madrid (Ley 6/2016, arts. 7, 10, 16, multas 3.001-30.001 €) reserva al Preparador Físico con grado CAFyD el entrenamiento de personas con patologías, con presencia física; Valencia (Ley 2/2022, art. 9) reserva el reentrenamiento de patologías diagnosticadas; Cataluña (Ley 3/2008, art. 2.1 bis) da competencia exclusiva sobre planes detallados de entrenamiento y considera infracción la mera publicidad. Venta online desde otra comunidad: zona gris. "Entrenador personal" es denominación reservada en Madrid.
3. **Nutrición individualizada**: la alimentación adecuada a necesidades fisiológicas o patológicas de la persona es acto propio del dietista-nutricionista (Ley 44/2003, art. 7.2.g). Intrusismo: Código Penal art. 403, multa de 12-24 meses; prisión de 6 meses a 2 años si te atribuyes públicamente la cualidad. Ninguna condena a coaches localizada 2020-2026; el propio Consejo de Dietistas admite que las denuncias tienen poco efecto. Riesgo bajo de sanción, riesgo alto de denuncia pública.

Lo que sí puedes vender [ABIERTA + INTERPRETACIÓN]: educación general no individualizada (cursos, vídeos, ebooks, comunidad); pautas de proteína por rango poblacional con la declaración autorizada de la EFSA ("las proteínas contribuyen a conservar la masa muscular"); programas de fuerza genéricos para adultos sanos con disclaimer y derivación; relato personal con cara ("qué hago yo con Mounjaro") como libertad de expresión, sin enlace a compra del fármaco; mención descriptiva de la marca ("para quien usa Mounjaro") sin registrar dominio ni nombre de app con ella; afiliación a proteína solo con declaraciones autorizadas. Publicidad de medicamento con receta al público: infracción muy grave, 90.001 a 1.000.000 € (Real Decreto Legislativo 1/2015, art. 80 y 111). Una app que registre dosis y síntomas exige consentimiento explícito (RGPD art. 9.2.a), evaluación de impacto y declaración de app de salud en las tiendas, sin usar esos datos para publicidad.

Nunca usar "nutricionista", "dietista", "coach nutricional" ni "entrenador personal".

---

## 6. Monetización: CAC y LTV por formato

Inputs con fuente: CPI app fitness 1,12 $ Android / 2,24 $ iOS (Searchlab) y 5,98 $ Meta (Superads); instalación a pago D35 en Health & Fitness 2,9 % mediana, trial a pago 37,7 %, ingreso realizado por pagador a 1 año 35,64 $, retención a 12 meses de planes mensuales 6-14 % (RevenueCat 2026, 115.000 apps) [ABIERTA]; CPC Google Ads Health & Fitness 6,17 $ y CPL 67,36 $ (LocaliQ 2026, EE. UU.) [ABIERTA]; CPM Meta EE. UU. 18,67 $ (Revealbot) [ABIERTA]; CPM Meta España NO ENCONTRADO, supuesto 9 €; conversión landing 1,4 % (Littledata). Supuestos marcados en cursiva en la nota.

| Formato | Ticket | LTV estimado | CAC estimado | LTV/CAC | Neto con 300 / 1.000 / 2.000 €/mes | Techo anual con 2.000 €/mes |
|---|---|---|---|---|---|---|
| A. App | 9,99-20 €/mes | 33 € (año 1, mediana) | 120 € (32-600) | **0,28** | Pierde en los tres | ≈ −17 k€ |
| B. Programa 12 semanas | 100 € | 100 € | 64-245 € | **0,4-1,6** | −56 a +169 / −187 a +563 / −374 a +1.125 € | −4,5 a +13,5 k€ |
| C. Comunidad | 45 €/mes | 180 € (*vida media 4 meses*) | 64-123 € | **1,5-2,8** | +140 a +545 / +465 a +1.810 / +930 a +3.625 € | +11 a +43 k€ |
| D. Canal con cara | mixto | 40 k€/año a 100.000 subs (cota superior) | tiempo, años | n/a | Los euros compran edición, no audiencia | n/a |
| E. B2B2C farmacias y clínicas | *10 €/paciente/mes* | sin dato | reuniones | sin dato | No aplican anuncios | n/a |

Cálculos clave:

- App: CAC por pagador = 3 € de CPI / 2,5 % = 120 €. LTV 33 €. Para 5.000 €/mes harían falta 150 pagadores nuevos al mes, 6.000 instalaciones, unos 18.000 €/mes de CPI.
- Comunidad: 100 k€/año = 8.333 €/mes / 45 € = 185 miembros permanentes. Con vida media de 4 meses son 46 altas al mes, es decir 3.000-5.700 €/mes de captación. Sobre 500.000 usuarios en España, 185 miembros es el 0,037 %, pero con los canales de pago cerrados solo llegas por orgánico.
- Canal: vidIQ (61,2 M canales) dice que el 1,3 % llega a 100.000 suscriptores y que el crecimiento mediano en la banda 10k-99k es 0,48 % al mes [ABIERTA]. Fit Generation tardó 9 años y 2.328 vídeos en llegar a 750K. El único indicio de conversión suscriptor a comprador es Fuertafit: "+200.000 personas" desde 2017 sobre 5,11 M de suscriptores, ≤0,4 % al año como cota superior. 100.000 subs × 0,4 % × 100 € = 40 k€/año.
- Afiliación: telesalud GLP-1 paga 3-500 $ por paciente, pero exige paciente residente en EE. UU. Suplementos: Amazon.es Deportes 4 %, Alimentación 1 %. Sobre 160.000 vistas al mes en español: unos 38 €/mes.
- B2B2C: ningún proveedor de programa para farmacias existe en España; el PVP está regulado y la farmacia comunitaria publica su propio protocolo (enero de 2026). Las clínicas online ya lo incluyen (Juniper 40-55 €/mes con médico). El comprador natural es el competidor y exige venta consultiva.

---

## 7. Por qué te gusta y por qué eso no basta

Tu ventaja real: eres usuario de Mounjaro, deportista de toda la vida e ingeniero. Eso te da tres cosas que el texto externo no tiene: credibilidad de primera persona, criterio para distinguir evidencia de marketing, y una historia que se puede contar con cara. Todo eso es cierto y no lo tienen ni Noom ni los 25 clones.

Lo que no te da:

- **Tamaño**: la demanda en español es el 1-3 % de la inglesa y la conversación cae un 41 % interanual en inglés. El autocompletado español pide precio, efectos y un PDF, no un programa de fuerza.
- **Canal**: la única palanca que te importa, el CAC, está cerrada por política de Google, Meta y TikTok para España. Queda orgánico, es decir, años de vídeos con cara, que es exactamente el formato que descartaste por plazo y por exposición.
- **Permiso**: el nicho es población con patología, el segmento más reservado del fitness español. Lo defendible es contenido editorial sin seguimiento individual, y eso lo comoditiza la IA mañana porque la pauta ya está publicada por las sociedades científicas.
- **Retención**: el 65 % de usuarios abandona el fármaco en un año y recupera dos tercios del peso. El cliente que entra por "dejar Mounjaro" deja de pagar en cuanto lo deja, y el hueco de "mantenimiento" puede existir precisamente por eso.

Respecto a tus cuatro restricciones: sin capital funciona; sin reuniones funciona; sin LinkedIn funciona; "no comoditizable por la IA" **no funciona**. Un canal con cara sí sería un foso, pero tarda años y es incompatible con el horizonte de ingresos que planteas. Normach con la escalera CRA, Máquinas y AI Act tiene retención legal obligatoria de 10 años y comprador con fecha límite; esto no tiene ninguna de las dos cosas.

---

## 8. Si aun así quieres probarlo: el test más barato

Coste 0 €, 90 días, sin tocar ninguna línea roja:

1. Diez vídeos en YouTube en español, con cara, sobre lo que el autocompletado pide y nadie cubre: "dejar Mounjaro sin rebote", "qué dicen las guías sobre proteína y fuerza con GLP-1", "mi año con Mounjaro entrenando". Relato personal más resumen de guías públicas. Sin pauta individual, sin la palabra entrenador, sin enlace a compra del fármaco.
2. Un PDF gratuito "guía de mantenimiento según las guías EASO/SEEDO" a cambio de email. La gente ya busca "dieta mounjaro pdf español".
3. Umbral para seguir: 1.000 suscriptores y 300 emails en 90 días. Por debajo, el nicho en español no da para una comunidad de 185 miembros.
4. Si pasa el umbral, el producto es la comunidad (formato C) a 45 €/mes con contenido educativo y sesiones grupales, no una app.

Lo que no haría en ningún caso: app con registro de dosis (RGPD, tiendas, LTV/CAC 0,28), anuncios de pago (política cerrada), nada que incluya "nutricionista", "entrenador personal" ni promesas de músculo o de dejar el fármaco sin rebote.

---

## 9. Lo no verificado

- PDF original de PwC (403): el 85 % y la redacción de la pregunta vienen de eMarketer.
- 500.000 usuarios en España: estimación de Lantern presentada en feria, metodología no publicada.
- CIMA/AEMPS inaccesible: precios oficiales de nomenclátor no verificados; OCU sin fecha visible.
- CPM y CTR de Meta en España: NO ENCONTRADO.
- Retención real de comunidades de coaching online: sin dato; la vida media de 4 meses es supuesto.
- Conversión suscriptor a comprador de creadores: solo el indicio de Fuertafit.
- Comunidades en español en Facebook, Telegram y Forocoches: existen según autocompletado, sin acceso.
- Suscriptores de Reddit: metadatos de arctic-shift, posiblemente desactualizados.
- Frecuencia de temas en Reddit: una docena de consultas a arctic-shift devolvieron timeout (marcadas "s.d." en la nota); los porcentajes del 2-4 % son cota inferior.
- Cobertura de seguro de responsabilidad civil para un no titulado online: sin dato.
- Google Trends (429), TikTok (CAPTCHA), Instagram, Udemy, Business of Apps, Social Blade: inaccesibles.

## 10. Confianza

- Alta en: cifras de ventas de Lilly y Novo (SEC), textos legales (BOE, EUR-Lex), políticas de Google, Meta y TikTok, fichas técnicas de la EMA, ensayos clínicos citados, valoraciones de apps (API iTunes), precios de Mounjaro (OCU).
- Media en: tamaño del mercado español, tasas de conversión de RevenueCat aplicadas a España, techo de la comunidad.
- Baja en: CAC en Meta España, retención de comunidades, conversión de creadores, existencia y tamaño de comunidades españolas fuera de Reddit.
