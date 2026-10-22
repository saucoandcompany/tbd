# Business plan v2: intermediación de gensets ≥1 MW y excedentes de proyecto eléctrico en la UE

Fecha: 22-10-2026. Sustituye a la v1 del mismo día tras la investigación adversarial (`reports/Investigacion adversarial - Broker equipos electricos.md`, 25 hipótesis, ≈380 páginas abiertas). Cada cifra lleva **[VERIFICADO]** (leído en página; fuente en las notas de `research_notes/Broker adversarial 2026/` y `Demanda voraz sin filtros 2026/`), **[FRAGMENTO]** o **[HIPÓTESIS]**. Las hipótesis que quedan son las que solo la prueba de mercado puede resolver.

---

## 0. Resumen ejecutivo

**Qué cambia respecto a la v1.** La investigación destruyó tres pilares: no hay inventario recurrente de transformadores de potencia usados en Europa (≈17 anuncios ≥1 MVA en la mayor plataforma europea, 8 de ellos ≥10 MVA, casi todos sin precio) [VERIFICADO]; la tasa de respuesta del 6 % no la sostiene ninguna muestra grande (mediana 0,74 % por contacto; buenos remitentes segmentados 2,5-4 %) [VERIFICADO]; y la comisión de mercado a éxito en maquinaria es 7-15 %, no 4-6 % [VERIFICADO]. Confirmó dos: la escasez de equipo nuevo es real y dura hasta 2029 [VERIFICADO], y hay demanda con permiso y reloj (11,8 GW de demanda industrial y de centros de datos con acceso otorgado desde 2022 y 0 en servicio; 28,1 GW de renovables que deben operar antes de junio de 2028) [VERIFICADO].

**El negocio, redefinido.** Intermediario independiente de una persona, en la UE, para dos productos:
1. **Grupos electrógenos ≥1 MW** (diésel y gas) nuevos de stock y usados con horas bajas: hay inventario (289 en Exapro, 3.973 ofertas en Mascus) y precios leídos de 82.000 a 595.000 € [VERIFICADO]. Compradores: centros de datos, industria, hospitales, EPC. Importaciones españolas de gensets >375 kVA ×2,4 en 2025 [VERIFICADO].
2. **Excedentes de proyecto**: transformadores de potencia, celdas MT/AT y gensets nuevos de proyectos cancelados o retrasados dentro de la UE. Caso tipo: Kolektor ETRA 100 MVA 110/33 kV fabricado en 2026, excedente de parque eólico con BESS, 1,8 M€ fijo, "muy por debajo del precio de compra" [VERIFICADO]. Vendedores: promotores y EPC con proyecto caído; compradores: promotores con autorización y plazo.

Solo UE: desde el 25-09-2026 la UE aplica una salvaguardia de 1.140 €/t de núcleo a todo transformador importado, nuevo o usado, de cualquier origen salvo Brasil (Reg. 2026/2133) [VERIFICADO]; los usados importados de terceros países además deben cumplir Tier 2 de ecodiseño y las celdas SF6 importadas chocan con las fechas del Reg. 2024/573 [VERIFICADO]. Las celdas SF6 usadas se pueden reinstalar dentro de la UE (art. 13.10) [VERIFICADO].

**Números de cabecera** (cálculo en sección 8; todos [HIPÓTESIS] salvo los costes unitarios de herramientas y cuotas):

| Magnitud | Pesimista | Base | Optimista |
|---|---|---|---|
| Ticket medio | 150.000 € | 300.000 € | 400.000 € |
| Comisión media efectiva | 8 % | 7 % | 6,5 % |
| Ingreso por operación | 12.000 € | 21.000 € | 26.000 € |
| Operaciones año 1 (Iberia, 4 buzones + LinkedIn) | 2 | 5 | 10 |
| Ingresos año 1 | 24.000 € | 105.000 € | 260.000 € |
| Costes fijos año 1 | 7.500 € | 8.700 € | 10.500 € |
| Resultado año 1 antes de IRPF | 16.500 € | 96.300 € | 249.500 € |
| Operaciones año 2 (+ Francia e Italia) | 4 | 12 | 25 |
| Ingresos año 2 | 48.000 € | 252.000 € | 650.000 € |
| Costes fijos año 2 | 14.000 € | 15.500 € | 26.000 € (con apoyo a tiempo parcial) |
| Resultado año 2 antes de IRPF | 34.000 € | 236.500 € | 624.000 € |

