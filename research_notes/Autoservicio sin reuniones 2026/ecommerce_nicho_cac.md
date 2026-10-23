# Ecommerce de nicho en España: CAC frente a margen bruto por pedido (dropshipping UE y stock mínimo)

Fecha: 23-10-2026. Fila: ecommerce de nicho (a) dropshipping/proveedor UE sin stock, (b) reventa con stock mínimo. Perfil: Jorge, ingeniero, sin reuniones de venta, el cliente compra solo en la web. Métrica: CAC vs margen bruto por pedido. Escenarios de anuncios: 300 / 1.000 / 2.000 €/mes.

Convenciones: [ABIERTA] = página abierta y leída con pwfetch/curl/jina; [FRAGMENTO] = cifra vista solo en un extracto de buscador o en una página que cita a otra; NO ENCONTRADO = se intentó y no apareció; "sin dato" = no hay cifra verificable. Toda cifra lleva moneda, fecha y URL. Los supuestos propios van marcados con asterisco (*).

---

## 0) Veredictos H1-H7

| Hipótesis | Veredicto | Resumen en una línea |
|---|---|---|
| H1. Conversión ecommerce España 2025-26 = 1-2 % general | **CONFIRMADA (con matiz)** | Flat 101 España (edición 2023, la última publicada en su web): 1,20 % medio, ticket medio 196,89 €. Littledata (433 tiendas Shopify, jul-oct 2026): mediana 1,4 %, AOV mediano 111 USD. Statista vía Shopify: 1,4 % global T1 2026. Por sector: 1,0 % hogar/mueble a 2,9 % belleza. No existe edición Flat 101 2025/2026 localizable (NO ENCONTRADO). |
| H2. CPC Shopping/Search España por categoría | **CORREGIDA** | No hay CPC público por categoría para España (Statista lo tiene de pago, dic-2024, con cifras ocultas). Lo mejor: smec Market Observer (650 M€ de inversión ecommerce europea, actualizado 19-10-2026): mediana CPC Shopping 0,34 €, PMax 0,41 €, Search 0,47 €. WordStream 2026 (EE. UU., búsqueda, USD) sirve de techo: hogar 8,33 $, salud 6,17 $, industrial 5,87 $, belleza 4,62 $. |
| H3. Margen dropshipping proveedor UE 20-40 %; cuota BigBuy | **CONFIRMADA (parcial)** | BigBuy: página oficial de tarifas bloqueada (403/401) incluso con navegador; fuentes secundarias 2025-26: pack Ecommerce 89 €/mes, Marketplace 119 €/mes, B2B 0 €/mes, +89 € de alta (Copyfy); 69-99 €/mes + 90 € de alta (Trendtrack). Ejemplo de desglose Copyfy sobre un PVP de 50 €: margen bruto 13,17 € (26 %), negativo con 20 € de publicidad. Printful: plan gratis 0 $/mes, Growth 24,99 $/mes; camiseta base ~10,75 $ + envío Europa 4,99 $ (+1,45 $ por unidad adicional). Gelato: precios bloqueados (403/401); solo "hasta 33 % de descuento" con Gelato+. |
| H4. CAC > margen bruto en la mayoría de nichos <60 € | **CONFIRMADA** | Con CPC mediano europeo (0,34-0,47 €) y conversiones sectoriales, el CAC va de 14 € (suplementos) a 47 € (hogar). Todos los nichos con ticket <60 € dan margen bruto por pedido inferior al CAC (ver tabla 4). Solo salen positivos: aire acondicionado portátil (ticket ~350 €, solo si el envío voluminoso no se come el margen), pedidos B2B de material eléctrico ≥ ~110-120 € y, como referencia externa, belleza (conversión 2,9 %). |
| H5. Supervivencia de tiendas nuevas | **CONFIRMADA (dato 2022)** | Globe and Mail (análisis de Store Leads, 2019-2022): solo el 34 % de las tiendas Shopify sobrevive un año (36 % cohorte 2019, 34 % 2020, 32 % 2021); Shopify Plus 62 %. Store Leads (16-10-2026): 3.163.099 tiendas Shopify activas, +15 % interanual. Mediana de ingresos por tienda: sin dato público. El "90 % fracasa" que circula en blogs no tiene fuente. |
| H6. Demanda España de 5 nichos | **SIN DATOS (parcial)** | Google Trends devolvió 429 en 3 intentos (con y sin navegador). Volumen "suplementos menopausia 1.300/mes" y "+64 % climatización" vienen del encargo, no se pudieron verificar aquí. Competencia Amazon.es sí se midió: menopausia 97 resultados (precios 9,82-19,04 €; top: Ymea 1,5 K reseñas y 200+ compras/mes); aire acondicionado portátil >20.000 resultados (180-1.489 €); guantes nitrilo >1.000 resultados (Amazon Basics 4,95 €/100 u, 9,5 K reseñas, 4 K+ compras/mes). Bornas, multímetro, deshumidificador y fusibles: Amazon devolvió 503 (bloqueo antibot). |
| H7. Amazon FBA sin reuniones | **CORREGIDA** | Comisiones oficiales Amazon.es (23-10-2026): plan Profesional 39 €/mes sin IVA o 0,99 €/unidad; referencia "la mayoría entre 8 % y 15 %"; vitaminas y suplementos ≤10 € bajan de 8 % a 5 % desde 5-1-2026; tabla de tarifas FBA local España no extraída (sin dato). PPC: mediana CPC Sponsored Products España 0,37 USD (ECDB, datos ~2023, [FRAGMENTO]); EE. UU. 2026: suplementos 1,50-3,00 $/clic, hogar 0,75-1,50 $ (Canopy). Rentabilidad: Jungle Scout 2024 (vía RevenueGeeks): 58 % rentables en el primer año, 22 % aún no; 57 % con margen >10 %. Jungle Scout 2025: informe tras formulario; solo visible que ~40 % de marcas enterprise temen por su rentabilidad por costes. No hay casos de vendedores españoles con ingresos publicados: Amazon solo da agregados (17.000 pymes, 1.200 M€ exportados en 2024 → ~70.600 € de exportación media por pyme, cálculo propio). |

