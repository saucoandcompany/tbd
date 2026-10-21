# Servicios con exceso de demanda en 2026 (cualquier país) que una o dos personas podrían empezar a servir — verificación abriendo páginas

**Fecha:** 2026-10-21. **Método:** se usó la nota de fragmentos `servicios_lista_espera.md` como mapa y se abrieron las páginas con `pwfetch.js` (HTTP directo o Chromium). **Presupuesto usado:** 45 aperturas de página (tope) y 7 búsquedas de 15. WebFetch no funcionó en este entorno (DNS), así que todo lo abierto pasó por pwfetch/curl.

**Etiquetas:** **[ABIERTA]** = la cifra se leyó en la página (texto o PDF descargado). **[FRAGMENTO]** = solo visto en extracto de buscador, no verificado en página. **[PRIMARIA]** = organismo oficial, documento original o dato propio de la plataforma; **[SECUNDARIA]** = prensa o consultora. País anotado en cada dato (UK = Reino Unido/Gran Bretaña; ES = España; IE = Irlanda; DE = Alemania; NL = Países Bajos; US = EE. UU.; CA = Canadá).

**Páginas que no se pudieron abrir (para que nadie las dé por leídas):** NHS Digital (autism statistics, mi-adhd) → 403 Cloudflare incluso con navegador; USCIS processing times → bloqueado; Congreso de los Diputados PDF 184/36125 → "Access Denied"; economie.gouv.fr (factura electrónica Francia) → 403; Bundesfinanzministerium FAQ E-Rechnung → 503 security check; Superprof.es → 403 incluso con navegador; CBR.nl → ECONNRESET; UNED PDF XXVI Dictamen Dependencia → conexión reiniciada; páginas de precios de RED y AA Driving School → 404 (la AA solo muestra precios tras introducir código postal); gov.uk "driving-test-waiting-times" (dataset) → 404 en la URL probada; Skills for Care "Recruitment and retention" → 404; IRCC (Canadá) carga pero el tiempo de tramitación requiere interacción con formulario (no leído).

---

## Pregunta 1 — ¿Qué 10-15 servicios muestran la evidencia más dura de exceso de demanda en 2026, con la cifra leída en página oficial o primaria?

### Takeaway
La evidencia más dura y **leída en página** se concentra en cuellos de botella públicos de UK, ES e IE: evaluaciones TDAH/autismo (Inglaterra >560.000 en lista; Gales mediana 101 semanas, FOI oficial), examen práctico de conducir (UK: media 22 semanas y 70 % de centros al máximo de 24 semanas según NAO; ES: 28.800 alumnos esperando hasta 6 meses en Madrid; IE: media nacional 12 semanas, Raheny 25 semanas), dependencia en España (320 días de media, 265.503 en lista), psicología pública en España (>6 meses) y atención temprana en Madrid (1.320 en lista, documento oficial). En oficios (DE, ES) la señal es de cartera de pedidos/precios al alza más que de lista de espera. Las obligaciones fiscales con fecha (Verifactu ES 2027, MTD UK 2026-2028) son demanda latente con calendario oficial leído. Contra-señal: la oferta de tutores online (Preply: 46.449 profesores de inglés) es abundante, y en NL el CBR está dentro de su objetivo de 7 semanas.

### Cited Findings (ranking por dureza de la evidencia)