IRPF efectivo sobre 66.550 € en Madrid: 28,45 % [VERIFICADO, cálculo en la nota fiscal]; sobre 96.300 € será mayor (tramo estatal 45 % desde 60.000 €; no calculado).

**Restricción personal que manda sobre el calendario.** Trabajar por cuenta propia durante la incapacidad temporal permite denegar, anular o suspender el subsidio (art. 175.1.b LGSS) y durante el permiso por nacimiento es incompatible (art. 180 LGSS) [VERIFICADO]. La prueba de 2 semanas no factura y es viable; la gestión activa de operaciones y el primer cobro esperan al fin de la baja.

---

## 1. Tesis

### 1.1 El problema, con datos

- Fabricantes de transformadores en España con cartera cubierta "al menos cuatro años"; plazo prepandemia 10-12 meses, hoy 3-4 años [VERIFICADO, El Español 23-06-2026]. GSU >160 semanas en 1T 2026 [VERIFICADO, Reuters/Wood Mackenzie]. Precios +77 % potencia, +45 % GSU desde 2019 [VERIFICADO, Wood Mackenzie vía POWER].
- Capacidad nueva de Hitachi Energy en Gallman desde 2029; Córdoba (+80 M€) a fin de 2027 [VERIFICADO].
- Demanda bloqueada con reloj: 11,8 GW de demanda otorgados desde 2022 y 0 en servicio; 28,1 GW de renovables con autorización de construcción que deben operar antes de junio de 2028; 22 GW de BESS con permiso y <300 MW operando [VERIFICADO, REE y prensa sectorial].
- Pero la causa documentada del bloqueo es acceso a red y tramitación (63 % de las subestaciones de la planificación con >7 años de retraso medio) [VERIFICADO, PwC-Aelec]; no se encontró ningún caso nominal español "parado por falta de transformador". Consecuencia: el dolor existe, pero el comprador no lo nombra como "me falta un trafo", sino como "no llego a la fecha". El mensaje comercial debe hablar de fecha, no de equipo.

### 1.2 Por qué excedentes y gensets, y no usados

El mercado europeo de transformadores de potencia usados es delgado y está en manos de 5-6 traders (Koopmann, Trafo-City, HT-Volteq en Alemania; BTB en Finlandia; Slaters en Reino Unido; LV Trading en Países Bajos) [VERIFICADO]. Competir con ellos en stock es imposible sin capital. En cambio:
- **Excedentes de proyecto** aparecen donde hay proyectos cancelados: en España se instalaron 10,1 GW fotovoltaicos en 2025 frente a 28,1 GW autorizados [VERIFICADO]; el diferencial es cancelación, retraso o venta de proyecto, y cada uno puede dejar un transformador o unas celdas pedidos o fabricados. Nadie los lista: hay que preguntar. Eso es prospección, el oficio de Jorge.
- **Gensets ≥1 MW** tienen inventario líquido, precios públicos y demanda creciente (centros de datos: 439 MW en 2025 → 2.537 MW en 2030 según Spain DC; CBRE 1,4 GW operativo o en construcción) [VERIFICADO].

### 1.3 Ventaja y límite

Ventaja: criterio técnico del fundador (ficha, ensayos, compatibilidad), base de datos propia de necesidades con fecha y de excedentes, idioma y presencia ibérica frente a traders alemanes y finlandeses. Límite: no escala sin personas; la ventana es 2026-2029.

---

## 2. Mercado

### 2.1 Tamaño (cálculo con datos de comercio exterior)

