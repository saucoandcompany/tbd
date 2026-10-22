# Herramientas y regulación técnica — verificación adversarial (H19–H25)

Fecha de consulta: 22-10-2026 (todas las páginas abiertas ese día desde la sesión, con Chromium/Playwright vía proxy).
Convención: **[ABIERTA]** = página oficial abierta y texto copiado; **[FRAGMENTO]** = sólo parte visible (p. ej. precio en JSON/acordeón, no en la vista principal); **NO ENCONTRADO** = no se pudo confirmar en fuente oficial.
Volcados completos de cada página en `/tmp/claude-0/-home-user-tbd/637262f0-646e-586f-83ef-8ef9d5653ca7/scratchpad/brk/pages/` (los `n_*.txt` son copias normalizadas de EUR-Lex/BOE).

---

## H19. Costes de herramientas

Hipótesis: Workspace 7 €/mes · Apollo 50–100 $/mes · Sales Navigator Core 90–110 €/mes · warm-up 20–40 €/mes · firma 0–15 €/mes · dominio 10–20 €/año.

| Herramienta | Precio oficial copiado (22-10-2026) | Estado | Veredicto vs hipótesis |
|---|---|---|---|
| **Google Workspace** (Business Starter, 1 usuario) | Centro de ayuda oficial (support.google.com/a/answer/1247360, es): «Pago mensual Business Starter: 8,4 USD por usuario … Business Starter: 7 USD por usuario [plan anual]… Pago anual … Business Starter: 84 USD por usuario … Total anual Business Starter: 100,8 USD por usuario». La página workspace.google.com/intl/es/pricing no renderizó las tarjetas de precio en headless (sólo «Todos los precios $», «Anual (ahorra un 16 % con un compromiso de 1 año)», «Todos los planes se facturan mensualmente»). | [ABIERTA] (ayuda) / [FRAGMENTO] (pricing) | **Parcialmente**: 7 $/mes sólo con compromiso anual; flexible 8,4 $/mes. El precio en € para España no se pudo leer → usar 7–8,4 €/mes como orden de magnitud (NO ENCONTRADO el € exacto). |
| **Apollo.io** | apollo.io/pricing (en): JSON-LD oficial de la página: Free «price: 0»; «Basic Plan … price: 49 … billingIncrement: Monthly»; «Professional Plan … price: 99 … Monthly»; «Enterprise Plan … Contact for pricing». Tarjetas renderizadas: «Basic $49», «$79» (Professional), «Organization $119», con etiquetas «/month», «per user», «billed annually» (precios con facturación anual; la FAQ dice «Facturación mensual: … El coste efectivo mensual es mayor»). | [ABIERTA] (texto FAQ) + [FRAGMENTO] (precios) | **Confirmada**: tarjetas con facturación anual Basic 49 $ / Professional 79 $ / Organization 119 $ por usuario/mes; el JSON-LD oficial da Basic 49 y Professional 99 (Monthly). Precio de Basic con facturación mensual sin compromiso: NO ENCONTRADO en el texto renderizado (la FAQ sólo dice que es «mayor»). Rango 50–100 $ correcto. |
| **LinkedIn Sales Navigator Core** | business.linkedin.com/es/es/sell/sales-navigator/compare-plans, FAQ «¿Cuánto cuesta LinkedIn Sales Navigator?» (acordeón): Core «EUR: 120,99 EUR/mes o 1.088,88 EUR/año» (= 90,74 €/mes anual); Advanced «EUR: 148,21 EUR/mes o 1.693,88 EUR/año»; Core USD «119,99 USD/mes o 1.079,88 USD/año». Página advierte que precios «pueden no incluir IVA». | [ABIERTA] / [FRAGMENTO] (acordeón) | **Corregir**: 90–110 € sólo si se paga el año (90,74 €/mes); mensual = 120,99 €/mes + IVA. |
| **Instantly** | instantly.ai/pricing: «Growth $47/monthly … Unlimited Email Accounts, Unlimited Email Warmup, 1000 Uploaded Contacts, 5000 Emails Monthly»; «Hypergrowth $97/monthly … 125 000 Emails Monthly»; «Light Speed $358/monthly». | [ABIERTA] | Warm-up incluido en el plan de envío (no hay plan sólo-warmup). 47 $/mes > hipótesis 20–40 €. |
| **lemlist** | lemlist.com/pricing: «Email … $69 / $55 / MONTH … 50,000 emails/mo»; «Multichannel … $109 / $87 / MONTH»; tabla: «Email From $55 /mo», «Multichannel From $87 /mo» (precio tachado = mensual, menor = anual). Incluye «Email warm-up & Deliverability hub». | [ABIERTA] | 55–69 $/mes por usuario; fuera del rango 20–40 €. |
| **MailReach** | mailreach.co/pricing (es): «Selecciona el número de buzones a calentar … $ 19.5 / buzón al mes»; toggles «Mensual / Anualmente — Ahorra 20%»; «Nuestro plan de email warmer siempre incluye al menos 20 créditos de spam tests». | [ABIERTA] | **Confirmada** para 1 buzón: ≈19,5–25 $/mes. |
| **Warmup Inbox** | warmupinbox.com/pricing: «Basic $15 /inbox/mo … $15 /mo for 1 inbox … $180 billed yearly»; otros tiers «$49 /inbox/mo … $588 billed yearly» y «$79 /inbox/mo … $948 billed yearly»; «Annual plans … save you 20% versus monthly». | [ABIERTA] | **Confirmada**: 15 $/buzón/mes. |
| **Smartlead** | smartlead.ai/pricing: «Base $32 /month … 2,000 contacts, 6,000 Email sends»; «Pro $78 /month … 90,000 Email sends»; «Unlimited Smart $144 /month»; «Unlimited Prime $315 /month»; «Warmup Pool» incluido; buzones propios «$4.5/mailbox/month … $13/domain/year». | [ABIERTA] | Base 32 $/mes (anual) ≈ hipótesis. |
| **DocuSign** | docusign.com/pricing (US): «Personal $11 /month … annual commitment of $132 … Send 5 envelopes per month»; «Standard $30 /user/month … $360»; «Business Pro $45 /user/month … $540». Página es-es/precios → 404. | [ABIERTA] | Personal 11 $/mes (5 sobres/mes). Rango 0–15 sólo con Personal. |
| **Signaturit** | signaturit.com/es/precios: «Business … 35€ … 516 € 420 € por usuario y año … Hasta 60 envíos al año»; «Business+ … 57€ … 864 € 684 € por usuario y año … Hasta 240 envíos al año … Firma cualificada»; «Business 35€ por usuario al mes»; «(Servicio no disponible para Consumidores)». | [ABIERTA] | **Refuta** 0–15 €/mes para Signaturit: 35–57 €/usuario/mes. |
| **Dropbox Sign** | sign.dropbox.com/products/dropbox-sign/pricing: «Essentials $15 USD / mo»; «Standard $25 USD / user / mo» (toggles «Billed monthly / Billed yearly»); «Premium Get a custom quote». | [ABIERTA] | 15 $/mes (Essentials). |
| **Dominio .com / .es** | dondominio.com/products/domains/com/: «Registro … 15,95 €», «Renovación … 15,95 €», «Transferencia 1 año(s) 15,95 €»; /es/: «Registro … 6,95 €», «Renovación … 6,95 €», «Transferencia 0,00 €». porkbun.com/products/domains: «.com $11.08» (registro/renovación/transfer). Cloudflare Registrar (products/registrar) no publica precios en la página. | [ABIERTA] | **Confirmada**: 7–16 €/año. |

