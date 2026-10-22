# Competencia europea e ibérica: broker de transformadores de potencia, celdas MT/AT y grupos ≥1 MW

**Fecha:** 22-10-2026 · **Rol:** investigador adversarial · **Hipótesis atacada:** *"Nadie en España y Portugal cruza de forma sistemática oferta y demanda de transformadores de potencia (1-100 MVA), celdas MT/AT y grupos electrógenos ≥1 MW con plazo corto; no hay brokers especializados activos en Iberia."*

**Método:** 80+ URLs abiertas con `tools/pwfetch.js` (HTTP y Chromium) y curl; WebSearch solo para localizar URLs. Etiquetas: **[ABIERTA]** = página real leída; **[FRAGMENTO]** = solo extracto de buscador/directorio/listado de terceros; **NO ENCONTRADO** = no se halló evidencia. No se inventa ninguna empresa: todo nombre citado aparece en una página abierta o en un fragmento identificado.

---

## 0. Veredicto en una línea

**CORREGIDA (no refutada, no confirmada).** En Iberia **sí existe** al menos un comprador-vendedor de transformadores y equipos de generación de segunda mano con almacén propio y marketing explícito de "plazo corto" (**AAM Global / Aznar Assets Management, Tarazona-Zaragoza**), más una sociedad registrada como intermediaria de alquiler/compraventa de transformadores (**Alquiler Transformadores SL, Oyón-Álava**, sin web). Pero **nadie en Iberia** publica stock con potencias/tensiones en el rango 1-100 MVA ni se presenta como "broker de transformadores de potencia"; el grueso de lo que hay es (a) generalistas de maquinaria usada que incluyen transformadores de distribución, (b) fabricantes con servicio de reparación, (c) alquiladores de grupos con transformadores ≤6,3 MVA. La **competencia relevante es europea** (Alemania, Países Bajos, Finlandia, Reino Unido) y ya vende a España vía marketplaces (Maschinensucher/Werktuigen/Machinio tienen listados ubicados en Aragón y Madrid). El hueco real es más estrecho de lo que dice el plan: **intermediación especializada en 1-100 MVA + celdas MT/AT con stock verificado y entrega corta, en castellano/portugués**, no "nadie hace nada".

---

## 1. Vendedores / intermediarios europeos de transformadores usados o reacondicionados