| Segmento | Dato abierto 2025 | Mercado aparente ES+PT estimado |
|---|---|---|
| Transformadores >10 MVA (8504.23) | Importaciones ES 256 M€ (68 en 2022, ×3,8), PT 17 M€; exportaciones ES 101 M€ [VERIFICADO, Comext] | 550-820 M€ [HIPÓTESIS: producción nacional 1-2× importaciones] |
| Transformadores 650 kVA-10 MVA (8504.22) | Imp. ES 281 M€ [VERIFICADO] | 400-600 M€ [HIPÓTESIS] |
| Celdas y cuadros MT/AT (8537.20, 8535) | Imp. ES 221 + 222 M€; ES exporta 464 M€ en 8537.20 [VERIFICADO] | 300-600 M€ [HIPÓTESIS] |
| Gensets >375 kVA (8502.13) | Imp. ES 128 M€ (54 en 2024, ×2,4) [VERIFICADO] | 150-300 M€ [HIPÓTESIS] |
| **Total alcance** | | **1.300-2.400 M€/año** |

Iberia pesa 1-1,5 % del mercado global de transformadores de potencia (≈30.000 M€), no el 2-3 % de la v1.

SAM [HIPÓTESIS]: 3-5 % del alcance pasa por canal secundario o acelerado → 40-120 M€/año. SOM año 2 [HIPÓTESIS]: 2-4 % del SAM → 1-5 M€ intermediados → 70.000-350.000 € de comisión al 7 %. El escenario base del año 2 (252.000 €) cae dentro del rango solo con Francia e Italia añadidas; sin ellas, el techo ibérico realista es el pesimista-base.

### 2.2 Universo de contactos (medido en Apollo, gratis, 22-10-2026)

| Lado | Empresas útiles en Iberia (tras descontar 35 % de ruido) |
|---|---|
| Promotores y EPC de renovables | ≥500 |
| Centros de datos | ≥130 |
| Ingeniería eléctrica y subestaciones | 160-390 |
| Electrointensivos | 100-260 |
| **Compradores** | **≈900-1.300** |
| Fabricantes, talleres, alquiladores, distribuidores de trafos, celdas y gensets | **≈65-195** |

Con 4 buzones (≈590 contactos nuevos al mes, ver 5.1) Iberia se agota en 2-3 meses. Por eso el plan v2 incorpora Francia e Italia desde el mes 4, no en el año 2.

### 2.3 Competencia y sustitutos [VERIFICADO salvo indicación]

| Actor | País | Qué hace | Amenaza |
|---|---|---|---|
| AAM Global (Aznar Assets Management) | ES, Tarazona | Compra-venta de trafos y motogeneradores de segunda mano "evitando grandes plazos", almacén propio; no publica kVA ni precio | Media: es el único ibérico; puede escalar |
| Alquiler Transformadores SL | ES, Oyón | CNAE 4614, intermediación y compraventa; sin web | Baja |
| BTB Transformers | FI | Marketplace 150+ unidades hasta 500 MVA, "Fast Track" | Alta en trafos grandes |
| Koopmann | DE | 210-250 trafos 50 kVA-63 MVA en stock, reparación hasta 110 kV, grupo de 370 empleados | Alta |
| Slaters Electricals | UK | Mayor stock reacondicionado del Reino Unido, celdas 11-33 kV con 36 meses de garantía | Media (post-Brexit, 50 Hz compatible) |
| Trafo-City, HT-Volteq | DE | 5-31,5 MVA 110 kV; trading y servicio | Media |
| General Power Holland, DPX Power | NL | Gensets usados ≥1 MW con stock list; GPH también compra trafos | Alta en gensets |
| Marketplaces (Maschinensucher, Machinio, Exapro, Mascus, Surplus Record) | — | Listan; Exapro cobra 15 % al vendedor | Fuente y competencia |
| Alquiler (Atlas Copco hasta 6,3 MVA, Bredenoord, Finanzauto, Himoinsa HRS) | ES/PT | Transformadores y gensets en alquiler ≤6,3 MVA | Sustituto en gensets |
| Fabricantes con servicio (Hitachi, Efacec, Gedelsa) | ES/PT | Reparación; ninguno publica stock ni canal de ocasión | Baja hoy |

Hueco confirmado: nadie en Iberia se presenta como intermediario especializado de 1-100 MVA y gensets ≥1 MW con verificación técnica en castellano y portugués. Hueco corregido: no estamos solos; los traders del norte ya venden a España a través de marketplaces.