**Veredicto H19:** parcialmente confirmada. Correctos: dominio (7–16 €/año), warm-up si se usa herramienta dedicada (MailReach/Warmup Inbox 15–25 $/buzón/mes), Apollo Basic 49 $/mes (anual) y Workspace ≈7–8,4 $/mes. **Corregir**: Sales Navigator Core 120,99 €/mes mensual (90,74 €/mes sólo anual, sin IVA); firma electrónica 11–15 $/mes (DocuSign Personal, Dropbox Sign Essentials), pero Signaturit (español, firma cualificada) 35–57 €/mes; plataformas de outreach completas (Instantly 47 $, lemlist 55–69 $, Smartlead 32 $) incluyen warm-up y sustituyen a la herramienta de warm-up. Presupuesto realista stack mínimo 1 persona: ≈ 8 + 59 + 121 + 25 + 11 ≈ 225 $/€ al mes (vs ≈ 180 € de la hipótesis), o ≈ 195 €/mes con todo anual.

---

## H20. Reglamento (UE) 2024/573 (gases fluorados) y aparamenta SF6 usada

Fuente: EUR-Lex CELEX 32024R0573 (ES) [ABIERTA].

**Hallazgo clave: el anexo IV NO contiene ninguna entrada de aparamenta eléctrica.** Las prohibiciones de aparamenta están en el **art. 13, apdo. 9**, y recaen sobre la «puesta en funcionamiento», no sobre la venta:

> Art. 13.9: «Se prohibirá la puesta en funcionamiento de la siguiente aparamenta eléctrica que use gases fluorados de efecto invernadero, o cuyo funcionamiento dependa de ellos, en un medio aislante o de ruptura:
> a) a partir del 1 de enero de 2026, aparamenta eléctrica de media tensión para distribución primaria y secundaria de hasta 24 kV;
> b) a partir del 1 de enero de 2030, aparamenta eléctrica de media tensión para distribución primaria y secundaria de más de 24 kV hasta 52 kV, inclusive;
> c) a partir del 1 de enero de 2028, aparamenta eléctrica de alta tensión a partir de 52 kV hasta 145 kV, inclusive, y hasta 50 kA, inclusive, de corriente de cortocircuito, con un potencial de calentamiento global igual o superior a 1;
> d) a partir del 1 de enero de 2032, aparamenta eléctrica de alta tensión de más de 145 kV o más de 50 kA de corriente de cortocircuito, con un potencial de calentamiento global igual o superior a 1.»

> **Art. 13.10** (segunda mano intra-UE): «No se considerará puesta en funcionamiento a efectos del presente artículo la desactivación de aparamenta eléctrica que esté en funcionamiento en la Unión y la posterior puesta en funcionamiento de esa aparamenta eléctrica en un lugar diferente de la Unión.»

