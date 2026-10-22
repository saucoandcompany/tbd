# Verificación en página: transformadores/switchgear, turbinas de gas/gensets, AC portátil y tierras raras

Fecha de verificación: 22-10-2026. Método: 45 aperturas de página (pwfetch.js directo o `--browser`, y `curl` con User-Agent declarado para SEC/EDGAR y para dos páginas que devolvían 403) y 10 búsquedas web usadas solo para localizar URLs. Etiquetas: **[ABIERTA]** = cifra leída en el texto de la página; **[FRAGMENTO]** = solo vista en extracto de buscador; **[NO ABRIBLE]** = la página no se pudo abrir (se indica el motivo). Veredictos: CONFIRMADO / CORREGIDO (ambas cifras) / NO VERIFICADO. Ninguna cifra se ha inventado; lo que no se leyó queda marcado.

Ficheros de partida: `research_notes/Mercados con exceso de demanda 2026/b2b_industrial.md` (secciones 1, 2, 3, 9 y 15), `consumo_fisico.md` (AC portátil) y `reports/Demanda voraz sin filtros 2026.md` (filas 3, 8, 12 y 19).

## Resumen

1. **Transformadores y switchgear: la fila se sostiene con fuentes primarias abiertas.** Siemens Energy (nota oficial, 05-08-2026): backlog de Grid Technologies 51.000 M€, book-to-bill 1,48, backlog de grupo 162.000 M€. GE Vernova (8-K, 22-07-2026): Electrification pedidos 6.300 M$ (+66 % orgánico), book-to-bill ≈1,7, backlog de equipos 40.600 M$ (+69 %). Eaton (10-Q, 31-03-2026): backlog 22.800 M$, 68 % entregable en 12 meses; 8-K Q2 (31-07-2026): backlog del sector eléctrico +43 % interanual, Electrical Global +103 %. GSU >160 semanas en 1T 2026 vs 143 en 2024 confirmado en el despacho de Reuters (09-07-2026, vía AJOT), atribuido a Wood Mackenzie. Precios: +79 % en EE. UU. (BNEF, pv magazine Latam) y +77 % potencia / +45 % GSU desde 2019 (Wood Mackenzie vía POWER) leídos en página. España: El Español (23-06-2026) confirma "cubiertos pedidos para, al menos, los próximos cuatro años" (Hitachi Energy) y 10-12 meses prepandemia → 3-4 años.
2. **Turbinas de gas: todo lo esencial queda [ABIERTA] y la fila mejora en "Dinero".** GE Vernova 8-K: 116 GW (53 GW backlog firme + 63 GW reservas), ≥125 GW a fin de 2026, 20 GW/año en 3T 2026 → 24 GW 2028 → 30 GW 2030. Siemens Energy: Gas Services backlog 73.000 M€, book-to-bill 2,65, "lead times de tres años o más" (CFO, Utility Dive 10-08-2026). Mitsubishi: backlog de turbinas grandes 35 GW (Utility Dive 13-08-2026). Caterpillar 8-K (04-08-2026): ventas de Power Generation +29 % a 3.098 M$ con "price realization" de 212 M$. Nuevo dato de precio: pedidos de GE Vernova 1S 2026 10-20 puntos más caros en $/kW que 4T 2025 y Wood Mackenzie proyecta 600 $/kW a fin de 2027 (≈3x 2019) (Power Engineering, 23-04-2026).
3. **AC portátil: confirmado el núcleo (Caixin, SCMP, 36Kr, GIGA), sin cifra española de cadenas.** Midea PortaSplit >200.000 unidades en 2026 (x2), agotado en DE/FR/NL/UK (Caixin 01-07-2026); reventa 2-3x (36Kr); oferta a 749 € "agotada antes de empezar" (GIGA 09-07-2026). España: asociación balear Abtecir cifra +30 % en ventas de portátiles en toda España (Última Hora 23-07-2026). Galaxus (+38 %) no se pudo abrir; nota de Midea NL da 404.
4. **Tierras raras: la fecha 10-11-2026 y los +20 %/+12 % de imanes están abiertos; las primas 3x-5x de la IEA no.** CIRS reproduce el Anuncio MOFCOM/GAC n.º 70/2025 (suspensión hasta 10-11-2026); PricePedia (21-09-2026) confirma FOB China +20 % e imanes europeos +12 % ene-sep 2026; tungsteno +622 % confirmado (Visual Capitalist sobre IEA). El resumen ejecutivo de la IEA devolvió 403 incluso con Chromium.
5. **Re-puntuación solo con [ABIERTA]:** Transformadores/switchgear 11 (sin cambio), Turbinas/gensets 11 (sube de 10 por precio), AC portátil 9 (baja de 10: espera 2→1 por falta de dato de reposición abierto), Tierras raras 8 (baja de 9: dinero 3→2 sin la IEA). Aceptando [FRAGMENTO]: 11 / 11 / 10 / 9.

## Tabla de verificación

