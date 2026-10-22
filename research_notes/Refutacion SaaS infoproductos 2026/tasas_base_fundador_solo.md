# Tasas base para un fundador solo sin capital: producto digital vs. servicio B2B productizado

**Fecha de investigación:** 22-10-2026 · **Método:** fuentes abiertas descargadas y leídas desde la sesión (herramienta `pwfetch.js` + `curl`; CSV del Census y tablas AEAT parseadas con Python; PDFs con `pdftotext`). Páginas abiertas con contenido leído: >50, más 8 bloqueadas o parciales (tabla al final). Etiquetas: **[ABIERTA]** = página/fichero leído íntegro o en la parte relevante; **[FRAGMENTO]** = sólo extracto vía buscador o página bloqueada; **NO ENCONTRADO** = buscado sin resultado utilizable.

**Afirmación a juzgar (analista):** "Para un fundador solo sin capital, la probabilidad de superar 100.000 €/año con un producto digital (SaaS o infoproducto) en 24 meses es inferior al 5 %, mientras que un servicio B2B productizado vendido por correo frío a empresas con una obligación legal tiene probabilidad mucho mayor aunque techo más bajo."

---

## 0. Veredicto resumido

| Rama | Mejor estimación P(>100 k€ ingresos/año a los 24 meses, fundador solo, sin capital) | Intervalo razonable | Calidad de la evidencia |
|---|---|---|---|
| Infoproducto / creador (cursos, Gumroad, Patreon, apps consumo) | **~1 %** | 0,3 % – 3 % | Alta: datos censales de plataforma (Gumroad 2020, Udemy 10-K, Patreon/Graphtreon, Census NAICS 611/7115) |
| SaaS indie B2B (bootstrapped, sin cofundador) | **~4 %** | 2 % – 8 % | Media: muestras autoseleccionadas (Indie Hackers Stripe-verified, MicroConf, Stripe Atlas) |
| Servicio B2B productizado por correo frío a obligados legales (consultoría cumplimiento, DPD externo, etc.) | **~15 %** | 8 % – 25 % | Media-baja: stocks de autónomos/nonemployers (Census NAICS 5415/5416, AEAT RAE 2022), tasas de respuesta de correo frío (Belkins 2025); **ningún dato directo** sobre "productized services" ni sobre el efecto de la obligación legal |

**Veredicto: la comparación queda CONFIRMADA en la dirección y MATIZADA en la magnitud.**
- "Inferior al 5 %" para producto digital: **confirmado** para infoproductos (las tasas observadas son ≤1 %), y **plausible pero no probado** para SaaS B2B (las muestras que superan el 5 % están fuertemente sesgadas hacia supervivientes).
- "Probabilidad mucho mayor" del servicio: **confirmado en orden de magnitud** (≈4-15× respecto al infoproducto, ≈2-5× respecto al SaaS), pero sigue siendo un resultado **minoritario** (~1 de cada 6-7), no "probable". El techo más bajo se confirma: los nonemployers de consultoría superan 250 k$ sólo en 4,5 % y 1 M$ en 0,5 % (Census 2022).
- La prima específica por "obligación legal" **no está cuantificada en ninguna fuente abierta**: hay evidencia de demanda estructural (DPD registrados en España 100 k → 120 k en 2 años; NIS2; Verifactu) pero también de que los picos se disipan y los plazos se aplazan (Verifactu: nueva previsión de ampliación comunicada el 05-10-2026).

---

## 1. Supervivencia y resultados de fundadores solos

### 1.1 Stripe Atlas (datos de plataforma, no encuestas)
- **Stripe Atlas 2025 Year in Review** (18-12-2025) [ABIERTA]: 23.000 empresas incorporadas en 2025; **20 % cobra a su primer cliente en los 30 días** tras incorporarse (8 % en 2020); mediana de ingresos de los primeros 6 meses **+39 % interanual**; el **número** de startups que alcanzan 100.000 $ de ingresos en los primeros 6 meses creció 56 % (es un recuento, no una proporción; Stripe no publica la proporción); sólo **2,2 %** levanta capital en los 3 meses tras incorporarse (3,1 % en 2024). Percentil 10: +18 %; percentil 90: +52 %.
- **Patrick Collison, "Atlas Year"** (19-12-2025) [ABIERTA]: confirma +39 % mediana, +52 % p90, +67 % p99; Atlas incorpora >20 % de las C-corps de Delaware.
- **Stripe, "Solo founding is at an all-time high"** (28-05-2026) [ABIERTA]: los fundadores solos son el **63 % de las C-corps** formadas vía Atlas en el 2T-2026 (máximo histórico). Entre startups de fundador solo incorporadas en 2025, **la mediana de ingresos de los primeros 6 meses cayó 23 % interanual mientras el decil superior subió 19 %**; el decil superior ingresa **61×** la mediana (34× hace cuatro años). "El número de solopreneurs que ingresan >100.000 $/año ha crecido un tercio desde 2022" (recuento, no proporción). Muestra: "miles" de startups de fundador solo incorporadas 2022-23 con ≥2 años de datos. **No publica medianas absolutas** → no permite calcular directamente P(>100 k$ a 24 meses).
- **Stripe Atlas: first five years** (01-07-2021) [ABIERTA]: 20.000 empresas, >3.000 M$ de ingresos acumulados → **media ≈150.000 $ acumulados por empresa en ≤5 años** (muy concentrada); encuesta a >1.000 fundadores: dos tercios bootstrapped.