> Art. 13.14: «El apartado 9 no se aplicará cuando el operador pueda aportar pruebas de que el pedido de la aparamenta eléctrica es anterior a 11 de marzo de 2024.»
> Art. 13.15: excepción para ampliaciones de aparamenta existente cuando los dispositivos sin F-gas «no sean compatibles con la aparamenta eléctrica existente».
> Art. 13.18: «Podrán instalarse partes de los aparatos para su reparación o revisión de la aparamenta eléctrica existente, siempre que no se produzca ningún cambio en el tipo de gases fluorados … o … un aumento de la cantidad de gases fluorados …».
> Art. 13.7: «A partir del 1 de enero de 2035, se prohibirá el uso del SF6 para el mantenimiento o revisión de aparamenta eléctrica a menos que se regenere o recicle…».
> Art. 13.11–12: excepciones vía licitación pública sin ofertas sin F-gas (2 años) o PCG < 1 000.

Definiciones (art. 3): «"introducción en el mercado": el despacho a libre práctica en la Unión o el suministro o puesta a disposición de otra persona en la Unión, por primera vez…». No existe definición de «puesta en funcionamiento» en el art. 3 (NO ENCONTRADO); el considerando 21 habla de prohibir «la puesta en funcionamiento de nueva aparamenta eléctrica».

Art. 11.1 (anexo IV): «Se prohibirá la introducción en el mercado de productos y aparatos, incluidas sus partes, enumerados en el anexo IV…»; «Un año después de las fechas individuales enumeradas en el anexo IV, el posterior suministro … de productos o aparatos introducidos en el mercado de manera lícita antes de la fecha … únicamente se permitirá si se aportan pruebas de que el producto o aparato se introdujo en el mercado lícitamente antes de dicha fecha.» → aplica a refrigeración/espumas/etc., no a celdas (no están en el anexo IV).

TARIC (22-10-2026, código 8504 22 90, Turquía) muestra la medida «Control de las importaciones de gases fluorados de efecto invernadero (02-07-2026 - ) (CD917) R0573/24» con la nota: «En virtud del artículo 11, apartado 1, párrafo segundo … se permitirá la introducción en el mercado de partes de productos y aparatos necesarias para la reparación y la revisión de los aparatos existentes enumerados en el anexo IV.» (control documental aduanero, no prohibición).

**Veredicto H20:** fechas y tensiones **confirmadas** (2026 ≤24 kV; 2028 52–145 kV; 2030 24–52 kV; 2032 >145 kV o >50 kA), pero la hipótesis ubica mal la norma: no es el anexo IV sino el art. 13.9, y prohíbe **poner en funcionamiento**, no vender. **Celdas SF6 usadas ya en servicio en la UE** pueden desmontarse, revenderse y reinstalarse en otro lugar de la UE (art. 13.10) y repararse (13.18). **Celdas SF6 importadas de fuera de la UE** (nuevas o usadas) no están cubiertas por 13.10 → su puesta en funcionamiento queda prohibida según las fechas de 13.9 (salvo excepciones 13.11–15). La reventa de celdas ≤24 kV usadas sin origen UE acreditado es, desde el 1-1-2026, un producto sin salida legal en la UE.

---

## H21. Ecodiseño de transformadores: Reglamento (UE) 548/2014 modificado por (UE) 2019/1783

Fuentes: EUR-Lex CELEX 32014R0548 y 32019R1783 (ES) [ABIERTA].

> Art. 1.1 (texto 2019/1783): «En el presente Reglamento se exponen los requisitos de diseño ecológico que deben cumplirse para introducir en el mercado o poner en servicio transformadores de potencia de una potencia mínima asignada de 1 kVA utilizados en redes de transmisión y distribución eléctrica de 50 Hz o para aplicaciones industriales. El presente Reglamento se aplicará a los transformadores adquiridos después del 11 de junio de 2014.»
> Art. 1.2: exclusiones, entre ellas e) «transformadores diseñados especialmente para una situación temporal en la que se interrumpe el suministro normal de energía debido a un suceso imprevisto … o un reacondicionamiento de la estación, pero no para una mejora permanente de una subestación existente».
> **Art. 1.3 (reparados):** «Los transformadores de potencia medianos y grandes, con independencia de cuándo se hayan introducido en el mercado o puesto en servicio por primera vez, deberán ser sometidos a una reevaluación de la conformidad y cumplir el presente Reglamento si son objeto de todas las operaciones siguientes: a) sustitución del núcleo o de parte de él; b) sustitución de una o varias bobinas completas.»
> Considerando 2019/1783: «La existencia de un mercado para la reparación de transformadores hace necesario proporcionar orientación sobre las circunstancias en las que un transformador que ha sido sometido a determinadas operaciones de reparación debe considerarse equivalente a un producto nuevo…»
> Anexo I: «2.ª etapa (1 de julio de 2021)»; excepciones Tier 1 cuando la sustitución «conlleve costes desproporcionados asociados a su transporte o instalación, o sea técnicamente inviable».
> Definiciones 2019/1783 art. 2: «"transformador de potencia mediano": … potencia asignada inferior o igual a 3 150 kVA y una tensión más elevada para los equipos superior a 1,1 kV e inferior o igual a 36 kV»; «"transformador de potencia grande": … potencia asignada superior a 3 150 kVA o bien una tensión … superior a 36 kV».
> 548/2014 art. 2: «"transformador de potencia": aparato estático con dos o más bobinas que, por inducción electromagnética, transforma un sistema de tensión y corriente alternas en otro…».