| # | Bolsillo | Afirmación del informe/notas | Cifra leída en página | Fecha de la página | URL | Etiqueta | Veredicto |
|---|---|---|---|---|---|---|---|
| A1 | Transformadores | GSU >160 semanas en 1T 2026 vs 143 semanas en 2024 (citando Reuters jul-2026) | "Generator step-up transformer lead times surpassed 160 weeks by the first quarter of 2026, compared with an average of 143 weeks in 2024"; interruptores AT 125 semanas (2S 2025) vs 77 (2023); Ben Boucher, Wood Mackenzie | Reuters, 09-07-2026 (reproducido por AJOT) | https://www.ajot.com/news/us-power-companies-scramble-to-secure-equipment-as-surging-data-center-demand-strains-supplies | [ABIERTA] | CONFIRMADO |
| A2 | Transformadores | Precios EE. UU. +79 % y plazos ≥100 MVA más que duplicados vs 2019 (BNEF) | "los plazos de entrega de los transformadores de gran tamaño (100 MVA y superiores) se han más que duplicado en comparación con 2019, y en el mercado estadounidense los precios ... han aumentado un 79 %" | pv magazine Latam, 27-02-2026 | https://www.pv-magazine-latam.com/2026/02/27/la-transicion-energetica-mundial-se-enfrenta-a-un-cuello-de-botella-en-el-hardware/ | [ABIERTA] | CONFIRMADO |
| A3 | Transformadores | PwC: plazos de alta capacidad "hasta cuatro años"; demanda GSU +274 % 2019-2025 (Wood Mackenzie) | "lead times for high capacity units to as long as four years, according to analysts from PwC"; GSU +274 % y subestación +116 % 2019-2025 | pv magazine USA, 11-05-2026 | https://pv-magazine-usa.com/2026/05/11/u-s-transformer-market-faces-severe-supply-constraints-as-lead-times-extend-to-four-years/ | [ABIERTA] | CONFIRMADO |
| A4 | Transformadores | Wood Mackenzie 2T 2025: potencia 128 semanas, GSU 144; déficit 30 %/10 %; GSU +45 % desde 2019 | "power transformers averaging 128 weeks and GSUs 144 weeks in WoodMac's second quarter 2025 survey"; "30% shortfall for power transformers and 10% for distribution"; precios desde 2019 +77 % potencia, +45 % GSU, hasta +95 % distribución | POWER, 02-01-2026 | https://www.powermag.com/transformers-in-2026-shortage-scramble-or-self-inflicted-crisis | [ABIERTA] | CONFIRMADO (añade +77 % potencia) |
| A5 | Transformadores (España) | Fabricantes "al completo cuatro años"; 10-12 meses prepandemia → 3-4 años; Hitachi Energy cubierta ≥4 años | "Tenemos cubiertos pedidos para, al menos, los próximos cuatro años" (Hitachi Energy); "antes de la pandemia ... 10 y 12 meses, hoy requiere una antelación mínima de 3 a 4 años"; mercado global de transformadores de potencia ≈30.000 M€ | El Español/Invertia, 23-06-2026 (act. 24-06-2026) | https://www.elespanol.com/invertia/empresas/energia/20260623/congestion-fabricantes-material-red-electrica-completo-pedidos-proximos-anos/1003744295811_0.html | [ABIERTA] | CONFIRMADO |
| A6 | Transformadores | Siemens Energy Grid Technologies backlog ≈51.000 M€, book-to-bill 1,48, pedidos +28 % | "Book-to-bill ratio was 1.48 and the order backlog increased to €51bn"; crecimiento "substantial ... in the transformer business including data center projects"; grupo: pedidos 17.900 M€, book-to-bill 1,57, backlog 162.000 M€ | Nota oficial Siemens Energy, 05-08-2026 (texto íntegro en EMR; listado de notas de siemens-energy.com confirma "Earnings Release Q3 FY 2026, August 5, 2026") | https://www.emr-online.com/siemens-energy-earnings-release-q3-fy-2026-siemens-energy-accelerates-profitable-growth-siemens-gamesa-delivers-a-positive-quarterly-result/ ; https://www.siemens-energy.com/global/en/home/press-releases.html | [ABIERTA] | CONFIRMADO (el +28 % no aparece en el texto leído; la tabla del PDF daría 27,6 % según buscador → ese decimal queda [FRAGMENTO]) |
| A7 | Transformadores | Siemens Energy ampliará capacidad de transformadores ~50 % hasta 2030 | "It plans to expand its transformer manufacturing capacity 50% by 2030" | Utility Dive, 10-08-2026 | https://www.utilitydive.com/news/siemens-gas-turbine-backlog-nears-70-gw-as-company-expands-manufacturing/827390/ | [ABIERTA] | CONFIRMADO |
| A8 | Transformadores | Hitachi Energy: planta de 528 M$ en Gallman (Misisipi), producción desde 2029; parte de 1.500 M$ en EE. UU. | "$528 million transformer factory in Gallman, Mississippi"; "transformer production at the Gallman site is scheduled to start in 2029"; "part of Hitachi's broader $1.5 billion investment to scale its U.S. manufacturing" | T&D World, 16-09-2026; American Public Power Association | https://www.tdworld.com/utility-business/news/55405686/hitachi-energy-selects-mississippi-for-528m-transformer-factory-to-bolster-us-manufacturing-grid-capacity ; https://www.publicpower.org/node/31233 | [ABIERTA] | CONFIRMADO (la cifra de "~6.000 M$ hasta 2027" no se leyó; pv magazine Latam habla de 9.000 M$ totales y 1.500 M$ en transformadores → CORREGIDO: 6.000 → 9.000 M$ según Hitachi Energy vía pv magazine) |
| A9 | Switchgear | GE Vernova Electrification: pedidos 6.300 M$ (+66 % orgánico), book-to-bill ≈1,7, backlog de equipos 40.600 M$ (+69 %) | "Orders of $6.3 billion increased +66% organically, driving a book-to-bill ratio of approximately 1.7"; "Increased equipment backlog to $40.6 billion, up $16.6 billion, or 69% year-over-year, including $5 billion from Prolec GE"; pedidos de centros de datos >5.000 M$ en el año, más del doble de todo 2025 | GE Vernova 8-K/Ex. 99, 22-07-2026 | https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000147/gevpressrelease2q26.htm | [ABIERTA] | CONFIRMADO |
| A10 | Switchgear | Eaton backlog ≈22.800 M$ a 31-03-2026, 68 % en 12 meses | "total backlog at March 31, 2026 was approximately $22.8 billion. ... approximately 68% of this backlog is targeted for delivery ... in the next twelve months" | 10-Q Eaton 1T 2026 | https://www.sec.gov/Archives/edgar/data/0001551182/000155118226000013/etn-20260331.htm | [ABIERTA] | CONFIRMADO |
| A11 | Switchgear | Eaton backlog eléctrico +43 % interanual en 2T 2026 | "total backlog growth of 43% in Electrical sector"; Electrical Americas backlog +33 %, Electrical Global +103 %; pedidos (media móvil 12 m) +41 % Americas, +33 % Global; book-to-bill eléctrico 1,2 | Eaton 8-K/Ex. 99, 31-07-2026 | https://www.sec.gov/Archives/edgar/data/0001551182/000155118226000027/etn06302026exhibit99.htm | [ABIERTA] | CONFIRMADO |
| A12 | Switchgear | Switchgear MT +50 % desde 2021; MT 44-80 semanas (Vawn, Terrapin, Electronate, Electrical Trader) | No abiertas en esta ronda (presupuesto dedicado a primarias) | — | — | [FRAGMENTO] | NO VERIFICADO |
| A13 | Transformadores | Distribución ~30 semanas; pad-mount empeora 2026-27 (DistroForge) | "26 to 40 weeks for standard catalog distribution units and 30 to 36 months for large power transformers, with extra-high-voltage units reaching 60 months"; pad-mount trifásico "shortages projected to worsen through 2026 and into 2027"; bushings AT hasta 130 semanas (informe de laboratorio nacional, may-2026) | DistroForge (blog de distribuidor, sin fecha visible; cita Reuters jul-2026) | https://distroforge.com/blog/transformer-procurement-2026/ | [ABIERTA] | CORREGIDO: "~30 semanas" → "26-40 semanas" |
| B1 | Turbinas | GE Vernova 2T 2026: 116 GW (vs 100), ≥125 GW a fin de 2026, 53 GW firmes + 63 GW reservas, 20 GW/año 3T 2026, 24 GW 2028, 30 GW 2030 | "Gas Power equipment backlog and slot reservation agreements grew from 100 to 116 GW; now anticipate reaching at least 125 GW by year-end 2026"; "backlog growth from 44 to 53 GW and an increase in slot reservation agreements from 56 to 63 GW"; "20 GW of annual gas turbine output in the third quarter of 2026, with 24 GW in 2028, and ... 30 GW in 2030"; backlog total 176.000 M$ | GE Vernova 8-K/Ex. 99, 22-07-2026 | https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000147/gevpressrelease2q26.htm | [ABIERTA] | CONFIRMADO |
| B2 | Turbinas | Plazos "directionally about three years"; pedido hoy = entrega 2031; ~20 % del backlog para centros de datos | Las frases "about three years" y "2031" NO aparecen en el 8-K; aparecen en artículos de prensa que recogen la call. Power Engineering (1T 2026): ~10 GW de capacidad 2029 disponible al entrar en el trimestre y clientes "pulled aggressively into 2030"; ~80 % de los 100 GW en EE. UU. | Power Engineering, 23-04-2026 | https://www.power-eng.com/gas/turbines/data-centers-drive-record-surge-in-ge-vernova-power-equipment-orders-as-turbine-slots-tighten-through-2030/ | [ABIERTA] (slots 2029-2030) / [FRAGMENTO] (2031, 20 %) | CORREGIDO: la fuente de "2031" y "20 %" es la call/prensa, no el 8-K; lo leído dice slots 2029-2030 |
| B3 | Turbinas | Precio: "Dinero 1, sin precio público" | "orders in the first half of 2026 is tracking 10 to 20 points higher on a dollar-per-kilowatt basis than fourth-quarter 2025 orders" (CEO); Wood Mackenzie: precios de turbinas de gas a 600 $/kW a fin de 2027, "nearly tripling from 2019 levels" | Power Engineering, 23-04-2026 | misma URL | [ABIERTA] | CORREGIDO: sí hay señal pública de precio (+10-20 p.p. $/kW trimestre a trimestre; ≈3x 2019) |
| B4 | Turbinas | Siemens Energy: backlog de turbinas de gas cerca de 70 GW; pedidos récord 17.900 M€ | Titular "gas turbine backlog nears 70 GW"; 15 GW de pedidos en el trimestre; ventas Gas Services +62 % a 10.000 M€; 6 GW enviados; "lead times across the company now run three years or more" (CFO); capacidad 15-16 GW/año | Utility Dive, 10-08-2026 | https://www.utilitydive.com/news/siemens-gas-turbine-backlog-nears-70-gw-as-company-expands-manufacturing/827390/ | [ABIERTA] | CONFIRMADO; la nota oficial añade Gas Services backlog 73.000 M€ y book-to-bill 2,65 [ABIERTA] |
| B5 | Turbinas | Mitsubishi Power (no estaba en notas) | "Mitsubishi's large-frame gas turbine backlog reaches 35 GW"; "plans to double its manufacturing capacity" (CFO Hiroshi Nishio) | Utility Dive, 13-08-2026 | https://www.utilitydive.com/news/mitsubishi-gas-turbine-backlog-earnings/827761/ | [ABIERTA] (titular y entradilla) | NUEVO DATO; "23 GW hace un año" solo [FRAGMENTO] |
| B6 | Gensets | Caterpillar backlog ≈63.000 M$ en 1T 2026 (Highways Today) / 72.100 M$ en 2T 2026 (buscador) | El 8-K del 2T no da la cifra: "Strong order rates and a growing backlog"; Power Generation 3.098 M$ (+29 %, +691 M$) "primarily in data center applications"; Power & Energy 8.238 M$ (+17 %), con "favorable price realization of $212 million" | Caterpillar 8-K/Ex. 99.1, 04-08-2026 | https://www.sec.gov/Archives/edgar/data/0000018230/000001823026000040/ex991toformcat2q2026earnin.htm | [ABIERTA] (ventas y precio) / [FRAGMENTO] (72.100 M$) | CORREGIDO: 63.000 M$ (1T) es dato viejo; el 2T se cita en prensa como 72.100 M$ (+92 %), no leído en documento primario |
| B7 | Gensets | Cummins "taking orders well into 2028" | No abierta (fuente Substack) | — | — | [FRAGMENTO] | NO VERIFICADO |
| C1 | AC portátil | Midea PortaSplit >200.000 unidades en 2026 (x2), agotado en DE/FR/NL/UK; exportaciones +55 % | "sales of a portable split air conditioner designed for Europe have topped 200,000 units this year, doubling from a year earlier, and the model has sold out in Germany, France, the Netherlands and the UK"; Gree +50 % en Francia 1S 2026 con instalaciones aplazadas a finales de agosto; Hisense +20 % Europa occidental; tren China-Europa recorta ~25 días | Caixin Global, 01-07-2026 (muro de pago; el párrafo clave y el resumen son visibles) | https://www.caixinglobal.com/2026-07-01/europes-heat-wave-lifts-sales-for-chinese-air-conditioner-makers-102459483.html | [ABIERTA] | CONFIRMADO (el +55 % de exportaciones queda tras el muro → [FRAGMENTO]) |
| C2 | AC portátil | Agotado en múltiples plataformas, reventa con prima | "has sold out across multiple e-commerce platforms as temperatures ... exceeded 40 degrees"; "fuels resale mark-ups and expedited shipping" | SCMP, 05-07-2026 | https://www.scmp.com/economy/global-economy/article/3359346/why-chinese-made-portable-ac-selling-out-across-heat-stricken-europe | [ABIERTA] (entradilla) | CONFIRMADO |
| C3 | AC portátil | Reventa 2-3x; agotado en DE/ES/FR | "completely sold out in Germany, Spain, and France. In the second-hand market, the price soared to two to three times the original price"; e-commerce alemán +37 % interanual en mayo | 36Kr Europe (2026, sin día visible) | https://eu.36kr.com/en/p/3877106650692489 | [ABIERTA] | CONFIRMADO |
| C4 | AC portátil | Folleto de bricolaje a 749 € ya "agotado" antes de la promoción | "Im Prospekt des V-Baumarkt ist die Midea PortaSplit für 749 Euro bereits als ausverkauft markiert ... Ausverkauft bevor die Aktion gestartet wurde"; PVP 1.199 € | GIGA, 09-07-2026 | https://www.giga.de/tech/midea-portasplit-heute-fuer-749-euro-baumarkt-reagiert--01KWV86RCWF1P8REQYSEYJAME2 | [ABIERTA] | CONFIRMADO |
| C5 | AC portátil | Midea: dos veranos seguidos agotado en Alemania (nota de empresa) | Página 404 | — | https://www.midea.com/nl/nieuws/midea-portasplit-responds-to-europes-growing-need-for-flexible-home-cooling | [NO ABRIBLE] | NO VERIFICADO |
| C6 | AC portátil | Galaxus +38 % en junio 2026, "almacenes europeos prácticamente agotados" | 403 directo; timeout con Chromium | — | https://www.digitec.ch/en/page/next-heatwave-to-hit-amid-a-shortage-of-fans-and-air-conditioners-43142 | [NO ABRIBLE] | NO VERIFICADO |
| C7 | AC portátil (España, nuevo) | Sin dato español en notas | "los equipos portátiles de refrigeración han experimentado un aumento en las ventas de un 30% en toda España" (Abtecir, asociación balear de técnicos) | Última Hora, 23-07-2026 | https://www.ultimahora.es/noticias/local/2026/07/23/2675977/tecnicos-climatizacion-detectan-aumento-del-ventas-equipos-portatiles-refrigeracion.html | [ABIERTA] | NUEVO DATO (asociación regional, no panel de ventas) |
| C8 | AC (España) | FECE +15 % ventas de AC (resultado de buscador) | La página es de 27-06-2019, no de 2026 | Alimarket, 27-06-2019 | https://www.alimarket.es/electro/noticia/300505/fece-estima-un-aumento-del-15--en-la-venta-de-aire-acondicionado-en-espana | [ABIERTA] | DESCARTADO (dato de 2019) |
| D1 | Tierras raras | Suspensión china expira 10-11-2026 | "Announcement No. 70 of 2025, announcing the suspension of multiple previous announcements effective immediately until November 10, 2026. The suspended announcements include MOFCOM and GAC Announcements No. 55, 56, 57, and 58 of 2025, as well as MOFCOM Announcements No. 61 and 62 of 2025" (todas de 09-10-2025) | CIRS Group, 12-11-2025 (reproduce el anuncio MOFCOM/GAC) | https://www.cirs-group.com/en/chemicals/china-temporarily-suspends-export-controls-on-key-raw-materials-including-rare-earths-lithium-batteries-and-diamond | [ABIERTA] | CONFIRMADO |
| D2 | Tierras raras | Exportaciones siguen muy por debajo (EUISS) | "China's rare-earth exports fell 9.6% to 43,711 tonnes in January to September 2026, even as September alone rose 6.7%" (Reuters/aduanas 14-10-2026); imanes a la UE ene-feb 2026 4.775 t (+28,4 %), a EE. UU. 994 t (−22,5 %); el régimen de licencias de abril 2025 para 7 tierras raras pesadas nunca se suspendió; IEA: 6,5 bn$/año de producción en riesgo si se aplicaran los controles | Technology.org, 19-10-2026 | https://www.technology.org/2026/10/19/china-rare-earth-export-pause-november-10/ | [ABIERTA] | CORREGIDO: "muy por debajo" → −9,6 % ene-sep 2026; los envíos de imanes a la UE suben (+28,4 %) |
| D3 | Imanes | FOB China +20 % vs ene-2026; Europa +12 % ene-sep 2026; prohibición a 14 empresas europeas (jul-2026) | "the two FOB prices in euros for Chinese exports of permanent magnets have increased by more than 20% compared with January 2026 levels"; "Between January and September 2026, European permanent magnet prices expressed in euros increased by more than 12%"; "banning ... dual-use goods, including rare-earth permanent magnets, to 14 European companies" | PricePedia, 21-09-2026 | https://www.pricepedia.it/en/magazine/article/2026/09/21/restrictions-on-chinese-exports-of-permanent-magnets-are-increasing/ | [ABIERTA] | CONFIRMADO |
| D4 | Tierras raras | IEA: disprosio/terbio ≈5x, galio ≈5x, germanio ≈3x el precio chino | 403 ("Just a moment") directo, curl y Chromium | — | https://www.iea.org/reports/global-critical-minerals-outlook-2026/executive-summary | [NO ABRIBLE] | NO VERIFICADO |
| D5 | Metales menores | Tungsteno +622 % ene-2025 → abr-2026 | "Tungsten prices surged 622% between January 2025 and April 2026"; tántalo +196 %, cobalto +134 %, neodimio +116 %, litio +108 %, praseodimio +107 % (datos IEA Outlook 2026) | Visual Capitalist, 06-08-2026 | https://elements.visualcapitalist.com/tungsten-leads-critical-mineral-price-gains-in-2026/ | [ABIERTA] | CONFIRMADO (añade neodimio +116 %, praseodimio +107 %) |

