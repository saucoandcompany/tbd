# Verificación con páginas abiertas: memoria (DRAM/HBM/NAND) y cómputo GPU

Fecha de verificación: 22 de octubre de 2026. Método: apertura real de páginas (pwfetch HTTP/Chromium y curl con User-Agent para sec.gov), 46 URL distintas intentadas (41 abiertas con contenido, 5 fallidas), 7 búsquedas web solo para localizar URL. Etiquetas: [ABIERTA] = cifra leída en el texto de la página abierta; [FRAGMENTO] = solo en snippet de buscador; [NO ABRIBLE] = página no abierta o cifra no presente en el texto.

## Resumen

1. **Memoria: el bolsillo se sostiene con fuentes primarias abiertas.** Micron (8-K/EX-99.1 de 30-sep-2026): ingresos FQ4-26 de $54.230 M frente a $11.320 M un año antes (x4,8); SK hynix (29-jul-2026): ingresos 2T26 de 79,32 bn ₩ (+257% interanual) con LTAs con ~10 clientes; Samsung (8-oct-2026): guía 3T26 de beneficio operativo ~107,4 bn ₩ frente a 12,17 bn ₩ en 3T25 (x8,8) y "supply constraints are expected to continue" (30-jul-2026).
2. **Los precios de memoria están confirmados en página**: DDR5 16 Gb spot $58,09/die a 22-oct-2026, +480% interanual (MemoryIndex); TrendForce: contrato DRAM convencional +90-95% intertrimestral en 1T26 (2-feb-2026), +10-15% en 4T26 y NAND +15-20% (30-sep-2026), HBM ASP mezclado +121% en 2027 (29-sep-2026). Lo único que no se vio en su fuente primaria: la asignación total de 2027 (sigue siendo DigiTimes "según insiders") y el SSD de 30 TB a $22.600 (tabla de VDURA reproducida por un revendedor; MemoryIndex cotiza un eSSD 30 TB QLC a $4.627, discrepancia a vigilar).
3. **GPU: crecimiento y backlog confirmados en documentos regulatorios**: NVIDIA 10-Q (trimestre a 26-jul-2026): ingresos $96.200 M (+106%), Data Center $89.000 M (+117%), "currently experiencing certain supply constraints"; CoreWeave 8-K (11-ago-2026): ingresos 2T26 $2.575 M (vs $1.212 M) y backlog ≈$104.000 M a 30-jun-2026 más >$25.000 M añadidos a inicios del 3T; Nebius PDF (12-ago-2026): $582,3 M, +454%.
4. **La cifra de precio GPU del informe original ($1,85→$2,40/h) no está en el texto de la página de Apollo** (solo la frase "on-demand GPU capacity is effectively sold out", 15-jun-2026). Sustituida por índices leídos: Silicon Data SDH100RT $2,86/GPU-h a 21-oct-2026 (+10% en 7 días); MemoryIndex mediana anunciada H100 $3,52 a 14-oct-2026 (+17,8% interanual); Ornn OCPI-B200 $9,40 a 21-oct-2026 (+21,9% en 30 días; $7,46 el 9-oct como decía el informe). Lambda cobra $3,99/GPU-h por H100 SXM on-demand y $6,69 por B200 (22-oct-2026). "Nebius sold out tres trimestres" no aparece en su nota de resultados: sigue siendo de terceros.
5. **Re-puntuación solo con [ABIERTA]**: memoria mantiene **11** (3-3-3-2); cómputo GPU baja a **10** (3-2-3-2) porque el alza de precio de alquiler es de dos dígitos (+17,8% interanual H100), no un múltiplo, y el hardware usado cae (-22,1%). Aceptando fragmentos, GPU volvería a 11.

## Tabla de verificación

### A. Memoria DRAM / HBM / NAND