| Empresa | País | Qué vende | Publica stock con kVA/kV/precio | Intermediación / compra-venta | Antigüedad | Tamaño visible | Estado |
|---|---|---|---|---|---|---|---|
| **BTB Transformers (BTB Plaza)** | Finlandia (Pietarsaari) | Nuevos a medida + *"Markkinapaikka"*: "yli 150 muuntajan valikoima" (más de 150 transformadores disponibles al instante), "Fast Track" para acortar meses de plazo, servicio de emergencia 24/7, "Myy muuntaja" (compra tu transformador). Ferias: usados/surplus hasta 500 MVA | Sí (lista de stock "Varastolista" en la web; la versión EN devolvió 502) | Sí, ambas direcciones, explícitamente un **marketplace** | n/d en portada | ISO 9001/14001/45001; stand en Hannover Messe | [ABIERTA] portada FI; [FRAGMENTO] ferias |
| **LV Trading B.V.** | Países Bajos (Rotterdam) | Transformadores aceite y secos, estaciones completas, celdas MT (Eaton Xiria 630 A), generadores, UPS, cables. Portada muestra 2×2000 kVA 10,75/0,42 kV (2011), 2×1000 kVA 11 kV ABB (2021), estación 1000 kVA | Sí: kVA, kV, año; precio "op aanvraag" | "in- en verkoop en verhuur" (compra, venta y alquiler) | Opalis: ficha actualizada 27/02/2025 | Se autodefine "kleine en flexibele organisatie" | [ABIERTA] |
| **Koopmann Transformatoren- und Energietechnik GmbH** (grupo Koopmann / hk-c.de) | Alemania (Blankenfelde-Mahlow/Dahlewitz, Cloppenburg, Bottrop, Speyer) | "approx. 210 oil-filled and cast resin transformers… some available for immediate delivery or with very short lead times", base de datos online con fichas; otro anuncio del mismo domicilio: "250 transformers constantly in stock… from 50 kVA up to 63 MVA", reparación hasta 63 MVA/110 kV, alquiler y achatarramiento | Sí (DB propia; anuncios en Werktuigen) | Compra-venta, alquiler, reparación | Grupo fundado 1982 | Grupo: 12 GmbH, 15 sedes, ~370 empleados (Wirtschaftsforum) | [ABIERTA] anuncio Werktuigen y hk-c.de; web específica de trafos NO ENCONTRADA |
| **Trafo-City GmbH** | Alemania (Langenhagen) | "An- und Verkauf von Transformatoren" + desmontaje de instalaciones. Listados en Maschinensucher: TuR 31,5 MVA 110/10,5 kV (1979, alquiler posible), Siemens 15 MVA 20-15/10,5 kV (2008), Schneider 10 MVA resina (2013), Schneider 5 MVA 20/10 kV (1999) | Sí, en Maschinensucher (MVA, kV, año; precio a consultar) | Compra-venta, alquiler | Fundada 01/05/2010 | Micro (GF Jan Hutzler) | [ABIERTA] web + listado 31,5 MVA |
| **HT-VOLTEQ GmbH** | Alemania (Cloppenburg) | "Transformatoren & Schaltanlagen Handel & Service"; "Kurze Lieferzeiten für gängige Ersatztransformatoren"; mantenimiento, aceite, estaciones. Vendedor probable del Alstom 20/25 MVA 110/20 kV (2001, Cloppenburg) en Maschinensucher | Parcial (anuncios en marketplaces) | Comercio + servicio | Fundada 2017 | ">100.000 kVA gewartet"; pyme joven | [ABIERTA] |
| **Slaters Electricals Ltd** | Reino Unido (Newcastle/Sheffield) | "UK's largest stock of quality new and refurbished power and distribution equipment for sale or hire"; celdas 11 kV reacondicionadas con **36 meses de garantía**; transformadores de potencia (Machinio: ABB/Brush 5-80 MVA, 33/11 kV, 66/11,5 kV, "fully refurbished and tested prior to dispatch, short lead time"); adjudicación pública enero 2026: trafo reacondicionado 1 MVA 11 kV/433 V por £59.680 | Sí (vía Machinio y directorios) | Venta y alquiler | Antiguo (legado Reyrolle etc.) | Medio | [FRAGMENTO] web propia inaccesible (TLS); perfil en plantautomation-technology [ABIERTA] |
| **Wilson Power Solutions** | Reino Unido (Leeds) | Fabricante nuevo 5-300 MVA; distribución con "stock availability" de diseños DNO. No usados | Parcial | No | 1946 | Medio | [ABIERTA] – sustituto "nuevo en stock", no broker |
| **General Power Holland B.V.** | Países Bajos (Brunssum) | Grupos gas/diésel usados ≥1 MW: CAT 3512-B 1600 kVA nuevo 0 h (12/2023), 2× Jenbacher J612 2800 kVA, CAT 3520-C 2500 kVA; "buying unused & used Transformers, Control cabinets, Breakers…"; Resale: 27-39 máquinas, J320 35.000 €, CAT 3520 180.000 € | Sí (kVA, horas; algunos precios) | Compra-venta mundial | KVK 2023; Resale desde 2022 | Micro (director M.J. Jafari) | [ABIERTA] |
| **DPX Power Global B.V.** | Países Bajos (Oudenbosch) | Grupos diésel nuevos y usados 10-2.000 kVA; lista de stock, "Verwacht", Perkins 4008TAG3 1.250 kVA | Sí (stock list) | Compra ("Uw generator verkopen?") y venta | KVK 863475322 | 4 comerciales en portada | [ABIERTA] |
| **Aznar Assets Management – AAM Global** | **España (Tarazona, Zaragoza)** | "Venta de Transformadores industriales de segunda mano… **evitando grandes plazos de entrega**… alta, media y baja tensión… **Disponibilidad inmediata en nuestro propio almacén**", marcas ABB/Siemens/Schneider; motogeneradores Jenbacher/MWM/CAT/Wärtsilä/Solar/Guascor; desmantelamiento de plantas; "Véndanos su equipo". Resale: 39 máquinas, "Transformer AREVA" 17/07/2025 | **No**: ni kVA ni kV ni precio en la página de trafos (catálogo 404) | Compra-venta, asesoría, almacenaje | ">15 años" (sociedad 2017); Resale desde 2021 | Micro/pyme | [ABIERTA] |
| **Aurinka PV Group** | España (Rivas-Vaciamadrid) | Listada como "Händler" de la rúbrica Transformatoren en Maschinensucher; web es de fotovoltaica | No | n/d | n/d | n/d | [ABIERTA] web; relevancia baja |
| **Use It Again S.L.** | España (Antequera) | Dealer en Machineseeker: "Impianto autorizzato per lo smaltimento RAEE nel sud della Spagna" – reciclaje, no broker | No | No | n/d | n/d | [ABIERTA] |
| **Surus Inversa S.L.** | España (Madrid) | Único dealer español en SurplusRecord junto a Maquinaria Conservera T. Guillén (Murcia); web no abrió | n/d | n/d | n/d | n/d | [FRAGMENTO] |
| **H&J Solutions** (Graz) / **Aleclavis** (CZ) | Austria / Chequia | Sourcing de transformadores nuevos (Corea) para utilities/EPC europeos | No | Sourcing nuevo | n/d | Micro | [FRAGMENTO] (LinkedIn 999) |
| **SD Myers** | EE. UU. | Mantenimiento, ensayos, "Asset Refurbishment & Replacement" | No | No | 1965 | Medio | [ABIERTA] – referencia de modelo, no competidor ibérico |
| **Diesel Service & Supply / Generator Source** | EE. UU. (Colorado, FL, TX) | Grupos nuevos/surplus/usados, "Immediate Availability", alquiler, compra ("Sell Your Generator") | Sí | Sí | 50+ años | Medio | [ABIERTA] – modelo de referencia; no opera en Europa |
| **Genpower Ltd** | Reino Unido | **Importador de herramientas JCB/Hyundai**, no dealer de grupos | – | – | – | – | [ABIERTA] – descartar como competidor |
| **Power Continental** | ? | Dominio powercontinental.com no responde (502/túnel); WebSearch no devuelve nada | – | – | – | – | **NO ENCONTRADO** |
| **Pramac usados** | Italia | No se encontró canal de ocasión propio | – | – | – | – | **NO ENCONTRADO** |