## Nuevas cifras leídas

**Transformadores / switchgear**
- Siemens Energy grupo (3T FY2026, 05-08-2026): pedidos 17.900 M€, book-to-bill 1,57, backlog 162.000 M€, ingresos 11.400 M€ (+18,5 % comparable); el flujo de caja "volvió a beneficiarse de anticipos de clientes, incluidas tasas de reserva" (reservation fees). Grid Technologies: book-to-bill 1,48, backlog 51.000 M€, "crecimiento sustancial del negocio de transformadores incluidos proyectos de centros de datos", Europa y Norteamérica como motores. [ABIERTA]
- GE Vernova Electrification (2T 2026): ingresos 3.600 M$ (+68 %, +29 % orgánico); pedidos de centros de datos >5.000 M$ en el año (más del doble de 2025); backlog de equipos 40.600 M$ incluye 5.000 M$ de Prolec GE. [ABIERTA]
- Eaton (2T 2026): Electrical Americas ventas récord 4.000 M$ (+18 % orgánico), margen 27,5 %; Electrical Global 2.500 M$ (+44 %, incl. Boyd Thermal, adquirida el 12-03-2026 por 9.550 M$); backlog eléctrico +43 %, Global +103 %; book-to-bill eléctrico 1,2 (12 m). [ABIERTA]
- Reuters (09-07-2026): interruptores AT 125 semanas (2S 2025) vs 77 (2023); "transformer costs could increase by around 4% to up to 10% over the next year"; capacidad de centros de datos EE. UU. 24 GW → 110 GW en 2030 y cuota de los centros de datos en el mercado de equipo eléctrico hasta 40 % (Wood Mackenzie). [ABIERTA]
- POWER (02-01-2026): ~40 millones de transformadores de distribución en EE. UU. más allá de su vida útil; ~1.800 M$ de ampliaciones anunciadas en Norteamérica; demanda +35 % a +274 % según tipo de equipo desde 2019 (Making the Connection, sep-2025). [ABIERTA]
- Hitachi Energy (vía pv magazine Latam, 27-02-2026): 1.500 M$ en transformadores dentro de 9.000 M$ de inversión total; plazos de adquisición de equipo de fábrica para transformadores grandes 2-4 años (Bruno Melles). [ABIERTA]
- DistroForge: EHV hasta 60 meses; RFP → contrato hasta 6 meses antes de empezar fabricación; bushings AT hasta 130 semanas. [ABIERTA, blog de distribuidor]