---

## 1) Conversión y ticket medio por sector (fuente y fecha)

| Fuente | Ámbito / muestra | Conversión | Ticket medio | Estado |
|---|---|---|---|---|
| Flat 101, Estudio de conversión 2023 (artículo de metodología) | España, >1.100 negocios digitales | Media 1,20 %; desktop 2,2 % vs móvil 0,9 %; app 2,47 % vs web 1,38 %; sesiones con buscador interno 5,12 % vs 1,04 % | 196,89 € (media de participantes, incluye viajes/servicios) | [ABIERTA] https://www.flat101.es/blog/analitica-web/estudio-de-conversion-2023-de-flat-101-recogida-tratamiento-y-analisis-de-datos/ |
| Flat 101, edición 2025/2026 | — | NO ENCONTRADO: la búsqueda interna de flat101.es solo lista ediciones 2016-2023; URL /estudio-conversion-negocios-digitales-2025/ da 404 | — | [ABIERTA] https://www.flat101.es/?s=estudio+conversion |
| Littledata, benchmark Shopify (generado 21-10-2026, 90 días jul-oct 2026) | 433 tiendas Shopify con GA4 | Mediana 1,4 % (media 1,9 %); top 20 % >2,7 %; top 10 % >3,6 %. Por sector: belleza 2,9 %, salud y suplementos 2,4 %, alimentación 2,4 %, moda 1,1 %, hogar y mueble 1,0 % | AOV mediano 111 USD; top 20 % 290 USD; ingreso por sesión mediano ~1 USD; abandono de carrito 78 % | [ABIERTA] https://www.littledata.io/average/ecommerce-conversion-rate-(all-devices) y https://www.littledata.io/average/average-order-value |
| Shopify blog (22-08-2026, datos de junio 2026) | Tiendas Shopify por industria | Alimentación 4,58 %; belleza 5,32 %; mascotas 5,7 %; moda 2,77 %; hogar y mueble 1,29 %; bienes de consumo 1,76 %; lujo y joyería 0,63 %. Cita Statista: 1,4 % global T1 2026; Dynamic Yield 2,66 % | sin dato | [ABIERTA] https://www.shopify.com/blog/ecommerce-conversion-rate |
| CNMC, comercio electrónico España | Oficial, T2 2025 | — | 28.346 M€ / 493 M transacciones en T2 2025 → ~57 € por transacción (cálculo propio); Marketing4ecommerce calcula 55,96 € para 2025 (desde 67,30 € en 2015) | [ABIERTA] https://www.cnmc.es/node/418044 ; https://marketing4ecommerce.net/decada-de-datos-del-comercio-electronico-en-espana/ |
| IAB Spain, Estudio Ecommerce 2025 | España | La página existe pero no muestra cifras sin descarga; NO ENCONTRADO el ticket medio | — | [ABIERTA] https://iabspain.es/estudio/estudio-ecommerce-2025/ |
| WordStream/LocaliQ 2026 (búsqueda, EE. UU.) | 16.000+ campañas | Conversión media de anuncios de búsqueda 8 % (2026), 7,52 % (2025); mueble 2,73 %, moda/joyería 3,99 %, regalos 3,83 %, industrial 7,17 % (2025). Incluye leads, no solo ventas | — | [ABIERTA] https://www.wordstream.com/blog/2026-google-ads-benchmarks y https://www.wordstream.com/blog/2025-google-ads-benchmarks |

Lectura: para una tienda nueva en España, planificar con 1,0-1,4 % (hogar/técnico) y 2,4 % (suplementos) es realista; las conversiones del 7-8 % de WordStream son de campañas de búsqueda con formularios de leads y no aplican a ecommerce.

---

## 2) CPC por sector (fuente y fecha)