---

## 3. Oferta y precios

| Servicio | Precio | Base |
|---|---|---|
| Intermediación a éxito | **8 % hasta 250.000 €; 6 % de 250.000 a 1 M€; 4 % por encima; mínimo 3.000 €** | Exapro 15 % mín. 1.000 €; consignación 10 %; subastas 7-9 % al vendedor; escalas decrecientes de aviación y M&A [VERIFICADO]; la cifra concreta es [HIPÓTESIS] a validar en las 3 primeras operaciones |
| Búsqueda bajo mandato (retainer) | 2.000-3.000 €, descontable de la comisión | [HIPÓTESIS]; comparable: retainers de M&A pyme 1-10 k€ [VERIFICADO] |
| Inspección técnica previa | 1.200-2.500 € + desplazamiento | [HIPÓTESIS] |
| Representación de un vendedor con excedente recurrente | 5 % con exclusividad por zona, **por lote identificado**, nunca encargo abierto | Evita la recalificación como agencia (Ley 12/1992 art. 3.1 imperativo; STS 448/2014) [VERIFICADO] |

Ejemplos de ingreso: genset CAT 2.000 kVA usado 199.000 € → 8 % = 15.920 €. Excedente Kolektor 100 MVA 1,8 M€ → 8 % × 250 k + 6 % × 750 k + 4 % × 800 k = 20.000 + 45.000 + 32.000 = 97.000 €. Trafo usado 1 MVA a 19.000 € → mínimo 3.000 € (16 %): solo se acepta si alimenta la base de datos.

---

## 4. Operación de una transacción

Igual que la v1 (captación, registro, búsqueda, precualificación técnica, presentación anonimizada, acuerdo de comisión firmado, puesta en contacto, compraventa, factura 50 % a la firma y 50 % a la entrega), con estas correcciones verificadas:

- **Contrato**: mediación o corretaje, atípico; la comisión está bajo condición suspensiva de que se celebre la compraventa salvo pacto expreso (STS 174/2010, 348/2007) [VERIFICADO]. Cláusula de protección: exclusiva de 6 meses prorrogable con penalización del 100 % de honorarios tiene aval del Supremo (STS 10-05-2019) [VERIFICADO]; una cola de 18 meses es defendible por el art. 1255 CC pero no hay fuente que la llame habitual. Se pacta 12 meses.
- **Riesgo agencia**: un encargo estable con un vendedor recurrente se recalifica como agencia con indemnización por clientela de hasta una anualidad de comisiones (art. 28 Ley 12/1992) [VERIFICADO]. Se contrata por lote.
- **IVA**: comisión al 21 %; a empresario de otro Estado miembro, no sujeta en España, factura con mención "inversión del sujeto pasivo", NIF-IVA del cliente, modelo 349 y alta previa en ROI [VERIFICADO].
- **Due diligence**: transformadores según IEC 60076 con protocolo de ensayos; si se sustituyen núcleo y bobinas, hay que recalificar a Tier 2 (Reg. 2019/1783 art. 1.3) [VERIFICADO]. Celdas SF6: reinstalación intra-UE permitida; importadas, no [VERIFICADO]. Gensets usados ya en la UE: sin Stage V; importados móviles sin Stage V no se pueden introducir [VERIFICADO]. Legalización en España: certificado del instalador y registro en la CCAA (ITC-RAT 22); inspección inicial por OCA solo >30 kV (ITC-RAT 23) [VERIFICADO].
- **Transporte**: >45 t exige autorización complementaria específica o excepcional de la DGT, plazo máximo 3 meses más informes, tasa 132,72 €, autorizaciones separadas en Cataluña, País Vasco y Navarra [VERIFICADO]. Se avisa al comprador desde la primera llamada: un 40 MVA tarda un trimestre en moverse.
- **Aduanas**: solo UE. Fuera, arancel 3,7 % (0 % desde EE. UU., Reino Unido y Turquía) más la salvaguardia de 1.140 €/t de núcleo (28.000-34.000 € en un 40 MVA) [VERIFICADO].