**Turbinas / gensets**
- GE Vernova (2T 2026): 20 GW nuevos contratos (18 GW reservas + 2 GW pedidos), 10 GW de reservas convertidas en pedidos, 3 GW enviados; backlog total 176.000 M$; FCF 5.100 M$. [ABIERTA]
- GE Vernova (1T 2026, vía Power Engineering 23-04-2026): GW bajo contrato 83 → 100; backlog 40 → 44 GW; reservas 43 → 56 GW; 25 turbinas enviadas (+32 %); ~80 % de los 100 GW en EE. UU.; ~10 GW de capacidad 2029 disponible al inicio del trimestre y clientes reservando ya en 2030; precios 1S 2026 +10-20 puntos en $/kW vs 4T 2025; Wood Mackenzie: 600 $/kW a fin de 2027 (~3x 2019). [ABIERTA]
- Siemens Energy Gas Services (3T FY2026): book-to-bill 2,65; backlog 73.000 M€; 15 GW pedidos en el trimestre, 6 GW enviados, 15-16 GW de entregas posibles en el año; "lead times de tres años o más" (CFO Maria Ferraro). [ABIERTA]
- Mitsubishi (ago-2026): backlog de turbinas grandes 35 GW; plan de duplicar capacidad. [ABIERTA, titular/entradilla]
- Caterpillar (2T 2026): ventas 20.500 M$ (+24 %), primer trimestre >20.000 M$; Power Generation 3.098 M$ (+29 %) "primarily in data center applications"; Power & Energy 8.238 M$ (+17 %) con 736 M$ de volumen y 212 M$ de precio. [ABIERTA]