**Veredicto H21:** Tier 2 desde 1-7-2021 **confirmado**. Alcance = «introducir en el mercado o poner en servicio» + «transformadores adquiridos después del 11 de junio de 2014». Un transformador **usado ya introducido/puesto en servicio en la UE** y revendido sin cambiar núcleo ni bobinas completas **no** requiere reevaluación (art. 1.3 a contrario; coherente con la Guía Azul, que limita la legislación de armonización a la primera introducción). Si se **rebobina y cambia núcleo (ambas)** debe cumplir Tier 2. Un transformador **usado importado de fuera de la UE** es primera introducción en el mercado de la Unión → debe cumplir Tier 2 (lectura literal del art. 1.1 + Guía Azul 2.1/2.5; no hay exención de segunda mano en el reglamento) — salvo que el contrato de adquisición original sea anterior al 11-6-2014, caso dudoso que el texto no resuelve expresamente.

---

## H22. DBT 2014/35/UE, Reglamento de Máquinas 2023/1230 y Guía Azul 2022: ¿nuevo CE para usado?

Fuentes: EUR-Lex CELEX 32014L0035 (ES), 32023R1230 (ES), 52022XC0629(04) Guía Azul 2022 (EN) [ABIERTA].

**Directiva 2014/35/UE**, art. 1: «La presente Directiva se aplicará al material eléctrico destinado a utilizarse con una tensión nominal comprendida entre 50 y 1 000 V en corriente alterna y entre 75 y 1 500 V en corriente continua…» → un transformador de potencia MT/AT (>1 000 V) **queda fuera** de la DBT por tensión (le aplica ecodiseño 548/2014 y, en su caso, EMC). Art. 2: «"introducción en el mercado": la primera comercialización de material eléctrico en el mercado de la Unión»; «"importador": toda persona física o jurídica establecida en la Unión que introduzca en el mercado de la Unión material eléctrico de un tercer país».

**Reglamento (UE) 2023/1230**, art. 3: «"introducción en el mercado": la primera comercialización de un producto … en el mercado de la Unión»; «"puesta en servicio": la primera utilización de una máquina … en la Unión de acuerdo con su uso previsto»; «"modificación sustancial": una modificación de una máquina …, después de que … se haya introducido en el mercado o puesto en servicio, que no haya sido prevista o planificada por el fabricante y que afecte a la seguridad … al generar un nuevo peligro o aumentar un riesgo existente, lo cual exija: a) la incorporación de resguardos o dispositivos de protección … que necesite la modificación del sistema de control de seguridad existente, o b) la adopción de nuevas medidas de protección para garantizar la estabilidad o la resistencia mecánica…». Considerando 10: «El presente Reglamento debe aplicarse a los productos que constituyan una novedad en el mercado de la Unión en el momento de introducirse en este, y que sean o bien productos nuevos fabricados por un fabricante establecido en la Unión o bien productos, nuevos o de segunda mano, importados de un tercer país.»

**Guía Azul 2022**, §2.1 «Product coverage»: «The Union harmonisation legislation applies to newly manufactured products but also to used and second-hand products, including products resulting from the preparation for re-use of electrical or electronic waste, imported from a third country when they enter the Union market for the first time. This applies even to used and second-hand products imported from a third country that were manufactured before the legislation became applicable.» … «Products which have been repaired (for example following a defect), without being considered as new products do not need to undergo conformity assessment again, whether or not the original product was placed on the market before or after the legislation entered into force. This applies even if the product has been temporarily exported to a third county for the repair operations.»
§2.3: «Used products, which are on the Union market, are subject to free movement according to the principles laid down by Articles 34 and 36 TFEU.»
§2.5: «Union harmonisation legislation applies to products outside the Union when they are made available on the Union market for the first time; not only to newly manufactured products but also to used and second-hand products …, but not to such products already on the EU market.» … «Furthermore, a person who places on the Union market second-hand products from a third country, or any product not designed or manufactured for the Union market, must assume the role of the manufacturer.»
§2.6: «Unless otherwise provided for in specific Union legislation, where products have been placed on the market in compliance with the Union harmonisation legislation applicable at that time, they can also be put into service even if that legislation has been amended…».

**Veredicto H22:** **Confirmada con matices.** (a) Genset o transformador BT usado **ya en el mercado UE**: no requiere nuevo marcado CE si no sufre «modificación sustancial» (2023/1230) y sólo se repara. (b) Usado **importado de fuera de la UE**: es primera introducción → el importador/bróker «must assume the role of the manufacturer» (declaración UE de conformidad, expediente técnico, CE conforme a la legislación vigente hoy, p. ej. 2023/1230 desde 20-1-2027 y Stage V). (c) Transformadores >1 kV: fuera de la DBT; su «CE» viene por ecodiseño (548/2014) y EMC, no por la DBT.

---

## H23. Emisiones gensets (Reglamento (UE) 2016/1628, Stage V) y legalización en España (RD 337/2014 / REBT)

Fuente: EUR-Lex CELEX 32016R1628 (ES) [ABIERTA].