| Afirmación del informe | Cifra original | Cifra leída | Fecha de la página | URL | Etiqueta | Veredicto |
|---|---|---|---|---|---|---|
| Spot DDR5 16 Gb, +480% interanual | $56,88/die a 15-oct-2026, +480% | $58,09/die, +5,69% en 30 días, +480,00% interanual; cesta de 13 contratos +487,69% interanual | 2026-10-22 00:00 Z | https://memoryindex.io/dram-prices | [ABIERTA] | CONFIRMADO (actualizado a $58,09) |
| Samsung, SK hynix y Micron han asignado toda la capacidad DRAM/HBM de 2027 (DigiTimes) | "toda la capacidad 2027 vendida" | TweakTown reproduce a DigiTimes "citing industry insiders": capacidad DRAM y HBM 2027 "reportedly" asignada; NAND podría quedar reservada a fin de agosto | 4-ago-2026 | https://www.tweaktown.com/news/113004/... | [ABIERTA] (fuente secundaria) | CONFIRMADO como informe de terceros; sin confirmación primaria. Soporte primario parcial: SK hynix "customer demand exceeds supply capabilities", LTAs con ~10 clientes (29-jul-2026); Micron: la mayor parte del HBM 2027 contratado (vía Seoul Economic Daily) |
| SSD empresarial 30 TB de $3.460 a $22.600 en un año | $3.460 → $22.600 | Tabla VDURA (18-ago-2026) reproducida: 3T25 $3.460 → 4T25 $7.765 → 1T26 $17.500 → 2T26 $18.900 → 3T26 $22.600 (TLC); QLC $18.080; "≈6,5x interanual" | Artículo 2026 (tabla del 18-ago-2026) | https://pcserverandparts.com/news/enterprise-ssd-prices-2026-server-storage-buying-guide/ | [ABIERTA] (revendedor citando a VDURA) | CONFIRMADO en página; contraste: MemoryIndex eSSD-30T QLC $4.627 a 22-oct-2026, otra metodología (nivel contrato/die) |
| Micron: contratos para la mayor parte del HBM 2027; precios "mucho más altos" | — | "completed contracts with customers for the bulk of its 2027 HBM bit supply"; CEO: precios 2027 "far higher" | 1-oct-2026 17:56 KST | https://en.sedaily.com/finance/2026/10/01/hbm-prices-to-more-than-double-next-year-as-shortage | [ABIERTA] | CONFIRMADO (vía prensa; el EX-99.1 de Micron no menciona HBM, fue en la llamada) |
| TrendForce: ASP de HBM +121% en 2027 | +121% | "Blended ASP is now projected to jump 121% YoY" (2027), HBM4e en 2S27 | 29-sep-2026 | https://www.trendforce.com/presscenter/news/20260929-13255.html | [ABIERTA] | CONFIRMADO |
| HBM4 12-high 36 GB ≈ $1.300 (el doble) | ≈$1.300 | "expected to more than double to around $1,300 next year from about $600" (estimación de la industria) | 1-oct-2026 | Seoul Economic Daily (misma URL) | [ABIERTA] | CONFIRMADO como estimación |
| Samsung: tensión de oferta hasta 2028, peor en 2027 (atribuido a IG) | "hasta 2028" | Nota oficial Samsung 2T26: "Despite efforts to increase production, supply constraints are expected to continue" (sin año). TechRadar: Samsung "tells analysts global memory supply shortage will persist through 2028 and grow more severe in 2027 than in 2026". La página de IG (8-jul-2026) NO contiene esa afirmación | Samsung 30-jul-2026; TechRadar 3-ago-2026; IG 8-jul-2026 | https://news.samsung.com/global/samsung-electronics-announces-second-quarter-2026-results ; https://www.techradar.com/computing/memory/samsung-warns-ram-pocalypse-could-last-until-2028-as-its-profits-continue-to-rise ; https://www.ig.com/en/news-and-trade-ideas/memory-chip-stocks-rally-2026-260708 | [ABIERTA] | CORREGIDO en la atribución: la cifra es de la llamada de resultados vía TechRadar, no de IG; el texto oficial solo dice "constraints expected to continue" |
| DRAM contrato +90-95% intertrimestral en 1T26; PC DRAM +105-110% | +90-95%; +105-110% | "conventional DRAM contract prices raised to +90–95% QoQ; NAND Flash to +55–60%"; PC DRAM "expected to at least double QoQ" | 2-feb-2026 | https://www.trendforce.com/presscenter/news/20260202-12911.html | [ABIERTA] | CONFIRMADO (+90-95%); PC DRAM leído como "al menos duplicar", no "105-110%" |
| Kioxia: capacidad 2026 vendida, tensión hasta 2027 | sold out 2026 | Titular y fecha: "NAND supply is sold out for this year and likely through 2027" | 21-ene-2026 | https://www.tomshardware.com/pc-components/ssds/kioxia-exec-says-... | [ABIERTA] (titular; cuerpo truncado) | CONFIRMADO |
| TrendForce: contratos SSD empresarial +23-28% en 4T26 | +23-28% | Nota 30-sep-2026: NAND +15-20% intertrimestral; "Enterprise SSDs are the only category expected to see price growth accelerate"; nota 21-sep-2026: pedidos 4T26 podrían superar 3T26. La cifra 23-28% solo apareció en snippet del informe de pago "4Q26 Memory Price Forecast" | 30-sep-2026 y 21-sep-2026 | https://www.trendforce.com/presscenter/news/20260930-13258.html ; https://www.trendforce.com/presscenter/news/20260921-13246.html | [ABIERTA] la dirección; [FRAGMENTO] el 23-28% | CONFIRMADO parcialmente (aceleración sí; el rango exacto no leído) |
| SanDisk ASP ≈ $0,31/GB (+340%) | +340% | No abierto (fuera de presupuesto) | — | PCSP / Nexus Compute | [NO ABRIBLE] | NO VERIFICADO |
| ISM sep-2026: Supplier Deliveries 59,0; Prices 77,9; DRAM y memoria en escasez | 59,0 / 77,9 | No abierto | — | ismworld.org | [NO ABRIBLE] | NO VERIFICADO |
| Precio de exportación coreano de DRAM $64.000/kg (post en X) | $64.000/kg | No abierto (X) | — | x.com | [NO ABRIBLE] | NO VERIFICADO |
| Pico de precios en FY2028 / expansiones llegan en 2028 | "pico FY2028" | IG: "None of this new capacity reaches volume production before 2027 ... several large expansions land in the market at roughly the same time in 2028 and beyond"; BofA extiende el superciclo a fin de 2027 con escenario hasta 2030 | 8-jul-2026 | IG (misma URL) | [ABIERTA] | CONFIRMADO como opinión de analistas |