| Fuente | Ámbito | Categoría | CPC | Estado |
|---|---|---|---|---|
| smec Market Observer (actualizado 19-10-2026) | Ecommerce europeo, 650 M€ de inversión | Mediana ecommerce | Shopping 0,34 €; PMax 0,41 €; Search 0,47 €. Inflación interanual 1-3 % en T4 2025 | [ABIERTA] https://smarter-ecommerce.com/en/smec-market-observer/metrics/cpc |
| smec, informe T4 2025 | Ecommerce europeo | Shopping | T3 2025 ~0,29-0,30 €, pico T4; Search ~0,40 € estable T3-T4 2025 | [ABIERTA] https://smarter-ecommerce.com/en/smec-market-observer/reports/Q4_2025/ |
| WordStream 2026 (búsqueda, EE. UU., USD) | Todas las industrias | Media 5 $ y pico | Hogar y reformas 8,33 $; salud y fitness 6,17 $; industrial y comercial 5,87 $; belleza 4,62 $; moda/joyería 4,44 $; regalos 4,14 $; mueble 3,97 $; mascotas 4,06 $ | [ABIERTA] https://www.wordstream.com/blog/2026-google-ads-benchmarks |
| WordStream 2025 (búsqueda, EE. UU., USD) | Todas | Media 5,26 $ (+12,88 % interanual) | Hogar 7,85 $; salud 5,00 $; industrial 5,70 $; belleza 5,70 $; mueble 3,86 $ | [ABIERTA] https://www.wordstream.com/blog/2025-google-ads-benchmarks |
| Statista, CPC Google Ads por industria en España (dic-2024, fuente Semrush) | España | Por industria | Cifras ocultas (****): banca online la más alta, belleza la más baja. Premium | [ABIERTA, de pago] https://www.statista.com/statistics/1243710/spain-search-advertising-cpc |
| Lionelz (agencia española, 2026) | España | Estimación | "En España los CPC suelen ser 20-40 % más bajos que EE. UU."; reconoce que no hay dato primario español | [ABIERTA] https://lionelz.com/blog/cuanto-cuesta-google-ads/ |
| Google Shopping por industria (WordStream vía SEJ, 2018) | EE. UU. | Shopping | Media 0,66 $ (dato antiguo, solo orientativo) | [FRAGMENTO] https://www.searchenginejournal.com/google-shopping-ads-industry-benchmarks-wordstream/302375/ |
| Amazon Ads España (ECDB, gráfico feb-2024) | Amazon.es | Sponsored Products | Mediana 0,37-0,38 USD; ACoS 28,8 %; Sponsored Brands 0,32 $; Display 0,18 $ | [FRAGMENTO] https://ecommercedb.com/insights/amazon-ad-types-in-spain-an-analysis-of-performance-metrics/4516 (la página abierta solo muestra portada comercial) |
| Amazon Ads EE. UU. 2026 (Canopy Management) | Amazon.com | Por competencia | Suplementos, electrónica, belleza 1,50-3,00 $/clic; hogar, mascotas, deporte 0,75-1,50 $; industrial más bajo | [ABIERTA] https://canopymanagement.com/?p=22791 |

CAC = CPC / conversión (ver tabla 4). Con la mediana europea de Shopping (0,34 €) y conversión sectorial: suplementos 14 €, belleza 12 €, general 24 €, hogar/clima 34 €. Con Search (0,47 €): 20 €, 16 €, 34 €, 47 €. Con CPC estadounidenses de búsqueda, los CAC se multiplican por 10-20 (p. ej. hogar 8,33 $/1 % = 833 $) y ningún nicho funciona.

---

## 3) Proveedores: márgenes, cuotas y costes