> Art. 2.1: «El presente Reglamento se aplica a todos los motores que entran dentro de las categorías establecidas en el artículo 4, apartado 1, que estén instalados o destinados a ser instalados en máquinas móviles no de carretera…». Art. 2.2: «El presente Reglamento no se aplica a los siguientes tipos de motores: … d) motores de máquinas estacionarias».
> Art. 3.36: «"máquina estacionaria": una máquina destinada a ser instalada de forma permanente en un lugar durante su primer uso y no destinada a moverse, por carretera ni en otro medio, salvo durante el envío desde el lugar de fabricación al lugar de su primera instalación».
> Art. 3.35: «"grupo electrógeno": una máquina móvil no de carretera independiente que no forma parte de un grupo motopropulsor, destinada primordialmente a generar electricidad». Art. 4.1.2: «"categoría NRG": motores con una potencia de referencia igual o superior a 560 kW destinados exclusivamente al uso en grupos electrógenos; los motores para grupos electrógenos distintos … se incluyen en las categorías NRE o NRS».
> Art. 3.48: «"introducción en el mercado": la primera comercialización en la Unión de un motor o máquina móvil no de carretera». Art. 3.51: «"importador": toda persona … que introduce en el mercado un motor desde un país tercero, con independencia de que el motor esté ya instalado o no en una máquina móvil no de carretera».
> Art. 3.11: «"motor de sustitución": un motor que: a) se utiliza exclusivamente para sustituir un motor ya introducido en el mercado e instalado en una máquina móvil no de carretera, y b) se ajusta a una fase de emisiones inferior a la aplicable en la fecha en que se sustituye el motor».
> Anexo III, cuadro III-1 (NRE): introducción en el mercado de motores: «1 de enero de 2019» (0–56 kW) y 1 de enero de 2020 (56–560 kW y >560 kW); transitorios art. 58.5–7: motores de transición hasta 18 meses (24–36 meses en casos especiales) desde esas fechas. Art. 58.10–11: motores de sustitución autorizados «por un período no superior a 15 años» (NRS ≥19 kW / NRG) y «no superior a 20 años» (otros, bajo condiciones).

**Veredicto H23 (Stage V):** **Corregida.** El reglamento se aplica a la **primera introducción en el mercado** del motor/máquina: un genset usado **ya en servicio en la UE** puede revenderse sin Stage V (no hay retroactividad; reglas de sustitución de motor en art. 58.10–11). Un genset **importado de fuera de la UE** (nuevo o usado) con motor sin homologación Stage V **no puede introducirse** en el mercado si es móvil (incl. en contenedor/remolque, NRE/NRG), salvo que sea una «máquina estacionaria» (art. 2.2.d: instalación permanente en su primer uso, sólo se mueve del fabricante al lugar de instalación) — nota: un genset usado trasladado ya no cumple literalmente «desde el lugar de fabricación al lugar de su primera instalación», lo que hace frágil la vía «estacionario» para usados importados. Para gensets estacionarios aplican además la Directiva de Emisiones Industriales/MCP (2015/2193) por instalación, no verificada aquí.

**España — RD 337/2014 (RAT) e ITC-RAT 22/23** (BOE-A-2014-6084 consolidado) [ABIERTA]:
> ITC-RAT 23 §3: «Todas las instalaciones de alta tensión deben ser objeto de una verificación previa a la puesta en servicio y de una inspección periódica, al menos cada tres años. … Las instalaciones de tensión nominal superior a 30 kV deberán ser objeto, también, de una inspección inicial antes de su puesta en servicio.» «Las verificaciones previas a la puesta en servicio … deberán ser realizadas por las empresas instaladoras que las ejecuten.» «…los agentes que lleven a cabo las inspecciones de las instalaciones deberán tener la condición de organismos de control, acreditados para este campo reglamentario.»
> ITC-RAT 22: «Las instalaciones de tensión nominal superior a 30 kV deberán ser objeto de la correspondiente Inspección Inicial por Organismo de Control, según lo establecido en la ITC-RAT 23. Finalizadas las obras y realizadas las verificaciones e inspección inicial …, la empresa instaladora deberá emitir un Certificado de Instalación, según modelo establecido por la Administración pública…». «Antes de la puesta en servicio de la instalación, el titular de la misma deberá presentar ante la Administración pública competente, al objeto de su inscripción en el correspondiente registro, el certificado de instalación…».
> ITC-RAT 23 §3.2.1: «En la inspección inicial se comprobará que los ensayos a realizar por la empresa instaladora … se ejecutan correctamente … También se comprobará que existe coincidencia entre las condiciones reales de la instalación y las condiciones de cálculo del proyecto…».
El RD 337/2014 **no contiene** ninguna regla específica sobre transformadores «de segunda mano» o «usados» (búsqueda de «segunda mano», «usados», «reutiliz»: sin resultados) → la legalización se hace como instalación nueva/modificación: proyecto (si procede), certificado de instalación del instalador AT, inspección inicial por OCA sólo si >30 kV (si ≤30 kV: verificación del instalador + inspección periódica trienal), registro en la CCAA. Para el equipo en sí no se exige marcado, pero el proyecto debe acreditar características (ensayos/placa).

**REBT RD 842/2002, ITC-BT-05 §4.1** [ABIERTA]: «Serán objeto de inspección inicial … a) Instalaciones industriales que precisen proyecto, con una potencia instalada superior a 100 kW»; «Se entenderá por modificaciones o reparaciones de importancia, a los efectos de … la obligatoriedad de inspección inicial, a las que afectan a más del 50 por 100 de la potencia instalada»; inspecciones periódicas «cada 5 años». Art. 18/19: «la empresa instaladora … emitirá un certificado de instalación … deberá depositarse ante el órgano competente de la Comunidad Autónoma».