### B. Cómputo GPU en alquiler / inferencia

| Afirmación del informe | Cifra original | Cifra leída | Fecha de la página | URL | Etiqueta | Veredicto |
|---|---|---|---|---|---|---|
| Apollo: capacidad on-demand "efectivamente agotada"; H100 de $1,85/h a ~$2,40/h | $1,85 → $2,40 | Texto: "On-demand GPU capacity is effectively sold out, and even older-generation chips are seeing rental rates increase to levels not seen since 2024". Las cifras $1,85/$2,40 NO aparecen en el texto ni en el HTML (236 KB); probablemente en un gráfico | 15-jun-2026 | https://www.apollo.com/wealth/insights-news/insights/2026/06/growing-compute-shortage | [ABIERTA] la frase; [NO ABRIBLE] la cifra | CORREGIDO: sustituir por índices leídos — Silicon Data SDH100RT $2,86/GPU-h (21-oct-2026, +10,0% en 7 días; FAQ de la misma página: $2,53); MemoryIndex mediana anunciada H100 $3,52 (14-oct-2026, +17,8% interanual; suelo 2024-25 ≈ $2,99) |
| Nebius 2T26 $582 M (+454%) | $582 M, +454% | Tabla: Revenues 105,1 → 582,3 M$ (+454%); 1S26 981,3 M$ (+529%); EBITDA ajustado 236,2 M$ | 12-ago-2026 | https://assets.nebius.com/assets/72a8c258-bbb7-4df7-ab9d-8698f6cb88fc/PR.pdf (vía https://nebius.com/newsroom/nebius-reports-second-quarter-2026-financial-results) | [ABIERTA] | CONFIRMADO |
| Nebius "sold out" en 3T25, 4T25 y 1T26 | 3 trimestres | No aparece en la nota de resultados (PDF); solo en blogs de terceros (Safeguard, AMCompute) | — | — | [FRAGMENTO] | NO VERIFICADO en fuente primaria |
| CoreWeave 2T26 ingresos $2.575 M; backlog ≈ $104.000 M a 30-jun-2026 | $2.575 M; ≈$104.000 M | EX-99.1: Revenue $2.575 M vs $1.212 M (2T25); 1S26 $4.653 M vs $2.194 M; "Revenue backlog was approximately $104 billion as of June 30, 2026", "does not include more than $25 billion of net new customer commitments added in early Q3"; pérdida neta -24% de margen, intereses netos $640 M | 11-ago-2026 | https://www.sec.gov/Archives/edgar/data/1769628/000176962826000362/coreweave2q26earningspress.htm | [ABIERTA] | CONFIRMADO |
| >98% de ingresos 2025 de CoreWeave en contratos take-or-pay | >98% | Safeguard (19-oct-2026) citando el 10-K: "over 98%"; cliente principal (Microsoft) ≈67% | 19-oct-2026 | https://safeguard.sh/resources/blog/gpu-as-a-service-economics-coreweave-nebius-backlog-debt-margins | [ABIERTA] (secundaria) | CONFIRMADO vía secundaria; 10-K no abierto |
| Índice B200 $7,46/GPU-h (9-oct-2026) | $7,46 | Ornn OCPI-B200: 9-oct $7,46; 21-oct $9,40 (+6,5% día, +19,3% 7 días, +21,9% 30 días); septiembre +33,3%; rango desde 22-jul $5,68–$9,40 | 21-oct-2026 | https://data.ornn.com/markets/b200 ; https://www.amcompute.com/blog/state-of-the-neoclouds-2026 | [ABIERTA] | CONFIRMADO y actualizado a $9,40 (Silicon Data SDB200RT marca $6,14, metodología distinta) |
| Índice de GPU usadas 75 (-22,1% interanual, ago-2026) | 75; -22,1% | "was 75 in August: down 12.3% on the month and 22.1% on the year" (índice propio de American Compute, 1S25 = 100) | oct-2026 (datos a ago-2026) | https://www.amcompute.com/blog/state-of-the-neoclouds-2026 | [ABIERTA] | CONFIRMADO |
| H100 usadas de $40-50K a $18-22K | $18-22K | MemoryIndex: módulo H100 SXM5 $25.000 (-16,7%), H200 $27.500 (-8,3%), B200 $34.000 (+9,7%), todo "estimate 2026-07" | 14-oct-2026 | https://memoryindex.io/gpu-prices | [ABIERTA] (estimaciones) | CONFIRMADO en dirección (caída); nivel leído $25.000, no $18-22K |
| NVIDIA 10-Q: Blackwell mayoría de envíos, Vera Rubin en producción, "certain supply constraints" | — | "Vera Rubin, began production shipments in the third quarter of fiscal year 2027 ... currently experiencing certain supply constraints"; Revenue $96.200 M (+106% interanual, +18% secuencial); Data Center $89.000 M (+117%); cargo de $400 M por exceso de inventario H200 | Trimestre a 26-jul-2026 | https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000075/nvda-20260726.htm (curl con UA) | [ABIERTA] | CONFIRMADO |
| Lead times 36-52 semanas (Spheron / GPU Seeker) | 36-52 sem. | No abierto | — | spheron.network | [NO ABRIBLE] | NO VERIFICADO |
| AWS subió precios de Capacity Blocks (ene-2026) | — | No abierto | — | vexxhost.com | [NO ABRIBLE] | NO VERIFICADO |
| TrendForce: GPUs 30-40 semanas, "parte menos restringida" (vía X) | 30-40 sem. | No abierto (X) | — | x.com | [NO ABRIBLE] | NO VERIFICADO |

