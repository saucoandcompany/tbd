# Herramientas odiadas con disparador 2026-2027: veredicto del barrido

Fecha: 23-10-2026. Encargo de Jorge: encontrar "el Google Analytics de tu mundo" para un micro-SaaS autoservicio construido con Claude Code, sin reuniones ni llamadas, precio objetivo 35-50 €/mes. Filtro de muerte acordado: (1) keyword con intención y volumen medible, (2) CPC plausible ≤3 €, (3) precio 35-50 €/mes sostenible frente a lo que ya existe, (4) disparador con fecha oficial en 2026-2027, (5) construible por una persona con IA en menos de 8 semanas.

Cinco investigadores en paralelo (ingeniería e industria; pyme y autónomo en España; fin de soporte y subidas de precio; regulación UE; minería de quejas en Reddit, Hacker News, Trustpilot y Capterra). Más de 700 páginas o llamadas de API abiertas en total. Notas con tablas de URLs en `research_notes/Herramientas odiadas con disparador 2026-2027/`.

Convenciones: [ABIERTA] página leída; [FRAGMENTO] solo fragmento de buscador o tercero; [INTERNO] Planificador de Google Ads de tu cuenta, sesión local del 4-10-2026; "sin dato" cuando no hay cifra verificable.

---

## 0. Resumen en diez líneas

1. Ningún candidato pasa limpio el filtro de muerte. El mejor puntúa 7 sobre 10 y los siguientes 6.
2. La criba de volumen y CPC no se pudo hacer: Google Trends devolvió 429 en todos los intentos de los cinco investigadores y Semrush, Ahrefs, SpyFu, Ubersuggest, AlternativeTo y G2 bloquearon. Solo hay cuatro CPC reales, los de tu Planificador.
3. Las fechas sí están verificadas en DOUE, BOE o web del fabricante, y varias que dábamos por buenas estaban mal (sección 3).
4. La ola de un disparador dura un mes en el incumbente y de dos a siete meses en los sustitutos. Solo VMware tras Broadcom lleva más de 30 meses viva, porque el disparador es escalonado.
5. Los casos de éxito de fundadores solos contra un incumbente odiado existen y están medidos con Stripe, pero todos atacan a un incumbente grande y empiezan a precio bajo o gratis. Ninguno a 35-50 €/mes. Ninguno en España.
6. El precio de 35-50 €/mes solo es "mitad de precio" frente a incumbentes de 70 €/mes o más. Frente a Holded, Quipu, Contasimple, Calendly o Clockify sería más caro que el incumbente.
7. El dolor más intenso y diario encontrado (sedes electrónicas, Cl@ve, Autofirma, notificaciones de varias administraciones) no se puede construir en 8 semanas: no hay API para pequeños destinatarios y el portal rechaza acceso automatizado.
8. El único candidato con cero competencia autoservicio en español y fecha dura es el expediente CE de máquinas (20-01-2027), con el problema de que casi nadie lo busca todavía y de que es el comprador de Normach.
9. El análogo real más cercano al patrón Plausible es francés: Khosmos, un fundador solo, facturación para artesanos montada sobre la factura electrónica obligatoria en Francia, 22.236 $ de MRR medidos por Stripe. En España ese disparador acaba de moverse a 2027-2028 y ya hay más de doce herramientas a 0-20 €/mes.
10. Siguiente paso que no cuesta dinero: pasar 40 keywords por tu Planificador (fichero `prompts/Prompt sesion local - Planificador herramientas odiadas.md`). Sin ese dato, construir cualquiera de estos es apostar a ciegas.

## 1. Tabla consolidada de candidatos

Puntuación 0-10 según el filtro de muerte, asignada por cada investigador y revisada aquí. "Volumen" y "CPC" son "sin dato" salvo que se indique [INTERNO].