**Marketplaces generalistas con oferta MVA en Europa** (todos [ABIERTA]):
- **Maschinensucher / Werktuigen / Machineseeker** (Essen): rúbrica "Gebrauchte Transformatoren" con 168-174 anuncios; 115 en Alemania, 22 Chequia, 11 Bélgica, **1 España**; filtro "Mva" 41 anuncios (5, 10, 15, 20/25, 31,5 MVA). Directorio de dealers de la rúbrica incluye Trafo City, HT-Volteq, EMEF-Energie, Power France (Montreuil), Hofstede Techniek (NL), Aznar AAM y Aurinka (ES).
- **Resale.info** (DE): "9149 results 1000 kva"; dealers General Power Holland, AAM.
- **Machinio**: agregador con listados de trafos "usados" en Aragón (Diestre 320/500 kVA, Alkargo 1250 kVA, estación 1600 kVA 2007-09) – bloqueado 403 a nuestro fetch [FRAGMENTO].
- **Mascus España**: 3.977 generadores en venta; vendedores LOXAM USADO (Gesan DVR150, Valladolid) y Ritchie Bros Auctioneers Spain (Ocaña).
- **Troostwijk Auctions** (NL): búsqueda "transformer" abrió pero sin resultados legibles.
- **SurplusRecord** (US): "Transformer Search", solo 2 dealers en España.

Conclusión §1: hay **≥6 traders europeos activos** con stock real en el rango 1-63 MVA (BTB, Koopmann, Trafo-City, HT-Volteq, Slaters, LV Trading hasta 2 MVA) y **≥2 traders de grupos ≥1 MW** en Países Bajos (GPH, DPX). En Iberia, **AAM Global** es el único que vende explícitamente "transformadores de segunda mano con disponibilidad inmediata", pero sin especificar potencias y como línea secundaria de un negocio de motogeneradores.

---

## 2. Talleres de reparación/reacondicionamiento de transformadores en España y Portugal

| Empresa | Ciudad | Web | ¿Vende reacondicionados? | Estado |
|---|---|---|---|---|
| **Hitachi Energy Spain** (ex-ABB) | Córdoba (fábrica potencia, >32.000 m² tras inversión >80 M€ anunciada 07/2024), Trapagaran-Bizkaia (servicio; oferta de empleo: "reparación de partes activas en taller") | hitachienergy.com/es | Servicio "para todas las marcas… más de 30 marcas heredadas", ciclo de vida completo; **no publica canal de ocasión** | [ABIERTA] |
| **Transformadores GEDELSA S.A.** | Salamanca | gedelsa.com | "empresa dedicada a la **fabricación y reparación** de transformadores de distribución y potencia… desde 1973… más de 70.000 transformadores". No vende usados | [ABIERTA] |
| **Rodritol S.L.** | Las Palmas de Gran Canaria | rodritol.com | Desde 1969; "reparación y mantenimiento de máquinas eléctricas estáticas y rotativas… BT y MT", "filtrado y regeneración de aceite de transformadores". Sin venta de usados | [ABIERTA] |
| **Arisa** | San Cibrao das Viñas (Ourense) | – | Directorio: reparación de transformadores BT/MT/AT, laboratorio de pruebas | [FRAGMENTO] |
| **Electromecánica Vigo** | Vigo | – | Directorio: "reparación de bobinas y núcleo del transformador" | [FRAGMENTO] |
| **Bobinados Quimar / Bobinados G. Romero** | Cartagena / Quart de Poblet | – | Directorio Empresite: bobinado, reparación trafos pequeños | [FRAGMENTO] |
| **Siemens Energy España** | – | siemens-energy.com/es | Página ES abrió vacía (JS); no se localizó taller de trafos en España | NO ENCONTRADO |
| **Efacec** | Portugal (Matosinhos) | efacec.pt/en/transformers | "power and distribution transformers, **mobile and portable solutions** as well as **maintenance services**"; >100.000 trafos fabricados; suministró 2 subestaciones móviles 15 MVA 66/21,5 kV a i-DE (Iberdrola) Navarra | [ABIERTA] – no vende usados |
| **ABB Service Portugal** | Portugal | PDF Voltimum | "reparação em oficina ou em campo… secagem da parte activa… tratamento de óleo" | [FRAGMENTO] |
| **Ambicare Industrial** | Portugal | – | LinkedIn: mantenimiento de transformadores | [FRAGMENTO] |
| **Electro Radio Bobinadora (Lisboa), Electro Universal (Matosinhos), Rebobinadora Pousense (Leiria), EBA (Sintra)** | Portugal | – | Directorio CAE 27110: bobinado/reparación motores; trafos no confirmado | [FRAGMENTO] |