**AC portátil**
- Gree: +50 % ventas en Francia 1S 2026, instalaciones aplazadas a finales de agosto, portátiles agotados en canales europeos; Hisense: +20 % Europa occidental, portátiles "en grave escasez"; Midea añadió turnos y usa tren China-Europa (−25 días de transporte). [ABIERTA, Caixin resumen]
- Midea e-commerce Alemania +37 % interanual en mayo 2026. [ABIERTA, 36Kr]
- PVP PortaSplit 1.199 €; promoción 749 € agotada antes de empezar (09-07-2026). [ABIERTA, GIGA]
- España: +30 % ventas de portátiles en toda España según Abtecir (23-07-2026). [ABIERTA, asociación regional]

**Tierras raras / imanes**
- Anuncio MOFCOM/GAC n.º 70/2025 suspende los anuncios 55-58, 61 y 62 (09-10-2025) hasta el 10-11-2026. [ABIERTA, CIRS]
- Exportaciones chinas de tierras raras ene-sep 2026: 43.711 t (−9,6 %); septiembre 4.269,8 t (+6,7 %); imanes a la UE ene-feb 2026 4.775 t (+28,4 %), a EE. UU. 994 t (−22,5 %); IEA: 6,5 bn$/año en riesgo; cuota china de refino 90 % (2023) → 85 % (2025) → 70 % (2035e); cerrar el gap de imanes exige ~60.000 M$ en una década. [ABIERTA, Technology.org]
- Imanes: FOB China +20 % vs ene-2026; Europa +12 % ene-sep 2026 (PricePedia); neodimio +116 %, praseodimio +107 % ene-2025 → abr-2026 (IEA vía Visual Capitalist). [ABIERTA]

