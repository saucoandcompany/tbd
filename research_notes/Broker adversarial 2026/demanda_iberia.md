# Demanda real de transformadores de potencia, celdas MT/AT y grupos electrógenos ≥1 MW en España y Portugal (2026-2029)

Nota adversarial. Fecha: 22-oct-2026. Método: solo páginas abiertas con pwfetch/curl desde la sesión (marcadas [ABIERTA]), fragmentos vistos solo en resultados de buscador ([FRAGMENTO]) o NO ENCONTRADO. Cada cifra lleva fecha y fuente; la tabla de URLs está al final. Los datos de comercio exterior se extrajeron directamente de la API de Eurostat Comext (dataset ds-045409, actualizado 16-oct-2026), no de terceros.

## 0. Veredicto en una línea por hipótesis

| Hipótesis | Veredicto | Motivo breve |
|---|---|---|
| H16 (ES+PT = 2-3 % del mercado global ≈ 750 M€/año transformadores de potencia; 1.200 M€ con aparamenta y gensets) | **NO SOSTENIBLE tal como está formulada; el orden de magnitud total (≈1.000-1.600 M€) sí es defendible si se amplía la definición** | Las importaciones de transformadores >10 MVA (TARIC 8504.23) de España+Portugal en 2025 fueron 273 M€ (Comext). Aun sumando producción nacional, el segmento "potencia" no llega a 750 M€; el 2-3 % no tiene base de dato abierto (peso de Iberia en demanda eléctrica mundial ≈ 1 %). Si se incluyen transformadores 650 kVA-10 MVA, secos >500 kVA y aparamenta MT/AT, el mercado aparente ES+PT se sitúa en 1.000-1.600 M€/año (cálculo en §4). |
| H17 (compradores con proyectos parados por falta de equipo) | **PARCIALMENTE CONFIRMADA: hay colas enormes de compradores, pero el cuello de botella documentado es acceso a red/permisos; la falta de equipo es un cuello secundario y no se ha encontrado ningún caso español documentado de proyecto parado "por falta de transformador"** | 129 GW de renovables, 16-22 GW de almacenamiento y 19 GW de demanda con permisos en red de transporte sin estar en servicio (REE, feb-2026); 86,3 % de subestaciones de distribución saturadas (FIE/Opina 360, mar-2026); fabricantes (Hitachi Energy, Ormazabal, Arteche, Schneider, Siemens Energy) con cartera llena 4 años y plazos de 3-4 años para transformadores de potencia (El Español, jun-2026). |
| H18 (centros de datos: varios GW en pipeline a 2030; transformadores 20-60 MVA y gensets 1-3 MW) | **CONFIRMADA en MW (con fuerte descuento por madurez); especificaciones de equipo plausibles pero NO verificadas en documentos españoles** | Spain DC: 439 MW (2025) → 2.537 MW (2030); CBRE (ago-2026): 1,4 GW IT operativo+construcción, 3,1 GW maduro, 10,5 GW anunciado en Iberia; BofA: 4,14 GW 2030; Planificación 2025-2030 reserva 3,8 GW para CPD. Gensets: Himoinsa HGY 1.250-3.500 kVA (1.000 uds/año, nueva planta Murcia); Genesal hasta 4.000 kVA. Tamaño de transformadores de campus: solo evidencia indirecta (subestaciones 220/20 kV, 400/150 kV). |

## 1. Red de transporte y distribución (REE, MITECO, CNMC, distribuidoras)

**Planificación de la red de transporte 2025-2030 (propuesta, no aprobada aún a 22-oct-2026)**
- [ABIERTA] MITECO, nota de prensa 09-oct-2025: propuesta inicial a audiencia pública (alegaciones hasta 16-dic-2025); inversión ≈13.600 M€; atender 27,7 GW de demanda desde la red de transporte frente a 2 GW de la planificación vigente; escenario 2030: 375 TWh de consumo, punta 61,4 GW (+60 % vs 2024), 159 GW de renovables integradas, >22 GW de almacenamiento.
- [ABIERTA] Ecoticias 13-sep-2025 (desglose de Aagesen): 422 ampliaciones de conexión (142 en transporte para nuevos consumidores, 84 agentes especiales ADIF/puertos, 196 apoyos a distribución); 9 GW industria, 1,8 GW residencial, 560 MW ferrocarril, 1,2 GW puertos; demanda = 40 % y almacenamiento = 19 % de las solicitudes.
- [ABIERTA] Bolsamania/Europa Press 17-sep-2025: 13.590 M€, +65,7 % sobre el plan anterior; proyecto legislativo pendiente de Congreso.
- [ABIERTA] MITECO, nota 24-sep-2026 (Groizard, Catalunya): tras 2.566 alegaciones la **nueva Propuesta supera los 17.000 M€**, "la planificación con mayor inversión de la historia"; se remitirá a Comisión de Transición Ecológica del Congreso y Consejo de Ministros (es decir, a 22-oct-2026 sigue sin aprobación formal). En Catalunya: +3,8 GW de demanda, +3 GW renovables, +1,5 GW almacenamiento.
- [ABIERTA] Bolsamania/Europa Press 11-jun-2026 y Economía3 06-may-2026 (informe PwC para Aelec): el borrador prevé **659 posiciones en 254 subestaciones**; el 54 % de las posiciones (354) con retraso medio de 5,7 años; el 63 % de las subestaciones (161) con retraso medio >7 años; 49 subestaciones con >10 años de parálisis; 402 de las 659 posiciones proceden de planificaciones anteriores (294 de 2021-2026, 67 de 2015-2020, 41 de 2008-2016); capex a posiciones y líneas con afección a demanda: 1.342 M€ (10 % del total).
- NO ENCONTRADO: número de transformadores/MVA nuevos de la propuesta 2025-2030 (el documento PDF de la propuesta no se localizó; la web de REE devuelve 403 Incapsula incluso con navegador). Referencia histórica [FRAGMENTO]: la planificación 2015-2020 incluía 11.907 MVA de transformación 400/220 kV.

**Inversión ejecutada por REE**
- [ABIERTA] Redeia, nota de resultados 2025 (PDF, 26-feb-2026): inversión en red de transporte y operación 1.551 M€ (+40,4 %), de los que **1.424 M€ a desarrollo y refuerzo de la red de transporte** (+448 M€); inversión total del grupo 1.626 M€ (+38,7 %); la inversión se ha multiplicado casi por 4 desde 2020.
- [ABIERTA] Renewable Energy Magazine 26-feb-2026: Corredor (Redeia) afirma que la red acoge 150 GW de generación instalada (70 % renovable); nuevo plan estratégico 2026-2029.