Conclusión §2: **ningún taller independiente ibérico publica venta de transformadores de potencia reacondicionados**. Los que reparan potencia (Hitachi Córdoba/Trapagaran, Gedelsa, Efacec) son OEM y no ofrecen canal de ocasión. Esto confirma la parte de la hipótesis "nadie cruza oferta y demanda de usados ≥1 MVA en Iberia", **pero** son proveedores naturales del broker (reacondicionado, ensayos, garantía) y también competidores potenciales si deciden abrir un canal "certified pre-owned".

---

## 3. Alquiler de subestaciones móviles y transformadores en Iberia

| Empresa | Qué ofrece (texto literal donde existe) | Plazos | Estado |
|---|---|---|---|
| **Atlas Copco Rental España** | Portada ES: "Soluciones de alimentación", "Asistencia de emergencia ininterrumpida", "Plazos de entrega", "Alquiler de suscripción". Página es-AR (misma flota global): "Generadores de 20 kVA a 1250 kVA o más con configuración en paralelo; **Transformadores de hasta 6300 kVA y tensión de hasta 25 kV**; alquiler temporal completo con accesorios" | No cuantificado | [ABIERTA] ES + AR |
| **Bredenoord** (NL, opera en EU) | "Transformers… up to 20 kV"; flota publicada: **6.300 kVA, 5.000 kVA, 2.500 kVA, 1.600 kVA (6 kV), 1.250 kVA** primario 10/15/20 kV; "Products in stock" para venta | "Reliable power, instantly available" | [ABIERTA] |
| **Aggreko España** | Portada ES: "Distribución eléctrica → Transformadores", "Bancos de carga"; páginas globales: modulares **hasta 5.000 kVA** (ZA), 7-150 kVA (US/CA/MY). Página ES de transformadores devolvió 404 | n/d | [ABIERTA] portada; detalle [FRAGMENTO] |
| **Energyst → Finanzauto Rental SLU** (Tesya) | Interempresas 2021: "Finanzauto Rental dispone de bancos de carga, **transformadores** y material auxiliares… grupos Cat en alquiler… central en Arganda del Rey y más de 40 centros en la Península Ibérica" (incluye STET Portugal). energyst.com y finanzautorental.es no abrieron | n/d | [ABIERTA] Interempresas; webs propias NO |
| **HIMOINSA (Yanmar)** | Producto propio **"Mobile Transformer Substation" HRS 6300 D5/6 (20', 2×3.150 kVA = 6,3 MVA) y HRS 3150 D5/6 (10', 3,15 MVA)**; BT↔MT 3,3/6,6/11/24 kV; hasta 4 grupos en paralelo; caso minería 5.080 kVA. Es venta a alquiladores; HIMOINSA Rental Range | n/d | [ABIERTA] |
| **Electra Molins** | TopGen 550-4.000 kVA; "Alquiler grupos electrógenos" | n/d | [ABIERTA] |
| **Genesal Energy** | Fabricante grupos hasta 3.000 kVA DCP (data center); sin alquiler propio ni ocasión | – | [ABIERTA] |
| **Grupel** (PT) | Fabricante hasta 4.200 kVA; gama "Rental"; sin ocasión | – | [ABIERTA] |
| **Ormazabal / Ingeteam** | Sin oferta de alquiler ni subestación móvil en portada/productos | – | [ABIERTA] |
| **Efacec** | "Mobile & Portable Solutions" (venta a utilities; 2×15 MVA 66/21,5 kV a i-DE) | – | [ABIERTA] |
| **Hitachi Energy** | Subestaciones móviles "hasta 420 kV y 120 MVA… pueden desplegarse con poca antelación" (venta) | – | [ABIERTA] |
| **Iberdrola i-DE** | Subestación móvil propia 12,5 MVA 45 kV (Castilla y León) – flota interna | – | [FRAGMENTO] (403) |
| **Koopmann/hk-c Mietstationen** (DE) | Estaciones móviles alquiler **hasta 1.000 kVA**, 24 h | – | [ABIERTA] |
| **Alquiler Transformadores SL** | Oyón (Álava), constituida 02/01/2014, CNAE 4614 "intermediarios del comercio al por mayor de maquinaria", objeto: "intermediación o comercialización en el alquiler de maquinaria… compraventa de material eléctrico"; capital 3-30 k€; sin web | – | [ABIERTA] ficha Iberinform |

Conclusión §3: el **alquiler** cubre bien **≤6,3 MVA / ≤25 kV** (Atlas Copco, Bredenoord, Aggreko, Finanzauto-Energyst, Himoinsa HRS). **No hay alquiler comercial de subestaciones móviles >10 MVA en Iberia**: las utilities compran las suyas (Efacec→i-DE). El tramo 10-100 MVA de plazo corto queda realmente sin cubrir salvo importación desde DE/FI/UK.