### 1.2 Carta
- **Founder Ownership Report 2025** [ABIERTA] (45.000 startups incorporadas 2015-2024): fundador solo = **35 % de las startups creadas en 2024** (17 % en 2017), pero sólo **17 % de las que cerraron una ronda VC** el mismo año → el fundador solo tiene ~la mitad de probabilidad relativa de financiarse. No hay datos de ingresos.

### 1.3 Census Bureau, Nonemployer Statistics 2022 (fichero `nonemp22us.txt`, descargado y calculado) [ABIERTA]
Distribución de **establecimientos sin asalariados** (29,8 M en EE. UU.) por clase de **ingresos brutos anuales (receipts, no beneficio)**. Códigos de tramo verificados por suma (111 <5 k$; 118 5-10 k; 119 10-25 k; 121 25-50 k; 122 50-100 k; 123 100-250 k; 125 250-500 k; 131 500 k-1 M; 133/141/1411 ≥1 M).

| NAICS | Sector | Establec. | Media receipts | % <10 k$ | % ≥50 k$ | **% ≥100 k$** | % ≥250 k$ | % ≥1 M$ |
|---|---|---|---|---|---|---|---|---|
| 00 | Todos | 29.811.495 | 57.923 $ | 37,9 | 24,5 | **13,4** | 4,7 | 0,39 |
| 54 | Prof., científicos y técnicos | 4.013.209 | 57.150 $ | 38,4 | 25,6 | **13,6** | 4,3 | 0,47 |
| 5415 | Diseño de sistemas informáticos | 342.033 | 59.133 $ | 37,6 | 27,6 | **15,3** | 4,6 | 0,46 |
| 5416 | Consultoría de gestión/técnica | 1.036.353 | 59.731 $ | 38,0 | 26,1 | **14,1** | 4,5 | 0,53 |
| 5418 | Publicidad y RR. PP. | 199.163 | 63.551 $ | 39,2 | 26,0 | **14,4** | 5,3 | 0,72 |
| 5412 | Contabilidad, fiscal, nóminas | 393.674 | 33.441 $ | 42,7 | 17,5 | **7,3** | 1,6 | 0,07 |
| 5411 | Servicios jurídicos | 283.944 | 80.601 $ | 28,4 | 37,8 | **22,5** | 7,4 | 0,55 |
| 51 | Información (incl. software/web) | 396.260 | 45.393 $ | 46,5 | 19,6 | **9,9** | 3,3 | 0,37 |
| 5182 | Hosting/procesamiento datos | 59.510 | 42.767 $ | 48,8 | 16,8 | **9,1** | 3,3 | 0,42 |
| 611 | Servicios educativos (cursos, formación) | 859.958 | 17.749 $ | 64,3 | 7,4 | **2,8** | 0,7 | 0,03 |
| 7115 | Artistas, escritores e intérpretes indep. | 1.067.295 | 30.501 $ | 55,5 | 11,6 | **4,9** | 1,4 | 0,23 |

Lectura: incluso el **stock** (todas las edades de negocio, no sólo 24 meses) de autónomos de consultoría/IT en EE. UU. supera 100 k$ de **facturación** sólo en ~14-15 %; en formación/creadores, 3-5 %. Un negocio de 24 meses está por debajo del stock (BLS: el mayor abandono ocurre en el primer año; sólo ~66 % de establecimientos sobreviven 2 años según BLS 2004 [FRAGMENTO, bls.gov devolvió 403]).

### 1.4 Encuestas de solopreneurs (EE. UU.)
- **Simply Business, "The Power of One: 2025 Solopreneur Report"** (PDF, n=1.023 clientes, junio 2025) [ABIERTA]: sólo **41 %** vive del negocio como ingreso principal a tiempo completo; **48 %** ha pasado ≥1 mes sin ingresos; 61 % tiene <6 meses de colchón. No publica tramos de facturación.
- **Branch & Mastercard Solopreneur Report** (ene-2026, n>1.400) vía founderreports.com [FRAGMENTO, fuente secundaria]: **55 % gana <50.000 $/año, 79 % <100.000 $** → ~21 % ≥100 k$ (ingreso personal autodeclarado, stock de solopreneurs, no cohortes de 24 meses). Gusto (sesgado a S-corps con nómina): el solopreneur típico se paga 41.000 $ el año 1 y 76.000 $ el año 2.

### 1.5 España: AEAT e INE
- **AEAT, Estadística de declarantes IRPF 2023 (total nacional)** [ABIERTA]: 2.960.730 declarantes con rendimientos de actividades económicas; **rendimiento neto medio 14.826 €** (es **beneficio fiscal**, no facturación); estimación directa: 1.921.802 declarantes, media **20.054 €**; módulos: 9.494 €.
- **AEAT, Estadística de Rendimientos de Actividades Económicas 2022, por epígrafe IAE (estimación directa)** [ABIERTA]. Rendimiento neto **positivo** medio = importe / nº actividades (importe en miles €), "tasa de fracaso" = % de actividades con rendimiento negativo o nulo:

| Epígrafe IAE | Nº actividades | Rendimiento positivo medio | Tasa de fracaso |
|---|---|---|---|
| Total estimación directa | 2.239.619 | 17.432 € | 16,0 % |
| 2763 Programadores y analistas informática | 20.731 | 31.616 € | 6,8 % |
| 2762 Licenciados en informática | 3.538 | 42.620 € | 6,0 % |
| 2741 Economistas | 15.215 | 45.591 € | 6,6 % |
| 2731 Abogados | 93.757 | 34.572 € | 11,3 % |
| 2751 Publicidad y RR. PP. (profesional) | 32.113 | 21.012 € | 7,5 % |
| 1844 Servicios de publicidad (empresarial) | 11.591 | 15.666 € | 13,7 % |
| 1849 Otros servicios a empresas n.c.o.p. | 36.303 | 10.179 € | 18,0 % |
| 2826 Docentes de enseñanzas diversas | 52.610 | 8.347 € | 11,7 % |
| 1933 Otras actividades de enseñanza | 17.754 | 8.727 € | 19,9 % |

- **AEAT RAE 2022, empresarios con actividad única y beneficios, por agrupación IAE y tramo de BASE IMPONIBLE total del IRPF** (7 tablas descargadas) [ABIERTA]. Ojo: la base imponible incluye otras rentas (salario, capital), por lo que **sobreestima** el beneficio de la actividad:

| Agrupación | Nº empresarios | % con BI > 60.101 € | % con BI > 30.050 € |
|---|---|---|---|
| Total | 2.795.373 | 8,7 % | 24,8 % |
| 2. Profesionales | 799.323 | **19,5 %** | 44,6 % |
| 27. Financieras, jurídicas, seguros (incluye 276 informática) | 313.370 | 17,5 % | 43,2 % |
| 28. Otros servicios (incluye sanitarios y docentes) | 297.771 | 23,7 % | 45,7 % |
| 18. Servicios a empresas (empresarial) | 91.335 | 10,0 % | 27,1 % |
| 16. Comercio, hostelería | 482.380 | 5,4 % | 14,9 % |
| 19. Otros servicios (empresarial) | 206.371 | 2,9 % | 12,6 % |
| 1. Empresariales | 1.183.434 | 5,0 % | 15,8 % |

Conversión aproximada: un servicio profesional con 100 k€ de facturación suele dejar 70-85 k€ de rendimiento neto; por tanto "BI > 60 k€" ≈ "facturación > ~75-85 k€". **~1 de cada 5 profesionales autónomos españoles (stock, todas las antigüedades) está en esa zona.**
- **Adecco/Infoempleo, Informe sobre trabajo autónomo** (PDF, encuesta, ~2015) [ABIERTA]: **91,9 % de autónomos factura <100.000 €/año**; 6,3 % entre 100-300 k; 0,8 % 300-500 k; 0,5 % 500 k-1 M; 0,5 % >1 M → **8,1 % > 100 k€ de facturación** (todos los sectores; 82 % sin empleados).
- **Infoautónomos / U. Granada, Estudio Nacional del Autónomo 2024** (PDF, n=1.163) [ABIERTA]: **55,3 % declara ingresos mensuales <1.850 €**; tramo modal 900-1.166,7 €/mes (12,3 %).
- **UPTA vía Forbes (18-12-2025)** [ABIERTA]: con datos AEAT 2023, **1.066.197 autónomos declaran rendimientos <900 €/mes**; ~800.000 ≤670 €/mes.
- INE: la tabla abierta (EPA, horas trabajadas) no aporta ingresos por actividad de autónomos sin asalariados → **NO ENCONTRADO** en INE un desglose de ingresos por actividad; la fuente útil es AEAT (arriba).

---

## 2. Productos digitales: distribución de ingresos por creador/vendedor

| Plataforma / fuente | Año, muestra, definición | Resultado | Cálculo implícito |
|---|---|---|---|
| **Gumroad** (datos oficiales 2020 reproducidos en StartupGTM) [ABIERTA] | 2020; 142 M$ pagados; ingresos brutos por creador | 45.917 creadores ganaron algo; 7.945 ≥1 k$; 1.853 ≥10 k$; **179 ≥100 k$**; 8 ≥1 M$ | ≥100 k$ = **0,39 % de los que vendieron algo**; ≥10 k$ = 4,0 % |
| **Profitable.app, Gumroad stats** (8-10-2026) [ABIERTA] | 4 M productos, 1,3 M vendedores; ingresos estimados de por vida | 2,3 % de productos con ≥1 venta; **0,4 % de productos >1.000 $ acumulados**; mediana de ingresos por vendedor **90 $**; 386 productos 100 k-1 M$, 21 >1 M$ | (386+21)/4 M = **0,01 % de productos ≥100 k$ acumulados** |
| **Udemy, 10-K FY2025 (SEC)** [ABIERTA] | 2025; >91.000 instructores; pagos a instructores | **168 M$** pagados (208,2 M$ en 2023, 190,6 M$ en 2024); 11 instructores >1 M$; **~1.600 instructores superan la renta media de su país** | Media = **1.846 $/instructor/año**; 1.600/91.000 = **1,8 %** supera una renta media (que en EE. UU./UE es <100 k$) |
| **Patreon vía Graphtreon** (22-10-2026) [ABIERTA] | 346.845 creadores con ≥1 patrón; payouts estimados excluyendo ocultos | **25,49 M$/mes** | Media **73 $/mes** por creador de pago |
| **Regner (Jena 2019 / J. Cultural Economics 2021)** [ABIERTA abstract; cifras vía Culturecase/IAPP FRAGMENTO] | Patreon, datos transaccionales 2013-15 | 25 % de campañas activas >120 $/mes; **5 % >750 $/mes; 1 % >2.500 $/mes** (=30 k$/año) | P(>100 k$/año) ≪ 1 % |
| **Etsy, 10-K FY2025 (SEC)** [ABIERTA] | 5,6 M vendedores activos; GMS marketplace 10.460,7 M$ | — | **≈1.870 $ GMS/vendedor/año** (cálculo propio; GMS ≠ ingreso neto) |
| **VisionMobile Developer Economics 2014** (vía SmartCompany) [ABIERTA] | 10.000 desarrolladores de apps | **69 % <1.000 $/mes**; 47 % <100 $/mes; 1,6 % >500 k$/mes concentran más que el 98,4 % restante; apps enterprise: 57 % ≥500 $/mes vs 26 % consumo | Dato antiguo; dirección consistente con lo demás |
| **Indie Hackers, productos con ingresos verificados por Stripe** (análisis 2022 vía Changelog) [ABIERTA] | 937 productos verificados | **54 % con 0 $**; **5 % >100 k$/año** | Muestra autoseleccionada hacia el éxito (sólo quien verifica) |
| **TrustMRR** (home abierta; análisis vía bigideasdb, 429) [FRAGMENTO] | 3.787 startups con ingresos; 5.079 Stripe-verified | 6,1 % >10 k$/mes; 0,9 % "breakout" (>10 k$/mes y >50 % crecimiento) | — |
| **MicroConf, State of Independent SaaS 2024** [FRAGMENTO: páginas de MicroConf y podcast ep. 721 abiertas; PDF no accesible sin registro] | ~700 respuestas (datos finales 2023), fundadores activos de SaaS bootstrapped | **17,7 % <1.000 $ MRR** (el tramo más numeroso); **50,7 % son fundadores solos**; en la edición 2020: >50 % <10 k$ MRR | Supervivientes y autoseleccionados; aun así la mayoría no llega a 100 k$ ARR |
| **Acquire.com, Biannual Multiples Report ene-2026** [ABIERTA, pero cuerpo tras formulario] | Listados 2025 | Sin mediana de ingresos accesible | NO ENCONTRADO el dato |
| **Substack** | — | Sólo agregadores sin fuente primaria | **NO ENCONTRADO** |
| **Shopify** | — | No publica distribución por tienda | **NO ENCONTRADO** |