**Permisos de acceso y saturación (CNMC / REE / distribuidoras)**
- [ABIERTA] Ara.cat 20-feb-2026 y El Debate 20-feb-2026: REE publica por primera vez los mapas de capacidad de demanda (obligada por la CNMC): solo el **25 % de los nudos de transporte** tiene capacidad para nueva demanda; **permisos vigentes en red de transporte: 129 GW eólica+FV, 16 GW almacenamiento, 19 GW demanda**; desde 2022 se han otorgado **11,8 GW de capacidad para nueva demanda y nada está aún en servicio** (equivaldría a +25 % de la demanda actual). El Ministerio habla de "acaparamiento indebido" y de caducidad a 5 años y aval del 10 %.
- [ABIERTA] Modo Energy (2026): según la publicación de REE de feb-2026, permisos de acceso para **22 GW de BESS** en transporte (frente a 25 MW de BESS instalados a fin de 2024 según REE) y otros 16 GW de almacenamiento pendientes; primer concurso de demanda cerrado 26-feb-2026 adjudicó 928 MW en cinco nudos a proyectos industriales con >3.100 M€ de inversión comprometida.
- [ABIERTA] Energía Estratégica 03-jul-2026: actualización mensual de REE: +12.405 MW de capacidad de evacuación, +20.882 MW para demanda NO-CEP y +32.424 MW para almacenamiento (de 100.108 a 132.532 MW) frente al cierre de 3-jun-2026.
- [ABIERTA] Energías Renovables 01-jul-2026: RDL 7/2026; 16 instalaciones de consumo renuncian a >1 GW de permisos en transporte; capacidad liberada reservada en Balsicas 220 kV y otros nudos para nuevas solicitudes de demanda.
- [ABIERTA] MITECO 23-sep-2026: instrumentos para conceder hasta 11 GW de capacidad en nudos de transición justa (A Coruña, Almería, Asturias, Burgos, Cádiz, León, Palencia, Puertollano).
- [ABIERTA] Energías Renovables 22-dic-2025 (aelec): en 2025 se solicitaron ≈40 GW de acceso en distribución; solo 12 % (4,5 GW) concedido, 66 % (25 GW) no atendido, 22 % (8,5 GW) en tramitación.
- [ABIERTA] Energías Renovables 19-ene-2026 y Renewable Energy Magazine 23-mar-2026 y Bolsamania 18-mar-2026 (FIE/Opina 360): 6.102-6.108 subestaciones de las 29 mayores distribuidoras (97 % del suministro): saturación 85,7 % (dic-2025) → **86,3 % (mar-2026); 5.265 subestaciones sin capacidad; 7.400 MW disponibles** frente a >10.000 MW en oct-2025; 8 provincias al 100 % (Almería, Málaga, Zaragoza, Albacete, Guadalajara, Salamanca, Álava, Vizcaya); Madrid pasa de 85,1 % a 90,9 %.
- [ABIERTA] Suelo Solar 04-jun-2026 (AFRY para Beyond Fossil Fuels): **7.000 M€ de proyectos renovables y de almacenamiento parados en listas de espera de conexión a distribución en España**; la cola de almacenamiento ≈40 % del objetivo nacional.
- NO ABIERTO: PDF de la CNMC (memoria justificativa acceso flexible) – error TLS en descarga; informes de la CNMC de supervisión de acceso no localizados.

**Planes de las distribuidoras**
- [ABIERTA] Vozpópuli 24-sep-2025: Iberdrola, plan 2025-2028: 58.000 M€; 37.000 M€ a redes (25.000 distribución, 12.000 transporte); **Península Ibérica 9.000 M€** (Reino Unido 20.000, EE. UU. 16.000).
- [ABIERTA] Bolsamania 23-feb-2026 y El Español 23-feb-2026: Enel destina 26.000 M€ a redes 2026-2028; **Endesa ≈5.200-5.460 M€ en distribución España+Portugal 2026-2028** (+30-36 % vs 4.000 M€ del plan 2025-2027). El Gobierno preveía elevar los topes de inversión en redes +3.600 M€ (transporte) y +7.700 M€ (distribución) hasta 2030.
- NO ENCONTRADO: cifras separadas de Naturgy (UFD) y EDP España en redes 2026-2028.

**Portugal**
- [ABIERTA] ECO 01-jul-2025: PDIRT-E 2024 de REN (2025-2034): 1.691 M€, de los que 705 M€ hasta 2029; ERSE lo considera "equilibrado".
- [ABIERTA] Observador/Lusa 06-ago-2026: Gobierno aprueba el **PDIRD-E 2026-2030 de E-REDES: 1,58 mil M€** (+50 % vs propuesta anterior), 20 % para robustez tras el apagón; primer parecer de ERSE sin recortes.
- [ABIERTA] APREN, Análise 2025 (PDF, ene-2026): en 2025 se instalaron 893 MW solares (vs 1,34 GW en 2024); resto de tecnologías renovables casi estancadas (+0,03 %).

## 2. Centros de datos