---

## 4. Fabricantes ibéricos: ¿stock, entrega inmediata, canal de ocasión?

| Fabricante | Lo que dice la web sobre plazo/stock/ocasión | Estado |
|---|---|---|
| **Gedelsa** (Salamanca) | Nada sobre plazos ni stock; "fabricación y reparación"; homologada en eléctricas | [ABIERTA] |
| **Alkargo** (Bizkaia) | "Full range up to 420 kV and 500 MVA"; nada de plazo/stock/ocasión | [ABIERTA] |
| **Imefy Group** (Toledo; IT, PL, CN) | Catálogos, "Condiciones Generales de Venta"; nada de plazo/stock | [ABIERTA] |
| **Ormazabal** (Bizkaia/Burgos/Loeches) | Transformadores distribución/potencia/OLTC; nada de plazo/stock/ocasión | [ABIERTA] |
| **Cotradis** (Ormazabal Cotradis) / **Jesiva** (Valencia) | Webs no respondieron (reset/502) | NO ABIERTA |
| **Efacec** (PT) | Nada de plazo; sí "maintenance services" y "mobile solutions" | [ABIERTA] |
| **Hitachi Energy España** | Inversión >80 M€ Córdoba; "pedidos cubiertos para, al menos, los próximos cuatro años" (El Español 23/06/2026) | [ABIERTA] |
| **Siemens Energy España** | Página vacía (JS); El Español: coincide con 3-4 años | [FRAGMENTO] |

**Dato clave de plazo** (El Español-Invertia, 23-06-2026, [ABIERTA]): *"Los plazos de entrega para equipos críticos como transformadores de potencia… ya se alargan hasta los cuatro años… Lo que antes de la pandemia se compraba y entregaba en un plazo habitual de entre 10 y 12 meses, hoy requiere una antelación mínima de 3 a 4 años"*. Hitachi, Arteche, Ormazabal, Schneider y Siemens Energy "coinciden". Fuentes secundarias: Wood Mackenzie 115-130 semanas; Kolektor Etra (SI) ganó 19 trafos 12,5-100 MVA para España afirmando que "los productores locales no estaban en buena forma".

Conclusión §4: **ningún fabricante ibérico publica stock, "entrega inmediata" ni canal de ocasión**. Esto valida el *dolor* del plan (plazo), pero no la ausencia de competidores: los sustitutos del broker son importadores de nuevo (Kolektor Etra, Elsewedy, Westrafo) y los traders alemanes/finlandeses.

---

## 5. LinkedIn: brokers de transformadores / equipment brokers en España y Portugal

- LinkedIn devuelve **HTTP 999** a cualquier fetch; solo fragmentos de buscador. [FRAGMENTO]
- Búsquedas "broker transformadores España", "equipment broker subestación", "transformer broker Spain/Portugal/Iberia", "compraventa transformadores LinkedIn": **ningún perfil ni empresa ibérica** que se describa como broker de transformadores. Únicos hits: Jonathan Ferreira (mantenimiento trafos, Ambicare Industrial, PT), Pedro Franklin Risco Aliaga (venta de trafos en stock, ubicación no ibérica), Kerem Gülec/Aleclavis (CZ, sourcing OEM), H&J Solutions (AT).
- Resultado: **NO ENCONTRADO** broker ibérico autodeclarado en LinkedIn. Coherente con que AAM Global y Alquiler Transformadores SL no usan la palabra "broker".

---

## 6. Asociaciones: ¿bolsa de equipos o directorio de proveedores?

| Asociación | Qué hay | Estado |
|---|---|---|
| **UNEF** | "Listado de socios" filtrable por CCAA y actividad ("Venta de equipos", "Fabricantes", "Distribuidores"); "Bolsa de empleo". **No** hay bolsa de equipos | [ABIERTA] |
| **AEE (eólica)** | "Nuestros socios" (>350), portal de empleo, Sistema de Inteligencia Territorial. **No** bolsa de equipos | [ABIERTA] |
| **Spain DC** | Socios y partners, Comité de Energía y suministro. **No** directorio técnico ni bolsa | [ABIERTA] |
| **AFBEL** | Comités "Transformadores Eléctricos", "Grupos Electrógenos", "Aparellaje MT y AT"; listado de socios por provincia (Gedelsa-Salamanca, Ormazabal MT-Burgos, Hitachi Energy Spain, Ormazabal Cotradis, Siemens, ABB-Madrid…). **No** bolsa de equipos ni mercado secundario | [ABIERTA] (página de socios dedicada 404) |

Conclusión §6: ninguna asociación opera bolsa de equipos. Espacio libre para un "tablón" sectorial.

---

## 7. Veredicto razonado

**La hipótesis queda CORREGIDA.**