Síntesis sección 2: para infoproductos y creadores, la fracción que supera 100 k$/año está **entre 0,01 % (productos Gumroad) y ~2 % (instructores Udemy sobre renta media)**, con el 1-5 % de Patreon/IH como cota alta en muestras sesgadas. Para SaaS indie, la cota alta observable (muestras de supervivientes/verificados) es **5 %**.

---

## 3. Servicios B2B productizados y consultoría independiente

- **Consulting Success, Consulting Fees Study** (actualizado 19-10-2026) [ABIERTA]: ~1.000 consultores (audiencia de una firma de coaching → sesgo hacia consultores establecidos): **38 % ingresa ≥10.000 $/mes** (≈120 k$/año run-rate); 52 % de los especialistas cobra ≥10 k$/proyecto vs 18 % de generalistas; 30 % cobra por proyecto, 29 % por hora, 16 % retainer, 15 % valor.
- **Malt, Freelancing in Europe 2024** (vía StartingUp) [ABIERTA]: n=5.029 freelancers; **72 % gana igual o más que asalariado**; 210.000 altas en Malt en 2023; colaboración freelance-gran empresa +220 % en España desde 2022. No publica distribución de ingresos.
- **freelancermap, Freelancer-Kompass 2026** (DACH, n≈5.400) [ABIERTA]: tarifa media **103 €/h** (96 € en 2022); **49 % reporta peor cartera de proyectos que el año anterior; casi la mitad sin carga de trabajo confirmada**. A 1.000 h facturables/año ⇒ ~103 k€; a 700 h ⇒ 72 k€.
- **Census NES 2022 (sección 1.3)**: consultoría de gestión (5416) **14,1 % ≥100 k$**; diseño de sistemas informáticos (5415) 15,3 %.
- **AEAT RAE 2022 (sección 1.5)**: profesionales con BI >60 k€: 19,5 %; economistas rendimiento medio 45,6 k€; informáticos 31,6-42,6 k€.
- **Correo frío (canal propuesto)**: **Belkins 2026 study** (7,5 M correos en 2025) [ABIERTA]: **tasa de respuesta 0,45 % sobre enviados** (0,54 % en febrero, 0,35 % en diciembre; fundadores/propietarios 0,57 %; empresas de 11-50 empleados 0,49 %; >10.000 empleados 0,22 %). **Backlinko/Pitchbox** (12 M correos, outreach SEO, 2019) [ABIERTA]: 8,5 % de respuesta. **Instantly** (jan-2026) [ABIERTA]: "bueno" = 5-10 % en B2B. Cálculo: con 0,45 % de respuesta y ~20 % de cierre sobre respuestas (supuesto), **cada cliente cuesta ~1.100 correos**; para 100 k€ con tickets de 3-5 k€ hacen falta 20-33 clientes/año ⇒ **22.000-37.000 correos/año**, factible para una persona pero exigente en infraestructura de entregabilidad.
- **ManyRequests, Productized Service Revenue 2026** [ABIERTA]: 10 agencias productizadas publicadas, 100 k$-3,6 M$/año; equipos de 1 a 11 personas. Muestra de supervivientes; sirve para el **techo** (una persona: 100-320 k$), no para la probabilidad.
- **Tasa de éxito de "productized services"**: **NO ENCONTRADO** ningún estudio con muestra.

---

## 4. Cumplimiento normativo como negocio