## Nuevas cifras leídas

**Memoria (fuentes primarias)**
- Micron, EX-99.1 del 8-K (30-sep-2026): ingresos FQ4-26 $54.230 M (FQ3-26 $41.460 M; FQ4-25 $11.320 M → +379% interanual); FY26 $133.190 M vs $37.380 M (+256%); beneficio neto GAAP FY26 $84.970 M; Cloud Memory BU $16.283 M con margen bruto 83%; guía FQ1-27 $61.500 M ± $1.500 M, margen bruto ≈86%. "We expect an even stronger fiscal 2027." https://www.sec.gov/Archives/edgar/data/723125/000072312526000018/a2026q4ex991-pressrelease.htm
- SK hynix (29-jul-2026): ingresos 2T26 79,3187 bn ₩, beneficio operativo 60,5426 bn ₩ (margen 76%), +257% y +557% interanual; LTAs con ~10 clientes; HBM4 en envíos masivos; "customer demand exceeds supply capabilities"; sala limpia Yongin Fase 1 a inicios de 2027. Resultados 3T26 convocados el 21-oct-2026 (aún no publicados). https://news.skhynix.com/en/q2-2026-business-results/
- Samsung, guía 3T26 (8-oct-2026): ventas ≈195 bn ₩, beneficio operativo ≈107,4 bn ₩ (2T26: 89,49; 3T25: 12,17 → x8,8). 2T26 (30-jul-2026): División DS +56% intertrimestral, Memoria con récord histórico, "supply constraints are expected to continue". https://news.samsung.com/global/samsung-electronics-announces-earnings-guidance-for-third-quarter-2026
- TrendForce (30-sep-2026): DRAM convencional contrato +10-15% intertrimestral en 4T26; NAND +15-20%; "Server DRAM is therefore expected to remain undersupplied in 4Q26"; ritmo de subida moderándose; LTAs con mecanismos de precio que frenan a algunos proveedores. https://www.trendforce.com/presscenter/news/20260930-13258.html
- TrendForce noticia (20-oct-2026): Commercial Times ve DRAM +≈20% intertrimestral en 4T26 pese a ganancias más lentas. https://www.trendforce.com/news/2026/10/20/...
- TrendForce (25-ago-2026): DRAM+NAND = 68% del capex de los grandes CSP en 2027 (47% en 2026); capex CSP +98% en 2026 y +50% en 2027. https://www.trendforce.com/presscenter/news/20260825-13198.html
- TrendForce (14-oct-2026, portada del Press Center): capex de los 9 grandes CSP $957.000 M en 2026 (+106%) y >$1,5 bn en 2027 (+60%); ingresos de servidores IA +90% en 2027.
- MemoryIndex (22-oct-2026): HBM3E-36G $2.100; HBM4-48G $3.506; DDR4-8G $46,97; RDIMM-64G $1.943; eSSD-30T QLC $4.627; kit retail DDR5 32 GB $459,55.