Lo que se **confirma**:
1. Ningún actor ibérico publica stock de transformadores 1-100 MVA con kVA/kV/precio ni se describe como broker (webs, LinkedIn, asociaciones, marketplaces: 1 solo anuncio español en Maschinensucher).
2. Los fabricantes ibéricos no ofrecen entrega inmediata ni ocasión; plazo OEM 3-4 años (El Español 2026).
3. No existe alquiler comercial de subestaciones móviles >6,3 MVA en Iberia.
4. Ningún taller independiente vende reacondicionados de potencia.

Lo que **refuta "nadie lo hace"**:
1. **AAM Global (Tarazona)** vende transformadores usados "evitando grandes plazos de entrega", con almacén propio y compra activa ("Véndanos su equipo"), más motogeneradores Jenbacher/CAT ≥1 MW. Es exactamente el modelo compra-venta, aunque sin especialización en MVA.
2. **Alquiler Transformadores SL (Oyón)** existe desde 2014 como intermediaria de alquiler/compraventa de material eléctrico (sin huella digital).
3. Los **traders alemanes y finlandeses venden ya a España** por Maschinensucher/Werktuigen/Machinio (anuncios localizados en Aragón y Madrid), y BTB se presenta como marketplace mundial con 150+ unidades y servicio 24/7.
4. **Alquiladores (Atlas Copco, Bredenoord, Finanzauto-Energyst, Aggreko)** cubren el plazo corto hasta 6,3 MVA / 25 kV, que es la banda baja del rango objetivo (1-100 MVA) y la banda de grupos ≥1 MW.

**Cuánta competencia europea hay**: identificados **6 traders de trafos con stock MVA** (BTB, Koopmann, Trafo-City, HT-Volteq, Slaters, LV Trading), **2-3 traders de grupos ≥1 MW** (GPH, DPX; más Resale/Exapro), **4 marketplaces** con oferta MVA, **4 alquiladores paneuropeos**. Es un mercado **fragmentado, de micro-pymes (1-10 personas) salvo Koopmann/Slaters/BTB**, sin líder ibérico ni marketing en castellano/portugués.

**Implicación para el plan**: reformular la hipótesis como *"no existe en Iberia un intermediario especializado 1-100 MVA + celdas MT/AT con stock verificado, ensayos y garantía, que compita con los traders DE/FI/UK en idioma, logística y homologación de compañías eléctricas"*. Riesgo principal: AAM Global o un alquilador (Finanzauto, Atlas Copco) escalen a la banda 10-60 MVA; o que BTB/Koopmann abran comercial ibérico.

---

## 8. Top 10 competidores o sustitutos más relevantes

1. **AAM Global / Aznar Assets Management (Tarazona, ES)** – único ibérico que vende trafos usados "con disponibilidad inmediata" y compra activos; también motogeneradores ≥1 MW.
2. **BTB Transformers (FI)** – marketplace con 150+ unidades, usados/surplus hasta 500 MVA, Fast Track y 24/7; el competidor conceptual más cercano al plan.
3. **Koopmann Transformatoren (DE)** – 210-250 trafos en stock de 50 kVA a 63 MVA, DB online, reparación hasta 110 kV, alquiler; grupo de 370 empleados.
4. **Slaters Electricals (UK)** – mayor stock UK de trafos y celdas 11-33 kV reacondicionados con 36 meses de garantía; vende 5-80 MVA; ya gana licitaciones públicas.
5. **Trafo-City GmbH (DE)** – compra-venta y alquiler de trafos 5-31,5 MVA 110 kV listados con ficha técnica; micro-empresa desde 2010 (modelo replicable).
6. **Maschinensucher/Werktuigen/Machinio** – canal donde ya se cruzan oferta y demanda MVA en Europa, con dealers españoles dados de alta; sustituto gratuito del broker.
7. **Atlas Copco Rental España / Bredenoord / Finanzauto Rental (ex-Energyst)** – alquiler de transformadores hasta 6.300 kVA / 25 kV y grupos hasta 1.250 kVA+ en paralelo: el sustituto real para "plazo corto" ≤6 MVA.
8. **HIMOINSA HRS (ES)** – fabricante murciano de subestaciones móviles 3,15/6,3 MVA en contenedor para alquiladores; puede verticalizar el alquiler.
9. **General Power Holland / DPX Power (NL)** – traders de grupos usados 1-2,8 MVA con stock publicado y compra de trafos usados; proveedores y rivales a la vez.
10. **Hitachi Energy / Efacec / Gedelsa (servicio OEM)** – no venden usados pero controlan reparación, ensayos y subestaciones móviles; si lanzan "certified pre-owned" o alquiler, cierran el hueco.

---

## 9. Tabla de URLs