- [ABIERTA] El Independiente 30-mar-2026 (informe anual Spain DC): **439 MW instalados** en ≈100 CPD (+23 % en 2025) → **2.537 MW en 2030** si sigue la tendencia; Madrid 238 MW → 721 MW; Aragón 108 MW → 1.098 MW; Cataluña 33 → 148 MW; País Vasco 26 → 114 MW; Navarra 0 → 140 MW; Castilla-La Mancha 0 → 80 MW; inversión prevista 66.900 M€ hasta 2030; Amazon eleva su inversión en Aragón a 33.700 M€ hasta 2034; Blackstone/QTS Calatorao 7.500 M€ con "subestación eléctrica propia".
- [ABIERTA] Energías Renovables 08-oct-2026 (Colliers, Iberian Snapshot abr-sep 2026): **≈450 MW TI operativos en Iberia** (+65 MW en 6 meses, +17 %); Madrid 175 → 212 MW TI; Barcelona 42 → 63 MW TI; **Aragón 108 MW TI operativos y 3.764 MW TI de "capacidad futura estimada"**; Derio/Paterna/Cantabria 42 MW operativos y 5.687 MW futuros "en fases iniciales"; Lisboa 25 MW operativos y 1.389 MW de pipeline. Colliers: "la materialización dependerá de la disponibilidad de potencia, la construcción de subestaciones y conexiones". Proyecto de RD (27-ago-2026) exige requisitos a CPD ≥1 MW que pidan acceso.
- [ABIERTA] Interempresas 04-ago-2026 (CBRE Iberian Data Center Market): **1,4 GW IT operativo + en construcción; 3,1 GW IT en desarrollo maduro; 10,5 GW IT anunciados**, de los que solo ≈40 % con capital institucional; Madrid 224 MW IT operativos + 228 MW IT en construcción; neoclouds contrataron 350-500 MW en Iberia en 12 meses.
- [ABIERTA] Idealista/Europa Press 15-jun-2026 (Morgan Stanley): ≈400 MW a fin de 2025 → **4,3 GW en 2035** (+55 % vs previsión anterior); Aragón potencial 3 GW; AWS 34.000 M€ (>1 GW); Microsoft >6.500 M€ Aragón; Merlin 150 MW Zaragoza + 280 MW Bilbao, pipeline 0,7 GW a 2032 + 4,4 GW largo plazo; QTS Calatorao 300 MW (12 edificios de 40 MW, operación 2032); Box2Bit 150 MW (2029) ampliable a 520 MW; SAMCA 300 MW (131 MW en 2028); Tillion 150 MW con red asegurada; Merlin-Edged Cáceres/Badajoz hasta 1 GW cada uno; Ingenostrum Badajoz 300 MW.
- [ABIERTA] Bolsamania/Europa Press 04-ago-2026 (BofA): **4,14 GW de carga informática en España en 2030** (escenario alta confianza), ≈21 TWh; Ferrovial MAD01 Alcobendas 60 MW (40 MW IT), 1.000 M€.
- [ABIERTA] Cushman & Wakefield 15-jun-2026: Madrid 538 MW de capacidad total de mercado → 1.105 MW en 2030.
- [ABIERTA] Structure Research (ficha informe 2026): la avalancha de solicitudes especulativas "ha llevado el desarrollo en Madrid casi a la paralización"; la Planificación 2025-2030 asigna **3,8 GW a centros de datos**; REE "incumplió su plan 2020-2025"; Madrid superará 1 GW construido en 2031.
- [ABIERTA] DCD 22-oct-2025 (EY/Spain DC): en Madrid solo queda un 4 % de capacidad disponible; en País Vasco ninguna; en riesgo >58.000 M€ de proyectos.
- [ABIERTA] Vozpópuli 08-abr-2025 (Colliers/Comunidad de Madrid): Madrid >50 % de la potencia instalada en España; objetivo Spain DC 735 MW en 2027; cartera 2030 ≈1,7 GW.
- [ABIERTA] DCD (feature 2026): mercado pasa de 293 MW a 500-600 MW en 2026; Nostrum Badajoz 500 MW escalable; "la ventaja competitiva de 2026 se decidirá por quién consigue un permiso integral de 50-100 MW".
- Portugal: [ABIERTA] Essential Business 06-may-2026 (Colliers oct-25/mar-26): Portugal >2,6 GW IT planificados; Lisboa 1.389 MW (373 MW un año antes), Merlin Edged hasta 1.300 MW; **Start Campus Sines 1.169 MW IT planificados**; Covilhã 75 MW. [ABIERTA] Lusa 14-ene-2026: SIN02 180 MW IT, 24 meses de obra incluyendo subestación AT y **subestación 400/150 kV**; campus 1,2 GW "a principios de los 2030", ≈8.500 M€. [ABIERTA] DCD Brasil 09-ago-2024: REN eleva la capacidad de Sines de 495 MW a 1,2 GW; edificios 2-6 de hasta 240 MW IT.
- Equipamiento: [FRAGMENTO] BOE 08-oct-2026: línea directa de Solaria a CPD desde subestación "Venero" 220/20 kV (Méntrida) conectada a Villaviciosa 400 kV (REE). [FRAGMENTO] REE: nueva subestación Calatorao 220 kV para consumidores conectados a transporte. NO ENCONTRADO: documento español que especifique transformadores de 20-60 MVA en un campus concreto.
- Gensets para CPD: [ABIERTA] Alimarket (2025): Himoinsa invirtió 100 M€ y abre fábrica en Alcantarilla (Murcia) de 17.000 m² para la serie HGY de misión crítica, **1.250-3.500 kVA (hasta 4.000 kVA), ≈1.000 generadores/año**. [ABIERTA] Interempresas 2026: Genesal Energy, capacidad hasta 4.000 kVA en 2026-2027; proyectos de 2.250-3.000 kVA para CPD en el norte de Europa; en España el caso documentado es un grupo de 165 kVA para un CPD de telecomunicaciones en Alcobendas (ene-2026). Spain DC (citado por Genesal): la potencia demandada por CPD pasaría de 355 MW en 2025 a >2.180 MW en 2030.

## 3. Renovables y almacenamiento

- [ABIERTA] MITECO 24-sep-2024 (PNIEC 2023-2030 aprobado): 2030 = 76 GW FV (19 GW autoconsumo), 62 GW eólica (3 GW marina), 22,5 GW almacenamiento, 12 GW electrolizadores; inversión total 308.000 M€, 17 % a redes.
- [ABIERTA] Energías Renovables 15-sep-2026 (Informe Anual UNEF): **10.105 MW FV nuevos en 2025** (8.966 MW suelo, 1.139 MW autoconsumo); FV = 18,4 % de la generación (21,3 % con autoconsumo); **71,5 GW de puntos de conexión de demanda concedidos o planificados hasta 2030 + 24 GW solicitados pendientes**; almacenamiento: 261 MW en suelo (241 MW hibridados) y 2.745 MWh acumulados detrás del contador; PIB 9.841 M€.
- [ABIERTA] Energías Renovables 16-jul-2026 (Anuario Eólico AEE 2026): 32,9 GW eólicos; **1.420 MW nuevos en 2025** frente a 5,8 GW/año necesarios para el PNIEC; **32,5 GW en tramitación**, buena parte bloqueada; **Galicia: 3,4 GW con autorización administrativa de construcción paralizados** (judicial); 46 repotenciaciones en desarrollo por 1.132 MW; exportaciones de aerogeneradores 1.953 M€.
- [ABIERTA] MITECO nota 29-jul-2024 (PDF) y pv magazine 30-jul-2024: hito 25-jul-2024: **283 proyectos / 28.123 MW con autorización de construcción** (24.870 MW FV, 2.680 MW eólica, 573 MW bombeo); 428 iniciaron, 321 con DIA favorable; inversión >17.000 M€; deben entrar en operación antes de jun-2028. Contraste: FV instalada 2025 ≈10,1 GW → una parte relevante de esos 28 GW sigue sin ejecutar (no hay cifra oficial del remanente: NO ENCONTRADO).
- [ABIERTA] Energía Estratégica 10-sep-2026: **pipeline BESS 3-4 GW; <300 MW en operación (≈290 MW)**; podría cerrar 2026 en ≈650 MW; en agosto-2026 avanzaron 327,6 MW; frenos: retrasos administrativos, ingresos inciertos, seguridad contra incendios, aseguradoras.
- [ABIERTA] ESS News 24-abr-2026 (Observatorio Opina 360, 1T-2026): 96 proyectos de almacenamiento / 2.121,5 MW entran en información pública (+464 % interanual); 46 con DIA favorable (1.144,6 MW); 15 con autorización de construcción (239,6 MW); FV con autorización de construcción en 1T-2026: 1.242 MW; nuevas entradas FV caen 1.353 MW interanual.
- [FRAGMENTO] FRV: >1.200 MW/5.000 MWh de BESS "ready to build" 2026-2027; Galileo 500 MW BESS con autorización de construcción en Cataluña.
- [ABIERTA] OKdiario (2023, contexto histórico): ≈110 GW con permiso de acceso, >60 % sin permiso de conexión; 61,7 GW con acceso y conexión.