| # | Candidato | Fila | Disparador y fecha oficial | Quién paga | Competencia autoservicio | Precio de mercado | Volumen / CPC | Construible en 8 semanas | Nota |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Expediente técnico, evaluación de riesgos y declaración UE de máquinas | Ingeniería | Reg. 2023/1230 aplicable **20-01-2027** (corrección DOUE 04-07-2023, EUR-Lex) | Fabricantes de maquinaria, integradores, retrofits | 0 en español; UE: Safexpert 99-264 €/mes, WEKA 2.799 €, CEM4 980 €; plantillas Euronorm 45-75 € | 39-49 €/mes defendible | "reglamento de máquinas 2027" <10/mes [INTERNO]; "marcado ce" plano en Trends; TÜV SÜD paga anuncios | Sí, 6-8 semanas; riesgo de responsabilidad normativa y derechos de normas UNE | **7/10** |
| 2 | Software CBAM para importadores pyme de acero, aluminio, cemento, fertilizantes | Regulación UE | Certificados desde 01-02-2027; primera declaración anual **30-09-2027** (Reg. 2025/2083 arts. 6.1 y 22.1); umbral 50 t | Importadores pyme | 39 proveedores, 9 con precio (79-145 €/mes pyme o 1.990-2.990 €/año), 2 españoles sin precio | 35-50 €/mes sería el más barato | sin dato | Sí; pero el Registro CBAM de la Comisión es gratis y los valores por defecto bastan a los pequeños; verificador externo obligatorio (art. 8) | 6/10 |
| 3 | Buzón único de notificaciones electrónicas con plazos y avisos para micro-SL | Pyme España | Operativo, no legal: TGSS pasa a buzón electrónico para autónomos (año sin verificar); AEAT 10 días y la notificación se da por hecha | Autónomo societario, micro-SL | Servicio humano a 19,95 € + IVA/mes (Ayuda T Pymes); enterprise sin precio (DEH Online, a3 Portal NEOS); avisos oficiales gratis | Techo 20 €/mes con 1 NIF | sin dato | **No**: DEHú sin API para pequeños, WAF comprobado, custodia de certificados; variante sin custodia sí | 6/10 |
| 4 | Panel multi-NIF para microgestorías (notificaciones, caducidad de certificados, calendario) | Pyme España | Ventana 2027-2028 de factura electrónica y Verifactu obliga a la gestoría a reorganizar cada cliente | Gestorías de 5-30 clientes | Solo dentro de ERP grandes; ningún autoservicio con tarjeta encontrado | 39-79 €/mes coherente (la gestoría cobra 65 €/mes por autónomo) | sin dato | Mismo cuello de botella técnico que el 3 | 6/10 |
| 5 | Planificador de salida de VMware para MSP: importa RVTools, compara coste de renovación con Proxmox, XCP-ng, Hyper-V, genera plan | Fin de soporte | vSphere 8 fin de soporte **11-10-2027** (Broadcom); disparador escalonado desde dic-2023 | MSP y pymes con virtualización | Calculadoras de Nutanix y Vates, RVTools e importador de Proxmox, todos gratis | 49 €/mes o 149 €/informe | Autocompletado "alternativa a vmware" y "migrar de vmware" 10/10 en ES y EN; CPC esperado >3 € (sin verificar) | Sí | 6/10 |
| 6 | Marcado y medición de planos PDF frente a Bluebeam | Minería | Fin de venta de Bluebeam 2018-20 el 31-07-2026 y fin de soporte **31-12-2026** (nemetschek/bluebeam.com) | Oficinas técnicas, construcción | Capterra 4,7 con 978 reseñas: usuario satisfecho, no odiado | Bluebeam 260-440 $/año; 35-50 €/mes plausible | "alternative to bluebeam" 10 sugerencias en EN, 0 en ES | Sí (PDF.js) | 6/10 |
| 7 | Expediente anexo VII y declaración anexo VIII del Reglamento de envases | Regulación UE | PPWR aplicable **12-08-2026**; etiquetado 12-08-2028 | Marcas y ecommerce con envase propio | 15 herramientas; PPWR Connect ya en español a 29 €/mes | 29 €/mes ya ocupado | sin dato | Sí; presión del Consejo (09-10-2026) sobre la responsabilidad ampliada, no sobre los anexos | 5/10 |
| 8 | Pasaporte digital de baterías con QR | Regulación UE | Reg. 2023/1542 arts. 77.1 y 13.6: **18-02-2027**; registro operativo 20-07-2026 | Fabricantes e importadores de baterías >2 kWh | DPP-Tool 29 €/mes, Batteriepasswerk gratis | 29 €/mes ya ocupado | sin dato | Sí, pero ESPR art. 10.4 prevé certificación de prestadores | 5/10 |
| 9 | Autoauditoría de licencias Autodesk y Adobe antes de la carta de cumplimiento | Fin de soporte | Sin fecha; cartas "License Compliance and Audit engagement" continuas | Pymes con CAD y diseño | Flexera, Snow, Licenseware (enterprise) | 249 € por auditoría más natural que 39 €/mes | sin dato | Sí | 5/10 |
| 10 | Radar de renovaciones y fin de soporte con "alternativa europea" | Fin de soporte | M365 +12-33 % desde 01-07-2026 [FRAGMENTO]; Office 2021 13-10-2026; Server 2016 12-01-2027; SAP ECC 31-12-2027 | Pymes de 10-50 puestos | endoflife.date gratis; Cledara 75 £/mes | 35 €/mes | Keyword casi inexistente | Sí | 5/10 |
| 11 | Gestión de calibraciones (sustituye al Excel de calidad) | Ingeniería | Ninguno con fecha | Responsables de calidad ISO 9001 | GageList 0-249 $, Gaugify 0-499 $; 0 en español | 35-50 €/mes frente a 70-79 $ de pago | sin dato | Sí, 4-6 semanas | 5/10 |
| 12 | Conector de factura electrónica B2B vía solución pública | Pyme España | RD 238/2026 y Orden HAC/1028/2026: >8 M€ hacia **06-10-2027**, resto hacia **06-10-2028** | Pymes proveedoras de grandes | ≥12 herramientas lo incluirán; AEAT promete formulario gratuito; plataformas privadas exigen ISO 27001 (art. 13) | 0-20 €/mes de mercado | "factura electrónica obligatoria" −89 % interanual [INTERNO] | Sí como cliente de la solución pública, no como plataforma | 5/10 |
| 13 | Comprobador "Verifactu-ready" | Fin de soporte | BOE dice 01-01-2027 y 01-07-2027, pero Hacienda anunció el 05-10-2026 aplazarlo a octubre de 2028, sin BOE | Pymes y gestorías | Saturado; app gratuita de la AEAT | 0-20 €/mes | 40.500/mes, −63 %, puja 4,99 € [INTERNO] | Sí | 5/10 |
| 14 | Plataforma de cursos frente a Kajabi | Minería | Subida ene-feb 2026 a 179/249/499 $ y recorte de contactos 10.000→2.500 | Creadores | Teachable, Podia, Thinkific, Hotmart en español | Trustpilot 3,4 con 2.347 reseñas; hueco a 35-50 € real pero saturado | sin dato | Sí | 5/10 |
| 15 | Formularios frente a Typeform | Minería | Ninguno 2026-2027 | Pymes, marketing | Tally ya lo hizo: 6 M$ ARR a precio 0-29 $ | Más caro que el sustituto que ya ganó | sin dato | Sí | 4/10 |
| 16 | Agenda para salones y fitness frente a Mindbody | Minería | Reestructuración feb-2026 | Salones, estudios | Fresha, Acuity, Vagaro a 24-30 $ | Hueco ya ocupado | sin dato | Sí | 4/10 |
| 17 | Libro de mantenimiento digital e inspecciones OCA | Ingeniería | Borrador del REBT con contrato de mantenimiento obligatorio, sin fecha ni texto aprobado | Mantenedores, titulares | 0 productos; tampoco evidencia de dolor | sin dato | sin dato | Sí | 4/10 |
| 18 | Facturación para autónomos frente a Holded, Quipu, Contasimple | Minería | Verifactu desplazado a 2028 | Autónomos | ≥8 apps indie lanzadas en r/autonomos en 12 meses; mercado 8,5-29 €/mes | Más caro que el incumbente | "alternativa a holded" existe en autocompletado ES | Sí | 3/10 |