**Veredicto H23 (España):** **Confirmada**: OCA inicial obligatoria en AT >30 kV (y en BT industrial >100 kW con proyecto); siempre certificado de instalador habilitado + registro autonómico; en AT ≤30 kV basta verificación del instalador.

---

## H24. Aduanas: arancel TARIC 2026 y medidas de defensa comercial

Fuente: TARIC (ec.europa.eu/taxation_customs/dds2/taric), fecha de referencia «22-10-2026», «Última actualización de TARIC: 22-10-2026» [ABIERTA, 16 consultas].

| Código | Descripción TARIC | Derecho terceros países | EE. UU. | Turquía | China | Reino Unido |
|---|---|---|---|---|---|---|
| 8504 21 00 00 | Transformadores de dieléctrico líquido ≤650 kVA | «3.70 %» (R2261/98) | «Preferencias arancelarias (01-07-2026 - ): 0 % (CD01100) R1455/26» | — (no consultado; igual que 8504 22) | 3,70 % | — |
| 8504 22 90 00 | 1 600–10 000 kVA | 3,70 % | — | «Derechos establecidos por la unión aduanera (01-01-2006 - ): 0 % D0142/96» | — | — |
| 8504 23 00 00 | >10 000 kVA | 3,70 % | 0 % (pref. 01-07-2026, R1455/26) | — | 3,70 % (sin antidumping) | «Preferencias arancelarias (01-01-2021 - ): 0 %» (ACC UE-RU, origen preferencial) |
| 8502 13 40 90 | Gensets diésel 750–2 000 kVA | «2.70 %» (R1719/05) | 0 % (pref. 01-07-2026) | 0 % (unión aduanera) | 2,70 % | 0 % (pref.) |

Notas literales: CD01100 (EE. UU.): «el origen de las mercancías se determinará de conformidad con las normas relativas al origen no preferencial … hasta que se adopten las normas de origen preferencial». Suspensiones a 0 % para «productos destinados a ciertas clases de buques y de plataformas» y «aeronavegabilidad».

**Medida nueva y decisiva (todas las líneas 8504 21/22/23):** «Países sujetos a derechos compensatorios — GOES, Laminations and Cores (SAFEGT GOES SLCs 5009) · Derechos adicionales (25-09-2026 - ) (TM01085) · R2133/26 · Excepto Brasil (BR)». Nota TM01085: «Se introduce un derecho de salvaguardia provisional en relación con las importaciones en la Unión de laminados y núcleos de acero, apilados o enrollados, clasificados actualmente en el código NC 8504 90 13, incorporados o no a transformadores, clasificados en los códigos NC 8504 21 00, 8504 22 10, 8504 22 90, 8504 23 00, 8504 31 21, 8504 31 29, 8504 31 80, 8504 32 00, 8504 33 00 y 8504 34 00. … El importe del derecho de salvaguardia provisional aplicable a las laminaciones y núcleos de acero … cuando estén incorporados en transformadores, será de 1 140 EUR por tonelada incorporada en el transformador. Los agentes económicos declararán el peso en toneladas de un núcleo en un transformador utilizando la unidad de medida TNEO.»

**Reglamento de Ejecución (UE) 2026/2133** (EUR-Lex CELEX 32026R2133, ES) [ABIERTA]: art. 1.3: «Se introduce un derecho provisional de salvaguardia sobre las importaciones en la Unión de laminaciones y núcleos de acero … estén incorporados o no en transformadores … durante un período de 155 días naturales a partir de la entrada en vigor»; art. 1.6: «…será de 1 140 EUR por tonelada del producto … tal y como se incorpore al transformador … Los productos … cuando se incorporan a transformadores … no están sujetos a contingentes»; art. 6: «…los derechos antidumping [2022/58] no se percibirán durante el período de aplicación del presente Reglamento, porque son inferiores a los derechos provisionales de salvaguardia»; art. 7: «El presente Reglamento entrará en vigor el 25 de septiembre de 2026.» (Hecho en Bruselas el 18-9-2026). Considerando: «…las medidas de salvaguardia provisionales debían aplicarse efectivamente al producto afectado cuando se incorpora a productos derivados, es decir, a transformadores … El núcleo de acero se incorpora al transformador pero no se absorbe, por lo que puede identificarse en un transformador.» Es una salvaguardia **erga omnes** (excepto Brasil y, en 7225, EAU/Turquía por lista de países en desarrollo): afecta a transformadores de **EE. UU., Reino Unido, Turquía y China** por igual, nuevos **y usados** (el texto no distingue), vigente hasta ≈ 27-2-2027 salvo medida definitiva.

**Antidumping GOES — Reglamento de Ejecución (UE) 2022/58** (CELEX 32022R0058) [ABIERTA]: art. 1.1: «Se establece un derecho antidumping definitivo en relación con las importaciones de los productos laminados planos de acero magnético al silicio, de grano orientado, de un grosor superior a 0,16 mm, … códigos TARIC 7225110011, 7225110015 y 7225110019 … que sean originarios de la República Popular China, Japón, la República de Corea, la Federación de Rusia y los Estados Unidos de América.» Art. 1.3 precios mínimos de importación: «2 043 … 1 873 … 1 536» EUR/t según pérdidas en el núcleo; art. 1.4 derechos ad valorem de respaldo: Baoshan 21,5 %, Wuhan 36,6 %, JFE 39,0 %, Nippon Steel 35,9 %, POSCO 22,5 %, NLMK/VIZ 21,6 %, AK Steel 22,0 %. Hecho el 14-1-2022 (vigencia ordinaria 5 años → enero 2027). Alcance: **sólo chapa GOES (7225/7226), no transformadores terminados**; en TARIC 7225 11 00 11 (China, 22-10-2026) la medida AD no aparece activa — está suspendida por el art. 6 de 2026/2133 mientras rige la salvaguardia (además: «Mecanismo de Ajuste en Frontera por Carbono - CBAM (01-01-2026 - 31-12-2026)» y «Control a la importación (19-12-2023 - 31-12-2027) R0833/14 excepto Rusia»).