**1. Evaluación de TDAH y autismo (UK — Inglaterra y Gales). Evidencia muy dura, 2026.**
- Gales (Hywel Dda UHB, respuesta FOI oficial, PDF): a 31-01-2026, **mediana de espera para evaluación de TDAH adulto 101 semanas (más larga: 505 semanas); autismo adulto mediana 103 semanas (más larga: 380 semanas)**; 1.040 menores de 18 esperando evaluación de TDAH — [Hywel Dda UHB, FOI disclosure log](https://hduhb.nhs.wales/about-us/governance-arrangements/freedom-of-information/disclosure-log/disclosure-logs/attention-deficit-hyperactivity-disorder-adhd-and-autism-spectrum-disorder-asd-assessments/) [PRIMARIA][ABIERTA]
- Inglaterra: "más de 560.000 personas en listas de espera de TDAH"; derivaciones abiertas ~562.000 en diciembre 2025 (desde ~365.000 en diciembre 2024); 61,6 % de adultos y 65,8 % de niños esperan más de un año; solo ~10 % atendidos en 13 semanas; ~20.000 derivaciones nuevas al mes (+400 % desde 2020); lista de adultos +86 % en un año; en Londres solo 16 % de la población con TDAH estimada recibe tratamiento (~33.800 de >207.000) — [Carnall Farrar, UK ADHD Crisis (análisis sobre datos NHS England)](https://www.carnallfarrar.com/uk-adhd-crisis/) [SECUNDARIA sobre datos oficiales][ABIERTA]
- Diciembre 2025: el Gobierno lanzó revisión formal de servicios de salud mental, TDAH y autismo con £688 millones y compromiso de 8.500 trabajadores adicionales — [Carnall Farrar](https://www.carnallfarrar.com/uk-adhd-crisis/) [SECUNDARIA][ABIERTA]
- **No leído**: la publicación oficial NHS England "ADHD management information" y "Autism Statistics" (403). La cifra 560k procede de la consultora que cita NHS England, no de la página oficial.

**2. Examen práctico de conducir e instructores (UK — Gran Bretaña). Evidencia muy dura, 2025-2026.**
- NAO (auditor público): **media de espera 22 semanas en septiembre 2025 frente a poco más de 5 semanas a inicios de 2020; 70 % de los centros de examen al máximo de 24 semanas**; backlog estimado 1,1 millones de tests, 360.000 aún sin reservar; 43 % más aprobados del teórico entre 2019-20 y 2024-25; 31 % de 21.656 encuestados usó revendedores externos, algunos pagando hasta £500 por una plaza; 30 % necesita conducir para su trabajo — [NAO, nota de prensa](https://www.nao.org.uk/press-releases/watchdog-urges-dvsa-to-address-driving-test-delay-backlog-and-cut-waiting-times/) [PRIMARIA][ABIERTA]
- AA Driving School (FOI a DVSA): la media subió de **20,8 semanas en enero 2026 a 22,4 semanas el 6 de abril de 2026**; 69 centros estuvieron a 24 semanas todos los meses de 2025 (58 en Inglaterra = 18 % de centros; 6 en Gales = 22 %; 5 en Escocia ≈ 10 %); objetivo DVSA de 7 semanas para fin de 2027; desde el 12-05-2026 es ilegal reservar o cambiar un examen en nombre de otra persona — [The AA, newsroom 12-05-2026](https://www.theaa.com/about-us/newsroom/changes-to-driving-test-booking-system-may-2026) [SECUNDARIA con datos oficiales FOI][ABIERTA]
- DVSA (blog oficial, 18-06-2026): nueva métrica mensual por centro; **mediana nacional reserva→examen de 9,7 semanas en mayo 2026 frente a 21,8 semanas de la medida "10 % de disponibilidad"**; ejemplo Darlington 13 semanas vs mediana 6,7; St Helens 16,5 vs 6,1 — [DVSA Despatch, 18-06-2026](https://despatch.blog.gov.uk/2026/06/18/giving-you-a-clearer-picture-of-driving-test-waiting-times/) [PRIMARIA][ABIERTA]. **Conflicto de medidas**: media/10 % (≈22 semanas) vs mediana (9,7); DVSA reconoce que "muchos alumnos siguen sufriendo esperas prolongadas".
- Fragmentos no verificados: 40 % de alumnos de agosto 2026 esperaron menos del objetivo de 7 semanas; 2,13 millones de exámenes en los 12 meses a agosto 2026 — [passrates.uk](https://passrates.uk/guide/driving-test-record-capacity-2026) [SECUNDARIA][FRAGMENTO]

**3. Dependencia y coordinación del cuidado de mayores (ES). Evidencia dura, 2026 (leída en prensa que cita Imserso).**
- **13.503 fallecidos en lista de espera de dependencia en los cinco primeros meses de 2026** (6.940 esperando valoración); lista de **265.503 personas** a cierre de mayo 2026 (+7.293 respecto a cierre de 2025); **tiempo medio solicitud→resolución 320 días** frente al plazo legal de 180; Murcia 552 días, Andalucía 446, Asturias 411, Madrid 346, Canarias 335; Navarra 211 y Baleares 203 — [El Debate, 15-06-2026, con datos Asociación de Directores y Gerentes en Servicios Sociales/Imserso](https://www.eldebate.com/sociedad/20260615/13500-muertes-listas-espera-dependencia-cinco-meses-estas-son-comunidades-afectadas_428672.html) [SECUNDARIA sobre datos oficiales][ABIERTA]
- El PDF primario (XXVI Dictamen del Observatorio) no se pudo descargar (conexión reiniciada) — [UNED](https://blogs.uned.es/catedraunedfuenlabrada/wp-content/uploads/sites/313/2026/07/XXVI-DICTAMEN-OBSERVATORIO-DE-LA-DEPENDENCIA.pdf) [PRIMARIA, no leído]

**4. Examen práctico de conducir y profesores de autoescuela (ES — Madrid). Evidencia dura, mayo 2026.**
- **28.800 alumnos esperan hasta 6 meses para examinarse en Madrid "debido a la falta de profesores y examinadores"**; bolsa de 72.000 alumnos con teórico aprobado, de los que solo 30-40 % estarían listos; una autoescuela concreta: ~100 alumnos esperando, media 4-6 meses; propuesta de "sistema mixto como Portugal" — [El Español, 22-05-2026](https://www.elespanol.com/madrid/sociedad/20260522/alumnos-esperando-meses-examinarse-carnet-madrid-jose-vilo-autoescuela/1003744254877_0.html) [SECUNDARIA][ABIERTA]
- Sin cifra oficial DGT leída (la DGT no publica tiempos de espera por provincia en una página localizada).

**5. Examen práctico de conducir (IE). Evidencia dura, junio 2026.**
- **Media nacional 12 semanas frente al objetivo de 10**; Raheny (Dublín) pasó de 17 semanas (28-05) a **25 semanas** (mediados de junio) más hasta 5 semanas adicionales hasta la cita; Mulhuddart 19 semanas; Dún Laoghaire bajó de 21 (marzo) a 13 (junio); Drogheda 17; Loughrea 15; Cavan, Buncrana, Tralee, Monaghan 14 — [The Irish Times, 16-06-2026](https://www.irishtimes.com/ireland/2026/06/16/raheny-has-longest-driving-test-waiting-time-at-six-months/) [SECUNDARIA con datos RSA][ABIERTA]
- Fragmentos: ~11,7 semanas de media en marzo 2026 (RTÉ/RSA) — [odo.ie](https://www.odo.ie/guides/driving-test-waiting-times-ireland) [SECUNDARIA][FRAGMENTO]

**6. Psicología clínica / terapia (ES). Evidencia dura pero de prensa, julio 2026.**
- "La lista de espera para una primera consulta de psicología clínica en la sanidad pública **supera los seis meses en la mayoría de comunidades**"; ~1.600 psicólogos clínicos en la sanidad pública, **3,4 por 100.000 habitantes**; los especialistas privados "dan cobertura a quienes pueden pagar **entre 50 y 80 euros por sesión**" — [Que.es, 25-07-2026](https://www.que.es/2026/07/25/falta-psicologos-sanidad-publica-pacto/) [SECUNDARIA][ABIERTA]
- UK (contexto de precios, no de espera): "más de la mitad de los terapeutas del directorio BACP anuncian entre £40 y £60 por sesión" — [BACP, How to get therapy](https://www.bacp.co.uk/about-therapy/how-to-get-therapy/) [PRIMARIA, dato propio del directorio][ABIERTA]
- DE (fragmento, dato 2022): espera media hasta plaza de psicoterapia 142,2 días (BPtK) — [Grüne Jugend NRW citando BPtK](https://nrw.antrag.gruene-jugend.de/lmv12026/Mentale-Gesundheit-darf-keine-Frage-des-Geldes-sein-64800/pdf) [SECUNDARIA][FRAGMENTO]; la página de Apotheken Umschau devolvió 302 y no se leyó.

**7. Atención temprana y logopedia infantil (ES — Comunidad de Madrid). Evidencia dura y oficial, pero muestra mejora.**
- Documento oficial: **1.320 demandantes en lista de espera de tratamientos de atención temprana a 31-01-2026** — [Comunidad de Madrid, DG Atención a Personas con Discapacidad, PDF](https://www.comunidad.madrid/docs/assets/2026/02/02/dgapcd-le-red-at-enero2026.pdf) [PRIMARIA][ABIERTA]
- Nota de prensa 23-09-2026: la lista bajó un 65 % desde el inicio de la legislatura; las familias esperan **65 días** entre solicitud de valoración y resolución para sesiones de estimulación, fisioterapia, psicomotricidad, logopedia, terapia ocupacional o psicoterapia — [Comunidad de Madrid, nota de prensa](https://www.comunidad.madrid/node/119569) [PRIMARIA][ABIERTA]. **Matiz**: la propia Administración presenta la cifra como logro; la demanda insatisfecha está en descenso en Madrid, no en aumento.

**8. Oficios de construcción e instalaciones (DE). Evidencia media-dura, cartera de pedidos, Q4 2025.**
- ZDH (patronal del Handwerk, informe de coyuntura 4T-2025): **alcance medio de cartera de pedidos 8,5 semanas en el conjunto del Handwerk; 12,5 semanas en los oficios de obra principal (Bauhauptgewerbe), +1 semana interanual**; utilización de capacidad 75 %; 43 % de empresas reportan buena marcha (+8 pp) — [ZDH Kurzbericht Konjunktur 4. Quartal 2025](https://www.zdh.de/ueber-uns/fachbereich-wirtschaft-energie-umwelt/konjunkturberichte/zdh-kurzbericht-konjunktur-4-quartal-2025/) [PRIMARIA (patronal)][ABIERTA]. Es tiempo de cartera del taller, no espera medida del cliente; una encuesta bávara citada en prensa habla de 4,7 semanas de espera del consumidor [FRAGMENTO, sin fecha].

**9. Fontanería y electricidad a domicilio (ES). Evidencia media (datos de plataforma, cualitativos) con precios al alza.**
- Cronoshare: "la demanda de fontanería y electricidad ha crecido de forma constante, pero la oferta de profesionales no ha avanzado al mismo ritmo"; "este desequilibrio... tiene un efecto directo en los precios, sobre todo en servicios urgentes"; **fontanero 25-40 €/h, electricista 20-70 €/h, urgencias 60-250 €/h**, "tendencia clara al alza"; la plataforma declara una comunidad de "más de un millón de profesionales" — [Cronoshare, sala de prensa](https://www.cronoshare.com/comunidad/p/sala-prensa/nacional/cronoshare-escasez-fontaneros-electricistas-espana) [PRIMARIA, dato propio de plataforma][ABIERTA]. La cifra "~600.000 solicitudes/año" de la nota anterior **no aparece** en la página abierta.

**10. Contabilidad/fiscalidad para autónomos ante obligaciones con fecha (ES Verifactu; UK Making Tax Digital). Demanda latente con calendario oficial.**
- ES, Agencia Tributaria (noticia oficial 03-12-2025, RDL 15/2025): **entidades que presentan Impuesto sobre Sociedades deben tener adaptados sus sistemas de facturación (SIF/VERI*FACTU) antes del 1 de enero de 2027; el resto de contribuyentes (autónomos) antes del 1 de julio de 2027** — [AEAT, Extension of the deadline for adapting SIF](https://sede.agenciatributaria.gob.es/Sede/en_gb/todas-noticias/2025/diciembre/3/ampliacion-plazo-adaptacion-sistemas-informaticos-facturacion.html) [PRIMARIA][ABIERTA]; página índice [AEAT SIF y VERI*FACTU](https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu.html) [PRIMARIA][ABIERTA]
- UK, HMRC: MTD for Income Tax obligatorio **desde 6 de abril de 2026 para ingresos cualificados >£50.000 (año 2024-25); desde 6 de abril de 2027 para >£30.000; desde 6 de abril de 2028 para >£20.000**; "you should've received a letter" para los afectados en 2026 — [GOV.UK, Check if you need to use MTD for Income Tax](https://www.gov.uk/guidance/check-if-youre-eligible-for-making-tax-digital-for-income-tax) [PRIMARIA][ABIERTA]
- **No hay cifra de exceso de demanda** (no se leyó vacantes ni esperas de asesores); es demanda inducida por norma.

**11. Gestión de alquiler turístico (ES). Evidencia débil (solo tarifas).**
- Comisión de gestión habitual en España **15-25 % de ingresos brutos** (rango general 15-30 %); incluye distribución en OTAs, huéspedes, limpieza, check-in, mantenimiento y pricing — [Hostaway, glosario ES, actualizado 23-02-2026](https://www.hostaway.com/es-ES/glossary/management-fee/) [SECUNDARIA, proveedor][ABIERTA]. Sin dato de exceso de demanda leído.

**12. Clases particulares / tutoría. Contra-señal de oferta abundante (global) y precios bajos (ES).**
- Preply: **46.449 profesores de inglés** disponibles, precio por clase de **$3 a $40+** (filtro), ejemplos de perfiles destacados a $60-100 por 50 min — [Preply, online English tutors](https://preply.com/en/online/english-tutors) [PRIMARIA, dato propio de plataforma][ABIERTA]. Indica **exceso de oferta**, no de demanda, en idiomas online.
- ES: clases particulares a domicilio **15-23 €/h de media nacional**; Madrid 14-17 €/h; Barcelona 14-16 €/h; Valencia 12-15 €/h (página fechada 02-01-2026) — [Cronoshare, cuánto cuesta](https://www.cronoshare.com/cuanto-cuesta/clases-particulares-a-domicilio) [PRIMARIA plataforma][ABIERTA]

**Señales negativas o no verificadas (importantes para no sobrevender):**
- **NL, examen de conducir**: a cierre del 2T-2026 los plazos de reserva del examen B en los 53 centros del CBR estaban dentro del objetivo de 7 semanas; 86 examinadores nuevos en 2025-26 frente a 75 salidas — cartas del Ministerio al Parlamento [officielebekendmakingen.nl](https://zoek.officielebekendmakingen.nl/kst-29398-1198.html) [PRIMARIA][FRAGMENTO]. **No hay exceso de demanda** en NL.
- **UK, cuidado de mayores**: Skills for Care publicó el 14-10-2026 "The state of the adult social care sector and workforce in England" (datos 2025/26) — [Skills for Care](https://www.skillsforcare.org.uk/Adult-Social-Care-Workforce-Data/Workforce-intelligence/publications/national-information/The-state-of-the-adult-social-care-sector-and-workforce-in-England.aspx) [PRIMARIA][ABIERTA solo la portada; **las cifras de vacantes están en visualización JS/PDF no leídos**].
- **UK, bombas de calor**: Boiler Upgrade Scheme statistics August 2026 publicado el 24-09-2026 (series mensuales) — [GOV.UK colección](https://www.gov.uk/government/collections/boiler-upgrade-scheme-statistics), [agosto 2026](https://www.gov.uk/government/statistics/boiler-upgrade-scheme-statistics-august-2026) [PRIMARIA][ABIERTA solo la portada; cifras en Excel/PDF no leídos].
- **ES/US/CA, trámites de inmigración**: Congreso (PDF 184/36125) denegado; USCIS bloqueado; IRCC interactivo. Sin cifra leída. Fragmentos de la nota anterior (100-500 € por cita de extranjería) siguen sin verificar.
- **US**: ninguna página de EE. UU. pudo leerse con cifra (USCIS bloqueado); no hay datos US en estas notas.

### Inferences
- Donde el Estado fija un plazo y lo incumple con cifra pública (UK TDAH, UK/IE/ES examen de conducir, ES dependencia, ES psicología) ya existe pago privado para saltar la cola documentado en página: £950 por evaluación TDAH online (Psychiatry-UK), hasta £500 a revendedores de citas de examen (NAO), 50-80 €/sesión de psicología privada (ES).
- La ilegalización el 12-05-2026 de reservar examen por terceros en UK cierra el nicho "buscador de cancelaciones" y desplaza el valor hacia la instrucción (ADI) y la preparación intensiva, donde la escasez de examinadores alarga el ciclo de cada alumno.
- En ES, la combinación de 28.800 alumnos esperando y escasez de profesores (El Español) sugiere que la cualificación de profesor de formación vial es el cuello de botella; igual que la mediana de 101 semanas en Gales sugiere que la evaluación clínica (no la "coordinación") es lo que escasea.
- Las obligaciones Verifactu (2027) y MTD (2026-28) crean una ventana de 6-18 meses de demanda de configuración/formación para autónomos sin cifra de espera, pero con fecha legal leída en la fuente oficial.

### Gaps
- No se pudo leer la publicación oficial de NHS England sobre TDAH/autismo (403): la cifra inglesa depende de la consultora Carnall Farrar.
- No se encontró ni se leyó estadística oficial de la DGT sobre tiempos de espera del examen práctico por provincia (2026).
- No hay cifra nacional de vacantes de cuidado de mayores leída en 2026 (UK: informe publicado pero contenido en PDF/JS; ES: dictamen no descargable).
- Sin datos leídos de EE. UU., Canadá, Francia, Italia ni Australia para ningún servicio.
- No se leyó ningún dato de mascotas, bodas, meal prep, traducción, admisiones universitarias, ghostwriting ni edición de pódcast/vídeo que evidencie exceso de demanda (no hubo presupuesto de aperturas tras priorizar las fuentes oficiales).

---

## Pregunta 2 — ¿Qué pagan los clientes (páginas de precios abiertas)?

### Takeaway
Las páginas de precios leídas muestran que el gasto privado para saltar listas públicas va de £40-60/sesión (terapia UK) y 50-80 €/sesión (psicología ES) hasta £950-1.950 por evaluación TDAH/autismo online (UK); en oficios ES la urgencia multiplica la tarifa (60-250 €/h frente a 25-40 €/h); la tutoría es el servicio con precios más bajos y oferta más abundante.

### Cited Findings
- UK, evaluación TDAH adulto privada online con psiquiatra: **£950** (incluye informe); autismo adulto **£1.950**; titulación de medicación 12 semanas; revisión anual £180; £25 por receta privada; £6 por minuto extra — [Psychiatry-UK, Fees](https://psychiatry-uk.com/fees/) [PRIMARIA, lista de precios del proveedor][ABIERTA]
- UK, terapia: más de la mitad de los listados del directorio BACP anuncian **£40-60 por sesión** — [BACP](https://www.bacp.co.uk/about-therapy/how-to-get-therapy/) [PRIMARIA][ABIERTA]
- ES, psicología privada: **50-80 €/sesión** — [Que.es, 25-07-2026](https://www.que.es/2026/07/25/falta-psicologos-sanidad-publica-pacto/) [SECUNDARIA][ABIERTA]
- UK, examen de conducir: algunos alumnos pagaron **hasta £500** a revendedores por una plaza (encuesta DVSA, 21.656 respuestas) — [NAO](https://www.nao.org.uk/press-releases/watchdog-urges-dvsa-to-address-driving-test-delay-backlog-and-cut-waiting-times/) [PRIMARIA][ABIERTA]. Precio de clase AA no visible sin código postal; la AA declara "más de 1,6 millones de horas de clase impartidas en 2025" — [AA Driving School](https://www.theaa.com/driving-school/driving-lessons) [PRIMARIA][ABIERTA]
- ES, oficios: fontanero **25-40 €/h**, electricista **20-70 €/h**, urgencias **60-250 €/h** — [Cronoshare](https://www.cronoshare.com/comunidad/p/sala-prensa/nacional/cronoshare-escasez-fontaneros-electricistas-espana) [PRIMARIA plataforma][ABIERTA]
- ES, clases a domicilio: **15-23 €/h** media nacional; bonos 10 h 60-90 € — [Cronoshare](https://www.cronoshare.com/cuanto-cuesta/clases-particulares-a-domicilio) [PRIMARIA plataforma][ABIERTA]
- Global, idiomas online: Preply **$3-40+ por clase** (filtro), perfiles destacados $60-100/50 min — [Preply](https://preply.com/en/online/english-tutors) [PRIMARIA plataforma][ABIERTA]
- ES, gestión de alquiler turístico: **15-25 %** de ingresos brutos — [Hostaway ES](https://www.hostaway.com/es-ES/glossary/management-fee/) [SECUNDARIA][ABIERTA]

### Inferences
- El ticket más alto por hora de trabajo humano entre lo leído es la evaluación TDAH (£950 por ~1 hora de consulta más informe), pero exige psiquiatra/psicólogo clínico; para no clínicos, el margen está en la coordinación y la terapia/coaching, con tickets de £40-80.
- La diferencia 25-40 €/h vs 60-250 €/h en urgencias (ES) es la señal de precio más clara de exceso de demanda en oficios.

### Gaps
- No se leyó precio por hora de instructores de autoescuela ni en UK (AA/RED exigen código postal o 404) ni en ES.
- No se leyó precio de evaluación TDAH privada en ES, ni de logopedia privada en 2026 (el 300-600 €/mes de la nota anterior sigue como fragmento).

---

## Pregunta 3 — ¿Qué licencia exige cada servicio y se puede prestar en remoto?

### Takeaway
Casi todos los servicios con la evidencia más dura exigen una cualificación regulada en el país (psiquiatra/psicólogo clínico, instructor de conducción registrado, electricista autorizado, Meister en Alemania) y varios solo pueden prestarse en persona (examen de conducir, oficios, cuidado). Los servicios de "navegación" (ayudar a la familia a tramitar dependencia, Right to Choose, Verifactu/MTD) son los que caben en remoto y sin licencia específica, pero en estas notas esa afirmación es inferencia, no dato leído.

### Cited Findings
- UK, evaluación TDAH/autismo: la oferta leída la prestan "Consultant Psychiatrist" y el servicio opera bajo CQC y vía NHS Right to Choose — [Psychiatry-UK, Fees](https://psychiatry-uk.com/fees/) [PRIMARIA][ABIERTA]. Servicio **online** (la propia página vende "1 hour online assessment").
- UK, examen de conducir: desde el 12-05-2026 "es contra la ley reservar o cambiar un examen en nombre de otra persona" — [The AA](https://www.theaa.com/about-us/newsroom/changes-to-driving-test-booking-system-may-2026) [ABIERTA]. La instrucción remunerada requiere registro ADI de DVSA (conocimiento general; **no leído en página en esta sesión**). Presencial.
- ES, examen de conducir: la escasez citada es de "profesores y examinadores" — [El Español](https://www.elespanol.com/madrid/sociedad/20260522/alumnos-esperando-meses-examinarse-carnet-madrid-jose-vilo-autoescuela/1003744254877_0.html) [ABIERTA]; el certificado de profesor de formación vial lo expide la DGT (**no leído**). Presencial.
- ES, atención temprana: los servicios en lista son estimulación, fisioterapia, psicomotricidad, logopedia, terapia ocupacional o psicoterapia — [Comunidad de Madrid](https://www.comunidad.madrid/node/119569) [PRIMARIA][ABIERTA]: profesiones sanitarias con grado universitario (**colegiación no leída**). Mayoritariamente presencial.
- ES, Verifactu: la obligación recae en el contribuyente y en los desarrolladores de software (infracción art. 201 bis LGT por fabricar/comercializar sistemas no conformes) — [AEAT](https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu.html) [PRIMARIA][ABIERTA]. Configurar/formar no exige licencia leída; remoto.
- UK, MTD: HMRC permite "sign up your client" (agente) — [GOV.UK](https://www.gov.uk/guidance/check-if-youre-eligible-for-making-tax-digital-for-income-tax) [PRIMARIA][ABIERTA]. Remoto. (La supervisión AML obligatoria para contables en UK **no se leyó**.)
- DE, Handwerk: el informe ZDH se refiere a empresas artesanas inscritas; la Meisterpflicht de electricistas/fontaneros es conocimiento general **no leído** — [ZDH](https://www.zdh.de/ueber-uns/fachbereich-wirtschaft-energie-umwelt/konjunkturberichte/zdh-kurzbericht-konjunktur-4-quartal-2025/) [ABIERTA]. Presencial.
- ES, gestión turística: Hostaway describe tareas (OTAs, huéspedes, limpieza, check-in) sin mencionar licencia — [Hostaway](https://www.hostaway.com/es-ES/glossary/management-fee/) [ABIERTA]; registro único estatal y normas autonómicas: solo [FRAGMENTO] en la nota anterior. Mixto (remoto + limpieza/llaves en persona).

### Inferences
- Para un equipo de 1-2 personas sin título sanitario, los huecos con evidencia dura y sin licencia específica son: (a) coordinación/tramitación de dependencia para familias (ES, 320 días de media), (b) acompañamiento a pacientes en Right to Choose/espera TDAH (UK) sin diagnosticar, (c) adaptación Verifactu/MTD a autónomos (ES/UK), (d) gestión de alquiler turístico. Todos son remotos o mixtos.
- Los servicios con mayor exceso de demanda (instrucción de conducir UK/ES/IE, oficios DE/ES, evaluación clínica UK/ES) exigen obtener primero la cualificación: la escasez de profesionales es precisamente la causa de la lista.

### Gaps
- No se leyó en página oficial ningún requisito de licencia (DVSA ADI, DGT profesor, colegios profesionales, Meisterpflicht, AML UK): todas las afirmaciones de licencia son conocimiento general y deben verificarse.

---

## Pregunta 4 — ¿Dónde buscan los clientes (plataformas abiertas, con recuento de proveedores si era visible)?

### Takeaway
Las únicas plataformas con recuento de proveedores leído son Preply (46.449 profesores de inglés — oferta masiva) y Cronoshare ("más de un millón de profesionales" declarados, sin verificar). En los servicios de cola pública el cliente llega vía la propia Administración (NHS Right to Choose, DVSA, Imserso/CCAA) y los proveedores privados se posicionan sobre esa derivación.

### Cited Findings
- Preply: 46.449 profesores de inglés, valoración media 4,9 — [Preply](https://preply.com/en/online/english-tutors) [PRIMARIA][ABIERTA]
- Cronoshare: se autodefine "observatorio del mercado de servicios técnicos" con "una comunidad de más de un millón de profesionales"; el cliente "pide presupuestos gratis" — [Cronoshare](https://www.cronoshare.com/comunidad/p/sala-prensa/nacional/cronoshare-escasez-fontaneros-electricistas-espana) [PRIMARIA plataforma, no verificado][ABIERTA]
- UK TDAH: Psychiatry-UK capta vía NHS Right to Choose (secciones "Right To Choose ADHD/Autism", "For GPs") y aseguradoras (Bupa, Peppy, HelloSelf) — [Psychiatry-UK](https://psychiatry-uk.com/fees/) [PRIMARIA][ABIERTA]
- UK terapia: directorio BACP de terapeutas — [BACP](https://www.bacp.co.uk/about-therapy/how-to-get-therapy/) [PRIMARIA][ABIERTA]
- UK examen: la DVSA publica datos mensuales por centro en GOV.UK y la AA Driving School declara 1,6 millones de horas de clase en 2025 — [DVSA Despatch](https://despatch.blog.gov.uk/2026/06/18/giving-you-a-clearer-picture-of-driving-test-waiting-times/), [AA](https://www.theaa.com/driving-school/driving-lessons) [PRIMARIA][ABIERTA]
- ES dependencia: la demanda está en las CCAA/Imserso (265.503 expedientes) — [El Debate](https://www.eldebate.com/sociedad/20260615/13500-muertes-listas-espera-dependencia-cinco-meses-estas-son-comunidades-afectadas_428672.html) [ABIERTA]
- Superprof (ES) no pudo abrirse (403) → sin recuento de profesores.

### Inferences
- En tutoría online la competencia por cliente es alta (decenas de miles de proveedores en una sola plataforma); en oficios y clínica, las plataformas sirven de canal pero el límite es la cualificación del proveedor.

### Gaps
- Sin recuento de proveedores leído para Superprof, Rover/Gudog, Airbnb co-hosts, directorios de instructores (DVSA "find a driving instructor"), ni para psicólogos privados ES.

---

## Tabla resumen (solo cifras leídas en página; país en cada fila)

| # | Servicio | País | Cifra leída (fuente) | Precio leído | Licencia (verificación) | Remoto/presencial |
|---|---|---|---|---|---|---|
| 1 | Evaluación TDAH/autismo | UK (Gales, Inglaterra) | Mediana 101 sem. TDAH / 103 sem. autismo a 31-01-2026 (FOI Hywel Dda); >560.000 en lista Inglaterra, >60 % >1 año (Carnall Farrar) | £950 TDAH, £1.950 autismo (Psychiatry-UK); terapia £40-60 (BACP) | Psiquiatra/psicólogo clínico (no leído) | Remoto (evaluación online) |
| 2 | Examen práctico / instrucción | UK (GB) | Media 22 sem. sep-2025, 70 % centros a 24 sem. (NAO); 22,4 sem. abr-2026 (AA); mediana 9,7 vs 21,8 sem. may-2026 (DVSA) | Hasta £500 a revendedores (NAO) | ADI DVSA (no leído); reservar por terceros ilegal desde 12-05-2026 (AA) | Presencial |
| 3 | Dependencia / cuidado mayores | ES | 320 días de media; 265.503 en lista; 13.503 fallecidos ene-may 2026 (El Debate/Imserso) | — | Coordinación: ninguna leída | Mixto |
| 4 | Examen práctico / profesores autoescuela | ES (Madrid) | 28.800 alumnos esperan hasta 6 meses; bolsa 72.000 (El Español) | — | Profesor formación vial DGT (no leído) | Presencial |
| 5 | Examen práctico | IE | Media 12 sem. vs objetivo 10; Raheny 25 sem. (Irish Times) | — | ADI RSA (no leído) | Presencial |
| 6 | Psicología | ES | >6 meses primera consulta pública; 3,4 clínicos/100k (Que.es) | 50-80 €/sesión (Que.es) | PGS/clínico (no leído) | Remoto posible |
| 7 | Atención temprana / logopedia | ES (Madrid) | 1.320 en lista a 31-01-2026 (PDF oficial); 65 días solicitud→resolución (nota 23-09-2026) | — | Grado sanitario (no leído) | Presencial |
| 8 | Oficios construcción | DE | Cartera 8,5 sem. Handwerk; 12,5 sem. obra (ZDH 4T-2025) | — | Meisterpflicht (no leído) | Presencial |
| 9 | Fontanería/electricidad | ES | Cualitativo: demanda > oferta, precios al alza (Cronoshare) | 25-40 / 20-70 / urgencias 60-250 €/h | Instalador autorizado (no leído) | Presencial |
| 10 | Adaptación Verifactu / facturación | ES | Plazos 01-01-2027 (IS) y 01-07-2027 (resto) (AEAT) | — | Ninguna leída | Remoto |
| 11 | Contabilidad MTD | UK | 06-04-2026 >£50k; 2027 >£30k; 2028 >£20k (HMRC) | — | AML (no leído) | Remoto |
| 12 | Gestión alquiler turístico | ES | Sin cifra de demanda | 15-25 % ingresos (Hostaway) | No leída | Mixto |
| 13 | Tutoría | Global / ES | Contra-señal: 46.449 profesores inglés (Preply) | $3-40+/clase (Preply); 15-23 €/h (Cronoshare ES) | Ninguna | Remoto |
| — | Examen conducir | NL | Dentro del objetivo de 7 sem. (Parlamento) [FRAGMENTO] | — | — | Sin exceso de demanda |