## Re-puntuación (escala 0-3: Crecimiento, Dinero/precio, Espera/backlog, Robustez del motor)

**A. Transformadores y switchgear — 11/12 con solo [ABIERTA] (sin cambio; antes 11 con FRAGMENTO).**
- Crecimiento 2: pedidos de Grid Technologies +27-28 % y Electrification +66 % orgánico, backlog Eaton eléctrico +43 % → crece fuerte pero no se multiplica salvo en GE Vernova (40,6/24,0 = x1,69).
- Dinero 3: +79 % precio EE. UU. (BNEF), +77 % potencia y +45 % GSU desde 2019 (Wood Mackenzie), +4-10 % previsto el próximo año (Reuters), Siemens cobra "reservation fees" → precio y anticipo.
- Espera 3: GSU >160 semanas (3,1 años) vs 143 en 2024; España 3-4 años vs 10-12 meses; 51.000 M€ / 3.624 M€ trimestrales ≈ 3,5 años de ingresos de Grid Technologies en cartera.
- Motor 3: capacidad nueva de Hitachi en 2029 y Siemens +50 % en 2030; plazos de equipo de fábrica 2-4 años → no hay alivio antes de 2029.
- Con [FRAGMENTO] aceptado: 11 (no añade nada que mueva un eje).

**B. Turbinas de gas y gensets grandes — 11/12 con solo [ABIERTA] (sube de 10).**
- Crecimiento 3: GE Vernova GW bajo contrato 62 (3T 2025) → 100 (1T 2026) → 116 (2T 2026), x1,9 en tres trimestres; Siemens Gas Services ventas +62 %; Caterpillar Power Generation +29 %.
- Dinero 2 (antes 1): precio en $/kW +10-20 puntos en un trimestre y trayectoria a 600 $/kW (~3x 2019) según Wood Mackenzie; Caterpillar 212 M$ de "price realization" en el segmento; no hay fee pública publicada → no llega a 3.
- Espera 3: 116 GW frente a 20 GW/año de salida = 5,8 años de producción contratada (3,2 años solo con el backlog firme de 53 GW... 53/20 = 2,65); Siemens 73.000 M€ / (10.000 M€·4) ≈ 1,8 años de ventas con "tres años o más" de plazo; Mitsubishi 35 GW vs 16 GW vendidos en FY2025 ≈ 2,2 años.
- Motor 3: salida 20 → 24 (2028) → 30 GW (2030); reservas convertidas a pedidos 10 GW/trimestre.
- Con [FRAGMENTO] aceptado (entregas 2031, Cummins hasta 2028, Caterpillar 72.100 M$): 11 (mismo resultado).