**Veredicto H24:** **Corregida/ampliada.** Arancel base 3,7 % (transformadores) y 2,7 % (gensets) confirmados; 0 % para Turquía (unión aduanera), Reino Unido (origen preferencial ACC) y **EE. UU. desde 1-7-2026** (R1455/26). No hay antidumping UE sobre transformadores terminados; el AD GOES (2022/58) es sobre chapa. **Pero desde 25-9-2026 existe una salvaguardia provisional de 1 140 €/t de núcleo sobre todo transformador importado (incl. usados, incl. EE. UU./UK/TR/CN)**: un 40 MVA con ~25–30 t de núcleo paga ≈ 28 000–34 000 € extra, lo que destruye el margen de importación de usados fuera de la UE mientras dure.

---

## H25. Transporte especial en España (transformador 40 MVA, 60–80 t)

Fuentes: dgt.es «Solicitud Autorización Complementaria de Circulación» (actualización «30/01/2026») y «Comunicación de inicio de viaje ACC»; BOE RD 2822/1998 Reglamento General de Vehículos [ABIERTA].

> RGV art. 14.2: «El órgano competente en materia de tráfico podrá conceder autorizaciones especiales y por un número limitado de circulaciones o por un plazo determinado, previo informe vinculante del titular de la vía, para los vehículos que, por sus características técnicas o por la carga indivisible que transportan, superen las masas y dimensiones máximas…». «…se entiende por carga indivisible aquella que para su transporte por carretera no puede dividirse en dos o más cargas sin coste o riesgo innecesario de daños…».
> DGT: «Los vehículos que superen los valores máximos de masas y dimensiones establecidos en el reglamento general de vehículos podrán circular previa solicitud de una Autorización Complementaria de Circulación (ACC).»
> Categorías (Grupo 1, VERTE): «Genérica, cuando el conjunto y su carga no supere los 20,55×3×4,5 m …, 45 T de masa total de conjunto…»; «Específica, cuando … supera alguno de los valores … y en ningún caso excede los 40×5×4,70 m … y las 110 T de masa total de conjunto»; «Excepcional, cuando el conjunto y su carga rebasa alguno de los valores máximos … considerados para las ACC de categoría específica.»
> **Plazos:** «El vehículo para el que se pide la autorización, no podrá iniciar ningún viaje hasta que haya obtenido la autorización. El plazo máximo de tramitación de la solicitud y entrega de la resolución al interesado será de 3 meses contados a partir del momento de la solicitud. De este plazo máximo se descontará el tiempo que tarden en emitir informe los titulares de la vía… El plazo máximo para que los titulares de las vías informen será de tres meses.»
> **Tasas:** «Coste del trámite: 132,72€ TIPO DE TASA: 1.3»; duplicado «20,81€ TIPO DE TASA: 4.4». Comunicación de inicio de viaje: «Coste del trámite: Gratuito».
> «No se puede pedir una prórroga de vigencia de las autorizaciones concedidas y solamente será posible pedir una nueva ACC.» «En ningún caso se podrá pedir una modificación del itinerario aprobado.»
> Competencia: DGT salvo País Vasco (Gobierno Vasco), Navarra (excepto AP-68), Cataluña (SCT; «A partir de [1-5-2024], las autorizaciones concedidas por la Dirección General de Tráfico no serán válidas para circular por las vías de Cataluña») y cascos urbanos (ayuntamientos).
> Inicio de viaje: «Deberán comunicar el inicio de viaje, todos los VERTEs que … precisen una ACC de categoría específica o excepcional.» «La comunicación de inicio de viaje deberá ser hecha con una antelación mínima de 24 horas al inicio de cada viaje, salvo que el conjunto precise algún tipo de acompañamiento por agentes de la autoridad o vaya a circular en auto-escolta.» «La solicitud del acompañamiento o auto-escolta deberá ser hecha con una antelación mínima de 72 horas…». «Estudios para la solicitud de conjuntos en orden de marcha que excedan las 300 toneladas» (estudio de viabilidad).

**Veredicto H25:** **Confirmada y cuantificada.** Un transformador de 40 MVA (60–80 t) sobre góndola supera con holgura las 45 t de la ACC genérica → **ACC específica** (hasta 110 t / 40×5×4,70 m) o excepcional si el conjunto rebasa esos valores; plazo legal de resolución hasta **3 meses** (descontando informes de titulares de vía, que a su vez tienen hasta 3 meses), tasa 132,72 €, comunicación de inicio de viaje ≥24 h (≥72 h con escolta), posibles escoltas/auto-escolta y estudios de viabilidad para estructuras. Un business plan debe reservar 2–3 meses de lead time para el transporte nacional del equipo (más si cruza Cataluña/País Vasco: autorizaciones separadas).