## 4. Importaciones, exportaciones y producción (Eurostat Comext, API directa; AFBEL; fabricantes)

Fuente: Eurostat Comext ds-045409, reporter ES/PT, partner WORLD, VALUE_IN_EUROS, anual; consulta 22-oct-2026 (datos actualizados 16-oct-2026). Cifras en M€.

| Código | Producto | ES imp 2022 | ES imp 2023 | ES imp 2024 | **ES imp 2025** | ES exp 2025 | PT imp 2025 | PT exp 2025 |
|---|---|---|---|---|---|---|---|---|
| 8504 | Transformadores + convertidores estáticos + inductores (total) | 2.644,6 | 2.779,5 | 2.746,4 | **3.047,9** | 2.807,9 | 511,0 | 242,4 |
| 8504.21 | Transf. dieléctrico líquido ≤650 kVA | 8,8 | 20,7 | 27,1 | **80,4** | 112,5 | – | – |
| 8504.22 | Transf. dieléctrico líquido 650 kVA-10 MVA | 139,3 | 223,9 | 291,8 | **280,9** | 188,6 | 24,0 | 7,6 |
| 8504.23 | **Transf. dieléctrico líquido >10 MVA (potencia)** | 68,1 | 164,0 | 220,2 | **256,4** | 65,8 | 17,0 | 35,2 |
| 8504.33 | Transf. secos 16-500 kVA | 24,3 | 28,4 | 44,7 | **33,6** | 43,9 | – | – |
| 8504.34 | Transf. secos >500 kVA | 49,3 | 43,5 | 75,7 | **84,1** | 51,5 | – | – |
| 8535 | Aparamenta >1.000 V (interruptores, seccionadores, etc.) | 141,2 | 185,9 | 185,2 | **222,0** | 86,0 | – | – |
| 8537.20 | Cuadros/celdas >1.000 V | 110,4 | 137,3 | 147,5 | **220,6** | 464,3 | – | – |
| 8502 | Grupos electrógenos (total) | 254,0 | 232,5 | 246,0 | **321,5** | 488,6 | 77,2 | 54,1 |
| 8502.12 | Gensets diésel 75-375 kVA | 12,7 | 20,6 | 21,0 | **32,2** | 91,5 | – | – |
| 8502.13 | **Gensets diésel >375 kVA** | 34,0 | 49,9 | 53,9 | **127,9** | 115,3 | 18,2 | 14,8 |

Lecturas clave:
- Las importaciones españolas de **transformadores de potencia >10 MVA se multiplicaron ×3,8 entre 2022 y 2025** (68 → 256 M€); las de ≤650 kVA ×9 (9 → 80 M€); las de gensets >375 kVA ×2,4 solo en 2025 (54 → 128 M€); las de celdas MT/AT (8537.20) +50 % en 2025. Esto es la señal más sólida de que la demanda interna supera la oferta nacional en esos segmentos.
- España es **exportadora neta** de celdas (8537.20: +244 M€), gensets (8502: +167 M€) y transformadores pequeños (8504.21: +32 M€); es **importadora neta** de transformadores >10 MVA (−191 M€) y 650 kVA-10 MVA (−92 M€).
- Producción nacional: NO ENCONTRADO dato PRODCOM/INE de valor de producción 2024-2025 (la API de Eurostat PRODCOM ds-059358 responde "extraction too big" sin filtros; INE no se abrió). Proxies abiertos: [ABIERTA] Velatia 2025 = 1.100 M€ (+5 %), 79 % Ormazabal ≈ 870 M€ (incluye aparamenta MT, 20 países); [ABIERTA] Ormazabal Loeches: capacidad ≈7 GW/año de transformadores, >300.000 unidades en 30 años, 15 M€ invertidos en 5 años y otros 15 M€ previstos; [ABIERTA] Hitachi Energy Spain 324,26 M€ en 2023 (+15,9 %), 903 empleados; ampliación de Córdoba >80 M€ (transformadores de potencia y reactancias, fin 2027) y nueva planta de secos en Zaragoza 30 M€ (fin 2026/traslado 2027); [ABIERTA] Vozpópuli (CIP-Maestrazgo): autotransformadores 315 y 680 MVA a 400 kV fabricados en Córdoba; [ABIERTA] Himoinsa >350 M€ en 2022 (objetivo 400 M€ 2023), >80 % exportación; [ABIERTA] Genesal >35 M€ en 2025 (27 M€ en 2024). Imefy (hasta 160 MVA/245 kV, contrato 5 años con Thüga, JV en China) y Alkargo, Cotradis, Jesiva (en liquidación feb-2026 según directorio): cifras NO ENCONTRADAS. Efacec: NO ENCONTRADO.
- [ABIERTA] AFBEL (tribuna en Energías Renovables, 17-dic-2025): "en 2025 incremento acelerado de las importaciones desde Asia, especialmente China y Turquía… aumenta la entrada de productos importados mientras cae la fabricación nacional"; **70 % del mercado de bienes de equipo eléctrico depende del sector regulado (T&D) y 30 % del privado (renovables, autoconsumo, CPD)**; para cumplir el PNIEC "habría que triplicar" la actividad. [ABIERTA] Solunion flash jul-2026 (AFME): ventas del material eléctrico BT/MT +4,33 % en 2025 y TAM +5,64 % a jun-2026; 2024 fue −0,34 %; exportaciones ≈35 % de las ventas. Sin cifras absolutas de facturación sectorial.