---

## 5. Go-to-market

### 5.1 Capacidad de prospección (parámetros verificados)

- Por buzón: 20 correos fríos al día (mediana real 14, top 10 % ≥42, techo recomendado 50) [VERIFICADO, Smartlead]. Calentamiento 3 semanas y warm-up continuo (Warmup Inbox: 95 % → 98 % de bandeja en 2 semanas, convergencia en la semana 12) [VERIFICADO]. Sin píxel de apertura (quitarlo duplica la respuesta, 1,08 → 2,36 %, Snov 44 M) [VERIFICADO].
- 4 buzones en 2 dominios: 4 × 20 × 22 = 1.760 envíos al mes; secuencia de 3 pasos → ≈590 contactos nuevos al mes.
- LinkedIn: ≤80 invitaciones a la semana, aceptación 25-28 %, respuesta 10 % por mensaje a aceptados [VERIFICADO, Expandi 13,2 M invitaciones; SmartReach 6,7 M mensajes].

### 5.2 Embudo año 1, Iberia (cálculo)

Correo (universo ≈1.350 contactos, se agota en 3 meses; después Francia e Italia):
- 1.350 contactos × 2,5 % de respuesta = 34 respuestas [base; pes. 1 % = 13; opt. 5 % = 68].
- 40 % con necesidad o equipo concreto → 13,5 [Apollo marca ≥40 % de respuestas como positivas, VERIFICADO].

LinkedIn (48 semanas × 80 invitaciones = 3.840):
- 25 % aceptan = 960; 10 % responden = 96; 40 % concretas = 38.

Total necesidades y equipos concretos registrados en el año: ≈52 [base].
- Cruce viable (hay equipo compatible disponible): gensets 40 %, trafos y celdas 15 % → media ponderada 30 % → 15,5 cruces.
- Cierre de cruce viable: 33 % → **5 operaciones** [base]. Pesimista (respuesta 1 %, cruce 20 %, cierre 25 %): 2. Optimista (5 %, 40 %, 40 %): 10.

Lo que la prueba de 2 semanas mide con 100 correos: la tasa de respuesta (entre 1 y 5 %) y la proporción de respuestas con necesidad concreta. Con esas dos cifras, el embudo deja de ser hipótesis.

### 5.3 Mensaje

Posicionamiento: **"Ingeniero. Encuentro el genset o el transformador que te hace llegar a la fecha de conexión."** Hablar de fecha y de permiso que caduca, no de equipo. Remitente Jorge con nombre real, sin marca. Las dos plantillas de la v1 se mantienen con dos cambios: añadir "gensets de 1 a 3 MW en stock en Europa" en primera posición, y preguntar por "equipo pedido para un proyecto que se ha retrasado o cancelado" en el correo a vendedores.

### 5.4 Fases geográficas

- Meses 1-3: España y Portugal (1.350 contactos).
- Meses 4-12: Francia e Italia (mismo problema de plazos, misma normativa; universo estimado ×3-4 el ibérico [HIPÓTESIS]). Plantillas en francés e italiano; LinkedIn en inglés.
- Año 2: Alemania, Países Bajos y Bélgica solo como fuente de inventario (ahí están los traders), no como compradores.

---

## 6. Legal, fiscal y personal (verificado)