| Proveedor | Cuota | Coste base / comisión | Margen observado | Estado |
|---|---|---|---|---|
| BigBuy (dropshipping UE, Valencia) | Oficial: página /es/tarifas bloqueada (403 directo y con navegador; 401 vía jina; la segunda carga jina devolvió solo menú). Secundarias: pack Ecommerce 89 €/mes, Marketplace 119 €/mes, B2B 0 €/mes, +89 € de alta, conectores aparte (Copyfy, 2025-26); 69-99 €/mes + 90 € de alta (Trendtrack, 2026) | Catálogo mayorista con filtros de margen; IVA según normativa UE; sin pedido mínimo | Ejemplo Copyfy, PVP 50 €: compra 18 € + envío 6 € + IVA 8,33 € + cuota prorrateada 3 € + pago 1,50 € = 36,83 €; margen bruto 13,17 € (26 %); con 20 € de ads por cliente margen neto −6,83 €. Recomienda ticket ≥70-80 € y conversión ≥2 %. Trendtrack: "márgenes a menudo bajos", problemas de sincronización de stock | [ABIERTA] https://www.copyfy.io/es/blog/opinion-bigbuy ; https://www.trendtrack.io/es/blog-post/resena-de-bigbuy-es-una-opcion-confiable-para-tu-sitio-de-dropshipping ; https://r.jina.ai/https://www.bigbuy.eu/es/dropshipping ; NO ENCONTRADO tarifa oficial |
| Printful (POD) | Free 0 $/mes; Growth 24,99 $/mes (gratis desde 12 K$/año de ventas; hasta 33 % de descuento en producto) | Camisetas base en catálogo (vista desde IP EE. UU.): Unisex Quality Tee 10,75 $; Printstar 10,xx $; Oversized 14,xx $; orgánica AS Colour 20,xx $. Envío Europa: 4,99 $ primera unidad + 1,45 $ adicional; EE. UU. 4,95 $ + 2,20 $. Extras: etiqueta interior 0,99 $, exterior 2,49 $ | Con PVP 29,99 € y coste ~15,74 $ (producto + envío) el margen bruto ronda el 50 % (FX no verificado*) | [ABIERTA] https://www.printful.com/pricing ; https://www.printful.com/shipping ; https://www.printful.com/custom/mens/t-shirts/bella-canvas-3001 (con navegador) |
| Gelato (POD) | Gelato+ con "hasta 33 % de descuento" y envío gratis en pedidos de 3+ hasta 30-11-2026; precio de suscripción no visible | sin dato (403 directo y con navegador; 401 jina en /es/) | sin dato | [FRAGMENTO] https://r.jina.ai/https://www.gelato.com/pricing |
| Shopify (plataforma) | Basic 29 USD/mes anual (39 USD mensual); Grow 79 USD; Advanced 299 USD; tarjeta desde 2,9 % + 30 ¢ | — | — | [ABIERTA] https://www.shopify.com/es/precios |
| Amazon.es (vendedor) | Profesional 39 €/mes sin IVA; Individual 0,99 €/unidad | Referencia: "la mayoría entre 8 % y 15 %". Cambios 2026: ropa ≤15 € 5 %, 15-20 € 10 %; hogar ≤20 € 8 %; vitaminas/suplementos y alimentación ≤10 € 5 %. FBA bajo precio para productos ≤20 € (−0,45 € de media). Almacenamiento: 27,54 €/m³/mes estándar (otras categorías), 19,99 €/m³ ropa; temporada alta 52,20 €/m³. Tarifa FBA local España por tamaño: NO ENCONTRADA en las páginas abiertas (las URLs de ayuda G201003400 redirigen a "mercancías peligrosas"; G201112650 muestra la tabla transfronteriza: sobre ligero ≤20 g a Portugal 7,71 € 1 ud) | Incentivos nuevo vendedor: 10 % de devolución sobre los primeros 45.000 € de marca registrada, 850 € de crédito publicitario | [ABIERTA] https://sell.amazon.es/precios (texto y navegador) ; https://sellercentral.amazon.es/help/hub/reference/external/G201112650?locale=es-ES |

---

## 4) CAC vs margen bruto por nicho (cálculo explícito)

Supuestos comunes: CPC mediano europeo smec (Shopping 0,34 €; Search 0,47 €, 19-10-2026). Conversión sectorial Littledata oct-2026 (suplementos 2,4 %; hogar/clima 1,0 %; moda/POD 1,1 %; belleza 2,9 %; resto 1,4 % general). Ticket: observado en Amazon.es el 23-10-2026 cuando hay dato, si no supuesto*. Margen bruto: 26 % dropshipping (ejemplo BigBuy/Copyfy) salvo donde se indica*. Costes fijos: Shopify Basic ~27 €/mes (29 USD, FX 0,92*) + BigBuy Ecommerce 89 €/mes = ~116 €/mes (no aplica a POD, que es 0 $/mes: ahí sobran ~89 € de los fijos). Fórmula: CAC = CPC / conversión; pedidos = presupuesto / CAC; margen neto mes = pedidos × margen bruto − presupuesto − fijos. Ticket de equilibrio = CAC / margen %.

| Nicho | Ticket € | Conv. % | Margen bruto €/pedido | CAC Shopping € | CAC Search € | ¿CAC < margen? | Ticket equilibrio (Shopping) € |
|---|---|---|---|---|---|---|---|
| Suplementos menopausia, dropshipping 26 % | 22,00 | 2,4 | 5,72 | 14,2 | 19,6 | NO | 54 |
| Suplementos menopausia, stock/marca propia 45 %* | 22,00 | 2,4 | 9,90 | 14,2 | 19,6 | NO | 31 |
| Aire acondicionado portátil, 15 %* | 350,00 | 1,0 | 52,50 | 34,0 | 47,0 | SÍ (Shopping y Search) | 227 |
| Aire acond. portátil, 15 % menos 15 € de envío voluminoso* | 350,00 | 1,0 | 37,50 | 34,0 | 47,0 | Solo Shopping, por 3,5 € | 317 |
| Deshumidificador, 15 %* | 180,00 | 1,0 | 27,00 | 34,0 | 47,0 | NO | 227 |
| EPI guantes nitrilo (caja), 30 %* | 15,00 | 1,4 | 4,50 | 24,3 | 33,6 | NO | 81 |
| Bornas/fusibles/relés B2C, 30 %* | 35,00 | 1,4 | 10,50 | 24,3 | 33,6 | NO | 81 |
| Bornas/fusibles/relés, pedido B2B 150 €*, 30 %* | 150,00 | 1,4 | 45,00 | 24,3 | 33,6 | SÍ | 81 |
| Multímetro/instrumentación barata, 20 %* | 60,00 | 1,4 | 12,00 | 24,3 | 33,6 | NO | 121 |
| Print-on-demand camiseta Printful, ~50 % | 29,99 | 1,1 | 14,99 | 30,9 | 42,7 | NO | 62 |
| Belleza/cuidado de la piel (referencia externa), 40 %* | 35,00 | 2,9 | 14,00 | 11,7 | 16,2 | SÍ (Shopping), NO (Search) | 29 |

