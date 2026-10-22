# Precios e inventario secundario de equipos eléctricos de potencia (ES/PT/UE) — verificación adversarial

Fecha de la investigación: 22-10-2026. Método: apertura real de páginas con `tools/pwfetch.js` (HTTP y Chromium), scripts Playwright propios, `curl`+`pdftotext` para PDFs de licitación y la API pública de TED (`api.ted.europa.eu/v3/notices/search`). 165 URLs distintas intentadas, 109 abiertas con HTTP 200 (tabla al final). WebSearch sólo para localizar URLs; el presupuesto de búsquedas se agotó al final (200/turno), por lo que algunas pistas (p. ej. Exapro transformadores, Mascus filtros país) se resolvieron por navegación directa.

Etiquetas: **[ABIERTA]** = leído en la página/PDF/JSON; **[FRAGMENTO]** = sólo extracto de buscador; **NO ENCONTRADO**.

Bloqueos relevantes (no se pudo leer contenido): Machinio (403 Akamai, también machinio.es y con Chromium), Kitmondo (403 Cloudflare), eBay .es/.de/.com (403), Milanuncios (403 "navegando fuera de España"), Wallapop (403), TradeMachines (522 / timeout en 3 intentos), McKinsey (timeout), op.europa.eu fichas TED (403), ted.europa.eu HTML/PDF/XML (202 anti-bot; se usó la API, que sí responde).

---

## VEREDICTOS

| Hipótesis | Veredicto | Cifra corregida / base |
|---|---|---|
| H1a. Trafo 1–2,5 MVA usado/nuevo 30.000–80.000 € | **CORREGIDA (usado a la baja; nuevo SIN DATOS directos)** | Usado 50 Hz en UE con precio publicado: 1.000 kVA 20/0,4 kV Siemens 19.000 € (DE); 4.000 kVA seco 10 kV/690 V Siemens 39.000 € (BE); 6.600 kVA seco 10/3 kV 49.500 € (BE). Rango observado usado 1–6,6 MVA: ≈19.000–50.000 €. Nuevo: único anclaje 11,5 MVA seco Resibloc nuevo sin usar 365.000 € (≈32 €/kVA) → extrapolado 1–2,5 MVA nuevo ≈ 32.000–80.000 € (inferencia, no precio leído). |
| H1b. Trafo 10–40 MVA 200.000–900.000 € | **SIN DATOS de usado; CONFIRMADA sólo por benchmarks de nuevo** | 9 anuncios usados 5–31,5 MVA en Maschinensucher, todos "Preisinfo/Preis auf Anfrage". Nuevo: 11,5 MVA 365.000 € (anuncio); 15.000–21.000 $/MVA (USITC vía NLR, NextMSC) → 10–40 MVA ≈ 150.000–840.000 $. |
| H1c. Trafo 100 MVA 2–4 M€ | **CONFIRMADA (con matiz: excedente nuevo a 1,8 M€)** | Kolektor ETRA 100 MVA 110/33 kV, fabricado 2026, excedente de proyecto, 1.800.000 € fijo, "muy por debajo del precio de compra" (DE). NextMSC: 100 MVA nuevo 1,5–2,1 M$; muy personalizado hasta ≈4 M$. |
| H1d. Celdas MT 20–30 kV 15.000–60.000 €/cubículo | **SIN DATOS por cubículo** | Sólo conjuntos: Madrid 2023 celdas MT centro seccionamiento 119.976,52 € (nº celdas no visible); conjunto Alstom 20 kV usado 126.500 €; compacta 630 kVA con celdas MT+BT usada 39.500 €; bloque Ormazabal GAE630 usado 4.500 €. Marcos Endesa agregados (5,4–9,3 M€). Ningún precio unitario por cubículo leído. |
| H1e. Grupo electrógeno 1–3 MW 150.000–700.000 € | **CONFIRMADA** | 18 anuncios ≥1 MW con precio en UE/TR (ver tabla): usados 82.000 € (2 MVA, 1998) a 340.000 € (CAT 3512, 2011, ES); nuevos 2024–2026 425.000–595.000 € (2–3,1 MVA). Licitación SAS Granada 1.250 kVA: 165.548,78 € sin IVA. |
| H2. Inventario secundario accesible (trafos 50 Hz ≥1 MVA; gensets ≥1 MW) en Europa | **CONFIRMADA PARCIALMENTE: gensets SÍ (decenas); trafos ≥1 MVA ESCASO (≈20 anuncios visibles en toda la UE, 10–100 MVA ≈8 unidades, casi todo "precio a consultar")** | Maschinensucher/Machineseeker: 169 anuncios "Transformatoren", ≈17 ≥1 MVA 50 Hz; Surplus Record: 7 anuncios 50 Hz trifásicos (vs 4.870 a 60 Hz), 2 de ellos ≥1 MVA; Exapro: sin categoría de transformadores, 1 anuncio (EFACEC 3,7 MVA, PT). Gensets: Exapro 289 grupos (≥10 de ≥1 MW con precio), Mascus 3.973 ofertas globales con ≥12 unidades ≥1 MW en NL/ES/DE/UK con precio; Surplus Record 31 diésel 50 Hz (vs 2.416 a 60 Hz). |

---

## 1. Marketplaces (páginas abiertas)