| Punto | Dato |
|---|---|
| Baja por IT | Trabajar por cuenta propia: subsidio "podrá ser denegado, anulado o suspendido" (art. 175.1.b LGSS); sanción LISOS: pérdida de 3 meses, con fraude 6 meses y exclusión 1 año; reintegro hasta 4 años |
| Permiso por nacimiento | Incompatible con trabajo por cuenta propia salvo pluriactividad previa (art. 180 LGSS); 19 semanas en 2026 |
| Qué se puede hacer durante la baja | Preparar: dominio, buzones, calentamiento, listas, modelo de contrato, alta censal 036 y ROI. La prueba de 2 semanas (100 correos de pregunta, sin facturar) es zona gris; la gestión activa de una operación con cobro, no |
| Forma | Autónomo, IAE grupo 511 (persona física, exenta de pago); SL cuando un cliente lo exija o la facturación supere 80.000 € [HIPÓTESIS el umbral] |
| Cuota | Año 1: cuota reducida de inicio (art. 38 ter LETA); importe 2026 no publicado en norma abierta, 80-90 €/mes en fuentes privadas [FRAGMENTO]. Año 2 con 66.550 € de rendimiento: tramo 11, ≈545,59 €/mes [VERIFICADO, Orden PJC/297/2026] |
| IRPF Madrid | 28,45 % efectivo sobre 66.550 € (18.934 €) [VERIFICADO] |
| IVA | 21 % nacional; intracomunitario B2B no sujeto, 349, ROI [VERIFICADO] |
| Seguro RC profesional | 200-400 €/año para 300-600 k€ de cobertura como consultoría o intermediación [VERIFICADO, Roams/ICEA feb-2026]; pedir tres cotizaciones describiendo "intermediación comercial sin ejecución ni certificación" |

---

## 7. Equipo

Jorge solo, 12 horas semanales en el año 1 (prospección 5 h, cualificación 3 h, llamadas 2 h, contratos y seguimiento 2 h). Año 2: apoyo a tiempo parcial (10-15 h/semana, 600-900 €/mes) para listas y seguimientos si el año 1 cierra ≥6 operaciones.

---

## 8. Finanzas

### 8.1 Costes fijos

| Partida | Año 1 | Año 2 | Fuente |
|---|---|---|---|
| Google Workspace, 4 buzones | 340 € | 340 € | 7 $/mes anual por buzón [VERIFICADO] |
| Warm-up, 4 buzones | 820 € | 820 € | 15-19,5 $/buzón/mes [VERIFICADO] |
| Apollo Professional | 950 € | 950 € | 79-99 $/mes [VERIFICADO] |
| Sales Navigator Core anual | 1.090 € | 1.090 € | 1.088,88 €/año [VERIFICADO] |
| Firma electrónica (Signaturit) | 420 € | 420 € | 35 €/mes [VERIFICADO] |
| Dominios (2) y web de una página | 150 € | 50 € | .com 15,95 €, .es 6,95 € [VERIFICADO] |
| Cuota de autónomos | 1.020 € | 6.550 € | 85 €/mes [FRAGMENTO]; 545,59 €/mes [VERIFICADO] |
| Gestoría | 900 € | 1.200 € | [HIPÓTESIS] |
| Seguro RC | 300 € | 300 € | [VERIFICADO rango] |
| Abogado: modelo de contrato | 600 € | 0 | [HIPÓTESIS] |
| Desplazamientos | 1.200 € | 2.400 € | [HIPÓTESIS] |
| Imprevistos 10 % | 780 € | 1.400 € | |
| **Total** | **≈8.600 €** | **≈15.500 €** | |

### 8.2 CAC

- Monetario: herramientas de prospección 3.770 €/año ÷ 5 operaciones = **754 € por operación** [base].
- Con tiempo a 50 €/h [HIPÓTESIS]: 12 h × 48 semanas = 576 h → 28.800 €; (3.770 + 28.800) ÷ 5 = **6.514 € por operación**, frente a 21.000 € de ingreso medio: ratio 3,2. En el pesimista (2 operaciones): 16.285 € por operación frente a 12.000 € de ingreso: el negocio no paga el tiempo. Esa es la frontera, y se conoce en el día 14 por la tasa de respuesta.

### 8.3 Escenarios

Ver tabla de cabecera. Año 2 asume Francia e Italia y ticket estable. Punto de equilibrio sobre fijos: 8.600 ÷ 21.000 = 0,4 operaciones. El riesgo nunca es de caja; es de tiempo del fundador y de calendario personal.

---

## 9. Riesgos