Descartados por los investigadores con motivo: CMMS (MaintainX y UpKeep a 0-24 $, saturado); Autodesk, SOLIDWORKS, EPLAN y visores DWG (no construibles por una persona); cálculo eléctrico en Excel (sin fecha, CYPE y dmELECT, responsabilidad); registro único de alquileres turísticos (anulado por tres sentencias del Supremo publicadas en el BOE el 08-06, 26-06 y 18-07-2026); registro horario digital (sin Real Decreto; dictamen del Consejo de Estado 19-03-2026); Ley 10/2025 de atención a la clientela (solo ≥250 trabajadores); accesibilidad web (ya aplicable, microempresas de servicios exentas, 119 herramientas); cookies (274 CMP registradas en TCF); EUDR (sistema gratuito y declaración simplificada); GPSR (persona responsable es una entidad jurídica, servicio y no software); AI Act (alto riesgo aplazado); RGPD (Facilita de la AEPD gratis); cuota de autónomos (anual, simuladores gratis).

## 2. Lo que el barrido enseña sobre el patrón Plausible

**La ola es corta.** Medido en vistas de Wikipedia: Skype pasó de 149.000 a 54.000 vistas en un mes tras el anuncio de cierre; Windows 10 de 151.000 a 60.000; la versión en español de 22.000 a 6.000. Los sustitutos (Zorin, Mint, Affinity) mantuvieron la atención 2-7 meses. Solo VMware tras Broadcom dura más de 30 meses, con 130 hilos en r/sysadmin y picos de 1.700-2.700 votos, porque las renovaciones vencen escalonadas. Lección: un disparador con una sola fecha te da un trimestre de pico; después el negocio es de régimen y vive del mismo SEO lento que cualquier otro.