**C. AC portátil en olas de calor (Europa) — 9/12 con solo [ABIERTA] (baja de 10).**
- Crecimiento 3: Midea >200.000 unidades, x2 interanual; Gree +50 % Francia; España +30 %.
- Dinero 3: reventa 2-3x el precio original (36Kr); SCMP "resale mark-ups"; oferta a 749 € agotada antes de empezar.
- Espera 1 (antes 2): la única cifra de espera abierta es "instalaciones aplazadas a finales de agosto" (Gree, Francia) y "agotado en pocas semanas"; el dato de reposición intra-temporada (Galaxus) y la nota de Midea no se abrieron → 1.
- Motor 2: estacional y dependiente de olas de calor; recurrencia de dos veranos solo [FRAGMENTO].
- Con [FRAGMENTO] aceptado (Galaxus +38 % y "almacenes europeos agotados", Midea dos veranos): 10.

**D. Tierras raras, imanes y metales menores (Europa) — 8/12 con solo [ABIERTA] (baja de 9).**
- Crecimiento 2: imanes a la UE +28,4 % ene-feb 2026 pero exportaciones totales chinas −9,6 % ene-sep → demanda en Europa crece, oferta restringida.
- Dinero 2 (antes 3): imanes Europa +12 % ene-sep 2026, FOB China +20 %, tungsteno +622 %, neodimio +116 %; las primas 3x-5x de la IEA no se leyeron → sin ellas no es 3.
- Espera 2: licencias por envío para 7 tierras raras pesadas desde abril 2025 nunca suspendidas; 14 empresas europeas vetadas desde jul-2026; sin cifra de plazo.
- Motor 2: la fecha 10-11-2026 es política; el propio artículo recoge argumentos de "no cliff edge" y caída de la cuota china de refino 90 → 85 %.
- Con [FRAGMENTO] aceptado (IEA 5x/5x/3x, germanio 6.355 vs 3.585 $/kg): 9.

## Lo que no se pudo abrir

| URL | Motivo | Qué se pierde |
|---|---|---|
| https://www.iea.org/reports/global-critical-minerals-outlook-2026/executive-summary | 403 "Just a moment" (Cloudflare) en directo, curl y Chromium | Primas 5x/5x/3x disprosio-terbio/galio/germanio Europa vs China |
| https://www.digitec.ch/en/page/next-heatwave-to-hit-amid-a-shortage-of-fans-and-air-conditioners-43142 | 403 en directo; timeout 30 s con Chromium | Galaxus +38 % junio 2026, "almacenes europeos prácticamente agotados" |
| https://www.midea.com/nl/nieuws/midea-portasplit-responds-to-europes-growing-need-for-flexible-home-cooling | 404 | Nota de Midea sobre dos veranos agotado en Alemania |
| https://www.nrel.gov/analysis/transformer-supply-chain | 502 | Informe DOE/NREL de cadena de suministro de transformadores (citado por DistroForge: bushings 130 semanas) |
| https://www.energy.gov/gdo/large-power-transformers | 404 | Página DOE sobre LPT |
| https://www.sec.gov/... (pwfetch directo) | 403 "Undeclared Automated Tool"; resuelto con curl y User-Agent declarado (GE Vernova 8-K, Eaton 10-Q y 8-K, Caterpillar Ex. 99.1 sí se leyeron) | — |
| https://www.sec.gov/cgi-bin/browse-edgar?...CIK=0000018230 | 403 incluso con curl (índice EDGAR); se localizó el Ex. 99.1 por buscador | — |
| https://www.nasdaq.com/articles/cat-ends-q2-record-backlog-demand-momentum-here-stay | 403 | Backlog Caterpillar 72.100 M$ en documento abierto |
| https://www.caterpillar.com/en/news/corporate-press-releases.html | timeout 30 s con Chromium | Nota oficial de Caterpillar (sustituida por el Ex. 99.1 en EDGAR) |
| https://www.gevernova.com/news | abrió (200) pero el listado renderizado no mostraba titulares de resultados; no se encontró nota del 3T 2026 (previsiblemente publicada hoy 22-10-2026, aún no indexada) | Datos 3T 2026 de GE Vernova |
| https://www.hitachienergy.com/news-and-events/press-releases | abrió (200) pero el listado no cargó contenido textual de notas | Nota oficial Gallman (sustituida por T&D World y APPA) |
| Wood Mackenzie 2026 (informe original) | no localizado por buscador; solo "Making the Connection" sep-2025 y declaraciones a Reuters jul-2026 | Serie 2026 de plazos de Wood Mackenzie |
| Red Eléctrica / CNMC (cola de acceso), ENTSO-E, AEMET, Daikin, Prysmian, Schneider, MP Materials, Lynas | no abiertas por presupuesto (45 aperturas agotadas en primarias de OEM y en las URL citadas) | Cola de conexión en España, datos de ola de calor, resultados de otros OEM |

## Registro de aperturas (45)