- **Mercado GRC global (Grand View Research)** [ABIERTA]: 72,4 B$ (2025) → 82,9 B$ (2026) → 203,7 B$ (2033), **CAGR 13,7 %**; software 65,3 %; dentro de servicios, consultoría es el mayor segmento. Es una previsión de consultora; sin desglose España.
- **RGPD en España – registro de DPD (AEPD)** [ABIERTA, 4 notas de prensa + Memoria 2023 PDF]: 10-01-2023: **100.350** DPD (91.221 privados); cierre 2022: 103.350; **cierre 2023: 111.070** (101.691 privados, 9.379 públicos); **cierre 2024: 119.803** (109.853 privados). Crecimiento **+7,5 % (2023) y +7,9 % (2024)**: demanda sostenida pero ya no explosiva. Reclamaciones: 21.590 en 2023 (+43 %), 18.855 en 2024. Memoria 2023: 991 consultas sobre comunicación de DPD.
- **IAPP (16-05-2019)** [ABIERTA]: al año del RGPD, **≥376.306 registros de DPD en 12 Estados**; estimación **~500.000 organizaciones en Europa**; la previsión de 2017 (75.000 DPO) "se quedó muy corta". Un DPD externo puede servir a muchas organizaciones (Francia: 52.000 registros vs ~18.000 personas, vía FRAGMENTO).
- **Pico 2018**: ReasonWhy/SEMrush (24-05-2018) [ABIERTA]: el interés de búsqueda por "GDPR/RGPD" en España despega desde **febrero de 2018**. Facturación de consultoras de protección de datos 2018: **NO ENCONTRADO** dato abierto. Mercado global "GDPR services" 907 M$ en 2018 (Research&Markets) [FRAGMENTO, 403].
- **ISO/IEC 27001 (ISO Survey vía DQS, 08-10-2026)** [ABIERTA], certificados en el mundo: 2018 31.910 → 2019 36.362 → 2020 44.486 → 2021 58.687 → 2022 71.549 → 2023 48.671 (cambio metodológico) → 2024 96.709 → **2025 125.622 (+29,9 %)**. España: 7.ª del mundo en 27001 (UNE, ISO Survey 2023 PDF) [ABIERTA]; +34 % en 2025 (DQS). Es el indicador abierto más claro de **demanda creciente de servicios de cumplimiento** no ligada a una fecha única.
- **NIS2**: Emprendedores.es (17-10-2024) [ABIERTA]: por tamaño (medianas y grandes) afecta "a algo más de un millar" de empresas españolas, más pymes de sectores críticos; otras estimaciones (Portal ERP 33.072, IONOS ~25.000) [FRAGMENTO]. Transposición española aún pendiente en 2025 (dictamen motivado de la Comisión). **ENISA NIS Investments 2024** [ABIERTA]: muestra de 1.350 organizaciones de los 27 EM; edición 2025 (08-12-2025): "la inversión pasa de personas a tecnología; el cumplimiento y NIS2 impulsan la acción pero la implementación es un reto".
- **Verifactu** (AEAT, página oficial leída el 22-10-2026) [ABIERTA]: plazos vigentes 1-1-2027 (IS) y 1-7-2027 (IRPF) tras el aplazamiento de 2025; **"Comunicación del Ministerio de Hacienda de 05/10/2026: previsión de ampliación del plazo de adaptación"** → riesgo real de que la fecha-gatillo vuelva a moverse. Nº de empresas afectadas y tamaño del mercado de software: **NO ENCONTRADO** con cifra oficial.
- Lectura para la tesis del analista: la obligación legal **crea demanda recurrente y medible** (DPD +8 %/año, 27001 +30 %/año), pero (a) el pico inicial se concentra en los 12-18 meses alrededor de la fecha (RGPD 2018; IAPP) y después se normaliza; (b) los plazos se aplazan (Verifactu dos veces); (c) el comprador pyme es sensible a precio, lo que fija el techo.

---

## 5. Estudios comparados de probabilidad por tipo de negocio

- Ninguna fuente abierta compara **cohortes** de solopreneurs por modelo de negocio con horizonte de 24 meses. Lo más cercano:
  - **Census NES 2022** (stock): consultoría/IT **14-15 % ≥100 k$** vs. educación **2,8 %** y artistas/escritores **4,9 %** → ratio **~3-5×** a favor del servicio.
  - **AEAT RAE 2022** (stock): profesionales **19,5 %** con BI >60 k€ vs. docentes/otros servicios 2,9-10 %.
  - **VisionMobile 2014**: apps enterprise 57 % ≥500 $/mes vs consumo 26 % → el B2B dobla al B2C incluso dentro de producto.
  - **Stripe 2025**: la dispersión entre fundadores solos crece (mediana −23 %, decil superior +19 %), lo que **empeora** la tasa base del fundador solo "típico" en producto.
- **Starter Story** y **MicroConf** no publican tasas de éxito por modelo; **NO ENCONTRADO** estudio académico con cohortes.

---

## 6. Cálculo de las dos probabilidades