**El patrón funciona contra grandes, a precio bajo.** Diez casos con ingresos medidos por Stripe en TrustMRR o autopublicados: Chatbase 863.632 $ MRR contra Intercom; Postiz 307.051 $ contra Buffer; Simple Analytics 37.527 $ contra Google Analytics con 3 personas; Liinks 31.329 $ contra Linktree con un fundador y planes de 5-12 $; Tally 6 M$ ARR contra Typeform con planes de 0-29 $; Senja 50.000 $ MRR; Testimonial.to 100.000 $ ARR en 9 meses en solitario. Todos atacan a un incumbente grande con el ángulo gratis, abierto, privado o simple, y ninguno empezó en 35-50 €/mes. El precio que fijamos ayer para que cuadre el CAC de pago choca con el único patrón que ha demostrado funcionar sin pagar tráfico.

**El dolor no se compra solo con software.** Lo más odiado en España son las sedes electrónicas y sus apps: Autofirma 2,2 estrellas con 5.280 reseñas, Cl@ve 3,2 con 32.400, Notifica App 3,6 con 2.920. Pero el Estado no se sustituye, DEHú no da API a pequeños destinatarios y el portal bloquea el acceso automatizado. La capa de pago que existe es humana, a 19,95 € + IVA al mes. Si se construye algo aquí es un panel de plazos y recordatorios sin custodia, no un buzón.

**El análogo más cercano es Khosmos.** Un fundador solo en Francia, facturación para artesanos construida sobre la obligación francesa de factura electrónica, 842 suscripciones y 22.236 $ de MRR medidos por Stripe. España tiene ahora el mismo disparador en BOE (RD 238/2026 y Orden HAC/1028/2026), pero con fechas en octubre de 2027 y 2028, más de doce herramientas a 0-20 €/mes, ocho apps indie lanzadas en un año en r/autonomos y la keyword principal cayendo un 89 % interanual. Llegas tarde al precio y pronto a la fecha.

## 3. Fechas verificadas que corrigen lo que decíamos

| Disparador | Lo que dábamos por bueno | Lo verificado el 23-10-2026 | Fuente |
|---|---|---|---|
| Reglamento de Máquinas 2023/1230 | 14-01-2027 | **20-01-2027** | Corrección de errores DOUE 04-07-2023, EUR-Lex CELEX 32023R1230R(01) [ABIERTA] |
| AI Act alto riesgo | 02-08-2026 | **02-12-2027 y 02-08-2028** | Reg. 2026/1744 (Ómnibus), DOUE 24-07-2026 [ABIERTA] |
| Verifactu | 2027 | BOE: 01-01-2027 y 01-07-2027 (RD 1007/2023 DF 4ª, RDL 15/2025); nota del Ministerio de Hacienda 05-10-2026 anuncia **octubre de 2028**, sin BOE | BOE-A-2025-25695; nota ministerial [ABIERTA] |
| Factura electrónica B2B | Sin reglamento | **Aprobado**: RD 238/2026 (BOE 31-03-2026) y Orden HAC/1028/2026 (BOE 05-10-2026); grandes hacia 06-10-2027, resto hacia 06-10-2028 | BOE [ABIERTA] |
| Registro horario digital | En trámite | Sin aprobar; dictamen Consejo de Estado 19-03-2026 | [ABIERTA] |
| Registro único de alquileres turísticos | Obligatorio desde 01-07-2025 | **Anulado** por tres sentencias del Supremo (BOE 08-06, 26-06 y 18-07-2026) | BOE [ABIERTA] |
| Windows 10 ESU consumidor | Hasta 13-10-2026 | Ampliado hasta **12-10-2027** | microsoft.com [ABIERTA] |
| Data Act | Obliga a fabricantes | Aplicable 12-09-2025, pero **exime a micro y pequeñas empresas** (art. 7.1) | EUR-Lex [ABIERTA] |
| CBAM | Régimen definitivo 01-01-2026 | Certificados desde 01-02-2027; primera declaración anual 30-09-2027; umbral 50 t | Reg. 2025/2083 [ABIERTA] |
| Bluebeam 2018-20 | — | Fin de venta 31-07-2026; fin de soporte 31-12-2026 | bluebeam.com [ABIERTA] |
| QuickBooks Online | — | Subidas del 13-24 % en renovaciones desde 01-08-2026 | swktech.com [ABIERTA] |
| Microsoft 365 | — | +12-33 % desde 01-07-2026 | The Register 05-12-2025 [FRAGMENTO, pendiente de la nota oficial] |