| # | URL | Método | Resultado |
|---|---|---|---|
| 1 | sec.gov/.../gevpressrelease2q26.htm | pwfetch | 403 |
| 2 | sec.gov/.../etn-20260331.htm | pwfetch | 403 |
| 3 | elespanol.com/.../congestion-fabricantes-material-red-electrica... | pwfetch | 200, leída |
| 4 | pv-magazine-latam.com/2026/02/27/... | pwfetch | 200, leída |
| 5 | pv-magazine-usa.com/2026/05/11/... | pwfetch | 200, leída |
| 6 | utilitydive.com/news/siemens-gas-turbine-backlog-nears-70-gw... | pwfetch | 403 |
| 7 | caixinglobal.com/2026-07-01/... | pwfetch | 200, leída (parcial, muro de pago) |
| 8 | midea.com/nl/nieuws/... | pwfetch | 404 |
| 9 | iea.org/reports/global-critical-minerals-outlook-2026/executive-summary | pwfetch | 403 |
| 10 | pricepedia.it/en/magazine/article/2026/09/21/... | pwfetch | 200, leída |
| 11 | sec.gov/.../gevpressrelease2q26.htm | curl UA declarado | 200, leída |
| 12 | sec.gov/.../etn-20260331.htm | curl UA declarado | 200, leída |
| 13 | emr-online.com/siemens-energy-earnings-release-q3-fy-2026-... | pwfetch | 200, leída |
| 14 | siemens-energy.com/global/en/home/press-releases.html | pwfetch --browser | 200, listado leído |
| 15 | tikr.com/blog/caterpillars-q2-earnings-cross-20-billion... | pwfetch | 200, leída |
| 16 | nasdaq.com/articles/cat-ends-q2-record-backlog... | pwfetch | 403 |
| 17 | tdworld.com/.../hitachi-energy-selects-mississippi-for-528m... | pwfetch | 200, leída |
| 18 | publicpower.org/node/31233 | pwfetch | 200, leída |
| 19 | powermag.com/transformers-in-2026-shortage-scramble-or-self-inflicted-crisis | pwfetch | 200, leída |
| 20 | ajot.com/news/us-power-companies-scramble-to-secure-equipment... | pwfetch | 200, leída |
| 21 | gevernova.com/news | pwfetch --browser | 200, sin titulares útiles |
| 22 | scmp.com/economy/global-economy/article/3359346/... | pwfetch | 200, leída (entradilla) |
| 23 | digitec.ch/en/page/next-heatwave-to-hit-amid-a-shortage... | pwfetch | 403 |
| 24 | technology.org/2026/10/19/china-rare-earth-export-pause-november-10/ | pwfetch | 200, leída |
| 25 | iea.org/... | curl UA navegador | 403 |
| 26 | utilitydive.com/news/siemens-gas-turbine-backlog... | curl UA navegador | 200, leída |
| 27 | sec.gov/cgi-bin/browse-edgar?...CIK=0000018230 | curl | 403 |
| 28 | iea.org/... | pwfetch --browser | 403 |
| 29 | digitec.ch/... | pwfetch --browser | timeout |
| 30 | caterpillar.com/en/news/corporate-press-releases.html | pwfetch --browser | timeout |
| 31 | hitachienergy.com/news-and-events/press-releases | pwfetch --browser | 200, sin texto de notas |
| 32 | siemens-energy.com/global/en/home/investor-relations.html | pwfetch --browser | 200, listado leído (Q3 FY26 Earnings Release 05-08-2026; Q4 FY2026 el 11-11-2026) |
| 33 | nrel.gov/analysis/transformer-supply-chain | pwfetch | 502 |
| 34 | energy.gov/gdo/large-power-transformers | pwfetch | 404 |
| 35 | distroforge.com/blog/transformer-procurement-2026/ | pwfetch | 200, leída |
| 36 | eu.36kr.com/en/p/3877106650692489 | pwfetch | 200, leída |
| 37 | giga.de/tech/midea-portasplit-heute-fuer-749-euro... | pwfetch | 200, leída |
| 38 | elements.visualcapitalist.com/tungsten-leads-critical-mineral-price-gains-in-2026/ | pwfetch | 200, leída |
| 39 | power-eng.com/gas/turbines/data-centers-drive-record-surge-in-ge-vernova... | pwfetch | 200, leída |
| 40 | sec.gov/.../etn06302026exhibit99.htm (Eaton 8-K 2T 2026) | curl UA declarado | 200, leída |
| 41 | utilitydive.com/news/mitsubishi-gas-turbine-backlog-earnings/827761/ | curl UA navegador | 200, titular y entradilla leídos |
| 42 | alimarket.es/electro/noticia/300505/fece-... | pwfetch | 200, leída (es de 2019) |
| 43 | ultimahora.es/noticias/local/2026/07/23/2675977/... | pwfetch | 200, leída |
| 44 | cirs-group.com/en/chemicals/china-temporarily-suspends-export-controls... | pwfetch | 200, leída |
| 45 | sec.gov/.../ex991toformcat2q2026earnin.htm (Caterpillar 8-K 2T 2026) | curl UA declarado | 200, leída |

Búsquedas web usadas (10, solo para localizar URLs): Siemens Energy Q3 FY2026; GE Vernova Q3 2026; Caterpillar Q2 2026; Hitachi Energy Gallman; Wood Mackenzie plazos 2026; Eaton Q2 2026; Mitsubishi Power backlog; MOFCOM 10-11-2026; AC portátil España 2026; Caterpillar 8-K 2T 2026.