**Cálculo alternativo a H16 (mercado aparente ES+PT 2025, orden de magnitud)**
Mercado aparente = producción nacional vendida en el país + importaciones − exportaciones. Como la producción nacional no está publicada, se acota con dos supuestos: (a) las ventas interiores de los fabricantes locales igualan a las importaciones (supuesto bajo para distribución, donde Ormazabal/Imefy/Cotradis dominan; razonable para potencia, donde Hitachi Córdoba exporta gran parte), y (b) duplican las importaciones.

| Segmento | Importaciones ES+PT 2025 | Supuesto (a) | Supuesto (b) |
|---|---|---|---|
| Transformadores de potencia >10 MVA (8504.23) | 273 M€ | ≈550 M€ | ≈820 M€ |
| Transformadores 650 kVA-10 MVA (8504.22) | 305 M€ | ≈610 M€ | ≈915 M€ |
| Transformadores ≤650 kVA y secos (8504.21/33/34, solo ES) | 198 M€ | ≈400 M€ | ≈600 M€ |
| Aparamenta y celdas >1 kV (8535 + 8537.20, solo ES) | 443 M€ | ≈885 M€ | ≈1.330 M€ |
| Gensets ≥375 kVA (8502.13, ES+PT) | 146 M€ | ≈290 M€ | ≈440 M€ |

Conclusiones del cálculo: (1) el segmento estricto "transformadores de potencia" (>10 MVA) en ES+PT ronda **0,5-0,8 mil M€** incluso con supuestos generosos; frente a un mercado global de ≈30.000 M€ (El Español, jun-2026; otras casas 26.500-30.400 M$ en 2025) eso es **≈1-1,5 % del mundo, no 2-3 %**; con solo importaciones, 0,9 %. (2) Si el plan de negocio define "transformador de potencia" como todo transformador ≥650 kVA, la cifra de 750 M€ es alcanzable (≈1.100-1.700 M€ con los supuestos anteriores), pero entonces compite con un tejido fabricante local muy fuerte en distribución. (3) El total "transformadores + aparamenta MT/AT + gensets ≥1 MW" se sitúa en **≈1.300-2.400 M€** con los supuestos (a)-(b), de modo que los 1.200 M€ de H16 son un suelo plausible pero obtenido con una regla ("2-3 % del mundo") que no se sostiene con dato abierto. (4) El segmento más importador-dependiente y de crecimiento más rápido es exactamente el de potencia >10 MVA y gensets >375 kVA: ahí hay hueco para intermediación; en celdas y gensets pequeños España exporta más de lo que importa.

## 5. Plazos de entrega y cuello de botella en fabricación (evidencia abierta)

- [ABIERTA] El Español/Invertia 23-jun-2026: Hitachi Energy: "tenemos cubiertos pedidos para, al menos, los próximos cuatro años"; Arteche, Ormazabal, Schneider Electric y Siemens Energy coinciden; transformadores de potencia pasan de 10-12 meses pre-pandemia a **3-4 años de antelación mínima**; mercado global de transformadores de potencia ≈30.000 M€; industria española a tres turnos; plantas de Córdoba y Zaragoza (Hitachi) y País Vasco invierten decenas de millones; McKinsey/Sightline: 30-50 % de los grandes proyectos digitales en riesgo de retraso por escasez de componentes.
- [ABIERTA] DCD 06-nov-2024 (CEO Hitachi Energy en FT): plazos de 6-8 meses a 115-130 semanas, hasta 4 años sin reserva; precios +60-80 % desde 2020; Rystad: mercado de transformadores 48.000 → 67.000 M$ en 2030; Hitachi invierte 6.000 M$ y 15.000 empleos; Wood Mackenzie: hasta 25 % de los proyectos renovables mundiales en riesgo por plazos de transformadores.
- [ABIERTA] Hitachi Energy 19-jul-2024: >80 M€ en Córdoba (transformadores y reactancias de potencia, fin 2027), dentro de 1.500 M$ globales; [ABIERTA] Invest in Spain 31-ene-2025 y Alimarket: 30 M€ en nueva fábrica de secos en Zaragoza (22.000 m²).
- [FRAGMENTO] Ecosistema Startup (403 al abrir) y Foro3D (blog): "36-48 meses en Europa", demanda +25-40 % vs capacidad +10-15 % – baja calidad, no verificable.

## 6. Casos documentados de proyectos retrasados por falta de transformador/aparamenta en ES/PT

- **NO ENCONTRADO ningún caso nominal** (promotor, planta, fecha) en prensa 2025-2026 en el que se atribuya el retraso a la falta de un transformador o celda. Lo que sí está documentado:
  - Retrasos sistémicos de subestaciones de transporte (PwC/Aelec, may-jun 2026): 161 subestaciones con >7 años de retraso medio; causa principal: tramitación/planificaciones heredadas, no suministro.
  - 11,8 GW de demanda con permiso desde 2022 y 0 en servicio (REE, feb-2026); 7.000 M€ de renovables/almacenamiento en cola de distribución (AFRY, jun-2026); 3,4 GW eólicos con AAC parados en Galicia por vía judicial (AEE, jul-2026); 25 GW de solicitudes de acceso no atendidas en 2025 (aelec).
  - Línea 400 kV La Plana-Morella para la gigafactoría de VW/PowerCo en Sagunto: autorización administrativa 22-jun-2026, operativa dic-2028 (El Español).
  - Colliers (oct-2026) y Structure Research (2026) atribuyen explícitamente el riesgo de los CPD a "construcción de subestaciones y conexiones" y a la capacidad de REE de entregar los 3,8 GW.
- Conclusión adversarial: el comprador "parado" existe en masa, pero está parado **antes** del pedido de equipo (sin punto de conexión). El cuello de equipo aparece en el eslabón de las subestaciones (REE, distribuidoras, campus con subestación propia) y se expresa como plazos de 3-4 años, no como proyectos cancelados. Un bróker de equipos debe apuntar a quien ya tiene permiso firme y fecha de caducidad (5 años; 11,8 GW de demanda; 28 GW de renovables con AAC que deben operar antes de jun-2028; 22 GW de BESS con permiso).

## 7. Veredictos razonados

**H16 – NO SOSTENIBLE en su forma (2-3 % del global = 750 M€ de potencia).** El dato abierto más duro (Comext 2025) sitúa las importaciones ES+PT de transformadores >10 MVA en 273 M€ y el mercado aparente estimado en 0,5-0,8 mil M€ (1-1,5 % del global). La cifra de 750 M€ solo se alcanza incluyendo transformadores de 650 kVA-10 MVA, y la de 1.200 M€ totales queda dentro del rango estimado (1,3-2,4 mil M€) pero por una vía distinta a la del plan. Recomendación: reescribir H16 con la tabla Comext y con supuestos explícitos de producción nacional; pedir a Datacomex/INE (no abiertos aquí) la serie PRODCOM 27.11.41/42.