## 4. Lo que te diría si tuviera que elegir hoy

**Ninguno pasa limpio, y el que más se acerca es el que vetaste.** El expediente CE de máquinas tiene fecha dura, cero competencia autoservicio en español y un precio defendible. También tiene el comprador de Normach, una ventana de tres meses y menos de diez búsquedas al mes para la keyword del disparador. Si lo descartas por ser Normach, la lista de 6/10 queda así:

1. **Panel multi-NIF para microgestorías**, variante sin custodia de certificados: plazos, lectura asistida del PDF de la notificación que sube el usuario, caducidad de certificados FNMT con 60 días de aviso, calendario fiscal por cliente. Precio 39-79 €/mes por despacho. Es el único con dolor diario documentado, precio sostenible y comprador que paga sin llamada si hay prueba gratuita. No se puede medir su demanda con lo que tenemos.
2. **Planificador de salida de VMware** para MSP a 49 €/mes o 149 € por informe. Único disparador de larga duración medido. El CPC previsible es alto y la competencia gratuita es de Nutanix y Proxmox; el valor está en el informe comparado, no en la herramienta.
3. **Software CBAM pyme** a 35-50 €/mes, el más barato de los 39 que hay. Fecha dura 30-09-2027, pero el registro gratuito de la Comisión cubre a los pequeños.

**Antes de escribir una línea de código, 30 minutos en tu Planificador.** He dejado la lista de 40 keywords agrupadas por candidato en `prompts/Prompt sesion local - Planificador herramientas odiadas.md`. El criterio de corte está en el fichero: volumen ES ≥200/mes en el bloque y puja superior ≤3 €. Con ese dato se cae la mitad de la tabla y lo que quede se puede probar con una landing y 300 € de anuncios, que ayer vimos que mide poco pero mide algo si la keyword es transaccional.

**Y la pregunta incómoda.** Los diez casos que funcionaron atacan a un gigante con precio bajo o gratis y tardaron años. Nuestra condición de 35-50 €/mes nació para que cuadre el CAC de pago porque no quieres reuniones ni escribir contenido. Las dos cosas no caben a la vez: o aceptas el precio bajo y el tiempo del patrón Plausible, o aceptas el precio alto y el canal de pago con sus 240 € de CAC y payback de 5-7 meses. Lo que no existe en los datos es precio alto, sin tráfico pagado, sin voz y rápido.

## 5. Confianza y límites

- Alta: fechas de la tabla 3 marcadas [ABIERTA]; ingresos de los casos medidos por Stripe en TrustMRR; precios públicos de competidores; puntuaciones de las apps oficiales en Google Play.
- Media: puntuaciones 0-10 (criterio de cada investigador, sin volumen ni CPC); duración de ola medida con vistas de Wikipedia como proxy de interés.
- Baja o nula: volumen de búsqueda y CPC de todas las keywords salvo cuatro [INTERNO]; año exacto del paso de la TGSS al buzón electrónico; cifra "41 % de errores en DEHú" (blog, no oficial); nota oficial de la subida de Microsoft 365.
- Errores corregidos en esta sesión: fecha del Reglamento de Máquinas (dos veces mal antes de verificarla en EUR-Lex); estado del registro horario, del registro de alquileres y de la factura electrónica.