| # | URL | Estado | Notas |
|---|---|---|---|
| 1 | https://www.btbplaza.com/ | ABIERTA 200 (FI) | /en/, /varastolista/, /fast-track/ → 502 |
| 2 | https://sahko.messukeskus.com/en/exhibitors/btb-transformers-oy-3/ | FRAGMENTO | "surplus and used transformers up to 500 MVA" |
| 3 | https://www.lvtrading.nl/ y /verkoop | ABIERTA 200 | stock kVA/kV |
| 4 | https://opalis.eu/fr/node/5484 | ABIERTA 200 | ficha LV Trading 27/02/2025 |
| 5 | https://www.werktuigen.com/koopmann-transformatoren/wt-747-519 | ABIERTA 200 | "approx. 210 transformers" |
| 6 | https://www.werktuigen.com/diverse-m/wt-381-5051 | ABIERTA 200 | "250 transformers… 50 kVA up to 63 MVA", Dahlewitz |
| 7 | https://www.hk-c.de/ , /leistungen/transformatoren/ , /leistungen/mietstationen/ | ABIERTA 200 | grupo Koopmann; alquiler ≤1.000 kVA |
| 8 | https://www.koopmann.de/ | ABIERTA 200 | ¡empresa distinta (imprenta)! descartada |
| 9 | https://www.maschinensucher.de/Transformatoren/ci-70 (+?kd=41102) | ABIERTA 200 | 168-174 anuncios; 1 en España |
| 10 | https://www.maschinensucher.de/alstom-leistungstrafo+20%2F25+mva…/i-21669853 | ABIERTA 200 | Alstom 20/25 MVA 110/20 kV, Cloppenburg |
| 11 | https://www.maschinensucher.de/tur+dd+31%2C5+mva…/i-14970319 | ABIERTA 200 | TuR 31,5 MVA 110/10,5 kV, Langenhagen |
| 12 | https://www.maschinensucher.de/Haendler/tci-70 | ABIERTA 200 | directorio dealers (Trafo City, HT-Volteq, AAM, Aurinka…) |
| 13 | https://www.werktuigen.com/Transformers/wcp-cat-70 | ABIERTA 200 | listado general |
| 14 | https://www.trafo-city.de/ | ABIERTA 200 | fundada 2010, An- und Verkauf |
| 15 | https://www.ht-volteq.de/ | ABIERTA 200 | fundada 2017, Handel & Service |
| 16 | https://www.machineseeker.com/Haendler/107446/ht-volteq-gmbh-cloppenburg | ABIERTA 200 | trust seal |
| 17 | https://plantautomation-technology.com/products/slaters-electricals-limited/mv-hv-switchgear | ABIERTA 200 | 36 meses garantía reacondicionado |
| 18 | https://www.slaterselectricals.com/ | NO (TLS alert 80 / 502) | FRAGMENTO vía Machinio/directorios |
| 19 | https://www.bowers.co.uk/ | NO (ECONNRESET) | – |
| 20 | https://www.wilsonpowersolutions.co.uk/ | ABIERTA 200 | nuevo 5-300 MVA |
| 21 | https://www.generalpowerholland.com/ | ABIERTA 200 | CAT 1600 kVA, Jenbacher 2800 kVA |
| 22 | https://resale.info/fr/used-machinery-dealer-59168/General-Power-Holland-BV | ABIERTA 200 | precios J320 35 k€, CAT 3520 180 k€ |
| 23 | https://www.dpxpower.nl/ | ABIERTA 200 | 10-2.000 kVA |
| 24 | https://www.dpxpower.com/ | ABIERTA 200 | empresa distinta (Texas) |
| 25 | https://www.resale.info/en/1000-kva/39/ | ABIERTA 200 | listado |
| 26 | https://www.dieselserviceandsupply.com/ | ABIERTA 200 | US |
| 27 | https://www.sdmyers.com/ | ABIERTA 200 | US, servicio |
| 28 | https://www.genpower.co.uk/ | ABIERTA 200 (curl) | importador JCB, no gensets |
| 29 | https://www.powercontinental.com/ | NO (502/túnel) | NO ENCONTRADO |
| 30 | https://www.aam-global.com/ y /transformadores/ | ABIERTA 200 | "disponibilidad inmediata… evitando grandes plazos" |
| 31 | https://resale.info/en/used-machinery-dealer-55757/Aznar-Assets-Management-SL | ABIERTA 200 | 39 máquinas, Transformer AREVA |
| 32 | https://www.aurinkapv.com/ | ABIERTA 200 | fotovoltaica |
| 33 | https://www.machineseeker.it/Haendler/52143/use-it-again-s-l-antequera | ABIERTA 200 | RAEE |
| 34 | https://surplusrecord.com/dealers/dealer-search-by-location/worldwide/spain/ | ABIERTA 200 | Surus Inversa, Maq. Conservera |
| 35 | https://www.machinio.com/transformers/power-transformers/spain | NO (403) | FRAGMENTO buscador |
| 36 | https://www.mascus.es/construccion/generadores-usados | ABIERTA 200 | 3.977 anuncios; LOXAM USADO, Ritchie Bros |
| 37 | https://www.milanuncios.com/maquinaria/grupo-electrogeno-1000-kva.htm | NO (403/405) | – |
| 38 | https://www.olx.pt/equipamentos-e-ferramentas/equipamento-industrial/geradores/ | NO (403/405) | FRAGMENTO: 624 anuncios, 275-450 kVA |
| 39 | https://www.troostwijkauctions.com/search?q=transformer | ABIERTA 200 | sin resultados legibles |
| 40 | https://www.exapro.com/used-transformers/ | 404 | – |
| 41 | https://www.gedelsa.com/ y /soporte/ | ABIERTA 200 | "fabricación y reparación" |
| 42 | https://www.alkargo.com/ | ABIERTA 200 | hasta 500 MVA/420 kV |
| 43 | https://www.imefy.com/ | ABIERTA 200 | – |
| 44 | https://www.ormazabal.com/es/ y /productos/transformadores/ | ABIERTA 200 | – |
| 45 | https://www.jesiva.com/ | NO (reset/502) | – |
| 46 | https://www.cotradis.com/ | NO (reset/502) | – |
| 47 | https://www.efacec.pt/en/ y /en/transformers/ | ABIERTA 200 | "mobile and portable solutions… maintenance" |
| 48 | https://transformer-technology.com/efacec-supplies-mobile-substations-for-iberdrola-project-in-spain/ | ABIERTA 200 | 2×15 MVA 66/21,5 kV |
| 49 | https://www.hitachienergy.com/es/es y …/transformers/transformer-service | ABIERTA 200 | servicio multimarca |
| 50 | https://www.hitachienergy.com/latam/es/…/mobile-substations/trailers-semi-trailers | ABIERTA 200 | hasta 420 kV / 120 MVA |
| 51 | https://www.hitachienergy.com/latam/es/news-and-events/press-releases/2024/07/… | ABIERTA 200 | >80 M€ Córdoba |
| 52 | https://www.siemens-energy.com/es/es.html | ABIERTA 200 (vacía) | JS |
| 53 | https://www.elespanol.com/invertia/empresas/energia/20260623/… | ABIERTA 200 | plazos 3-4 años |
| 54 | https://www.aggreko.com/es-es | ABIERTA 200 | menú "Transformadores"; subpáginas 404 |
| 55 | https://www.atlascopco.com/es-es/rental | ABIERTA 200 | – |
| 56 | https://www.atlascopco.com/es-ar/rental/promotions/rental-power-generator | ABIERTA 200 | "Transformadores de hasta 6300 kVA y hasta 25 kV" |
| 57 | https://www.bredenoord.com/en/ y /en/rental/transformers/ | ABIERTA 200 | 1.250-6.300 kVA, 10/15/20 kV |
| 58 | https://www.energyst.com/ | NO (502/túnel) | – |
| 59 | https://www.interempresas.net/Alquiler-OP/375587-… | ABIERTA 200 | Finanzauto Rental: transformadores, 40 centros |
| 60 | https://www.finanzautorental.es/ | NO (421) | – |
| 61 | https://www.himoinsa.com/ y …/mobile-transformer-substation/…/eng.html | ABIERTA 200 | HRS 6300/3150 |
| 62 | https://www.genesalenergy.com/ | ABIERTA 200 | – |
| 63 | https://www.electramolins.com/ y /alquiler-grupos-electrogenos/ | ABIERTA 200 | TopGen 550-4.000 kVA |
| 64 | https://grupel.eu/ | ABIERTA 200 | hasta 4.200 kVA |
| 65 | https://www.ingeteam.com/es-es/ | ABIERTA 200 | sin alquiler |
| 66 | https://www.rodritol.com/ | ABIERTA 200 | 1969, regeneración aceite |
| 67 | https://www.iberinform.es/empresa/6320851/alquiler-transformadores | ABIERTA 200 | Alquiler Transformadores SL, 2014, CNAE 4614 |
| 68 | https://www.unef.es/ y /es/asociados/listado-de-socios | ABIERTA 200 | sin bolsa de equipos |
| 69 | https://aeeolica.org/ | ABIERTA 200 | sin bolsa |
| 70 | https://spaindc.com/ y /socios/ | ABIERTA 200 | sin bolsa |
| 71 | https://www.afbel.es/ | ABIERTA 200 | comités trafos/GE; sin bolsa |
| 72 | https://cz.linkedin.com/in/kerem-gulec-73a40b42 | NO (999) | FRAGMENTO Aleclavis |
| 73 | https://iberdrolaespana.com/press-room/news/detail/240621-… | NO (403) | FRAGMENTO 12,5 MVA 45 kV |
| 74 | https://www.surus.es/ | NO (reset/502) | – |
| 75 | https://www.gruposelectrogenosleston.com/ | NO (502) | FRAGMENTO directorio |
| 76 | https://www.loxam.es/es/maquinaria-de-ocasion | NO (cert) | – |
| 77 | https://www.rbauction.es/ | NO (403) | presente en Mascus |
| 78 | https://www.asset-trade.de/en/transformers | 404 | FRAGMENTO: secos 800-1250 kVA (2021) |
| 79 | https://www.hj-solutions.at/ | NO (502) | FRAGMENTO |
| 80 | https://content.voltimum.com/pt/14613/transformadores_abb_service_portugal.pdf | FRAGMENTO | ABB Service PT |

Páginas realmente abiertas con contenido (STATUS 200 y texto legible): **≈62**. Fragmentos: ≈12. Fallos de red/bloqueo: ≈16.