---

## Resumen de veredictos

| H | Veredicto |
|---|---|
| H19 | Parcial: dominio, warm-up dedicado, Apollo Basic y Workspace OK; Sales Navigator (120,99 €/mes mensual) y firma (Signaturit 35 €+) infravalorados. |
| H20 | Fechas/tensiones OK pero la norma es art. 13.9 (puesta en funcionamiento), no anexo IV; usado intra-UE reinstalable (13.10); importado de fuera UE prohibido según fechas. |
| H21 | Tier 2 OK; usado intra-UE sin reevaluación salvo cambio de núcleo + bobinas (art. 1.3); usado importado = primera introducción → Tier 2. |
| H22 | Guía Azul: usados ya en UE libres; usados importados → el importador asume el rol de fabricante y CE actual; transformadores >1 kV fuera de la DBT. |
| H23 | Stage V sólo a la primera introducción (usados UE libres; importados móviles bloqueados); España: OCA inicial AT >30 kV, certificado de instalador siempre. |
| H24 | 3,7 %/2,7 % base; 0 % US (desde 1-7-2026), TR, UK; sin AD sobre transformadores; **salvaguardia 1 140 €/t de núcleo desde 25-9-2026 sobre todo transformador importado**. |
| H25 | ACC específica/excepcional, hasta 3 meses, 132,72 €, aviso 24/72 h. |

---

## Tabla de URLs abiertas (22-10-2026)

| # | URL | Estado | Uso |
|---|---|---|---|
| 1 | https://workspace.google.com/intl/es/pricing | 200, tarjetas no renderizadas (sólo texto marco) | H19 |
| 2 | https://workspace.google.com/pricing | 200, idem | H19 |
| 3 | https://workspace.google.com/intl/de/pricing | 200, idem | H19 |
| 4 | https://support.google.com/a/answer/1247360?hl=es | 200, precios USD | H19 |
| 5 | https://www.apollo.io/pricing | 200 (es y en) | H19 |
| 6 | https://business.linkedin.com/es/es/sell/sales-navigator/compare-plans | 200 (precios en FAQ) | H19 |
| 7 | https://business.linkedin.com/es-es/sales-solutions/compare-plans | 200 | H19 |
| 8 | https://instantly.ai/pricing | 200 | H19 |
| 9 | https://www.lemlist.com/pricing | 200 | H19 |
| 10 | https://www.mailreach.co/pricing | 200 | H19 |
| 11 | https://www.warmupinbox.com/pricing | 200 | H19 |
| 12 | https://www.smartlead.ai/pricing | 200 | H19 |
| 13 | https://www.docusign.com/pricing | 200 (es-es/precios → 404) | H19 |
| 14 | https://www.signaturit.com/es/precios | 200 | H19 |
| 15 | https://sign.dropbox.com/products/dropbox-sign/pricing | 200 | H19 |
| 16 | https://www.dondominio.com/products/domains/com/ y …/es/ | 200 | H19 |
| 17 | https://porkbun.com/products/domains | 200 | H19 |
| 18 | https://www.cloudflare.com/products/registrar/ | 200, sin precios | H19 |
| 19 | https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32024R0573 | 202→render OK | H20 |
| 20 | https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32014R0548 | OK | H21 |
| 21 | https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32019R1783 | OK | H21 |
| 22 | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52022XC0629(04) | OK (Guía Azul 2022) | H22 |
| 23 | https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32014L0035 | OK | H22 |
| 24 | https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32023R1230 | OK | H22 |
| 25 | https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32016R1628 | OK | H23 |
| 26 | https://www.boe.es/buscar/act.php?id=BOE-A-2014-6084 (RD 337/2014) | 200 | H23 |
| 27 | https://www.boe.es/buscar/act.php?id=BOE-A-2002-18099 (RD 842/2002) | 200 | H23 |
| 28 | https://ec.europa.eu/taxation_customs/dds2/taric/measures.jsp?Lang=es&SimDate=20261022&Area=US&Taric=8504210000 (+ US/GB/CN 8504230000, TR 8504220000/8504229000, CN/US/GB/TR 8502134090, CN/JP 7225110000/7225110011, CN 8504901300/8504901310) | 200 ×16 | H24 |
| 29 | https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32022R0058 | OK | H24 |
| 30 | https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32026R2133 | OK | H24 |
| 31 | https://www.dgt.es/nuestros-servicios/autorizaciones-obras-y-usos-excepcionales-de-la-via/autorizaciones-especiales-de-circulacion/autorizaciones-complementarias-de-circulacion-para-vertes/solicitud-autorizacion-complementaria-de-circulacion/ | 200 | H25 |
| 32 | https://www.dgt.es/…/autorizaciones-complementarias-de-circulacion-para-vertes/comunicacion-de-inicio-de-viaje-acc/ | 200 | H25 |
| 33 | https://www.boe.es/buscar/act.php?id=BOE-A-1999-1826 (RD 2822/1998, RGV) | 200 | H25 |

No encontrado / no abierto: precio en € de Google Workspace para España (tarjetas JS no renderizadas); página de precios DocuSign en español (404); Access2Markets (no necesario, TARIC consultado directamente); páginas de la sede DGT (404 en rutas probadas; se usó dgt.es). WebSearch agotado tras 2 consultas (presupuesto compartido), por lo que todo lo anterior se obtuvo por apertura directa.