**GPU**
- Lambda, página de precios (22-oct-2026): on-demand 8x B200 SXM6 $6,69/GPU-h; 8x H100 SXM $3,99; 1x H100 SXM $4,29; A100 80 GB $2,79; clústeres 1-Click B200 $8,87–9,86/GPU-h, H100 $5,54–6,16 (2 semanas–1 año). https://lambda.ai/pricing
- RunPod (22-oct-2026): H100 SXM $3,99/h; H100 PCIe $2,89; H200 $5,29; B200 ~$8,64 (serverless). https://www.runpod.io/pricing
- CoreWeave (22-oct-2026): HGX H100 8x $49,24/h on-demand ($6,16/GPU), spot $19,51–19,71; HGX H200 $50,44; HGX B200 $68,80 (spot $34,87); GB200 NVL72 $42,00 por instancia de 4 GPU. https://www.coreweave.com/pricing
- Silicon Data (21-oct-2026): SDH100RT neo-cloud $2,86/GPU-h (+10,0% 7 días); H200 $3,47; A100 $1,55; B200 $6,14 (+6,6%); B300 $7,02; MI300X $2,75. https://www.silicondata.com/products/silicon-index/h100
- Ornn OCPI-B200 (21-oct-2026): $9,40, mediana 30 días $7,92, mes de septiembre +33,3%, agosto -5,3%. https://data.ornn.com/markets/b200
- MemoryIndex GPU (14-oct-2026): mediana anunciada H100 $3,52/GPU-h en 41 proveedores, +17,8% interanual; "the 2026 re-tightening is the story". https://memoryindex.io/gpu-prices
- NVIDIA 10-Q: RPO de contratos >1 año $3.200 M; cargo H200 $400 M por "demand for H200 products diminished" (contraseñal de hardware anterior).
- Nebius newsroom (21-oct-2026): "Nebius brings compute pricing into the open"; colocación de convertibles por ≈$5.750 M (24-ago-2026). Vast.ai: precios fijados por oferta/demanda en 40+ centros, sin cifras en la página estática.