**Rama A — producto digital, fundador solo, sin capital, 24 meses, >100 k€/año de ingresos**
1. Tasa base de plataforma (infoproducto): 0,39 % de los creadores Gumroad que vendieron algo (2020) alcanzan 100 k$; ~1,8 % de instructores Udemy superan la renta media de su país (<100 k$); 1 % de Patreon >30 k$/año. Sobre el total de quien *intenta* (incluidos los que venden 0), la fracción cae otro orden de magnitud (Gumroad: sólo 2,3 % de productos vende algo).
2. SaaS indie: 5 % >100 k$/año entre productos **verificados** en Indie Hackers (sesgo hacia arriba); en MicroConf 2024, 17,7 % de fundadores activos <1 k$ MRR y en 2020 >50 % <10 k$ MRR (supervivientes de varios años). Ajuste a cohorte de 24 meses y sin capital: ÷1,5-2.
3. Stock censal de software/información sin asalariados: 9-10 % ≥100 k$ (incluye negocios de 10+ años y servicios IT disfrazados).
⇒ **Infoproducto 0,3-3 % (central ~1 %); SaaS B2B 2-8 % (central ~4 %).** La afirmación "<5 %" se sostiene; para SaaS B2B el límite superior del intervalo la roza.

**Rama B — servicio B2B productizado por correo frío a obligados legales**
1. Stock de autónomos de consultoría/IT ≥100 k$ facturación: 14-15 % (Census); profesionales españoles con BI >60 k€: 19,5 % (AEAT); autónomos españoles >100 k€ facturación (todos los sectores): 8,1 % (Adecco).
2. Ajuste por horizonte 24 meses y arranque desde cero (sin red de clientes): ×0,6-0,8 → 9-15 %.
3. Ajuste por canal (correo frío 0,45 % de respuesta; la mayoría de consultores vive de referencias — Consulting Success: >60 % del negocio por referidos en más de la mitad de consultores): neutro a ligeramente negativo; compensado parcialmente por la demanda inducida por la norma (DPD +8 %/año; 27001 +30 %/año).
4. Techo: ≥250 k$ sólo 4,5 % de nonemployers de consultoría; ≥1 M$ 0,5 %; capacidad física ~1.000-1.400 h/año × 80-120 €/h ⇒ 80-170 k€ sin contratar.
⇒ **8-25 % (central ~15 %)**, techo típico 100-250 k€.

**Ratio B/A ≈ 4-15× frente a infoproducto y ≈ 2-5× frente a SaaS.** Dirección del analista confirmada; la magnitud "mucho mayor" es cierta en términos relativos, pero en absoluto la rama B sigue fallando ~85 % de las veces en 24 meses.

---

## 7. Qué datos faltan (y dónde conseguirlos)

1. **Cohortes de 24 meses** de fundadores solos por modelo de negocio con ingresos observados (Stripe tiene el dato —percentiles absolutos de Atlas por tipo de negocio— pero sólo publica variaciones relativas). Petición directa a Stripe Atlas / Carta.
2. **Distribución completa de MRR** del informe MicroConf SOIS 2024 (PDF tras registro) y su cruce con "fundador solo" y "antigüedad <2 años".
3. **AEAT RAE 2022-2023 por epígrafe IAE con tramos de rendimiento** (no de base imponible) y por antigüedad de alta: existe en la publicación pero no se ha localizado la tabla por tramos de rendimiento; permitiría una P(>75 k€ beneficio) limpia para informáticos/consultores españoles. Además, alta de autónomos por año (TGSS) cruzada con rendimiento a 24 meses.
4. **Facturación agregada de consultoras de protección de datos/DPD externo en España** (CNAE 6920/7022/6910 no las aísla); sólo hay número de DPD registrados.
5. **Tasa de éxito de "productized services"**: no existe muestra pública; habría que construirla (p. ej., registros de Indie Hackers + Latka + Starter Story con fecha de inicio).
6. **Ingreso mediano por vendedor** en Udemy/Etsy/Substack: las compañías publican totales y recuentos, no distribuciones; sólo Gumroad (2020) publicó la distribución completa.
7. **Verifactu**: número oficial de obligados y calendario definitivo (nota del Ministerio 05-10-2026 anuncia nueva ampliación).

---

## 8. Tabla de URLs