**H17 – PARCIALMENTE CONFIRMADA.** Compradores bloqueados: sí y en volumen sin precedentes (129 GW RES, 16-22 GW BESS, 19 GW demanda con permiso; 86 % de subestaciones de distribución saturadas; 7.000 M€ en cola). Pero el bloqueo documentado es acceso a red y tramitación, no falta de equipo; ningún caso abierto de "proyecto parado por falta de transformador". La escasez de equipo (3-4 años) está documentada por los fabricantes y afecta sobre todo a transformadores de potencia e interruptores AT. Las "distribuidoras pequeñas" y los "EPC industriales" como compradores desesperados: NO ENCONTRADO en fuentes abiertas.

**H18 – CONFIRMADA en pipeline (con descuento), NO VERIFICADA en especificaciones.** Operativo 2026: ≈450 MW TI (Colliers) / 439-538 MW (Spain DC, C&W). Pipeline 2030: 2,5 GW (Spain DC tendencia), 4,1 GW (BofA), 3,1 GW maduro + 1,4 GW (CBRE), 3,8 GW asignados en la Planificación; Portugal 2,6 GW (Sines 1,2 GW). CBRE advierte que solo ≈40 % de los 10,5 GW anunciados tiene capital institucional. Gensets 1-3 MW: coherente con las gamas de Himoinsa (1.250-3.500 kVA, 1.000 uds/año) y Genesal (hasta 4.000 kVA) y con el salto de importaciones 8502.13 (+137 % en 2025). Transformadores 20-60 MVA: plausible por la arquitectura 220/20 kV de las subestaciones de CPD documentadas en BOE, pero sin documento español que lo especifique.

## 8. Tabla de URLs