## Re-puntuación (escala 0-3; solo evidencia [ABIERTA])

### A. Memoria DRAM/HBM/NAND
| Criterio | Puntos | Justificación aritmética |
|---|---|---|
| Crecimiento | 3 | Micron FQ4-26 $54,23 bn vs $11,32 bn (+379%); SK hynix 2T26 +257%; Samsung beneficio operativo 3T26e 107,4 bn ₩ vs 12,17 bn ₩ (x8,8). |
| Dinero/precio | 3 | DDR5 16 Gb spot +480% interanual (22-oct-2026); contrato DRAM +90-95% en 1T26 y aún +10-15% en 4T26; HBM ASP +121% previsto para 2027. |
| Espera/backlog | 3 | Samsung "supply constraints expected to continue"; SK hynix "demand exceeds supply capabilities" con LTAs a ~10 clientes; Micron con la mayor parte del HBM 2027 contratado; TrendForce: server DRAM "undersupplied" en 4T26. La asignación total de 2027 sigue siendo informe de DigiTimes, no primario. |
| Robustez del motor | 2 | Multianual pero cíclico: TrendForce ya modera el ritmo (de +90-95% a +10-15% intertrimestral), los LTAs incluyen techos de precio, y las nuevas fábricas (Yongin 2027, expansiones 2028) coinciden en 2028; Samsung sitúa el alivio en 2028 (vía TechRadar). |
| **Total** | **11** | Igual que el informe original; ahora con base [ABIERTA]. Aceptando [FRAGMENTO] (SanDisk +340%, ISM, 23-28% eSSD) seguiría en 11. |

### B. Cómputo GPU en alquiler / inferencia
| Criterio | Puntos | Justificación aritmética |
|---|---|---|
| Crecimiento | 3 | NVIDIA Data Center $89,0 bn (+117% interanual); CoreWeave 2T26 $2.575 M vs $1.212 M (+112%); Nebius +454%. |
| Dinero/precio | 2 | Subidas de dos dígitos, no múltiplos: H100 mediana $3,52 (+17,8% interanual), SDH100RT $2,86 (+10% en 7 días); B200 $9,40 (+21,9% en 30 días). El H100 sigue muy por debajo de 2023 y el hardware usado cae (índice 75, -22,1%; módulo H100 $25.000, -16,7%). La cifra $1,85→$2,40 del informe no se pudo leer. |
| Espera/backlog | 3 | Backlog CoreWeave ≈$104 bn = ≈10x el ritmo anualizado de ingresos ($2.575 M x 4 = $10,3 bn) más >$25 bn añadidos en 3T; NVIDIA "experiencing certain supply constraints"; Apollo: on-demand "effectively sold out". |
| Robustez del motor | 2 | Depende del capex de CSP (TrendForce: $957 bn 2026 → >$1,5 bn 2027, cifras de previsión) y de megavatios, no de chips; contraseñales leídas: cargo NVIDIA de $400 M por exceso de H200, hardware usado -22%, CoreWeave con margen operativo -2% e intereses $640 M/trimestre. |
| **Total** | **10** | Baja de 11 a 10 por el criterio de precio. Si se aceptara el [FRAGMENTO] de Apollo ($1,85→$2,40 = +30%) junto con "Nebius sold out 3 trimestres" y la subida de AWS, Dinero/precio volvería a 3 y el total a **11**. |