| # | Fuente | URL | Estado |
|---|---|---|---|
| 1 | Stripe Atlas 2025 Year in Review | https://stripe.com/blog/stripe-atlas-startups-in-2025-year-in-review | ABIERTA |
| 2 | Patrick Collison, Atlas Year | https://patrickcollison.com/dispatches/atlas-year | ABIERTA |
| 3 | Stripe Atlas first five years | https://stripe.com/en-pt/blog/atlas-first-five-years | ABIERTA |
| 4 | Stripe, Solo founding all-time high | https://stripe.com/blog/top-solo-founder-traits | ABIERTA |
| 5 | Stripe Atlas guides (sin datos) | https://stripe.com/atlas/guides | ABIERTA |
| 6 | Carta Founder Ownership Report (full) | https://carta.com/data/founder-ownership-full-report/ | ABIERTA |
| 7 | Carta Founder Ownership Report | https://carta.com/data/founder-ownership/ | ABIERTA |
| 8 | Carta Data LinkedIn archive (solo founders) | https://carta.com/data/linkedin-solo-founder-explosion-2024/ | ABIERTA (archivo genérico) |
| 9 | Census NES about | https://www.census.gov/programs-surveys/nonemployer-statistics/about.html | ABIERTA |
| 10 | Census NES tables | https://www.census.gov/programs-surveys/nonemployer-statistics/data/tables.html | ABIERTA |
| 11 | Census NES 2022 US dataset (zip/csv) | https://www2.census.gov/programs-surveys/nonemployer-statistics/datasets/2022/historical-datasets/nonemp22us.zip | ABIERTA (descargado y calculado) |
| 12 | Census API variables NES 2022 | https://api.census.gov/data/2022/nonemp/variables.json | ABIERTA (la API de datos exige clave) |
| 13 | SBA Advocacy FAQ 2024 | https://advocacy.sba.gov/2024/07/23/frequently-asked-questions-about-small-business-2024/ | ABIERTA |
| 14 | BLS BED survival tables | https://www.bls.gov/bdm/us_age_naics_00_table7.txt ; https://www.bls.gov/bdm/bdagefaq.htm | FRAGMENTO (403) |
| 15 | Kauffman Indicators | https://indicators.kauffman.org/indicator/startup-early-survival-rate | ABIERTA (sin cifra en página) |
| 16 | Founder Reports, Solopreneur statistics 2026 | https://founderreports.com/solopreneur-statistics/ | ABIERTA (secundaria) |
| 17 | Simply Business 2025 Solopreneur Report (PDF) | https://www.simplybusiness.com/wp-content/uploads/sites/2/2025/08/Simply_Business_2025_Solopreneur_Report.pdf | ABIERTA |
| 18 | AEAT IRPF declarantes por municipios 2023, total nacional | https://sede.agenciatributaria.gob.es/AEAT/Contenidos_Comunes/La_Agencia_Tributaria/Estadisticas/Publicaciones/sites/irpfmunicipios/2023/jrubikf6137aa0a177061ca8bf3a96cad86e6217d8a7d23.html | ABIERTA |
| 19 | AEAT RAE 2022 índice | https://sede.agenciatributaria.gob.es/AEAT/Contenidos_Comunes/La_Agencia_Tributaria/Estadisticas/Publicaciones/sites/rae/2022/home.html | ABIERTA |
| 20 | AEAT RAE 2022 rendimiento por epígrafe IAE (directa) | https://sede.agenciatributaria.gob.es/AEAT/Contenidos_Comunes/La_Agencia_Tributaria/Estadisticas/Publicaciones/sites/rae/2022/jrubikf56de5ae960c562d02ef5831541e42e0835cd13e4.html | ABIERTA |
| 21 | AEAT RAE 2022 por agrupación IAE y tramos de BI (total + 7 tramos) | https://sede.agenciatributaria.gob.es/AEAT/Contenidos_Comunes/La_Agencia_Tributaria/Estadisticas/Publicaciones/sites/rae/2022/jrubik6af0a413ea01d5380ab0875cce6a6b62d6cdb4fc.html (y jrubik5ae57…, jrubikf4e16…, jrubik569e8…, jrubik6aaef…, jrubik22b76…, jrubikf5a6d…, jrubik6ba5c….html) | ABIERTA (8 páginas) |
| 22 | AEAT RAE 2019 metodología y tablas CCAA | https://sede.agenciatributaria.gob.es/AEAT/Contenidos_Comunes/La_Agencia_Tributaria/Estadisticas/Publicaciones/sites/rae/2019/docf104f0e354dbd082d504446b5f54d2183abaa753a.html (+2 tablas) | ABIERTA |
| 23 | Adecco/Infoempleo informe autónomos (PDF) | https://www.reasonwhy.es/media/library/informe_infoempleo_adecco.pdf | ABIERTA |
| 24 | Infoautónomos ENA 2024 (PDF) | https://infoautonomos.com/wp-content/uploads/2024/10/ESTUDIO-NACIONAL-DEL-AUTONOMOS-INFOAUTONOMOS-2024.pdf | ABIERTA |
| 25 | Forbes España / UPTA | https://forbes.es/?p=848084 | ABIERTA |
| 26 | Invoo (cita AEAT 14.826 €) | https://invoo.es/es/blog/formacion/cuanto-cobra-autonomo-neto-espana-2026/ | ABIERTA (secundaria) |
| 27 | INE EPA tabla 4879 | https://www.ine.es/jaxiT3/Tabla.htm?t=4879 | ABIERTA (no útil) |
| 28 | Gumroad about | https://gumroad.com/about | ABIERTA |
| 29 | Profitable.app Gumroad statistics | https://profitable.app/gumroad/stats | ABIERTA |
| 30 | StartupGTM, Gumroad 2020 distribution | https://startupgtm.substack.com/p/zero-to-142-million-inside-gumroads | ABIERTA |
| 31 | Udemy 10-K FY2025 (SEC) | https://www.sec.gov/Archives/edgar/data/1607939/000160793926000034/udmy-20251231.htm | ABIERTA |
| 32 | Etsy 10-K FY2025 (SEC) | https://www.sec.gov/Archives/edgar/data/1370637/000137063726000019/etsy-20251231.htm | ABIERTA |
| 33 | Graphtreon Patreon stats | https://graphtreon.com/patreon-stats | ABIERTA |
| 34 | Regner, Crowdfunding a monthly income (IDEAS/RePEc) | https://ideas.repec.org/p/jrp/jrpwrp/2019-010.html | ABIERTA (abstract) |
| 35 | VisionMobile 2014 vía SmartCompany | https://www.smartcompany.com.au/technology/69-of-all-smartphone-app-developers-earn-less-than-us1000-per-month-survey/ | ABIERTA |
| 36 | Changelog: How much money do IH products make | https://changelog.com/news/9llJ | ABIERTA |
| 37 | Indie Hackers products (solo) | https://www.indiehackers.com/products?founders=solo | ABIERTA (listado dinámico) |
| 38 | Indie Hackers posts (Stripe-verified analyses) | https://www.indiehackers.com/post/how-much-money-do-indie-hackers-products-make-74db9631f0 ; …/i-analyzed-5-079-stripe-verified-startups-f0f6bd053f | FRAGMENTO (403) |
| 39 | blog.mean.ceo Indie Hacker statistics 2026 | https://blog.mean.ceo/indie-hacker-business-statistics/ | ABIERTA (secundaria) |
| 40 | TrustMRR | https://trustmrr.com/ ; https://bigideasdb.com/starter-story-alternative | ABIERTA / FRAGMENTO (429) |
| 41 | MicroConf SOIS 2024 | https://microconf.com/saas-this-year ; https://stateofindiesaas.com/ ; https://microconf.com/founders/0-10k-arr | ABIERTA (PDF tras registro) |
| 42 | Startups for the Rest of Us ep. 721 | https://www.startupsfortherestofus.com/episodes/episode-721-7-key-takeaways-from-the-2024-state-of-independent-saas-report | ABIERTA |
| 43 | Acquire.com Multiples Report Jan 2026 | https://blog.acquire.com/acquire-com-biannual-acquisition-multiples-report-jan-2026/ | ABIERTA (cuerpo tras formulario) |
| 44 | Consulting Success fees study | https://www.consultingsuccess.com/consulting-fees-study | ABIERTA |
| 45 | Malt Freelancing in Europe 2024 (vía StartingUp) | https://www.starting-up.de/gruenden/freiberufler/freelancing-in-europe-2024-report.html | ABIERTA |
| 46 | freelancermap Freelancer Study 2026 | https://www.freelancermap.com/market-study ; https://www.freelancermap.de/marktstudie | ABIERTA |
| 47 | Upwork Freelance Forward | https://www.upwork.com/research/freelance-forward-2023-research-report | FRAGMENTO (403) |
| 48 | ManyRequests productized service revenue | https://manyrequests.com/blog/productized-service-revenue | ABIERTA |
| 49 | Belkins cold email response rates 2026 | https://belkins.io/blog/cold-email-response-rates | ABIERTA |
| 50 | Backlinko/Pitchbox outreach study | https://backlinko.com/email-outreach-study | ABIERTA |
| 51 | Instantly cold email benchmarks | https://instantly.ai/blog/cold-email-reply-rate-benchmarks?lng=en | ABIERTA |
| 52 | Grand View Research eGRC market | https://www.grandviewresearch.com/industry-analysis/enterprise-governance-risk-compliance-egrc-market | ABIERTA |
| 53 | AEPD >100.000 DPD (10-01-2023) | https://www.aepd.es/prensa-y-comunicacion/notas-de-prensa/mas-de-100.000-organizaciones-ya-cuentan-con-un-delegado-de | ABIERTA |
| 54 | AEPD Memoria 2023 nota de prensa | https://www.aepd.es/prensa-y-comunicacion/notas-de-prensa/aepd-recibe-por-tercer-anno-consecutivo-mayor-numero-reclamaciones-historia | ABIERTA |
| 55 | AEPD Memoria 2023 (PDF) | https://www.aepd.es/memorias/memoria-aepd-2023.pdf | ABIERTA |
| 56 | AEPD Memoria 2024 nota de prensa | https://www.aepd.es/prensa-y-comunicacion/notas-de-prensa/aepd-recibio-19000-reclamaciones-con-ia-espacios-de-datos-y-neurodatos-entre-retos-prioritarios | ABIERTA |
| 57 | IAPP 500K organizations registered DPOs | https://iapp.org/news/a/study-an-estimated-500k-organizations-have-registered-dpos-across-europe | ABIERTA |
| 58 | ENISA NIS Investments 2024 / 2023 | https://www.enisa.europa.eu/publications/nis-investments-2024 ; https://www.enisa.europa.eu/publications/nis-investments-2023 | ABIERTA |
| 59 | AEAT Verifactu | https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu.html | ABIERTA |
| 60 | Emprendedores.es NIS2 | https://emprendedores.es/actualidad/nis2-empresas/ | ABIERTA |
| 61 | DQS ISO Survey 2025 | https://www.dqsglobal.com/es/acerca-de/sala-de-prensa/iso-survey-2025-las-certificaciones-iso-crecen-un-11-en-el-mundo-y-un-28-en-espana | ABIERTA |
| 62 | UNE nota ISO Survey 2023 (PDF) | https://www.une.org/salainformaciondocumentos/NP_UNE_ISO-Survey2023.pdf | ABIERTA |
| 63 | ReasonWhy/SEMrush RGPD 2018 | https://www.reasonwhy.es/actualidad/digital/la-resonancia-que-provoca-el-nuevo-rgpd-en-google-espana-2018-05-24 | ABIERTA |
| 64 | El Independiente, RGPD 2018 | https://www.elindependiente.com/futuro/2018/12/30/el-ano-que-aprendimos-a-proteger-nuestros-datos | ABIERTA (sin cifras de mercado) |
| 65 | Lucintel Spain data compliance market; GlobeNewswire GDPR services 2018; ScienceDirect/SSRN Regner; ATA informes; ISO.org survey | varias | FRAGMENTO / 403 / ECONNRESET |

Ficheros de trabajo (CSV, PDFs, HTML parseados): `/tmp/claude-0/-home-user-tbd/637262f0-646e-586f-83ef-8ef9d5653ca7/scratchpad/refut_e/` (NES: `nes/nonemp22us.txt`, resumen `nes_summary.txt`; AEAT: `rae2022_directa_iae.html`, `tramo_*.html`; PDFs AEPD, Adecco, Infoautónomos, Simply Business, UNE).