| Riesgo | Probabilidad | Mitigación |
|---|---|---|
| Tasa de respuesta ≤1 % | Media (es la mediana del mercado) | Listas <200 muy segmentadas, sin píxel, 3 pasos, LinkedIn en paralelo, llamada a los que abren; se mide en el día 14 |
| Sin excedentes de proyecto accesibles | Media-alta | Arrancar con gensets, donde el inventario existe; pivote a agente de compras con retainer |
| Traders del norte (Koopmann, BTB) abren comercial ibérico | Media | Velocidad y base de datos propia; acuerdo de colaboración con uno de ellos como fuente |
| Salvaguardia 1.140 €/t se hace definitiva y sube | Media | Ya se opera solo intra-UE |
| Recalificación como agencia | Baja si se contrata por lote | Contrato por equipo identificado |
| Incompatibilidad con la baja | Alta si se gestiona una operación con cobro antes de terminarla | Solo preparación y prueba durante la baja; primer cierre después |
| Rodeo | Media | Anonimato hasta firma; exclusiva 6-12 meses con penalización (STS 10-05-2019) |
| Transporte de un 40 MVA bloquea la entrega | Media | Avisar del plazo de 3 meses de la DGT en la primera llamada; preferir equipos <45 t en el año 1 |

---

## 10. Plan de 90 días

**Días 1-21 (durante la baja, sin facturar):** gestoría (fecha fin de baja, compatibilidad, 036 y ROI); 2 dominios y 4 buzones con SPF, DKIM, DMARC y warm-up; listas ibéricas (900-1.300 compradores, 65-195 vendedores) desde la sesión local de Apollo y Sales Navigator; modelo de contrato con abogado; perfil de LinkedIn reorientado.

**Días 22-35 (prueba):** 100 correos (50 compradores, 50 vendedores) a 20 por buzón y día, seguimiento al día 4; 80 invitaciones de LinkedIn a la semana. Pedir tres ofertas de trafos 10-40 MVA usados a Koopmann, Trafo-City y BTB para fijar el precio que la investigación no encontró. Decisión día 35: tasa de respuesta ≥2,5 % y ≥5 necesidades concretas → seguir; 1-2,5 % → seguir solo con gensets y LinkedIn; <1 % → cerrar o pivotar a agente de compras.

**Días 36-90:** escalar a 590 contactos nuevos al mes; primer cruce y acuerdo de comisión firmado; contratar seguro RC; empezar Francia e Italia en el día 90. Si la baja ha terminado: cerrar la primera compraventa y facturar el 50 %. Si no: pipeline en espera con fecha.

KPI día 90: tasa de respuesta medida sobre ≥500 correos; ≥25 necesidades y ≥10 equipos registrados; ≥1 acuerdo de comisión firmado; 3 precios de trafos 10-40 MVA obtenidos.

---

## 11. Decisiones de continuación y cierre

| Momento | Señal | Decisión |
|---|---|---|
| Día 35 | Respuesta ≥2,5 % y ≥5 necesidades concretas | Seguir con el plan completo |
| Día 35 | Respuesta 1-2,5 % | Seguir solo gensets + LinkedIn; recortar Sales Navigator si LinkedIn no aporta |
| Día 35 | Respuesta <1 % | Cerrar (gasto <1.000 €) o pivotar a agente de compras con retainer |
| Día 90 | Ningún acuerdo de comisión firmado | Extender 60 días solo si hay ≥2 cruces en negociación |
| Mes 12 | <3 operaciones | Cerrar o dejar en modo oportunista sin herramientas de pago |
| Mes 12 | ≥6 operaciones | Apoyo a tiempo parcial, SL, Alemania y Países Bajos como fuente |

---

## 12. Lo que sigue siendo hipótesis y cómo se resuelve

| Hipótesis | Cómo se resuelve | Cuándo |
|---|---|---|
| Tasa de respuesta de compradores ibéricos (1-5 %) | 100 correos de la prueba | Día 35 |
| Comisión 8/6/4 % aceptada | Tres primeros acuerdos firmados | Día 90-180 |
| Precio de trafos usados 10-40 MVA | Tres ofertas a traders alemanes y finlandés | Día 35 |
| Existencia de excedentes de proyecto accesibles | Respuestas de EPC y promotores a la pregunta directa | Día 35-90 |
| Cuota reducida de autónomos 2026 | Gestoría o publicación en BOE | Día 21 |
| Universo francés e italiano | Sondeo gratuito en Apollo | Día 60 |