## Lo que no se pudo abrir

- `https://www.sec.gov/...nvda-20260726.htm` con pwfetch: 403 (sec.gov exige User-Agent identificable); resuelto con curl + UA, igual que los 8-K de Micron y CoreWeave.
- `https://investors.micron.com/news-releases`: 404 (la ruta cambió); se usó el EX-99.1 en EDGAR.
- `https://news.skhynix.com/sk-hynix-reports-second-quarter-2026-financial-results/` y `/sk-hynix-announces-2q26-financial-results/`: 404 (URL adivinadas); la real es `/en/q2-2026-business-results/`.
- `https://www.trendforce.com/presscenter/news/2` y `/semiconductors`: 404 (paginación no es por ruta).
- `https://investors.coreweave.com/news/`: cuerpo vacío por JavaScript ("Loading...", plataforma Q4 Inc) en HTTP y 403 en Chromium; sustituido por el 8-K en EDGAR.
- Apollo: página abierta (200) pero las cifras $1,85/$2,40 no están en el texto ni en el HTML (236 KB); se asume gráfico/imagen.
- Tom's Hardware e IG: pwfetch trunca a 20.000 caracteres (menús); el HTML completo vía curl (2,0 MB y 0,7 MB) confirma titulares y fechas, pero el cuerpo de IG no contiene "2028" asociado a Samsung.
- No abiertos por presupuesto: ISM, Spheron, Vexxhost, Nexus Compute, Luminix, posts de X, 10-K de CoreWeave, informe de pago "4Q26 Memory Price Forecast" de TrendForce.

## Registro de aperturas (46 URL distintas; 41 con contenido, 5 fallidas)