Escenarios con CPC Shopping 0,34 € (pedidos/mes y margen neto tras anuncios y fijos de 116 €/mes):

| Nicho | 300 €/mes | 1.000 €/mes | 2.000 €/mes |
|---|---|---|---|
| Suplementos menopausia 26 % | 21 ped / −295 € | 71 ped / −712 € | 141 ped / −1.308 € |
| Suplementos menopausia 45 %* | 21 ped / −206 € | 71 ped / −417 € | 141 ped / −718 € |
| Aire acondicionado portátil 15 %* | 9 ped / +48 € | 29 ped / +428 € | 59 ped / +973 € |
| Aire acond. portátil 15 % menos envío 15 €* | 9 ped / −85 € | 29 ped / −13 € | 59 ped / +90 € |
| Deshumidificador 15 %* | 9 ped / −177 € | 29 ped / −322 € | 59 ped / −527 € |
| EPI guantes nitrilo 30 %* | 12 ped / −360 € | 41 ped / −930 € | 82 ped / −1.745 € |
| Bornas/fusibles B2C 30 %* | 12 ped / −286 € | 41 ped / −683 € | 82 ped / −1.251 € |
| Bornas/fusibles B2B 150 €* | 12 ped / +140 € | 41 ped / +737 € | 82 ped / +1.590 € |
| Multímetro 20 %* | 12 ped / −267 € | 41 ped / −622 € | 82 ped / −1.127 € |
| POD camiseta Printful ~50 % (fijos 27 €) | 10 ped / −181 € | 32 ped / −542 € | 65 ped / −1.056 € |
| Belleza (referencia) 40 %* | 26 ped / −57 € | 85 ped / +78 € | 171 ped / +273 € |

Escenarios con CPC Search 0,47 €:

| Nicho | 300 €/mes | 1.000 €/mes | 2.000 €/mes |
|---|---|---|---|
| Suplementos menopausia 26 % | 15 ped / −328 € | 51 ped / −824 € | 102 ped / −1.532 € |
| Aire acondicionado portátil 15 %* | 6 ped / −81 € | 21 ped / +1 € | 43 ped / +118 € |
| Aire acond. portátil menos envío 15 €* | 6 ped / −176 € | 21 ped / −318 € | 43 ped / −520 € |
| Bornas/fusibles B2B 150 €* | 9 ped / −14 € | 30 ped / +225 € | 60 ped / +565 € |
| Belleza (referencia) 40 %* | 19 ped / −157 € | 62 ped / −252 € | 123 ped / −388 € |
| Resto (EPI, B2C eléctrico, multímetro, POD, deshumidificador) | negativos de −243 a −375 € | negativos de −541 a −982 € | negativos de −967 a −1.848 € |

Lectura adversarial:
- Con ticket <60 € ningún nicho cubre el CAC con el margen bruto del primer pedido, ni con la mediana europea de CPC (que es la de anunciantes consolidados; una tienda nueva sin historial paga por encima de la mediana).
- Los únicos casos positivos exigen ticket alto (aire acondicionado ~350 €, pedidos B2B ≥110-120 €) y dependen de supuestos de margen (15 %, 30 %) y de envío que BigBuy no permitió verificar. En aire acondicionado portátil el margen neto a 1.000 €/mes oscila entre −13 € y +428 € según el coste de envío de un bulto de 25-30 kg: es un negocio de céntimos de sensibilidad, estacional y con >20.000 resultados en Amazon.es, muchos de vendedores chinos a 180-500 €.
- Suplementos de menopausia solo cuadra con recompra: el margen por pedido (5,7-9,9 €) es inferior al CAC (14-20 €); haría falta LTV ≥2-3 pedidos por cliente, dato que no se ha verificado. Amazon.es ya tiene 97 resultados con marcas farmacéuticas (Ymea, Cumlaude, Ana María Lajusticia) con 600-1.500 reseñas.
- POD: margen del 50 % pero conversión de moda 1,1 % → CAC 31-43 € frente a 15 € de margen. Solo funciona con tráfico orgánico/social gratuito, no con anuncios.

Caso Amazon FBA (suplemento menopausia, PVP 19,99 €): referencia 15 % (categoría salud, "la mayoría entre 8 y 15 %") = 3,00 €; publicidad con ACoS 28,8 % (ECDB España, [FRAGMENTO]) = 5,76 €; tarifa FBA local: sin dato; coste de producto marca blanca: sin dato. Antes de FBA y producto ya se van 8,76 € (44 %) del PVP. Jungle Scout 2024: 22 % de vendedores aún no rentables al año; 57 % declaran margen >10 %.

---

## 5) Supervivencia y éxito de tiendas nuevas