### 1.1 Maschinensucher.de / Machineseeker.com (misma base de datos; DE/BE/NL/CZ/UK/HU/PL)
**[ABIERTA]** Categoría "Transformatoren / Trafo gebraucht kaufen (169)" (https://www.maschinensucher.de/Transformatoren/ci-70, páginas 1–6) + búsquedas "mva" (41 resultados) y "transformer 20kv" (757 resultados en Machineseeker, mezcla con componentes).

Anuncios ≥1 MVA, 50 Hz, Europa, identificados (título → precio):
| Equipo | Tensión | Año | Lugar | Precio publicado | Fuente |
|---|---|---|---|---|---|
| Kolektor ETRA T22-0909.1, 100 MVA ONAF (80 MVA ONAN), YNyn0+d, nuevo, excedente de parque eólico+BESS; recepción en fábrica Ljubljana 23-24/10/2026 | 110/33 kV | 2026 | Ascheberg, DE | **1.800.000 € Festpreis** (IVA no desglosable) | [ABIERTA] i-22892625 |
| Hitachi Energy RESIBLOC seco, 11,5 MVA, nuevo sin usar (almacenado) | n/d en texto leído | 2025 | Hilden, DE | **365.000 € EXW** + IVA | [ABIERTA] i-22292972 |
| TuR DD, 31,5 MVA aceite, regulador 19 tomas, Yy0 | 110/10,5 kV | 1979 | Langenhagen, DE | Preisinfo (a consultar) | [ABIERTA] i-14970319 |
| ALSTOM TC1743G 20/25 MVA aceite ONAN, 19 tomas, 40,8 t | 110/20 kV | 2001 | Cloppenburg, DE | Preisinfo | [ABIERTA] i-21669853 |
| Siemens TSLN7244, 15 MVA aceite, Ynd5 | 20-15/10,5 kV | 2008 | Langenhagen, DE | Preisinfo | [ABIERTA] listado |
| ETD Czech, 12,5 MVA | 110/23 kV | n/d | Hrušovany u Brna, CZ | Preisinfo | [ABIERTA] listado |
| Schneider Tricast seco 10 MVA | 10,5/6 kV | 2013 | Langenhagen, DE | Preisinfo | [ABIERTA] listado |
| TuR Dresden TDLF10000-30, 10 MVA aceite, YNyn0 | 30/10,5 kV | 1978 | Langenhagen, DE | Preisinfo | [ABIERTA] i-16458041 |
| Trafo-Union TG6841K seco 6.600 kVA | 10 kV/3.000 V | n/d | Lanaken, BE | **49.500 €** (antes 52.000) + IVA | [ABIERTA] i-20892377 |
| SGB 5760 / 2880-2880 kVA | 20/0,63-0,63 kV | n/d | Cloppenburg, DE | Preisinfo | [ABIERTA] listado |
| Schneider 5 MVA aceite Yy0 | 20/10 kV | 1999 | Langenhagen, DE | Preisinfo | [ABIERTA] listado |
| Siemens 4DG6644-8ZY seco 4.000 kVA | 10 kV/690 V | n/d | Lanaken, BE | **39.000 €** (antes 40.000) + IVA | [ABIERTA] i-20892037 |
| SGB DTTHDG 4000/20, 3.500 kVA (1750/1750) seco, Dy5d6 | 20 kV/2×690 V | 2010 | Langenhagen, DE | Preisinfo | [ABIERTA] i-22052013 |
| Siemens 2× 2.500 kVA secos (secundario rebobinado) + 2× 100 kVA | 6/0,4 kV | 2013 | Hrušovany u Brna, CZ | Preisinfo | [ABIERTA] i-22749402 |
| ALSTOM TRAFTA 1.600 kVA seco | 22/0,4 kV | n/d | CZ | Preisinfo | [ABIERTA] listado |
| TESAR seco nuevo 630/1000/1600/2000 kVA, ecodesign, sin usar | 20/0,4 kV | n/d | CZ | Preisinfo | [ABIERTA] i-12588860 |
| ABB 1.000 kVA | 20/0,41 kV | n/d | CZ | Preisinfo | [ABIERTA] listado |
| Siemens 1.000 kVA aceite hermético Dy11, pérdidas reducidas (Reg. 548/2014) | 20/0,4 kV | n/d | Ludwigshafen, DE | **19.000 € VB** + IVA | [ABIERTA] i-19507991 |
| Pauwels 1.600 kVA aceite | 21 kV/690 V | 2001 | Langenhagen, DE | n/d (sólo fragmento) | [FRAGMENTO] |

Otros con precio pero potencia no visible en título: Trihal resina 15.000 € (Cloughoge, IE); OMEXOM estación compacta 630 kVA 10 kV con celdas MT y BT 39.500 € (Viersen, DE); Siemens Energy GEAFOL Neo nuevo 2023 sin poner en servicio 28.000 € VB (Elmstein, DE); Holec RF.475 9.500 €; Trafo-Union TG 5841 C 9.500 €; France Transfo 2.500–3.500 €; 100 kVA ZSE 12.000 €.
Conclusión: de ≈17 anuncios ≥1 MVA, sólo 4 tienen precio (19.000 € / 39.000 € / 49.500 € / 365.000 € / 1.800.000 €); todos los 10–31,5 MVA usados son "a consultar".

Celdas/aparamenta MT **[ABIERTA]** (búsquedas "mittelspannungsschaltanlage", "schaltanlage"): Ormazabal GAE630 1M5-9 bloque 4.500 € (Wiefelstede, DE); Alstom Schaltanlage 20 kV con 3 trafos, distribuidor principal 400 V 2500 A, 126.500 € (Gondelsheim, DE); subestación móvil 630 kVA 22/0,4 kV y cuadro 6 kV 1250 A 40 kA ABB SR7 (CZ) a consultar.

Gensets **[ABIERTA]** (búsquedas "stromerzeuger", "dieselaggregat", "notstromaggregat"): MTU 20V4000 P63 2.500 kW (Haaksbergen, NL) Preisinfo; Cummins C2250 D5 2,25 MVA QSK60 (Glossop, UK) Preisinfo; resto <500 kVA con precio (p. ej. MAN 320 kVA 18.000 €; 300 kVA MECC ALTE 15.000 €; 60 kVA nuevo 13.015 €).

### 1.2 Surplus Record (EE. UU.) **[ABIERTA]**
- Búsqueda "transformer mva": categorías **"60 Hz Three Phase Transformers (4.870)"**, "60 Hz Padmount (2.985)", **"50 Hz Three Phase Transformers (7)"**. Diésel: "60 Cycle (2.416)" vs **"Diesel Driven Generators, 50 Cycle (31)"**.
- Categoría 50 Hz trifásicos (7 anuncios): 12 kVA Trasfor; 51 kVA Hitran 380/220 **850 $**; 145 kVA Hevi-Duty; **2.000 kVA Bowers 11.450 V/415 V, Dyn11, ONAN, 2011, 5 unidades, "Location: Europe"** (vendedor Savona Equipment, BC, Canadá) precio a consultar; **2.200 kVA IMEFY 33 kV/420 V** (mismo vendedor) a consultar; 5.000 kVA Sunbelt 4160/600 V 2018 padmount. Sólo 2 anuncios ≥1 MVA y 50 Hz.
- Fichas 60 Hz abiertas (sin precio publicado, todo "Request Quote"): 85 MVA GE 138/13,8 kV GSU (Power Asset Recovery, OH); 135/180/225 MVA Hico 345/34,5 kV **nuevo 2026** con LTC (Transformer Exchange, MI); 20 MVA Magnetek 69/13,2 kV 1994 (vendido); 2.500 kVA Surplec 27,6-13,8 kV/600 V 2026 (QC); 1.500 kVA Surplec 24,94 kV/600 V.
- Nota abnewswire 13-10-2026 sobre Surplus Record: **NO ENCONTRADO**. Abiertas https://www.abnewswire.com/pressreleases/?s=surplus+record, ?s=transformer y ?s=used+transformers (200): ningún resultado de Surplus Record. Búsquedas web con "Surplus Record" + abnewswire: 0 resultados.

### 1.3 Exapro **[ABIERTA]** (Chromium; 289 anuncios en "Energy - Generator sets"; no existe categoría de transformadores)
| Equipo | Potencia | Año | Horas | País | Precio |
|---|---|---|---|---|---|
| MTU 20V4000 DS3300 diésel abierto, 50 Hz, 400 V, nuevo | 3.100 kVA | 2024 | 0 | Turquía | **500.000 €** |
| MTU 16V4000 gas natural, 50 Hz, nuevo | 2 MW / 2.500 kVA, 11 kV | 2026 | 0 | Turquía | **595.000 €** |
| MTU 12V4000L64FNER gas natural, insonorizado, nuevo | 1,5 MW | 2024 | 0 | Turquía | **470.000 €** |
| CAT G3520C gas natural, 50 Hz | 2.500 kVA | 2007 | 30.000 h | Turquía | **350.000 €** |
| Jenbacher J612 GS-F11 planta completa, 400 V | 1.871 kW | 2008 | 55.000 h | Portugal | **150.000 €** |
| SREE grupo diésel 400 V | 2.000 kVA | ~1998 | 2.400 h | Rumanía | **82.000 €** |
| Jenbacher J616 GS-J11 gas, 690 V | 1.800 kVA (2.745 kW motor) | 2012/2015 | n/d | Turquía | a consultar |
| 4× Mitsubishi S12N-PTA diésel 380 V 50 Hz | 1.100 kVA c/u | 1991 | 832 h | Turquía | a consultar |
| CAT G3516A gas | ≈1 MW (1.030 kW) | 1997 | n/d | Reino Unido | a consultar |
| MTU 16V4000 ×3 bloque 6 MW **60 Hz** 13,2 kV | 6.000 kVA | 2005 | 703 h | EE. UU. | 1.103.000 € (no aplica 50 Hz) |
| SE2M/Scania 640 kVA PRP, nuevo | 640 kVA | 2023 | 0 | Francia | 58.000 € |
| EFACEC transformador seco Powercast 3.700 kVA 15/6,3 kV 50 Hz | 3,7 MVA | 1999 | – | Portugal | a consultar |
Texto de categoría Exapro: "Our generator sets range in price from €5,000 for basic models to €100,000 for advanced, high-capacity units" (genérico).

### 1.4 Mascus (**[ABIERTA]** mascus.com, .nl, .es, .co.uk; 3.973–3.977 ofertas de generadores globales; la portada global muestra EE. UU.)
| Equipo | Potencia | Año | Horas | Lugar | Precio |
|---|---|---|---|---|---|
| CAT 3516 (CYCLICA) | 1.825 kVA (detalle de 2011) / anuncio 2024 | 2024 | n/d | Madrid, ES | **556.000 €** |
| CAT 3512 (CYCLICA) ×2 | ≈1.600 kVA (3512B detalle) | 2011 / 2012 | n/d | Madrid, ES | **340.000 €** c/u |
| CAT C32 PGAG (CYCLICA) | ≈1.000 kVA clase | 2007 | 1 h | Madrid, ES | **225.000 €** |
| CAT 3508B (CYCLICA) | ≈1.000 kVA clase | 2005 | 202 h | Madrid, ES | 156.000 € |
| CAT 3412 (CYCLICA) ×3 | <1 MW | 2001–2006 | 2.107–6.413 h | Madrid, ES | 111.500–122.500 € |
| CAT 810 kVA (GMM) | 810 kVA | 2012 | 3.500 h | ES | 72.750 € |
| CAT 3516B (Marketplace-E Benelux) | 2.000 kVA / 1.600 kW | 2025 | n/d | Zevenbergen, NL | **425.000 €** (Koop nu) |
| CAT 3512C módulo perforación 995 ekW (DPX Power) | ≈1.250 kVA | 2008 | 6.302 h | Dordrecht, NL | **270.000 €** |
| CAT G3520 gas ×2 (DPX Power) | 2.150 kVA | 2009 | 49.800 h | Dordrecht, NL | **249.000 €** c/u |
| CAT XQ2000 (DPX Power) | 2.250 kVA | 2010 | 4.772 h | Dordrecht, NL | **199.000 €** |
| CAT 3512B módulo perforación 995 ekW (DPX Power) | ≈1.250 kVA | 2003 | 41.436 h | Dordrecht, NL | **165.000 €** |
| CAT 3512 (DPX Power) | 1.250 kVA | 2011 | 1.417 h | Dordrecht, NL | **150.000 €** |
| Cummins KTA38-G5 (DPX Power) | 1.100 kVA | 2026 | n/d | Dordrecht, NL | **128.576 GBP** (≈150 k€) |
| CAT 3516B-HD | 2.000 kW / 2.500 kVA | 2007 | 193 h | Moerdijk, NL | a consultar |
| Ferbo FE810-S Scania | 725 kVA | 2026 | 0 | UK | 67.208 GBP |
| CAT DE715E0 | 715 kVA | 2026 | 0 | UK | 76.500 GBP |
Mascus no tiene categoría de transformadores de potencia.

### 1.5 Otros marketplaces/portales
- Milanuncios, Wallapop, eBay (.es/.de/.com), Machinio, Kitmondo, TradeMachines: **bloqueados** (ver arriba). NO ENCONTRADO contenido.
- used-machines.com (anuncio "2000 kVA + 200 kVA", Alemania) **[ABIERTA]**: sin precio en la página.
- resale.info "1000 kva" **[ABIERTA]**: página de índice sin anuncios de grupos ≥1 MVA con precio legible.
- hellopro.fr guía de precios de grupos electrógenos **[ABIERTA]** (octubre 2026): nuevo 100–250 kVA 25.000–50.000 €; >500 kVA "sur devis"; contenedorizado nuevo 600 kVA ≈155.000 €, **1.000 kVA reciente ≈135.000 €**; ocasión >500 kVA 50.000–100.000 €+; ejemplos 350 kVA/1.200 h ≈19.000 €, 580 kVA/150 h ≈38.000 €, 700 kVA 2006/800 h ≈55.000 €.
- surplusrecord.com/news "selling used transformers" **[ABIERTA]**: sin precios; "over 100,000 active buyers every month", 0 comisiones.

---

## 2. Licitaciones públicas España/Portugal 2024-2026 (importes leídos)

Fuente principal: API TED (JSON) **[ABIERTA]**, PDFs de PLACSP/Junta de Andalucía/Zaragoza/BOE **[ABIERTA]**. contrataciondelestado.es (portal JSF) no indexa por buscador y su buscador no es navegable sin sesión; se cubrió vía TED (que replica los anuncios SARA).

### Grupos electrógenos
1. **SAS – H.U. Virgen de las Nieves (Granada), exp. ASU023-2026 (431/2026), memoria 30/04/2026**: Lote 1 **GE 1.250 kVA / 1.000 kW: 165.548,78 € sin IVA (200.314,02 € IVA incl.)**; Lote 2 **GE 850 kVA / 680 kW: 96.849,35 € sin IVA (117.187,71 €)**; PBL total 317.501,74 € IVA incl.; VE 262.398,13 €. [ABIERTA PDF 408797/408821]
2. **SAS – AGS Sur de Granada, exp. 258-2026**: 2× GE 55 kVA/40 kW (PPT sin importe en el PDF leído). [ABIERTA PDF 391602]
3. **H.U. Reina Sofía (Córdoba), emergencia 29/04/2025**: reparación GE 51.298,01 € sin IVA (62.070,59 €). [ABIERTA PDF]
4. **Ayto. Zaragoza, contrato menor (julio 2025)**: GE insonorizado 44/40 kVA, 12.900 € sin IVA (15.609 €). [ABIERTA PDF 100225]
5. **Ayto. Zaragoza**: GE 30/33 kVA, 14.500 € sin IVA (17.545 €). [ABIERTA PDF 85759]
6. **AEAT – GE para CPD del DIT (Madrid), exp. 25700060200**: adjudicado **1.235.710,04 €** a FIBRATEL (03/12/2025); potencia no indicada en el anuncio. [ABIERTA TED 11648-2026 + BOE-B-2026-629]
7. **ENAGÁS Transporte – 10 generadores de emergencia de AT para regasificadoras**: VE **15.000.000 €** (≈1,5 M€/ud; 20/01/2026). [ABIERTA TED 41717-2026]
8. **Fórum Evolución Burgos – 2 GE**: VE **397.736,57 €** (03/03/2026). [ABIERTA TED 146141-2026]
9. **Melilla (Comandancia Gral.)**: 2 GE emergencia Base Tte. Flomesta, adjudicado 03/07/2026 a Metalúrgica Andaluza de Maquinaria (importe no legible en el PDF) [ABIERTA BOE-B-2026-24265]; 4 GE 20 kVA adjudicados 13/07/2026 [ABIERTA BOE-B-2026-26231].
10. **Depto. Salud Xàtiva-Ontinyent – GE Hospital Lluís Alcanyís**: adjudicado 268.620 € (YOMEE, 13/03/2025). [ABIERTA TED 164134-2025]
11. **Aigües de Barcelona – cuadro general + GE ET1 EDAR Sant Feliu**: VE 516.000 €, adjudicado 410.637,79 € (Elecnor, 26/12/2025). [ABIERTA TED]
12. **Madrid Salud – GE a gas natural laboratorio**: VE 485.595,30 € (06/2024). [ABIERTA TED]
13. **Consorcio Aguas Zona Gaditana – GE + SAI**: VE 382.000 €, adjudicado 274.695 € (31/12/2025). [ABIERTA TED]
14. Portugal: ULS Gaia/Espinho GE redundante 380.000 € (08/2025); Marinha 3 grupos NRP Sagres lote 469.500 € (04/2024); EMARP Portimão geradores 327.000 € en 3 lotes (12/2025). [ABIERTA TED]

### Transformadores de potencia
15. **Adif AV – autotransformadores de aislamiento seco, subestación de tracción Montesa (Valencia–La Encina)**: VE 2.032.050 €, **adjudicado 1.953.045 € a Hitachi Energy Spain** (21/10/2024). [ABIERTA TED 374999/637019-2024]
16. **Adif AV – autotransformadores de tracción Montesa**: VE 882.782,14 € (02/2024). [ABIERTA TED 88623-2024]
17. **Serveis Ferroviaris de Mallorca – 6 transformadores de potencia subestaciones de tracción (EXP 1/25)**: VE 546.762,52 €; **adjudicado 424.342,96 € a Sampol** (09/09/2025) → ≈70.700 €/ud instalado (potencia no indicada). [ABIERTA TED 151311/588181-2025]
18. **IREC – PLEMCAT, trafo 132/66 kV 50 MVA ONAN / 65 MVA ONAF**: consulta preliminar de mercado 24/02/2025, sin valor. [ABIERTA TED 122126-2025]
19. **Red Eléctrica – 13 bancos autotransformadores monofásicos 200 MVA 400/220 kV + 4 trafos 125 MVA 220/66 kV**: adjudicado a EFACEC (29/01/2026), **importes no publicados (-1)**. [ABIERTA TED 65790-2026]
20. **Endesa/e-distribución**: 3 TR 315+80 MVA 400/132 kV (Garraf, Amantes, Baza) y 2 TR 200 MVA 230/132 kV (SE Cinca) y 3 ATR 160-200+63 MVA 230/138 kV — anuncios de adjudicación 24/07/2024 **sin importe**. Suministro trafos Baraka Logistics (Antequera) adjudicado **1.521.488 €** (25/06/2025, Fontecha Yébenes). Trafos distribución MT/BT: marcos 1.134.528 € y 3.849.097,86 € (Ormazabal, 11/2024) y 4× 21.445.184 € (12/2024, Matelec/Gedelsa/Ormazabal). [ABIERTA TED]
21. **Fira València – sustitución trafos secos encapsulados**: VE 315.000 € (18/02/2026). [ABIERTA TED 114309-2026]
22. **Zorrotzaurre (Bilbao) – centros de transformación de compañía**: 3 CT 320.000 € (03/2025) y 4 CT 430.000 € (09–10/2025) → ≈107.000 €/CT completo instalado. [ABIERTA TED 185121/629374/640387-2025]
23. **EEM Madeira – 5 transformadores de potencia AT/MT**: VE **4.067.818 €** (lotes 1.781.440 € y 2.286.378 €; 03/2025) → ≈814.000 €/ud (potencias no indicadas). [ABIERTA TED 161310-2025]
24. **DOE Extremadura 04/2025**: autorización sustitución T-1 66/23 kV 8 MVA por 20 MVA (Badajoz) — sin importe. [ABIERTA PDF]

### Celdas MT / aparamenta
25. **Comunidad de Madrid 2023 – celdas MT para centro de seccionamiento**: VE 119.976,52 € sin impuestos (145.171,59 € con) [FRAGMENTO; la página print/pdf abrió pero sin texto extraíble]; Gobierto 4325539 (CPV 31214520, CONEMAR): PBL 168.787,50 €, adjudicado 182.090,79 € (2023). [ABIERTA]
26. **Ayto. Málaga – celdas y cuadros BT para CT recinto ferial**: VE 542.822,92 €, adjudicado 324.933,82 € (04/2026). [ABIERTA TED]
27. **Aigües de Barcelona – cabinas subestaciones anillo MT depuradora Baix Llobregat**: VE 2.003.189 € (18/07/2025). [ABIERTA TED 472334-2025]
28. **Endesa – celdas MT SF6 cabinas de secundaria (GSM001)**: adjudicaciones 9.341.176,50 € ×2 (Ormazabal/Inael, 11/2024); 5.379.955,35 € (Inael, 08/2025); 810.830 / 3.183.526,75 / 3.848.281 € (Col Giovanni Paolo/Inael/Ormazabal, 11/2025). Celdas GIS 66 kV Base Naval Rota 1.178.150 €; ampliación 1 posición GIS 856.592–1.054.742 € (Siemens Energy/Hitachi/GE). [ABIERTA TED]
Ningún documento leído da precio por cubículo.

---

## 3. Informes y prensa con precio por MVA/kVA
- **Wood Mackenzie, nota de prensa 14/08/2025 [ABIERTA]**: déficit de oferta 2025 30 % (potencia) y 10 % (distribución) en EE. UU.; demanda +116 % (potencia) y +41 % (distribución) desde 2019; importaciones 80 %/50 %. Sin €/MVA.
- **Transformer Magazine 04/09/2025 [ABIERTA]** (fuente WoodMac): precios unitarios desde 2019 **+45 % GSU, +77 % transformadores de potencia, +78–95 % distribución**; GSU demanda +274 %.
- **Transformer Magazine 30/06/2026 "Used transformer demand rises sharply" [ABIERTA]** (https://transformers-magazine.com/tm-news/used-transformer-demand-rises-sharply/, fuente USA Today): Surplus Record procesó **>5.000 consultas de transformadores en el último año**; plazos de nuevo **18–24 meses o más**; demanda concentrada en **1–2,5 MVA**; secundario 480 V el más pedido; primarios 12.470 V y 13.800 V (padmount); trifásicos la mayor cuota; padmount trifásicos el mayor crecimiento interanual. Es mercado EE. UU. 60 Hz.
- **NextMSC "US transformer & switchgear prices, lead times" (oct. 2026) [ABIERTA]**: PPI transformadores ≈+90 % vs ene-2020 (jul-2026); switchgear +89,4 %; plazo LPT 30–36 meses; **precio nuevo LPT 15.000–21.000 $/MVA (USITC vía NLR)**; **100 MVA 1,5–2,1 M$; 100 MVA muy personalizado hasta ≈4 M$**; benchmark unitario superior ≈10 M$; acero+cobre ≈50 % del coste.
- **iRecruit "Substation construction cost 2026" [ABIERTA]**: MISO 4.600–18.500 $/MVA instalado según tensiones; autotrafo 345/138 kV 6.880 $/MVA; hasta 13.784 $/MVA; trafo de potencia solo 0,3–8 M$; plazos 128–144 semanas (hasta 4 años); +77 % desde 2019.
- **Thunder Said Energy [ABIERTA]**: coste de fabricación ≈8 $/kVA en puerta de fábrica para TIR 10 %; +2–3 $/kVA instalado; mano de obra ≈25 %, ≈45 h-hombre/MVA.
- **pv-magazine India [ABIERTA]**: precios +≈80 % en 5 años; esperas de 4 años; "others are resorting to refurbishing older equipment".
- **T&D World [ABIERTA]**: reproduce WoodMac (30 %/10 %, +116 %/+41 %, arancel cobre 50 %).
- BNEF, Siemens Energy, McKinsey (timeout): NO ENCONTRADO precio por MVA.
- Nota de prensa Surplus Record en abnewswire (13-10-2026): **NO ENCONTRADO** (ver 1.2).

---

## 4. Lectura adversarial
1. **El "inventario secundario" europeo de transformadores de potencia es muy delgado**: en la mayor plataforma de maquinaria usada de la UE hay ≈17 anuncios ≥1 MVA (de 169 "transformadores"), 8 de ellos ≥10 MVA, concentrados en 2–3 vendedores alemanes (Langenhagen, Cloppenburg) y uno checo; Surplus Record tiene 7 anuncios 50 Hz frente a 4.870 a 60 Hz. Un broker no puede contar con un flujo recurrente de 10–40 MVA usados; el caso Kolektor (excedente de parque eólico/BESS cancelado, nuevo 2026) muestra que el producto real es **excedente de proyecto**, no "usado".
2. **La opacidad de precios es la norma**: 0 de 9 anuncios 5–31,5 MVA usados publica precio; Surplus Record no publica precios en ≥1 MVA; REE y Endesa ocultan importes de adjudicación. Las horquillas de H1b sólo se sostienen con benchmarks de nuevo en EE. UU. (15–21 k$/MVA).
3. **1–2,5 MVA usados valen menos de lo supuesto**: los precios leídos (19.000 € por 1 MVA aceite; 39.000 € por 4 MVA seco) indican 10–20 €/kVA usado; la horquilla 30–80 k€ sólo cuadra para equipo nuevo (≈32 €/kVA en el Resibloc nuevo).
4. **Gensets ≥1 MW sí tienen mercado secundario visible y con precio**, aunque buena parte del stock "nuevo" barato está en Turquía (MTU/CAT a 350–595 k€) y los usados europeos con pocas horas se venden a 150–340 k€ (CAT 3512/XQ2000 en NL/ES). La licitación andaluza (165.549 € por 1.250 kVA nuevo instalado, sin IVA) marca el techo de lo que paga un hospital por 1,25 MVA.
5. **Celdas MT**: no existe ningún precio público por cubículo en lo abierto; los datos son de conjuntos/marcos. H1d queda sin base verificable.

---

## 5. Tabla de URLs abiertas y estado HTTP
| # | URL | Estado HTTP |
|---|---|---|
| 1 | https://www.woodmac.com/press-releases/power-transformers-and-distribution-transformers-will-face-supply-deficits-of-30-and-10-in-2025/ | 200 |
| 2 | https://www.machinio.com/transformers | 403 |
| 3 | https://www.exapro.com/used-transformers/ | 404 |
| 4 | https://www.surplusrecord.com/transformers/ | 404 |
| 5 | https://www.mascus.com/construction/used-generators | 200 |
| 6 | https://www.kitmondo.com/used-transformers | 404 |
| 7 | https://transformers-magazine.com/tm-news/us-transformer-market-faces-severe-bottlenecks/ | 200 |
| 8 | https://trademachines.com/used-transformers | 522 |
| 9 | https://www.surplusrecord.com/electrical-power/transformers/ | 404 |
| 10 | https://www.mascus.es/construccion/grupos-electrogenos-usados | 404 |
| 11 | https://www.machinio.com/generators?power_kw_min=1000 | 403 |
| 12 | https://www.milanuncios.com/anuncios/transformador-trifasico-kva.htm | 403 |
| 13 | https://www.ebay.es/sch/i.html?_nkw=transformador+trifasico+kva&_sop=16 | 403 |
| 14 | https://www.kitmondo.com/search?q=transformer | 403 |
| 15 | https://www.exapro.com/search/?q=transformer | 404 |
| 16 | https://www.surplusrecord.com/search/?q=transformer+mva | 200 |
| 17 | https://trademachines.com/search?q=transformer | FAIL/timeout |
| 18 | https://ted.europa.eu/es/notice/290094-2025/pdf | 202 |
| 19 | https://ted.europa.eu/es/notice/629374-2025/pdf | 202 |
| 20 | https://contratos.gobierto.es/licitaciones/121051 | 200 |
| 21 | https://conseils.hellopro.fr/guide-des-prix-des-groupes-electrogenes-1159.html | 200 |
| 22 | https://pv-magazine-usa.com/2025/08/14/grid-transformers-face-significant-supply-deficits-says-wood-mackenzie/ | 200 |
| 23 | https://www.maschinensucher.de/mss/mva | 200 |
| 24 | https://surplusrecord.com/listing/85-mva-138000y-primary-13800-delta-secondary-general-electric-gsu-oil-594308/ | 200 |
| 25 | https://surplusrecord.com/listing/1500-kva-24940y-primary-600y-secondary-transformer-1058445/ | 200 |
| 26 | https://www.maschinensucher.de/alstom-leistungstrafo+20%2F25+mva+%7C+110kv+%2F+20kv/i-21669853 | 200 |
| 27 | https://www.maschinensucher.de/Transformatoren/ci-70 | 200 |
| 28 | https://surplusrecord.com/listing/2500-kva-27600x13800y-primary-600y-secondary-surplec-1039457/ | 200 |
| 29 | https://www.machineseeker.com/mss/transformer+20kv | 200 |
| 30 | https://surplusrecord.com/listing/225-mva-345kv-34-5kv-1048930 | 200 |
| 31 | https://www.surplusrecord.com/listing/1994-magnetek-20-mva-69-13-2-7-62-kv-transformer-7-65-impedance-1066863/ | 200 |
| 32 | https://www.exapro.com/atlas-aj-s-1250-p260902655 | 200 |
| 33 | https://www.mckinsey.com/industries/electric-power-and-natural-gas/our-insights/the-transformer-supercycle-why-demand-is-outrunning-supply | FAIL/timeout |
| 34 | https://www.maschinensucher.de/trafo-union-tg6841k/i-20892377 | 200 |
| 35 | https://www.maschinensucher.de/omexom-m/i-22164707 | 200 |
| 36 | https://www.maschinensucher.de/siemens-4dg6644-8zy/i-20892037 | 200 |
| 37 | https://www.maschinensucher.de/mss/stromerzeuger+kva | 404 |
| 38 | https://www.maschinensucher.de/hitachi-standard+resibloc/i-22292972 | 200 |
| 39 | https://www.maschinensucher.de/siemens+energy-geafol+neo+4+gx+6581+4+ec/i-21592223 | 200 |
| 40 | https://contratos-publicos.comunidad.madrid/sites/default/files/PCON/2024-04/pliego_de_prescripciones_tecnicas_particulares_17.pdf | 200 |
| 41 | https://www.maschinensucher.de/kolektor+etra-t22-0909.1/i-22892625 | 200 |
| 42 | https://www.machineseeker.com/mss/generator+1000+kva | 404 |
| 43 | https://www.maschinensucher.de/siemens-2500kva+6%2F0%2C4kv/i-22749402 | 200 |
| 44 | https://www.maschinensucher.de/tur+dresden+10mva+%C3%B6l+30-10%2C5kv%2C+1978-tdlf10000-30%2C+ynyn0/i-16458041 | 200 |
| 45 | https://www.maschinensucher.de/3500kva%2C+20kv%2F690%2F690v%2C+sgb%2C+2010-dtthdg+4000%2F20/i-22052013 | 200 |
| 46 | https://www.maschinensucher.de/tur+dd+31%2C5+mva+%C3%B6l-leistungstrafo+110-10%2C5+kv%3B+yy0/i-14970319 | 200 |
| 47 | https://www.juntadeandalucia.es/haciendayadministracionpublica/apl/pdc_sirec_documentacion/rest/descargar/documento/408797 | 200 |
| 48 | https://www.machinio.es/transformadores | 403 |
| 49 | https://www.truck1.eu/construction-equipment/generators | 202 |
| 50 | https://www.maschinensucher.de/mss/notstromaggregat+1000+kva | 404 |
| 51 | https://www.machineseeker.com/mss/generator+set+kva | 404 |
| 52 | https://www.maschinensucher.de/mss/mittelspannungsschaltanlage | 200 |
| 53 | https://transformers-magazine.com/?s=used+transformer | 200 |
| 54 | https://ted.europa.eu/en/notice/-/detail/629374-2025 | 202 |
| 55 | https://ted.europa.eu/en/notice/-/detail/290094-2025 | 202 |
| 56 | https://trademachines.com/transformers | FAIL/timeout |
| 57 | https://www.maschinensucher.de/mss/schaltanlage+20+kv | 404 |
| 58 | https://www.machineseeker.com/mss/generator+1000kva | 404 |
| 59 | https://www.maschinensucher.de/mss/mittelspannung | 404 |
| 60 | https://www.mascus.es/construccion/grupos-electrogenos | 404 |
| 61 | https://www.maschinensucher.de/mss/stromerzeuger | 200 |
| 62 | https://www.machineseeker.com/Generators/ci-1133 | 200 |
| 63 | https://transformer-magazine.com/news/used-transformer-demand-rises-sharply/ | 200 |
| 64 | https://transformers-magazine.com/tm-news/used-transformer-demand-rises-sharply/ | 200 |
| 65 | https://www.mascus.com/construction/used-generators/europe | 200 |
| 66 | https://www.mascus.com/construction/used-generators?power_output_min=1000 | 403 |
| 67 | https://www.exapro.com/used-electronics/ | 404 |
| 68 | https://www.exapro.com/used-energy-generator-sets/ | 404 |
| 69 | https://www.surplusrecord.com/search/?q=50+hz+three+phase+transformer | 200 |
| 70 | https://thundersaidenergy.com/downloads/transformers-companies-and-costs/ | 200 |
| 71 | https://www.maschinensucher.de/mss/mtu+20v4000 | 404 |
| 72 | https://www.indexbox.io/store/united-states-medium-power-transformers-market-analysis-forecast-size-trends-and-insights/ | 200 |
| 73 | https://www.machineseeker.com/mss/generator+mva | 404 |
| 74 | https://contratos.gobierto.es/licitaciones?q=transformador+de+potencia | 200 |
| 75 | https://contratos.gobierto.es/licitaciones/4325539 | 200 |
| 76 | https://www.nextmsc.com/industry-deep-dive/us-transformer-switchgear-prices-lead-times-2026 | 200 |
| 77 | https://www.maschinensucher.de/mss/generator+mva | 404 |
| 78 | https://autoline.es/-/grupos-electrogenos--c5447 | 200 |
| 79 | https://www.machineseeker.com/Power-engineering-equipment-electrical-supplies/ci-1000 | 200 |
| 80 | https://contratos-publicos.comunidad.madrid/contrato-publico/print/pdf/node/274413 | 200 |
| 81 | https://ted.europa.eu/es/notice/472334-2025/pdf | 202 |
| 82 | https://op.europa.eu/en/web/public-procurement/procurement-details/-/procurement/08cfd36b-df70-3d7d-a1f7-09eb3765ba8f | 403 |
| 83 | https://op.europa.eu/es/web/public-procurement/procurement-details/-/procurement/6b6a7143-d4cc-4c8d-b6ae-2a1cf6b8848c | 403 |
| 84 | https://www.surplusrecord.com/electrical-power/diesel-generators/ | 200 |
| 85 | https://www.surplusrecord.com/electrical-power/60-hz-three-phase-transformers/ | 200 |
| 86 | https://www.surplusrecord.com/electrical-power/50-hz-three-phase-transformers/ | 200 |
| 87 | https://contrataciondelestado.es/wps/portal/licitaciones | 200 |
| 88 | https://ted.europa.eu/en/notice/-/detail/146141-2026 | 202 |
| 89 | https://www.used-machines.com/m-m/gm-345-7364 | 200 |
| 90 | https://alicanteplaza.es/alicanteplaza/adif-licita-el-contrato-para-la-estacion-electrica-del-tramo-la-encina-xativa-del-ave | 200 |
| 91 | https://www.bolsamania.com/noticias/empresas/economia--adif-adjudica-a-lantania-la-puesta-en-servicio-de-una-subestacion-electrica-en-pontevedra-por-6-millones--7871162.html | 200 |
| 92 | https://www.resale.info/en/1000-kva/36/ | 200 |
| 93 | https://www.surplusrecord.com/electrical-power/diesel-driven-generators-50-cycle/ | 404 |
| 94 | https://www.exapro.com/generator-sets-compressors-generator-sets-c99/ | 200 |
| 95 | https://www.machineseeker.com/mss/emergency+power+generator+kva | 404 |
| 96 | https://www.machineseeker.com/Transformers/ci-70 | 200 |
| 97 | https://www.maschinensucher.de/mss/notstromaggregat | 200 |
| 98 | https://www.maschinensucher.de/mss/mtu+dieselaggregat | 404 |
| 99 | https://www.irecruit.co/guides/substation-construction-cost | 200 |
| 100 | https://www.tdworld.com/substations/news/55310262/report-warns-of-worsening-transformer-shortages-amid-rising-us-power-demand | 200 |
| 101 | https://energy-solutions.co/supply-chain/manufacturers/east-asia-transformer-mega-hub-07b4 | 403 |
| 102 | https://www.maschinensucher.de/Transformatoren/ci-70?page=2 | 200 |
| 103 | https://www.machineseeker.com/mss/transformer+mva | 404 |
| 104 | https://www.machineseeker.com/Power-generators/ci-1134 | 200 |
| 105 | https://es.wallapop.com/app/search?keywords=transformador%20trifasico%20kva | 403 |
| 106 | https://www.milanuncios.com/anuncios/grupo-electrogeno-kva.htm | 403 |
| 107 | https://www.kitmondo.com/used-generator-sets | 403 |
| 108 | https://www.ebay.com/sch/i.html?_nkw=transformer+mva | 403 |
| 109 | https://www.ebay.de/sch/i.html?_nkw=transformator+kva+20kv | 403 |
| 110 | https://www.surplusrecord.com/search/?q=1500+kva+transformer | 200 |
| 111 | https://www.exapro.com/generator-sets-compressors-generator-sets-c99/?page=1 | 200 |
| 112 | https://www.maschinensucher.de/mss/alstom+schaltanlage | 404 |
| 113 | https://www.maschinensucher.de/Transformatoren/ci-70?page=3 | 200 |
| 114 | https://surplusrecord.com/news/selling-used-transformers-online-questions/ | 200 |
| 115 | https://www.maschinensucher.de/Transformatoren/ci-70?page=6 | 200 |
| 116 | https://www.maschinensucher.de/Transformatoren/ci-70?page=5 | 200 |
| 117 | https://www.maschinensucher.de/Transformatoren/ci-70?page=4 | 200 |
| 118 | https://conseils.hellopro.fr/combien-coute-un-groupe-electrogene-en-container-ou-un-container-technique-pour-groupe-electrogene-4823.html | 200 |
| 119 | https://www.maschinensucher.de/mss/schaltanlage | 200 |
| 120 | https://www.pv-magazine-india.com/?p=14896 | 200 |
| 121 | https://www.energypower.com.au/shop/ua931/ | 200 |
| 122 | https://www.usatoday.com/search/?q=surplus+record+transformer | 200 |
| 123 | https://www.abnewswire.com/pressreleases/?s=surplus+record | 200 |
| 124 | https://www.machineseeker.com/Generators/ci-1134 | 200 |
| 125 | https://www.maschinensucher.de/Stromerzeuger/ci-1134 | 200 |
| 126 | https://www.machineseeker.com/Power-generators/ci-1136 | 200 |
| 127 | https://www.exapro.com/search/?keywords=transformer | 404 |
| 128 | https://www.surplusrecord.com/search/?q=50+hz+diesel+generator+kw | 200 |
| 129 | 1792706330 | 200 |
| 130 | https://www.maschinensucher.de/tesar+italy-630%2C+1000%2C+1600%2C+2000kva++20%2F0%2C4kv/i-12588860 | 200 |
| 131 | https://www.mascus.de/bau/generatoren | 404 |
| 132 | https://www.maschinensucher.de/siemens-1000+kva+20%2F0%2C4+kv+dy11/i-19507991 | 200 |
| 133 | https://www.mascus.nl/bouw/generatoren | 200 |
| 134 | https://www.mascus.es/construccion/generadores | 200 |
| 135 | https://www.mascus.co.uk/construction/used-generators | 200 |
| 136 | STATUS 200 | exapro detail |
| 137 | https://www.machineseeker.com/mss/caterpillar+generator+kva | 404 |
| 138 | https://www.machineseeker.com/mss/mtu+generator | 404 |
| 139 | https://www.maschinensucher.de/mss/dieselaggregat | 200 |
| 140 | https://www.mascus.co.uk/construction/used-generators/cummins | 200 |
| 141 | https://www.mascus.nl/bouw/generatoren/caterpillar | 200 |
| 142 | https://www.mascus.co.uk/construction/used-generators/caterpillar | 200 |
| 143 | https://www.mascus.es/construccion/generadores/caterpillar | 200 |
| 144 | https://www.mascus.co.uk/construction/used-generators/2 | 200 |
| 145 | https://www.mascus.es/construccion/generadores-diesel/cat-3512-b/gqangteo.html | 200 |
| 146 | https://www.mascus.nl/bouw/diesel-generatoren/cat-3512-1250-kva-used-generator-dpx-12662/prrjgmqk.html | 200 |
| 147 | https://www.mascus.es/construccion/generadores-diesel/cat-3516/7x8tbx5u.html | 200 |
| 148 | https://www.mascus.nl/bouw/diesel-generatoren/cat-3516b-hd-used-2000-kw-193-hrs/jqiqfpqq.html | 200 |
| 149 | https://www.mascus.nl/bouw/diesel-generatoren/cat-3516b/hfkcrpnk.html | 200 |
| 150 | https://www.mascus.es/construccion/generadores-diesel/cat-3516/5uelfm8t.html | 200 |
| 151 | https://www.mascus.nl/bouw/diesel-generatoren/cat-xq2000-2-250-kva-generator-dpx-12671/korohdqg.html | 200 |
| 152 | https://www.juntadeandalucia.es/haciendayadministracionpublica/apl/pdc_sirec_documentacion/rest/descargar/documento/408821 | 200 (PDF) |
| 153 | https://www.juntadeandalucia.es/haciendayadministracionpublica/apl/pdc_sirec_documentacion/rest/descargar/documento/391602 | 200 (PDF) |
| 154 | https://ws040.juntadeandalucia.es/webconsejos/cgobierno/transparencia/250625/documentos/32Expediente.pdf | 200 (PDF) |
| 155 | https://www.zaragoza.es/sede/servicio/contratacion-publica/anuncio/100225/document.pdf | 200 (PDF) |
| 156 | https://www.zaragoza.es/sede/servicio/contratacion-publica/anuncio/85759/document.pdf | 200 (PDF) |
| 157 | https://doe.juntaex.es/pdfs/doe/2025/740o/25080334.pdf | 200 (PDF) |
| 158 | https://www.boe.es/boe/dias/2026/08/06/pdfs/BOE-B-2026-26231.pdf | 200 (PDF) |
| 159 | https://www.boe.es/boe/dias/2026/07/16/pdfs/BOE-B-2026-24265.pdf | 200 (PDF) |
| 160 | https://www.boe.es/boe/dias/2026/01/13/pdfs/BOE-B-2026-629.pdf | 200 (PDF) |
| 161 | https://www.boe.es/boe/dias/2026/09/01/pdfs/BOE-B-2026-28287.pdf | 200 (PDF) |
| 162 | https://www.boe.es/boe/dias/2026/07/17/pdfs/BOE-B-2026-24414.pdf | 200 (PDF) |
| 163 | https://www.boe.es/boe/dias/2026/08/26/pdfs/BOE-B-2026-27820.pdf | 200 (PDF) |
| 164 | https://api.ted.europa.eu/v3/notices/search (POST; 7 consultas: CPV 3117xxxx ESP, 3112xxxx ESP x2, 31214520/3121xxxx ESP, 3117/3112 PRT, FT~MVA ESP, ND IN (...)) | 200 (JSON) |
| 165 | https://ted.europa.eu/es/notice/{629374-2025,290094-2025,472334-2025,146141-2026,41717-2026,683682-2025,166444-2026,73280-2026,240049-2026,312657-2026,380517-2026}/pdf|xml | 202 (challenge anti-bot, sin contenido) |

Total URLs distintas intentadas: 165; con 200: 109