| # | URL | Herramienta | Estado |
|---|---|---|---|
| 1 | https://www.trendforce.com/presscenter/news | pwfetch | 200, índice (14-oct capex CSP; 19-oct fibra; 22-oct CPU) |
| 2 | https://investors.micron.com/news-releases | pwfetch | 404 |
| 3 | https://news.skhynix.com/ | pwfetch | 200, índice (convocatoria 3T26 el 21-oct) |
| 4 | https://news.samsung.com/global/ | pwfetch | 200, índice |
| 5 | https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000075/nvda-20260726.htm | pwfetch → 403; curl+UA → 200 (1,5 MB) | Leído |
| 6 | https://memoryindex.io/dram-prices | pwfetch | 200, leído |
| 7 | https://www.tweaktown.com/news/113004/... | pwfetch | 200, leído |
| 8 | https://en.sedaily.com/finance/2026/10/01/hbm-prices-to-more-than-double-next-year-as-shortage | pwfetch | 200, leído |
| 9 | https://news.samsung.com/global/samsung-electronics-announces-earnings-guidance-for-third-quarter-2026 | pwfetch | 200, leído |
| 10 | https://news.samsung.com/global/samsung-electronics-announces-second-quarter-2026-results | pwfetch | 200, leído |
| 11 | https://news.skhynix.com/sk-hynix-reports-second-quarter-2026-financial-results/ | pwfetch | 404 |
| 12 | https://news.skhynix.com/category/ir/ | pwfetch | 200, índice |
| 13 | https://www.trendforce.com/presscenter/news/2 | pwfetch | 404 |
| 14 | https://www.trendforce.com/presscenter/news/semiconductors | pwfetch | 404 |
| 15 | https://investors.coreweave.com/news/ | pwfetch 200 (vacío JS); --browser 403 | Fallida |
| 16 | https://nebius.com/newsroom | pwfetch | 200, índice |
| 17 | https://lambda.ai/pricing | pwfetch | 200, leído |
| 18 | https://www.runpod.io/pricing | pwfetch | 200, leído |
| 19 | https://vast.ai/pricing | pwfetch | 200, sin cifras (JS) |
| 20 | https://www.coreweave.com/pricing | pwfetch | 200, leído |
| 21 | https://www.sec.gov/cgi-bin/browse-edgar?...CIK=0000723125&type=8-K (atom) | curl+UA | 200, listado |
| 22 | https://news.skhynix.com/sk-hynix-announces-2q26-financial-results/ | pwfetch | 404 |
| 23 | https://nebius.com/newsroom/nebius-reports-second-quarter-2026-financial-results | pwfetch | 200, enlaces PDF |
| 24 | https://www.apollo.com/wealth/insights-news/insights/2026/06/growing-compute-shortage | pwfetch 200; curl 200 | Leído; sin cifras $/h |
| 25 | https://safeguard.sh/resources/blog/gpu-as-a-service-economics-coreweave-nebius-backlog-debt-margins | pwfetch | 200, leído |
| 26 | https://www.amcompute.com/blog/state-of-the-neoclouds-2026 | pwfetch | 200, leído |
| 27 | https://pcserverandparts.com/news/enterprise-ssd-prices-2026-server-storage-buying-guide/ | pwfetch | 200, leído |
| 28 | https://www.tomshardware.com/pc-components/ssds/kioxia-exec-says-... | pwfetch 200; curl 200 | Titular/fecha leídos |
| 29 | https://www.ig.com/en/news-and-trade-ideas/memory-chip-stocks-rally-2026-260708 | pwfetch 200; curl 200 | Leído; sin "Samsung 2028" |
| 30 | https://memoryindex.io/gpu-prices | pwfetch | 200, leído |
| 31 | https://www.sec.gov/Archives/edgar/data/723125/000072312526000018/0000723125-26-000018-index.htm | curl+UA | 200 |
| 32 | https://www.sec.gov/Archives/edgar/data/723125/000072312526000018/a2026q4ex991-pressrelease.htm | curl+UA | 200, leído |
| 33 | https://www.sec.gov/cgi-bin/browse-edgar?...company=coreweave&type=8-K (atom) | curl+UA | 200, listado |
| 34 | https://www.sec.gov/Archives/edgar/data/1769628/000176962826000362/0001769628-26-000362-index.htm | curl+UA | 200 |
| 35 | https://www.sec.gov/Archives/edgar/data/1769628/000176962826000362/coreweave2q26earningspress.htm | curl+UA | 200, leído |
| 36 | https://assets.nebius.com/assets/72a8c258-bbb7-4df7-ab9d-8698f6cb88fc/PR.pdf | curl + pdftotext | 200, leído |
| 37 | https://www.trendforce.com/presscenter/news/20260930-13258.html | pwfetch | 200, leído |
| 38 | https://www.trendforce.com/presscenter/news/20260921-13246.html | pwfetch | 200, leído |
| 39 | https://www.trendforce.com/presscenter/news/20260202-12911.html | pwfetch | 200, leído |
| 40 | https://www.trendforce.com/presscenter/news/20260825-13198.html | pwfetch | 200, leído |
| 41 | https://www.trendforce.com/news/2026/10/20/news-dram-prices-seen-rising-20-qoq-in-4q26-... | pwfetch | 200, leído |
| 42 | https://news.skhynix.com/en/q2-2026-business-results/ | pwfetch | 200, leído |
| 43 | https://www.silicondata.com/products/silicon-index/h100 | pwfetch --browser | 200, leído |
| 44 | https://data.ornn.com/markets/b200 | pwfetch --browser | 200, leído |
| 45 | https://www.trendforce.com/presscenter/news/20260929-13255.html | pwfetch | 200, leído |
| 46 | https://www.techradar.com/computing/memory/samsung-warns-ram-pocalypse-could-last-until-2028-... | pwfetch | 200, leído |

Búsquedas web usadas (7, solo para localizar URL): TrendForce DRAM 4Q26; TrendForce NAND/eSSD 4Q26; SK hynix 2Q26; Silicon Data H100; TrendForce HBM 2027 +121%; Samsung 2T26 "2028". Los snippets de búsqueda no se han usado como evidencia salvo donde se marca [FRAGMENTO].