| Dato | Fuente / fecha | Estado |
|---|---|---|
| 34 % de las tiendas Shopify sobreviven un año (36 % cohorte 2019, 34 % 2020, 32 % 2021); Shopify Plus 62 %. Shopify nunca ha publicado tasas de supervivencia | The Globe and Mail, análisis de datos Store Leads 2019-2022 (artículo 2022) | [ABIERTA] https://www.theglobeandmail.com/business/article-shopify-customer-retention-problem/ |
| 3.163.099 tiendas Shopify activas; +1,7 % trimestral y +15 % interanual en T3 2026 | Store Leads, actualizado 16-10-2026 | [ABIERTA] https://storeleads.app/reports/shopify |
| Mediana de ingresos de tiendas Shopify | — | sin dato público; NO ENCONTRADO |
| "90 % fracasan el primer año" | Blogs sin fuente primaria (Tevello, Shipaid, nas.com) | [FRAGMENTO] vía búsqueda; descartado por falta de fuente |
| Amazon: 58 % de negocios rentables en el primer año, 22 % aún no rentables; 57 % con margen >10 %; 15 % con margen 21-25 % (encuesta 2024) | Jungle Scout State of the Amazon Seller 2024, citado por RevenueGeeks | [FRAGMENTO] https://revenuegeeks.com/research/amazon-seller-statistics |
| Amazon: 64 % de vendedores FBA rentables en 12 meses; margen neto medio FBA 15-20 % | SmartScout (blog, sin fuente primaria clara) | [ABIERTA, fiabilidad baja] https://smartscout.com/blog/amazon-seller-statistics |
| Jungle Scout 2025: encuesta a ~1.500 vendedores (ene-2025); ~40 % de marcas enterprise preocupadas por rentabilidad; 32 % por costes publicitarios; cifra de % rentables no visible sin formulario | Jungle Scout | [ABIERTA] https://www.junglescout.com/resources/reports/amazon-seller-report-2025/ |
| 17.000 pymes españolas en Amazon exportaron >1.200 M€ en 2024 (+20 %); 75 % vende fuera de España | Amazon nota de prensa 10-2025 (agregado, sin mediana por vendedor) | [ABIERTA] https://press.aboutamazon.com/es/noticias/impacto-economico/2025/10/pymes-espanolas-venden-amazon-1-200-millones-euros-exportaciones-2024 |

---

## 6) Riesgos y lo no verificado

1. **Demanda no medida**: Google Trends bloqueó (HTTP 429) los 3 intentos; el "+64 % de interés en climatización" y las "1.300 búsquedas/mes de suplementos menopausia" proceden del encargo y no se han contrastado. Sin volumen propio, la columna de pedidos/mes solo depende del presupuesto, no de si hay búsquedas suficientes.
2. **CPC España**: no existe dato público por categoría; se usa la mediana europea de ecommerce (smec) como suelo. Una tienda nueva, sin historial ni feed optimizado, debe esperar CPC superiores a la mediana. Si el CPC real dobla la mediana, incluso el aire acondicionado portátil pasa a negativo en los tres escenarios.
3. **BigBuy**: tarifas oficiales no accesibles (403/401). Cuotas y márgenes vienen de dos reseñas de terceros (Copyfy, Trendtrack) que además son competidores/afiliados. Coste de envío de voluminosos (aire acondicionado) sin dato: es la variable que decide el nicho.
4. **Márgenes supuestos** (15 % electro, 30 % material eléctrico, 45 % marca blanca de suplementos): no verificados con catálogo real; marcados con asterisco.
5. **Devoluciones y garantía** no incluidas: en electro y clima la tasa de devolución y el coste de recogida de 25-30 kg pueden anular el margen; en suplementos hay regulación sanitaria (etiquetado, notificación AESAN) que no se ha analizado.
6. **Amazon FBA**: tarifa de gestión logística local España no extraída; PPC España solo con dato ~2023 (0,37 USD mediana) y ACoS 28,8 %. Los casos de vendedores españoles con ingresos públicos: NO ENCONTRADOS; Amazon publica agregados.
7. **Supervivencia**: el único dato duro (34 % a un año) es de 2022 y mide dominios activos, no rentabilidad.
8. **Competencia en Amazon**: en los nichos medidos, los 3 primeros resultados tienen 600-9.500 reseñas y "200-4.000+ compras/mes"; la propia Amazon Basics domina EPI (4,95 €/100 guantes). Para bornas, fusibles, multímetro y deshumidificador no se pudo medir (503).
9. **Sesgo de fuentes**: Littledata y Shopify publican datos de tiendas vivas (sesgo de supervivencia); WordStream mezcla leads y ventas; Copyfy y Trendtrack venden herramientas de dropshipping.

Conclusión para Jorge: con compra 100 % autoservicio y tráfico de pago, el modelo solo tiene margen cuando el ticket supera ~110-230 € (según sector) o cuando la conversión supera el 2,5 % con margen ≥40 %. Los candidatos de la fila (suplementos, EPI, consumibles eléctricos B2C, instrumentación barata, POD) no lo cumplen con pedido único. Las dos vías que no quedan refutadas son (a) climatización portátil con proveedor UE que incluya envío de voluminosos a coste conocido y (b) venta B2B de material eléctrico con pedido mínimo ≥120 € y recompra, ambas pendientes de verificar demanda y envío.