| # | Fuente / fecha | URL | Estado |
|---|---|---|---|
| 1 | REE planificación | https://www.ree.es/es/actividades/planificacion-de-la-red-de-transporte | 403 Incapsula (directo y --browser) |
| 2 | REE nota renuncias jul-2026 | https://www.ree.es/en/press-office/news/press-release/2026/07/16-consumption-facilities-relinquish... | 403 |
| 3 | REE PDF capacidades demanda | https://www.ree.es/sites/default/files/2026-07/0107_NP%20CapacidadesDemanda.pdf | devuelve HTML (bloqueo) |
| 4 | MITECO planificación 09-oct-2025 | https://www.miteco.gob.es/es/prensa/ultimas-noticias/2025/octubre/el-miteco-lanza-la-propuesta-de-planificacion-electrica-con-hori.html | ABIERTA |
| 5 | MITECO Groizard 24-sep-2026 | https://www.miteco.gob.es/es/prensa/ultimas-noticias/2026/septiembre/joan-groizard-avanza-el-resultado-de-la-nueva-propuesta-de-plani0.html | ABIERTA |
| 6 | MITECO PNIEC 24-sep-2024 | https://www.miteco.gob.es/es/prensa/ultimas-noticias/2024/septiembre/el-gobierno-aprueba-la-actualizacion-del-plan-nacional-integrado.html | ABIERTA |
| 7 | MITECO 28 GW AAC 29-jul-2024 (PDF) | https://miteco.gob.es/content/dam/miteco/es/prensa/24_07_29_NdP_El_MITECO_autoriza_la_construcción_de_28_GW_de_nuevas.pdf | ABIERTA (pdftotext) |
| 8 | MITECO 11 GW transición justa 23-sep-2026 | https://www.miteco.gob.es/es/prensa/ultimas-noticias/2026/septiembre/el-miteco-lanza-instrumentos-para-conceder-hasta-11-gw-de-capaci.html | ABIERTA |
| 9 | Bolsamania/EP planificación 17-sep-2025 | https://www.bolsamania.com/noticias/empresas/economia--aagesen-tiende-la-mano-en-el-congreso-para-aprobar-la-planificacion-de-la-red-de-electricidad-hasta-2030--20900069.html | ABIERTA |
| 10 | Ecoticias desglose planificación 13-sep-2025 | https://www.ecoticias.com/energias-renovables/propuesta-planificacion-electrica-2030-sara-aagesen-pormenoriza-detalles-multiplicara-por-14-los-2-gw-actuales | ABIERTA |
| 11 | Bolsamania/EP PwC-Aelec 11-jun-2026 | https://www.bolsamania.com/noticias/empresas/economia--electricas-alertan-de-retrasos-medios-de-hasta-7-anos-en-infraestructuras-clave-de-la-planificacion-electrica--22704036.html | ABIERTA |
| 12 | Economía3 PwC-Aelec 06-may-2026 | https://economia3.com/2026/05/06/751808-las-infraestructura-electrica-espanola-acumula-retrasos-de-seis-anos/ | ABIERTA |
| 13 | Redeia resultados 2025 (PDF) 26-feb-2026 | https://www.redeia.com/sites/default/files/paragraph/2026/02/file/2602_NP_Resultados_Redeia_2025.pdf | ABIERTA (pdftotext) |
| 14 | REM Corredor 26-feb-2026 | https://www.renewableenergymagazine.com/panorama/beatriz-corredor-defiende-que-la-red-de-20260226 | ABIERTA |
| 15 | Ara.cat 129 GW 20-feb-2026 | https://es.ara.cat/economia/energia/ministerio-dice-existe-acaparamiento-indebido-permisos-conexion-no-saturacion-red-electrica_1_5654769.html | ABIERTA |
| 16 | El Debate 25 % nudos 20-feb-2026 | https://www.eldebate.com/economia/20260220/red-electrica-revela-solo-puede-conectar-nueva-demanda-25-puntos-red-transporte_387610.html | ABIERTA |
| 17 | Modo Energy BESS 22 GW (2026) | https://modoenergy.com/research/es/connecting-to-spains-transmission-grid-bess-has-dedicated-headroom | ABIERTA |
| 18 | Energía Estratégica REE 32 GW 03-jul-2026 | https://www.energiaestrategica.com/es/notes/red-electrica-mueve-el-tablero-mas-de-20-gw-para-nueva-demanda-y-32-gw-para-storage-reabren-la-carrera-por-los-nudos-en-espana | ABIERTA |
| 19 | ER renuncias 1 GW 01-jul-2026 | https://www.energias-renovables.com/panorama/liberado-un-gigavatio-de-permisos-de-acceso-20260701 | ABIERTA |
| 20 | ER aelec 12 % 22-dic-2025 | https://www.energias-renovables.com/panorama/solo-el-12-de-las-solicitudes-de-20251223 | ABIERTA |
| 21 | ER FIE/Opina 360 19-ene-2026 | https://www.energias-renovables.com/panorama/estas-son-las-6-provincias-espa-olas-20260119 | ABIERTA |
| 22 | REM FIE/Opina 360 23-mar-2026 | https://www.renewableenergymagazine.com/panorama/casi-el-90-de-las-subestaciones-no-20260323 | ABIERTA |
| 23 | Bolsamania 86,3 % 18-mar-2026 | https://www.bolsamania.com/noticias/empresas/economia--la-red-electrica-espanola-alcanza-ya-una-saturacion-del-863-con-apenas-7400-mw-disponibles--22083694.html | ABIERTA |
| 24 | Suelo Solar AFRY 04-jun-2026 | https://suelosolar.com/noticias/interconexiones/espana/4-6-2026/el-liderazgo-espana-energias-renovables-se-frena-por-congestion-red-distribucion | ABIERTA |
| 25 | CNMC memoria acceso flexible (PDF) | https://www.cnmc.es/sites/default/files/editor_contenidos/Energia/Consulta%20Publica/RDC_DE_008_25_Tr%C3%A1mite_audiencia_Memoria%20justificativa.pdf | NO ABIERTA (error TLS curl 35) |
| 26 | Vozpópuli Iberdrola plan 24-sep-2025 | https://www.vozpopuli.com/economia/energia/iberdrola-antepone-eeuu-y-reino-unido-por-espana-en-su-nuevo-plan-estrategico-de-58000-millones-en-inversiones.html | ABIERTA |
| 27 | Bolsamania Endesa redes 23-feb-2026 | https://www.bolsamania.com/noticias/empresas/economia--endesa-impulsara-sus-inversiones-en-redes-un-36-con-casi-5500-millones-en-los-proximos-tres-anos--21790548.html | ABIERTA |
| 28 | El Español Endesa 5.200 M€ 23-feb-2026 | https://www.elespanol.com/invertia/empresas/energia/20260223/endesa-dispara-inversion-redes-millones-pese-choque-cnmc-retribucion/1003744141341_0.html | ABIERTA |
| 29 | ECO REN PDIRT 01-jul-2025 | https://eco.sapo.pt/2025/07/01/regulador-considera-proposta-de-investimento-da-ren-equilibrada-mas-deixa-varias-recomendacoes/ | ABIERTA |
| 30 | Observador E-REDES 06-ago-2026 | https://observador.pt/2026/08/06/governo-aprova-plano-de-158-mil-milhoes-para-modernizar-rede-eletrica-nacional-ate-2030/ | ABIERTA |
| 31 | APREN Análise 2025 (PDF) | https://www.apren.pt/wp-content/uploads/2026/01/PR-APREN-Analise-2025.pdf | ABIERTA (pdftotext) |
| 32 | REN PDIRT PDF | https://www.ren.pt/media/is3na0iv/pdirt2025-rnt-poscp.pdf | ABIERTA pero es la AAE del PDIRT 2018-2027 (no útil) |
| 33 | El Independiente Spain DC 30-mar-2026 | https://www.elindependiente.com/economia/2026/03/30/inteligencia-artificial-centros-datos-espana-aragon/amp/ | ABIERTA |
| 34 | ER Colliers snapshot 08-oct-2026 | https://www.energias-renovables.com/panorama/la-capacidad-operativa-de-los-data-centers-20261008 | ABIERTA |
| 35 | Interempresas CBRE 04-ago-2026 | https://www.interempresas.net/Robotica/660337-El-mercado-iberico-de-centros-de-datos-supera-los-4-5-GW-de-potencial-ejecutable.html | ABIERTA |
| 36 | Idealista Morgan Stanley 15-jun-2026 | https://www.idealista.com/news/node/901950 | ABIERTA |
| 37 | Bolsamania BofA 04-ago-2026 | https://www.bolsamania.com/noticias/empresas/economia--espana-eleva-sus-previsiones-de-capacidad-en-centros-de-datos-para-2030-segun-bank-of-america--23182798.html | ABIERTA |
| 38 | Cushman & Wakefield 15-jun-2026 | https://www.cushmanwakefield.com/es-es/spain/news/2026/06/madrid-ranks-among-the-top-five-data-center-markets-in-emea | ABIERTA |
| 39 | Structure Research Madrid/Barcelona 2026 | https://www.structureresearch.net/product/madrid-barcelona-dci-report-2026-data-centre-colocation-hyperscale-cloud-ai-interconnection/ | ABIERTA |
| 40 | DCD boom 90.000 M€ (2026) | https://www.datacenterdynamics.com/es/features/data-centers-en-españa-hacia-2026-un-boom-de-90000-millones-en-proyectos/ | ABIERTA |
| 41 | DCD saturación EY 22-oct-2025 | https://www.datacenterdynamics.com/es/noticias/el-auge-inversor-en-data-centers-choca-con-la-saturación-de-la-red-eléctrica-española/ | ABIERTA |
| 42 | DCD colapso red Europa 03-abr-2026 | https://www.datacenterdynamics.com/es/noticias/el-colapso-de-la-red-eléctrica-en-europa-pone-en-riesgo-la-ambición-de-españa-como-hub-digital/ | ABIERTA |
| 43 | Vozpópuli Madrid Colliers 08-abr-2025 | https://www.vozpopuli.com/espana/madrid/comunidad-madrid-tendra-inversion-estimada-23400-millones-euros-sector-centros-datos-proximos-tres-anos-sg.html | ABIERTA |
| 44 | Essential Business Portugal Colliers 06-may-2026 | https://www.essential-business.pt/2026/05/06/portugal-strengthens-its-role-as-european-data-centres-hub/ | ABIERTA |
| 45 | Lusa/Aman Start Campus 14-ene-2026 | https://www.aman-alliance.org/Home/ContentDetail/99289 | ABIERTA |
| 46 | DCD BR Start Campus 1,2 GW 09-ago-2024 | https://www.datacenterdynamics.com/br/notícias/start-campus-aumenta-a-capacidade-de-energia-do-campus-em-sines-portugal-para-12-gw/ | ABIERTA |
| 47 | Portugal News JLL 18-feb-2026 | https://www.theportugalnews.com/news/2026-02-18/portugal-stablished-as-emerging-data-centre-market/969169 | ABIERTA (texto mínimo) |
| 48 | ER UNEF informe anual 15-sep-2026 | https://www.energias-renovables.com/fotovoltaica/espa-a-bate-su-r-cord-fotovoltaico-20260915 | ABIERTA |
| 49 | ER AEE anuario 16-jul-2026 | https://www.energias-renovables.com/eolica/la-e-lica-consolida-su-peso-en-20260716 | ABIERTA |
| 50 | pv magazine 28 GW 30-jul-2024 | https://pv-magazine.com/2024/07/30/spain-approves-construction-of-24870-mw-of-pv | ABIERTA |
| 51 | Energía Estratégica BESS 10-sep-2026 | https://www.energiaestrategica.com/es/notes/bess-se-consolida-en-espana-y-aseguradoras-aparecen-como-el-nuevo-filtro-para-los-proyectos | ABIERTA |
| 52 | ESS News Opina 360 24-abr-2026 | https://www.ess-news.com/?p=8779 | ABIERTA |
| 53 | OKdiario 50.000 M€ (2023) | https://okdiario.com/economia/renovables-ven-peligrar-50-000-millones-inversion-paron-autonomias-ayuntamientos-11067089 | ABIERTA |
| 54 | Eurostat Comext API ds-045409 (ES/PT, 8504.xx, 8535, 8537.20, 8502.xx, 2022-2025) | https://ec.europa.eu/eurostat/api/comext/dissemination/statistics/1.0/data/ds-045409?reporter=ES&partner=WORLD&product=850423&flow=1&indicators=VALUE_IN_EUROS&freq=A&time=2025 (y variantes) | ABIERTA (JSON) |
| 55 | Eurostat PRODCOM ds-059358 | https://ec.europa.eu/eurostat/api/comext/dissemination/statistics/1.0/data/ds-059358 | NO UTILIZABLE (extraction too big / dimensiones desconocidas) |
| 56 | TrendEconomy ES 8504 (2012-2023, USD) | https://trendeconomy.com/data/h2/Spain/8504 | ABIERTA |
| 57 | TrendEconomy PT 8504 | https://trendeconomy.com/data/h2/Portugal/8504 | ABIERTA |
| 58 | Datacomex | (no intentado: aplicación dinámica) | NO ABIERTA |
| 59 | ER AFBEL tribuna 17-dic-2025 | https://www.energias-renovables.com/panorama/la-digitalizaci-n-de-la-red-el-20251217 | ABIERTA |
| 60 | Solunion flash material eléctrico jul-2026 (PDF) | https://www.solunion.es/wp-content/uploads/2026/07/Flash-sectorial-material-electrico-2026_Solunion.pdf | ABIERTA (pdftotext) |
| 61 | Bolsamania Velatia 01-jul-2026 | https://www.bolsamania.com/noticias/empresas/economia--el-grupo-industrial-velatia-alcanza-una-facturacion-de-1100-millones-de-euros-en-2025-un-5-mas--22891528.html | ABIERTA |
| 62 | ER Ormazabal Loeches 06-oct-2025 | https://www.energias-renovables.com/panorama/ormazabal-loeches-la-mayor-f-brica-de-20251006 | ABIERTA |
| 63 | Hitachi Energy Córdoba 19-jul-2024 | https://www.hitachienergy.com/latam/es/news-and-events/press-releases/2024/07/hitachi-energy-invests-over-80-million-euros-to-expand-transformer-capacity-and-operations-in-spain | ABIERTA |
| 64 | Alimarket Hitachi Zaragoza (2025) | https://www.alimarket.es/construccion/noticia_amp/401968/hitachi-energy-invierte-30-m--en-expandir-su-fabrica-de-transformadores-secos-en-zaragoza | ABIERTA |
| 65 | Invest in Spain Hitachi 31-ene-2025 | https://www.investinspain.org/en/noticias-main/2025/hitachi-energy | ABIERTA |
| 66 | Vozpópuli CIP Maestrazgo-Hitachi | https://www.vozpopuli.com/economia/energia/copenhagen-infrastructure-partners-cierra-contrato-para-suministro-transformadores-cluster-maestrazgo-parque-eolico-teruel.html | ABIERTA |
| 67 | Transformer Technology Imefy-Thüga (may-2025) | https://transformer-technology.com/imefy-to-supply-distribution-transformers-to-thuega-utilities-network-transformer-technology-news/ | ABIERTA |
| 68 | Interempresas Himoinsa 2022 (17-feb-2023) | https://www.interempresas.net/Ferreteria/467219-Himoinsa-supera-los-350-millones-de-euros-de-facturacion-en-2022.html | ABIERTA |
| 69 | Alimarket Himoinsa Murcia (2025) | https://www.alimarket.es/construccion/noticia_amp/420958/himoinsa-ultima-la-puesta-en-marcha-de-una-nueva-fabrica-en-murcia | ABIERTA |
| 70 | Corresponsables Genesal 2025 | https://www.corresponsables.com/actualidad/genesal-energy-afianza-en-2025-su-papel-como-proveedor-estrategico-de-energia-de-respaldo/ | ABIERTA |
| 71 | Interempresas Genesal 2026 | https://www.interempresas.net/ObrasPublicas/619944-energia-como-ventaja-competitiva-lineas-maestras-que-guian-a-Genesal-Energy-en-2026.html | ABIERTA |
| 72 | Interempresas Genesal CPD Alcobendas 21-ene-2026 | https://www.interempresas.net/TIC/619814-Genesal-Energy-refuerza-la-seguridad-energetica-de-un-data-center-en-Madrid.html | ABIERTA |
| 73 | El Español congestión fabricantes 23-jun-2026 | https://www.elespanol.com/invertia/empresas/energia/20260623/congestion-fabricantes-material-red-electrica-completo-pedidos-proximos-anos/1003744295811_0.amp.html | ABIERTA |
| 74 | DCD CEO Hitachi Energy 06-nov-2024 | https://www.datacenterdynamics.com/es/noticias/el-ceo-de-hitachi-energy-advierte-sobre-escasez-de-suministro-de-transformadores/ | ABIERTA |
| 75 | Ecosistema Startup 48 meses | https://ecosistemastartup.com/?p=93022 | 403 (FRAGMENTO) |
| 76 | ER gran industria AEGE 08-oct-2025 | https://www.energias-renovables.com/panorama/la-gran-industria-exige-prioridad-en-la-20251008/ | ABIERTA (texto relevante escaso) |
| 77 | Imefy/Cotradis/Alkargo/Jesiva/Efacec cuentas | – | NO ENCONTRADO en abierto |
| 78 | Datos INE PRODCOM 27.11 | – | NO ENCONTRADO |