---

## 7) URLs abiertas y estado (23-10-2026)

| # | URL | Método | Estado | Uso |
|---|---|---|---|---|
| 1 | https://www.flat101.es/estudio-conversion-negocios-digitales-2025/ | pwfetch | 404 | H1 (no existe) |
| 2 | https://www.shopify.com/blog/ecommerce-conversion-rate | pwfetch | 200 [ABIERTA] | H1 conversión por sector |
| 3 | https://www.littledata.io/average/ecommerce-conversion-rate-(all-devices) | pwfetch | 200 [ABIERTA] | H1 mediana 1,4 % |
| 4 | https://www.wordstream.com/blog/2025-google-ads-benchmarks | pwfetch | 200 [ABIERTA] | H2 CPC/CVR 2025 |
| 5 | https://www.wordstream.com/blog/ws/2023/04/26/google-shopping-benchmarks | pwfetch | 404 | H2 |
| 6 | https://www.bigbuy.eu/es/tarifas | pwfetch / --browser | 403 / 403 | H3 (bloqueo Cloudflare) |
| 7 | https://www.printful.com/pricing | pwfetch | 200 [ABIERTA] | H3 planes Printful |
| 8 | https://sell.amazon.es/precios | pwfetch / --browser / jina | 200 [ABIERTA] | H7 comisiones |
| 9 | https://r.jina.ai/https://www.bigbuy.eu/es/tarifas | jina | 401 / 200 (solo menú) | H3 |
| 10 | https://r.jina.ai/https://www.bigbuy.eu/es/dropshipping | jina | 200 [ABIERTA] | H3 enlaces |
| 11 | https://www.littledata.io/average/average-order-value | pwfetch | 200 [ABIERTA] | H1 AOV 111 USD |
| 12 | https://www.gelato.com/pricing | pwfetch / --browser / jina | 403 / 403 / 200 (sin precios) | H3 |
| 13 | https://www.wordstream.com/blog/2026-google-ads-benchmarks | pwfetch | 200 [ABIERTA] | H2 CPC 2026 |
| 14 | https://sell.amazon.es/precios/tarifas-por-referencia | pwfetch | 404 | H7 |
| 15 | https://sell.amazon.es/precios/tarifas-de-gestion-logistica | pwfetch | 404 | H7 |
| 16 | https://trends.google.com/trends/explore?geo=ES&q=aire%20acondicionado%20portatil (2 variantes) | --browser | 429 ×2 | H6 |
| 17 | https://trends.google.com/trends/explore?geo=ES&q=suplementos%20menopausia | --browser | 429 | H6 |
| 18 | https://www.theglobeandmail.com/business/article-shopify-customer-retention-problem/ | pwfetch | 200 [ABIERTA] | H5 |
| 19 | https://www.junglescout.com/resources/reports/amazon-seller-report-2025/ | pwfetch | 200 [ABIERTA] (gated) | H7 |
| 20 | https://ecommercedb.com/insights/amazon-ad-types-in-spain-an-analysis-of-performance-metrics/4516 | pwfetch | 200 (portada sin datos) | H7 [FRAGMENTO vía búsqueda] |
| 21 | https://www.trendtrack.io/es/blog-post/resena-de-bigbuy-es-una-opcion-confiable-para-tu-sitio-de-dropshipping | pwfetch | 200 [ABIERTA] | H3 |
| 22 | https://marketing4ecommerce.net/bigbuy-opiniones-y-valoracion/ | pwfetch | 200 [ABIERTA] (sin cifras) | H3 |
| 23 | https://www.flat101.es/ ; /blog/ ; /?s=estudio+conversion ; /estudio-conversion/ | pwfetch | 200/200/200/404 | H1 |
| 24 | https://www.flat101.es/blog/analitica-web/estudio-de-conversion-2023-de-flat-101-recogida-tratamiento-y-analisis-de-datos/ | pwfetch | 200 [ABIERTA] | H1 1,20 %, 196,89 € |
| 25 | https://www.flat101.es/estudio-conversion-negocios-digitales-espanoles-2022/ | pwfetch | 200 (sin cifras en página) | H1 |
| 26 | https://www.printful.com/custom/mens/t-shirts/bella-canvas-3001 | pwfetch / --browser / jina | 200 [ABIERTA con navegador] | H3 precios base |
| 27 | https://www.printful.com/shipping | pwfetch | 200 [ABIERTA] | H3 envíos Europa |
| 28 | https://iabspain.es/estudio/estudio-ecommerce-2025/ | pwfetch | 200 (sin datos) ; variante /estudio-de-ecommerce-2025/ 404 | H1 |
| 29 | https://sellermetrics.app/cost-of-amazon-ads/ | pwfetch | 200 (vacío) | H7 |
| 30 | https://canopymanagement.com/?p=22791 | pwfetch | 200 [ABIERTA] | H7 CPC Amazon 2026 |
| 31 | https://revenuegeeks.com/research/amazon-seller-statistics | pwfetch | 200 [ABIERTA] | H5/H7 Jungle Scout 2024 |
| 32 | https://www.marketplacepulse.com/shopify | pwfetch | 404 | H5 |
| 33 | https://www.shopify.com/blog/dropshipping-profit-margin (y -margins, y /es/) | pwfetch | 404 ×3 | H3 |
| 34 | https://sellercentral-europe.amazon.com/help/hub/reference/external/G200336920?locale=es-ES ; https://sellercentral.amazon.es/.../G200336920 | --browser | 200 (hub sin tabla) | H7 |
| 35 | https://sellercentral.amazon.es/help/hub/reference/external/G201003400?locale=es-ES (y -europe) | --browser | 200 (es la guía de mercancías peligrosas) | H7 |
| 36 | https://sellercentral.amazon.es/help/hub/reference/external/G201112650?locale=es-ES | --browser | 200 [ABIERTA] tabla transfronteriza | H7 |
| 37 | https://www.amazon.es/s?k=suplementos+menopausia | --browser | 200 [ABIERTA] | H6 97 resultados |
| 38 | https://www.amazon.es/s?k=aire+acondicionado+portatil | jina / --browser ×2 | 503 / 503 / 200 [ABIERTA] | H6 >20.000 resultados |
| 39 | https://www.amazon.es/s?k=guantes+trabajo+nitrilo+caja | --browser | 200 [ABIERTA] | H6 >1.000 resultados |
| 40 | https://www.amazon.es/s?k=bornas+carril+din ; multimetro+digital ; deshumidificador ; fusibles+industriales | --browser ×2 | 503 (bloqueo) | H6 sin dato |
| 41 | https://www.statista.com/statistics/1243710/spain-search-advertising-cpc | pwfetch | 200 (cifras ocultas, premium) | H2 |
| 42 | https://www.shopify.com/es/precios | pwfetch | 200 [ABIERTA] | Costes fijos |
| 43 | https://linkmybooks.com/blog/how-many-sellers-are-on-amazon | pwfetch | 200 (sin rentabilidad) | H7 |
| 44 | https://press.aboutamazon.com/es/noticias/impacto-economico/2025/10/pymes-espanolas-venden-amazon-1-200-millones-euros-exportaciones-2024 | pwfetch | 200 [ABIERTA] | H7 |
| 45 | https://www.cnmc.es/node/418044 | pwfetch | 200 [ABIERTA] | H1 ticket medio ES |
| 46 | https://marketing4ecommerce.net/decada-de-datos-del-comercio-electronico-en-espana/ | pwfetch | 200 [ABIERTA] | H1 55,96 € |
| 47 | https://smarter-ecommerce.com/en/smec-market-observer/metrics/cpc | pwfetch | 200 [ABIERTA] | H2 CPC Europa |
| 48 | https://smarter-ecommerce.com/en/smec-market-observer/reports/Q4_2025/ | pwfetch | 200 [ABIERTA] | H2 |
| 49 | https://storeleads.app/reports/shopify | pwfetch | 200 [ABIERTA] | H5 |
| 50 | https://www.searchenginejournal.com/google-shopping-ads-industry-benchmarks-wordstream/302375/ | pwfetch | 200 (texto parcial) | H2 [FRAGMENTO] |
| 51 | https://lionelz.com/blog/cuanto-cuesta-google-ads/ | pwfetch | 200 [ABIERTA] | H2 |
| 52 | https://codedesign.org/google-ads-cost-europe-your-complete-guide/ | pwfetch | 200 (sin CPC España) | H2 |
| 53 | https://pacvue.com/guides-reports/accelerate-growth-with-benchmark-data-for-amazon-in-europe/ | pwfetch | 403 | H7 |
| 54 | https://www.bigbuy.eu/blog/en/?p=27214 | pwfetch | 403 | H3 |
| 55 | https://www.copyfy.io/es/blog/opinion-bigbuy | pwfetch | 200 [ABIERTA] | H3 cuotas y desglose |
| 56 | https://www.minea.com/es/proveedor-dropshipping/mejores-proveedores-dropshipping/resenas-bigbuy | pwfetch | 200 (sin cifras) | H3 |
| 57 | https://www.sellerapp.com/blog/amazon-ppc-cost/ | pwfetch | 200 (sin CPC numérico) | H7 |
| 58 | https://r.jina.ai/https://www.bigbuy.eu/es/packs-mayoristas.html | jina | 200 (sin precios) | H3 |
| 59 | https://smartscout.com/blog/amazon-seller-statistics | pwfetch | 200 [ABIERTA] | H5/H7 |
| 60 | https://www.junglescout.com/?p=172852 | pwfetch | 200 (landing) | H7 |
| 61 | https://html.duckduckgo.com/html/?q=... (4 consultas) | curl | página anti-bot, sin resultados | búsqueda |
| 62 | WebSearch (11 consultas: Flat 101, Jungle Scout, supervivencia Shopify, CPC Amazon ES, BigBuy tarifas, CPC España, Shopping benchmarks, CNMC, Amazon pymes, flat101.es) | WebSearch | [FRAGMENTO] | localización de URLs y fragmentos citados |

Total: 78 intentos de apertura registrados (62 URL distintas), 38 páginas con contenido útil leído [ABIERTA].
