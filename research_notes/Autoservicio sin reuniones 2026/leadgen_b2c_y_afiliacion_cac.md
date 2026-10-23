# Webs de captación B2C (leads a profesionales y afiliación CPA): CAC frente a ingreso por lead

Fecha: 23-10-2026. Investigador adversarial. Fila: (a) venta de leads de particulares por unidad a profesionales/plataformas (modelo Habitissimo, Cronoshare, Certicalia…); (b) afiliación/CPA con redes (Awin, Adtraction, Tradedoubler, TimeOne, Daisycon, TradeTracker…) donde el anunciante paga por lead o por venta.
Contexto del encargo: negocio 100 % solo con IA, sin capital, sin ninguna reunión de venta (solo correo como mucho). Métrica central: coste por lead (CPC / conversión) frente a precio de venta del lead. Escenarios de anuncios: 300 / 1.000 / 2.000 €/mes.

Convenciones: [ABIERTA] = página abierta y leída en esta sesión (pwfetch, curl, navegador headless o WebFetch); [FRAGMENTO] = cifra vista solo en un extracto de buscador o citada por una página que no es la fuente original; NO ENCONTRADO = se buscó y no apareció; "sin dato" = no hay cifra pública verificable. Toda cifra lleva moneda, fecha de consulta (23-10-2026 salvo fecha de publicación indicada) y URL. Los supuestos propios van marcados con asterisco (*). Semrush publica el CPC en USD; donde se convierte a euros se aplica 0,90 €/USD como supuesto*.

Páginas solicitadas: 96 URLs (tabla en §6); 61 devolvieron contenido útil. Herramientas de CPC por keyword (Semrush Keyword Overview, Ahrefs Keyword Generator, Ubersuggest, KeywordTool, Seobility, SE Ranking) bloquean el CPC sin cuenta: el CPC España por keyword exacta queda "sin dato" salvo las muestras públicas de Semrush "website overview" (top 5 keywords orgánicas por dominio, USD, septiembre 2026). Trustpilot solo se abrió con navegador headless; Gowork y Certicalia (profesionales) quedaron tras Cloudflare; Reddit (arctic-shift) no tiene hilos relevantes sobre Habitissimo/Cronoshare en r/spain, r/es, r/askSpain, r/autonomos ni r/SpainFIRE.

---

## 0) Veredictos H1–H7

| Hipótesis | Veredicto | Resumen de la evidencia |
|---|---|---|
| H1. Habitissimo/Cronoshare cobran al profesional 2–40 € por contacto según categoría | **CORREGIDA** | Habitissimo (centro de ayuda, actualizado 13-10-2026): "el trabajo medio cuesta 12 €", 1 de cada 10 solicitudes se convierte en trabajo, precio según tipo de trabajo, oferta/demanda y **"coste de adquisición del contacto: invertimos en marketing"**; precios dinámicos dentro de un rango. Ejemplos oficiales (calculadora): con 300 € en Madrid, 9 contactos de Reformas de Viviendas (**33,3 €/contacto**) o 24 de Reformas de Cocinas (**12,5 €**); 100 contactos ≈ 1.222 € (12,2 €); inversión mínima 75 €. Reseñas: 47 € por 2 contactos (23,5 €; Trustpilot, 22-09-2026); Portugal "a partir de 7 € cada contacto" (Portal da Queixa, 15-05-2026). El rango observado es **7–33 €**, no 2–40 €, y cada solicitud se vende hasta a **4 profesionales** (ingreso por solicitud para la plataforma hasta ~4×). Cronoshare: paga por contacto en "cronos" (comisión + gastos de gestión), recarga mínima 0,15 €, **importe por contacto no público**; un profesional declara >150 € gastados (Gowork, 2023, [FRAGMENTO]). Categorías caras confirmadas: reformas de viviendas/integrales (33 €). Placas solares, abogados, residencias, seguros, préstamos: **sin precio público por lead en plataformas españolas**. |
| H2. CPC Google Ads España para las keywords objetivo | **SIN DATOS (parcial) / CORREGIDA** | Ninguna herramienta gratuita da CPC España por keyword. Muestras públicas Semrush (España, sep-2026, USD): "comparador seguros coche" 27.100 búsquedas, **7,15 $**; "reforma cerca de mi" 3.600, **2,40 $**; "placas solares" 22.200, 0 $ (sep-2026; 122.200 y 2,68 $ en la instantánea de nov-2025 [FRAGMENTO]); "cedula de habitabilidad" 6.600, 1,38 $; "empresas de limpieza" 4.400, 1,19 $; "brackets" 18.100, 2,79 $; "blanqueamiento dental" 18.100, 0,90 $; "abogado penalista" 6.600, 5,26 $ (SEOJuice [FRAGMENTO]). Referencia sectorial EE. UU. (WordStream, abr-2025→mar-2026): abogados 9,87 $, hogar/reformas 8,33 $, dentistas 8,00 $, finanzas/seguros 3,39 $. "abogado herencias", "mudanzas madrid", "residencia de ancianos madrid", "seguro de salud", "certificado energetico precio", "presupuesto reforma": **sin dato** de CPC España. Un blog de agencia afirma que España va un 20–40 % por debajo de EE. UU. "sin dato primario publicado" (lionelz.com, abr-2026). |
| H3. Conversión landing→lead 5–15 % | **CORREGIDA** | Unbounce (Conversion Benchmark Report 2024, 57 M conversiones): mediana general **6,6 %**; legal 6,3 % (búsqueda de pago 8,3 %); servicios comerciales/profesionales 6,1 % (búsqueda de pago 7,8 %; "reparación y mantenimiento convierte casi 3× mejor que reformas"); finanzas/seguros 6,7 % (búsqueda de pago 10,1 %, seguros 8,3 %); Google paid search 11,3 % de media (todas las industrias). WordStream 2026 (búsqueda): hogar/reformas **8,05 %**, abogados **5,55 %**, finanzas/seguros **2,64 %**, dentistas 10,67 %, servicios personales 12,34 %. Rango realista para una landing nueva: **3–8 %**; 10–15 % solo en lo mejor del percentil. |
| H4. Comisiones CPA/CPL públicas en España y aceptación de afiliados nuevos | **CORREGIDA** | Payouts públicos son escasos y bajos: Gana Energía (BlueAff, abierto) **2,2 $/lead + 14 $/venta**, ~10 % lead→venta; Aon ES CPL **3,5 €/lead** (cerrado, [FRAGMENTO]); iSalud CPL (Adstrategy, abierto) importe no publicado; Holaluz CPL (Adstrategy, abierto) importe no publicado; Allianz Assistance ES (Awin) **8 % CPA** solo seguro de viaje; Lampara ES (Awin) 5–8 % CPO. Daisycon no lista campañas españolas de seguros/energía/alarmas (Verisure 50 € es Bélgica). Adtraction ES: directorio dominado por préstamos rápidos y banca (Moneyman, Vivus, Cofidis, Bankinter…), más Prima Seguros, Life5, Santalucía Fondos y Sicor Teleasistencia, sin comisión visible sin cuenta. Afiliado nuevo: Awin exige **depósito de 5 £/5 €** (se devuelve con la primera comisión) y declarar la URL/canal; Adtraction aprueba primero el canal y luego cada marca; cada anunciante acepta o rechaza (Allianz enumera tipologías: contenido, cupones, cashback, display, social). **Ningún mínimo de tráfico publicado**, pero la aceptación es discrecional por marca. |
| H5. Margen positivo solo en 2–3 categorías con lead >25 € | **CORREGIDA (hacia abajo)** | Con los datos obtenidos (§4) solo **una** categoría da margen positivo y solo en el mejor caso: reformas de vivienda/integral en Madrid (precio 33,3 €, CPL 27,5 € con CPC 2,2 € y 8 % de conversión → +63 € con 300 €/mes, +424 € con 2.000 €). En el caso típico (CPC 6 €, 4 %) pierde 233–1.556 €/mes. Cocinas (12,5 €), solar, energía, seguros de salud y mudanzas dan margen negativo o nulo. Y el precio de 33 € es el que cobra Habitissimo **tras vender cada solicitud hasta a 4 profesionales**; un individuo que vende a un solo profesional sin reunión no accede a ese precio: las redes CPL pagan 2–5 €/lead, por debajo de cualquier CPL plausible (≥10 €). |
| H6. Arbitraje saturado: los marketplaces y grandes afiliados pujan y Google restringe | **CONFIRMADA (con matiz)** | Matiz: Habitissimo y Cronoshare **no** dominan por Ads sino por SEO: Habitissimo 27 anuncios en el Centro de Transparencia (varios anunciantes), tráfico de búsqueda de pago 320 visitas/mes vs Authority 54 y 381 K backlinks (Semrush, sep-2026); Cronoshare 1 anuncio. En seguros/energía/certificados sí dominan los grandes: Selectra ~600 anuncios, Rastreator ~400, Certicalia ~500, Acierto 27,3 K visitas/mes de pago, Adeslas 28,5 K (+60 %). Google: verificación de anunciante para todos "en algún momento" y obligatoria para servicios financieros; en España, desde 24-01-2023 anunciar servicios financieros exige acreditar autorización de CNMV, Banco de España o **DGSFP (seguros)**; la política de préstamos personales se aplica expresamente a "generadores de oportunidades de venta"; requisitos de destino prohíben "páginas puente… que solo se usan para enlazar a otros sitios"; formularios de clientes potenciales exigen buen historial de políticas y política de privacidad; Google prohibió anuncios de cerrajeros en España desde 04-11-2024 (Política de Servicios Locales). |
| H7. Vender leads exige consentimiento explícito para cesión; hay multas AEPD | **CONFIRMADA** | PS/00437/2022 (resolución 09-03-2023): **10.000 €** a Alpa 57 Producciones (telemarketing) por ceder datos de una reclamante a una comercializadora eléctrica en una cadena de subcontratas ("origen lead y gestión: AIMART MARKETING"), art. 6.1 RGPD. MasLuz Energy: **90.000 €** (2023) arts. 6 y 13 por contratar con datos de origen desconocido. Más Sol Energía (exp202416818, 2026): **10.000 €** (2×5.000) a una comercializadora de paneles solares por llamar con una base de datos comprada: "no es aceptable que la compradora… no verificara la validez del consentimiento remitido por el proveedor". PS/00135/2025: 5.000 € por una llamada comercial sin base acreditada. Endesa PS/00002/2023: 6,1 M€ (seguridad/accesos indebidos a datos usados por terceros para spam). Vodafone 2021: 8,15 M€ (telemarketing sin consentimiento). Criterio: el comprador del lead responde igual que el vendedor; la cesión necesita consentimiento específico e informado con destinatarios identificados (Circular 1/2023 AEPD; RD 88/2026 art. 13.y para electricidad desde junio 2026, [FRAGMENTO]). |

**Conclusión operativa para Jorge**: la variante (a) solo es rentable para quien, como Habitissimo, (1) compra el tráfico mayoritariamente vía SEO/marca, (2) vende la misma solicitud hasta a 4 profesionales y (3) tiene una fuerza comercial que capta y cobra a 450.000 profesionales, es decir, requiere exactamente la venta B2B que Jorge descarta. La variante (b), la única realmente sin reunión, paga 2–5 € por lead en energía/seguros frente a un coste por lead de 10–240 € con tráfico de pago. Con 300, 1.000 o 2.000 €/mes de anuncios el resultado esperado es pérdida en todas las categorías salvo un caso límite (reformas integrales, mejor escenario) que exige vender el lead a 33 € a un profesional concreto, algo que no se consigue sin contacto comercial.

---

## 1) Precio por lead que pagan los profesionales (variante a)

| Plataforma | Categoría / zona | € por contacto | Modelo | Fuente y estado |
|---|---|---|---|---|
| Habitissimo | Media de todas las categorías | **12 €** ("el trabajo medio cuesta 12 €"; ingreso medio del profesional por trabajo ~10.000 €, mediana 1.300 €; cierra 1 de cada 10) | Pago por contacto; precios dinámicos "dentro de un rango"; precio según tipo de trabajo, oferta/demanda y coste de adquisición en marketing | [ABIERTA] https://soporte.habitissimo.com/hc/es/articles/203978696 (actualizado 13-10-2026, vía API Zendesk) |
| Habitissimo | Reformas de Viviendas, Madrid | **33,3 €** (300 € → 9 contactos) | Idem | [ABIERTA] https://habitissimo.es/calculadora-profesionales |
| Habitissimo | Reformas de Cocinas, Madrid | **12,5 €** (300 € → 24 contactos) | Idem | [ABIERTA] misma URL |
| Habitissimo | Calculadora genérica | 70 contactos = 855,40 € (**12,2 €**); 100 = 1.222 €; 200 = 2.444 € | Inversión mínima **75 €**; presupuesto semanal; documentación de autónomo/empresa | [ABIERTA] misma URL y https://www.habitissimo.es/premium |
| Habitissimo | Aire acondicionado, Madrid (ejemplo oficial) | 300 € de inversión → facturación estimada 19.558 € (ticket medio 1.398 €) → implica ~14 trabajos/300 € de contactos, es decir, el ejemplo oficial asume un cierre muy superior al 10 % | — | [ABIERTA] misma URL (incoherencia interna señalada, no verificable) |
| Habitissimo | Reseñas de profesionales España | 47 € ingresados → 2 contactos (**23,5 €**) (22-09-2026); "15,33 por 9 trabajos que te envían/cobran al día" (06-07-2026, ambiguo); 200 € invertidos → "solo he conseguido contactar con dos" (02-04-2026) | Compra automática por suscripción, quejas de duplicados | [ABIERTA, navegador] https://es.trustpilot.com/review/www.habitissimo.es?stars=1 (TrustScore 3,7; 22 % de 1 estrella) |
| Habitissimo (Portugal) | Pintura | "a partir de **7 €** cada contacto"; recarga 100 € + IVA; compra automática | Idem | [ABIERTA] https://portaldaqueixa.com/brands/habitissimo/complaints/habitissimo-solicitacao-de-esclarecimento-urgente-estorno-de-saldo-155316326 (15-05-2026) |
| Habitissimo (Portugal) | Construcción (2018) | Cargos de 51,20 €, 54,80 € y 57,60 € en días alternos por "Serviço Prioritário com Desconto" (20 % de descuento) | Idem | [ABIERTA] https://portaldaqueixa.com/brands/habitissimo/complaints/habitissimo-desonestidade-e-nao-cumprimento-de-anulacao-de-servico-19387218 |
| Habitissimo | Máximo de compradores por solicitud | **4 profesionales** por solicitud; teléfono validado por SMS/llamada; no valida intención ni solvencia | — | [ABIERTA] https://soporte.habitissimo.com/hc/es/articles/18746713098012 (11-03-2025) |
| Cronoshare | Todas | **sin dato** público; "pequeño pago… varía según servicio y zona"; coste = comisión + gastos de gestión; Garantía devuelve la comisión en cronos (no dinero); recarga mínima **0,15 €**; packs Bronce/Plata/Oro; 30 € gratis por profesional invitado | Pago por contacto en cronos, sin suscripción | [ABIERTA] https://www.cronoshare.com/registrar-empresa · https://www.cronoshare.com/cronos · https://www.cronoshare.com/devoluciones · https://www.cronoshare.com/comunidad/comparativas/cronoshare-vs-habitissimo-espana (">30.000 peticiones al mes") |
| Cronoshare | Reseñas de profesionales | ">150 euros" en contactos sin intención (2023, Gowork [FRAGMENTO]); "la garantía… no llega ni a un 20 % del precio del contacto" [FRAGMENTO]; 1 estrella 4 % de 4.531 opiniones, quejas de clientes ficticios/curiosos (sep–oct 2026) | — | [ABIERTA, navegador] https://es.trustpilot.com/review/www.cronoshare.com?stars=1 |
| Certicalia (certificados energéticos) | Técnicos | **sin dato** (páginas de profesionales tras Cloudflare 403) | — | NO ABIERTA https://www.certicalia.com/profesionales |
| Placas solares, abogados, residencias, dentistas, seguros de salud, préstamos | — | **sin dato**: ninguna plataforma española publica precio por lead; Solarmente 0 anuncios en Google; Inforesidencias/Miresi funcionan por comisión de colocación, no por lead (no verificado aquí) | — | NO ENCONTRADO |

Lectura: el único precio por lead verificable que supera 25 € es reformas de vivienda (33,3 €) y lo cobra una plataforma con 6,5 M de presupuestos históricos, 494.621 profesionales y 2 M de visitas/mes [ABIERTA, calculadora]. Para un individuo, "vender leads por unidad a profesionales" implica captar y cobrar a cada profesional: no existe en España un marketplace público donde subir leads de particulares y cobrar sin hablar con nadie (NO ENCONTRADO: Leadsale 502, NetSalesMedia 502, Kimia redirección infinita; AdSalsa es agencia, no compra leads a terceros).

---

## 2) Payouts públicos de afiliación/CPA (variante b)

| Red | Anunciante (país) | Pago | Requisitos / validación | Estado | URL |
|---|---|---|---|---|---|
| BlueAff (vía affi.io) | Gana Energía (ES) | **2,2 $/lead + 14 $/venta** (CPA+CPL); otra ficha CPA sin importe; "conversión ~10 %" lead→venta; venta válida solo cuando el cliente está activo | Excluye formularios incompletos, Canarias/Ceuta/Melilla, teléfonos erróneos | Abierto | [ABIERTA, WebFetch] https://affi.io/m/gana-energia- |
| MyLead | Gana Energía (ES) | 5 $ registro **solo si hay venta** + 25,2 $ venta | — | Cerrado | misma URL |
| TradeTracker / Sale Gains | Gana Energía, Tarífalo (comparador luz/gas), Holaluz CPA (ES) | Importe **no publicado** ("n/c"); cookie 30–60 días | — | Abiertos | [ABIERTA, WebFetch] https://affi.io/m/tarifalo · https://affi.io/m/holaluz |
| Adstrategy | Holaluz [CPL], iSalud [CPL] (ES) | Importe **no publicado**; "lead generado al completar el formulario con datos válidos"; validación 30 días; 18+; prohibidos leads falsos, duplicados y bots; acciones publicitarias aprobadas por el gestor antes de lanzar | — | Abiertos | [ABIERTA, WebFetch] https://affi.io/m/isalud · https://affi.io/m/holaluz |
| Adservice | Holaluz Solar (ES, "only email") | Conversión = usuario introduce teléfono y envía la solicitud; importe no publicado; BAT aprobado por el account manager | Solo emailing | Cerrado (hace 3 años) | misma URL |
| Awin | iSalud ES, AON ES CPL | Cerrados; importe n/c (una ficha de TradeTracker citaba **3,5 € por lead válido** = formulario correcto con datos reales, [FRAGMENTO]) | — | Cerrados | [ABIERTA, WebFetch] https://affi.io/m/aon-es-cpl |
| Awin | Allianz Assistance ES | **8 % CPA** por venta válida (4 % postview); solo seguro de viaje; cookie 30 días; enlaces nofollow obligatorios | Tipologías buscadas: contenido, blogs de viaje, cupones, cashback, display, social; "criterios de aceptación" por anunciante | Abierto | [ABIERTA] https://ui.awin.com/merchant-profile/15115 |
| Awin | Lampara ES | 5 % (con cupón) / 8 % CPO; carrito medio >150 € → ~12 €/pedido | — | Abierto | [ABIERTA] https://ui.awin.com/merchant-profile/10548 |
| Awin (red) | Condiciones de afiliado España (ago-2025) | "Lead aprobado" = lead aprobado por el anunciante (cl. 5); se paga solo cuando Awin cobra del anunciante; **depósito de suscripción devuelto con el primer abono de comisiones** | Formulario en ui.awin.com/publisher-signup/es/awin/; aceptación o rechazo por correo | — | [ABIERTA, PDF] https://www.awin.com/docs.awin.com/Legal/Publisher+Terms/2025/ES_Awin-AG-Publisher-terms_August-2025.pdf |
| Awin (red) | Cuota de alta | **5 £** de depósito al solicitar el alta; "la única red que lo pide", para verificar identidad vía tarjeta | — | — | [ABIERTA] https://www.awin.com/gb/compliance-and-regulations/application-process-and-joining-fee |
| Adtraction | Directorio España | ~130 marcas, mayoría préstamos/banca (Moneyman, Vivus, Cofidis, Bankinter, BBVA, Sabadell Hipotecas…), Prima Seguros, Life5, Santalucía Fondos, Sicor Teleasistencia, Petplan; comisiones **no visibles sin cuenta**; "sólo pagas cuando consigues una venta confirmada" (mensaje a marcas) | Alta gratis → aprobación del canal → solicitud marca a marca | — | [ABIERTA] https://adtraction.com/es/brand-directory/ · https://adtraction.com/es/partners · https://adtraction.com/es/marcas |
| Daisycon | Campañas ES | Sin campañas españolas de seguros/energía/alarmas localizadas; Verisure 50 € es Bélgica [FRAGMENTO]; "Comparison tools" dependen de los anunciantes incluidos | — | — | [ABIERTA] https://daisycon.com/es/campanas/ (listado no renderizado) |
| Tradedoubler / TradeTracker / TimeOne | — | Directorios públicos no accesibles sin cuenta (TimeOne /es/ 404; Tradedoubler /es/afiliados/ 404) | — | — | [ABIERTA] https://www.tradedoubler.com/es/ · https://tradetracker.com/es/afiliados/ |
| Rastreator / Selectra / Acierto | — | Sin programa de afiliados público localizado; Rastreator cobra comisión a la aseguradora por póliza contratada [FRAGMENTO] | — | — | NO ENCONTRADO |
| Placas solares (ES) | — | Ningún programa CPL/CPA de instaladora fotovoltaica española localizado en Awin/Tradedoubler/affi.io | — | — | NO ENCONTRADO |

Lectura: el único importe por lead verificado en una ficha abierta es 2,2 $ (energía); el único en euros es 3,5 € (Aon, cerrado, fragmento). Todo lo demás es CPA sobre venta (8 %) o importe oculto hasta ser aceptado. Un afiliado nuevo puede registrarse (5 £ en Awin; gratis en Adtraction) pero cada anunciante aprueba a discreción y varios exigen aprobar previamente las "acciones publicitarias" (Adstrategy, Adservice), lo que ya es un intercambio con un gestor aunque sea por correo.

---

## 3) Keywords: volumen España y CPC

Fuente principal: páginas públicas "website overview" de Semrush (España, septiembre 2026, CPC en USD). Son las 5 keywords orgánicas principales de cada dominio, no una búsqueda por keyword; por eso faltan varias de las pedidas.

| Keyword (exacta) | Volumen ES/mes | CPC | Fuente | Estado |
|---|---|---|---|---|
| placas solares | 22.200 (sep-2026) / 122.200 (nov-2025) | 0 $ (sep-2026) / 2,68 $ (nov-2025) | https://www.semrush.com/website/autosolar.es/overview/ · https://zh.semrush.com/website/autosolar.es/overview | [ABIERTA] / [FRAGMENTO] para nov-2025 |
| paneles solares | 9.900 | 0 $ | misma (autosolar.es) | [ABIERTA] |
| baterias para placas solares | 54.400 | 0,63 $ | semrush website sotysolar.es (sep-2025) | [FRAGMENTO] |
| instalar placas solares | 2.900 (jun-2022; 1.600 en ene-2021) | sin dato | https://www.energias-renovables.com/autoconsumo/las-bnsquedas-en-google-sobre-instalacion-de-20250203 (informe Barcelona Energia) | [ABIERTA] |
| placas solares precio | sin dato | sin dato | Semrush Keyword Overview sin cuenta devuelve "n/a" | NO ENCONTRADO |
| reforma cerca de mi | 3.600 | **2,40 $** | https://www.semrush.com/website/habitissimo.es/overview/ | [ABIERTA] |
| empresas de limpieza | 4.400 | 1,19 $ | misma | [ABIERTA] |
| puertas de garaje | 3.600 | 0,59 $ | misma | [ABIERTA] |
| presupuesto reforma | sin dato | sin dato | — | NO ENCONTRADO |
| comparador seguros coche | 27.100 | **7,15 $** | https://www.semrush.com/website/acierto.com/overview/ · https://zh.semrush.com/website/rastreator.com/overview | [ABIERTA] |
| acierto seguros | 2.400 | 3,19 $ | misma (acierto.com) | [ABIERTA] |
| seguro de salud | sin dato (Adeslas: "adeslas" 246.000, 0,86 $; "sanitas" 135.000, 1,22 $; "sanitas dental" 27.100, 53,95 $ anómalo) | sin dato | https://www.semrush.com/website/segurcaixaadeslas.es/overview/ · …/sanitas.es/overview/ | [ABIERTA]; keyword objetivo NO ENCONTRADA |
| cedula de habitabilidad | 6.600 | 1,38 $ | https://www.semrush.com/website/certicalia.com/overview/ | [ABIERTA] |
| certificado energetico precio | sin dato | sin dato | — | NO ENCONTRADO |
| abogado penalista | 6.600 | 5,26 $ | seojuice.com (agregador de datos tipo Semrush) | [FRAGMENTO] |
| abogado herencias | sin dato ("legalitas" 27.100, 1,85 $) | sin dato | https://zh.semrush.com/website/legalitas.com/overview | NO ENCONTRADO |
| brackets / blanqueamiento dental | 18.100 / 18.100 | 2,79 $ / 0,90 $ | https://www.semrush.com/website/vitaldent.com/overview/ | [ABIERTA] |
| mudanzas madrid | sin dato | sin dato | dominios de mudanzas no indexados en Semrush público | NO ENCONTRADO |
| residencia de ancianos madrid | sin dato ("cuidum" 5.400, 0,46 $) | sin dato | https://www.semrush.com/website/cuidum.com/overview/ | NO ENCONTRADO |

Referencias sectoriales (búsqueda, EE. UU., WordStream by LocaliQ, 13.000 campañas abr-2025→mar-2026, publicado 2026): CPC medio 5,42 $; abogados 9,87 $; hogar/reformas 8,33 $; dentistas 8,00 $; servicios personales 7,17 $; salud/fitness 6,17 $; servicios empresariales 5,87 $; finanzas/seguros 3,39 $; inmobiliario 3,22 $. Conversión: hogar 8,05 %, abogados 5,55 %, dentistas 10,67 %, finanzas/seguros 2,64 %, servicios personales 12,34 %, media 8,18 %. Coste por lead: abogados 131,63 $, hogar 90,92 $, finanzas/seguros 74,44 $, dentistas 72,97 $, servicios personales 54,60 $, media 66,69 $ — [ABIERTA] https://www.wordstream.com/blog/2026-google-ads-benchmarks (tabla CPC y CTR leída en la fuente; CVR y CPL confirmados por https://www.searchenginejournal.com/what-are-good-google-ads-benchmarks/546995/ y https://megadigital.ai/en/blog/google-ads-benchmarks/, ambas [ABIERTA]). Edición 2025 (abr-2024→mar-2025): abogados 8,58 $, servicios a domicilio 7,85 $, CPL medio 70,11 $ [ABIERTA] https://www.wordstream.com/blog/2025-google-ads-benchmarks y https://lionelz.com/blog/cuanto-cuesta-google-ads/. Statista tiene el CPC por sector en España (dic-2024, Semrush) pero con cifras ocultas tras pago [ABIERTA] https://www.statista.com/statistics/1243710/spain-search-advertising-cpc.

---

## 4) CAC y margen por categoría; escenarios 300 / 1.000 / 2.000 €

Fórmulas: CPL = CPC / conversión; leads = presupuesto / CPL; ingreso = leads × precio del lead; margen = ingreso − presupuesto (sin IVA, sin herramientas ni tiempo). Supuestos marcados con *. "Mejor caso" usa el CPC España más bajo disponible y la conversión sectorial alta; "típico" usa CPC EE. UU. × 0,8 × 0,90 €/USD* y la conversión sectorial baja.

| Categoría | Precio de venta del lead (€) | CPC usado (€) | Conversión | CPL (€) | Margen por lead (€) |
|---|---|---|---|---|---|
| A. Reforma integral/vivienda (Madrid) | 33,3 (Habitissimo) | mejor 2,2 ("reforma cerca de mi" 2,40 $) / típico 6,0 (8,33 $×0,8×0,9) | 8 % (WordStream hogar) / 4 %* (Unbounce: reformas ≈ 1/3 de reparación) | **27,5 / 150** | **+5,8 / −116,7** |
| B. Reforma de cocina (Madrid) | 12,5 (Habitissimo) | 2,2 / 6,0 | 8 % / 4 %* | 27,5 / 150 | −15 / −137,5 |
| C. Placas solares (instalador) | sin dato; proxy 12 €* (media Habitissimo) | 1,5* / 4,0* (Semrush 0–2,68 $ informacional) | 10 %* / 5 %* | 15 / 80 | −3 / −68 |
| D. Energía: cambio de comercializadora (CPL afiliación) | 3,2 (2,2 $ + 10 % × 14 $ = 3,6 $ × 0,9) | 1,0* / 3,0* (sin dato ES) | 10 %* / 5 %* | 10 / 60 | −6,8 / −56,8 |
| E. Seguro de salud (CPL afiliación) | 3,5 (Aon, cerrado) | 3,1 (3,39 $×0,9) / 6,4 (7,15 $×0,9 "comparador seguros coche") | 10,1 % (Unbounce F&I paid search) / 2,64 % (WordStream F&I) | 31 / 242 | −27 / −239 |
| F. Abogado herencias | sin dato (Cronoshare no publica; CPL objetivo de agencias 30–250 € [FRAGMENTO]) | 4,7 (5,26 $×0,9) / 7,1 (9,87 $×0,8×0,9) | 8,3 % (Unbounce legal paid) / 5,5 % (WordStream) | 57 / 129 | precio de equilibrio 57–129 €; EE. UU. 131,63 $ |
| G. Mudanzas | sin dato; proxy 12 €* | 1,5* / 4,0* | 12 % (servicios personales) / 8 %* | 12,5 / 50 | −0,5 / −38 |
| H. Certificado energético | sin dato (Certicalia 403) | 1,2 ("cedula de habitabilidad" 1,38 $×0,9) / 2,0* | 12 %* / 8 %* | 10 / 25 | precio de equilibrio 10–25 €; Certicalia ~500 anuncios activos |
| I. Dentistas | sin dato (no hay comprador por lead; Doctoralia es suscripción, no verificado) | 0,8–2,5 (Semrush ES) / 7,2 (8,00 $×0,9) | 10,67 % | 8–67 | sin dato |
| J. Residencias de mayores | sin dato | sin dato | sin dato | sin dato | sin dato |

Escenarios mensuales (leads = presupuesto / CPL):

| Categoría y caso | 300 € | 1.000 € | 2.000 € |
|---|---|---|---|
| A. Reforma integral, mejor (CPL 27,5; 33,3 €) | 10,9 leads → 363 € → **+63 €** | 36,4 → 1.212 € → **+212 €** | 72,7 → 2.424 € → **+424 €** |
| A. Reforma integral, típico (CPL 150) | 2,0 → 67 € → **−233 €** | 6,7 → 222 € → **−778 €** | 13,3 → 444 € → **−1.556 €** |
| B. Cocinas, mejor (CPL 27,5; 12,5 €) | 10,9 → 136 € → −164 € | 36,4 → 455 € → −545 € | 72,7 → 909 € → −1.091 € |
| C. Solar, mejor (CPL 15; 12 €*) | 20 → 240 € → −60 € | 66,7 → 800 € → −200 € | 133 → 1.600 € → −400 € |
| D. Energía CPL, mejor (CPL 10; 3,2 €) | 30 → 96 € → −204 € | 100 → 320 € → −680 € | 200 → 640 € → −1.360 € |
| E. Seguro salud CPL, mejor (CPL 31; 3,5 €) | 9,7 → 34 € → −266 € | 32,3 → 113 € → −887 € | 64,5 → 226 € → −1.774 € |
| F. Abogado herencias, mejor (CPL 57) | 5,3 leads; equilibrio si el despacho paga ≥57 €/lead | 17,5 leads | 35 leads |
| G. Mudanzas, mejor (CPL 12,5; 12 €*) | 24 → 288 € → −12 € | 80 → 960 € → −40 € | 160 → 1.920 € → −80 € |
| H. Certificado energético, mejor (CPL 10) | 30 leads; equilibrio si el técnico paga ≥10 €/lead | 100 leads | 200 leads |

Notas al cálculo:
- El precio de 33,3 € (A) y 12,5 € (B) es lo que **cobra Habitissimo**, que además vende la misma solicitud a hasta 4 profesionales (ingreso potencial por solicitud ≈ 4× el precio unitario). Un individuo sin equipo comercial no replica ni el multiplicador ni el precio.
- Habitissimo declara que su propio coste de adquisición depende de "campañas de anuncios… con distintos costes de adquisición según el canal", pero su tráfico de pago es marginal (320 visitas/mes, Semrush sep-2026) frente a 2 M de visitas/mes: su CPL real se apoya en SEO y marca, no en Google Ads.
- Con 300 €/mes y CPC de 2–6 € se compran 50–150 clics: 2–12 leads/mes, insuficientes para optimizar (el propio Habitissimo recomienda ≥15 solicitudes para valorar; lionelz: datos accionables a partir de 600–800 €/mes). Con 2.000 €/mes, el mejor escenario de A deja 424 € antes de herramientas (landing, dominio, validación telefónica) y del coste de vender cada lead.
- Umbral de equilibrio general: el precio del lead debe superar CPC/conversión. Con conversión 6 % y CPC 3 €, el equilibrio es 50 €/lead; ninguna red CPL española paga eso y solo las reformas integrales se acercan (33 €).

---

## 5) Riesgos, saturación, políticas y lo no verificado

Saturación y competencia (H6)
- Centro de Transparencia de Google (región España, 23-10-2026): habitissimo.es 27 anuncios (varios anunciantes, incluidos profesionales que enlazan a su ficha); cronoshare.com 1 anuncio; selectra.es ~600; rastreator.com ~400; certicalia.com ~500 (incluye Idealista); solarmente.com 0 — [ABIERTA, navegador] https://adstransparency.google.com/?region=ES&domain=habitissimo.es (y dominios análogos).
- Semrush (sep-2026): habitissimo.es Authority 54, 381 K backlinks, tráfico de pago 320 visitas/mes (−24 %); certicalia.com tráfico de pago 882 (−22 %); acierto.com 27,26 K de pago (−28 %); segurcaixaadeslas.es 28,55 K (+60 %); sanitas.es 11,43 K; autosolar.es 2,73 K; vitaldent.com 5,13 K — [ABIERTA] https://www.semrush.com/website/<dominio>/overview/. Lectura: en reformas el incumbente gana por SEO (keywords de 2–3 K búsquedas con CPC 0,6–2,4 $); en seguros/salud los anunciantes directos compran decenas de miles de visitas al mes.
- Quality Score: un anunciante nuevo sin historial parte con CPC real más alto; "QS 8 puede pagar un 40 % menos que QS 5" (lionelz, afirmación de agencia, sin fuente primaria) [ABIERTA].

Políticas de Google Ads que afectan a un generador de leads individual
- Verificación del anunciante: "todos los anunciantes deberán completar la verificación… en algún momento"; motivos de selección incluyen "publicas anuncios para ciertos sectores, como el de servicios financieros"; la cuenta puede pausarse hasta verificar — [ABIERTA] https://support.google.com/adspolicy/answer/9703665?hl=es.
- Servicios financieros en España (incluye seguros): desde el 24-01-2023 hay que acreditar autorización de CNMV, Banco de España, **DGSFP**, ICAC, ABE, AEVM o AESPJ y haber completado la verificación de anunciante — [ABIERTA] https://support.google.com/adspolicy/answer/12390454?hl=es · https://blog.google/intl/es-es/productos/tecnologia/2022_10_verificacion-de-los-anunciantes-de/. Un comparador o landing de seguros de salud de un particular no mediador no supera este filtro sin un anunciante autorizado detrás (la política de préstamos personales se aplica expresamente a "generadores de oportunidades de venta y los que ponen en contacto a los consumidores con entidades crediticias" — [ABIERTA] https://support.google.com/adspolicy/answer/2464998?hl=es).
- Requisitos de destino: se rechazan "página puente, entrada, pasarela u otras páginas intermedias que solo se usan para enlazar a otros sitios", "destinos diseñados exclusivamente para enviar a los usuarios a otro lugar" y contenido "con la finalidad principal de mostrar anuncios" — [ABIERTA] https://support.google.com/adspolicy/answer/6368661?hl=es. Una landing de afiliado con solo formulario y redirección es candidata a rechazo.
- Formularios para clientes potenciales (lead form assets): exigen "un buen historial de cumplimiento de políticas", vertical apta y política de privacidad enlazada — [ABIERTA] https://support.google.com/adspolicy/answer/9472930?hl=es.
- Servicios locales: Google prohibió los anuncios de cerrajería en España desde el 04-11-2024 por prácticas de precio engañoso — [ABIERTA] https://www.vozpopuli.com/actualidad/adios-anuncios-cerrajeros-google-sd.html. Los Anuncios de Servicios Locales (pago por contacto, "Protección de Google") existen en España desde 2020 para fontaneros, limpieza y electricistas [FRAGMENTO]: canalizan la demanda hacia profesionales verificados, no hacia intermediarios.
- Abogados: la publicidad está sujeta a la Ley 34/1988 y al Código Deontológico; expedientes colegiales posibles — [ABIERTA] https://asesor.legal/campanas-de-google-ads-para-abogados/.

RGPD y venta de leads (H7)
- PS/00437/2022 (resolución 09-03-2023; recurso 2023): 10.000 € a Alpa 57 Producciones por ceder los datos de una reclamante a Suministrador Ibérico de Energía (Mas Luz) en una cadena de telemarketing subcontratado; la recurrente alega que su único registro era "origen lead y gestión: AIMART MARKETING" — [ABIERTA, PDF] https://www.aepd.es/es/documento/reposicion-ps-00437-2022.pdf.
- MasLuz Energy Power: 90.000 € (publicado 10-08-2023) por arts. 6 y 13 RGPD: contrato tramitado con datos de origen desconocido — [ABIERTA] https://www.economistjurist.es/actualidad-juridica/sancionada-con-90-000-euros-masluz-energy-por-usar-datos-personales-sin-un-consentimiento-acreditado.
- Más Sol Energía (exp202416818; noticia 05-08-2026): 10.000 € (5.000 LGT + 5.000 art. 14 RGPD) por llamar a un inscrito en Lista Robinson con una "base de datos" comprada; la AEPD: "no es aceptable que la compradora de la base de datos no verificara la validez del consentimiento remitido por el proveedor" — [ABIERTA] https://www.moncloa.com/2026/08/05/multa-aepd-spam-mas-sol-energia-3410709/ · https://www.economistjurist.es/?p=252000 (muro de pago parcial). Resolución original en aepd.es: NO ENCONTRADA.
- PS/00135/2025: 5.000 € a Negocios R&R 2020 por una llamada comercial (04-12-2023) sin base acreditada; "un contrato entre empresas que describe una actividad de marketing no demuestra por sí solo que una persona concreta autorizara la llamada" — [ABIERTA] https://www.legiscope.com/blog/aepd-sanciones-marketing-publicidad.html (blog jurídico; cita la resolución).
- Endesa PS/00002/2023: 6.100.000 € (accesos indebidos a su plataforma comercial, datos usados por terceros para spam telefónico) — [ABIERTA] https://www.xatakahome.com/… y https://www.legiscope.com/blog/aepd-sanciones-energia-utilities.html. Vodafone 2021: 8.150.000 € [FRAGMENTO].
- Reglas aplicables al modelo: el consentimiento para ceder a terceros debe identificar destinatarios y finalidad ("socios" genérico no vale), el comprador debe revisar formulario original, texto informativo, casilla y fechas; Circular 1/2023 AEPD para llamadas; art. 13.y del Reglamento del RD 88/2026 para comunicaciones a consumidores de electricidad desde junio 2026 — [ABIERTA] Legiscope (síntesis de despacho; el RD no se ha abierto aquí, [FRAGMENTO]). Habitissimo lo resuelve con un texto de privacidad que nombra a Habitissimo y Homeserve y pide consentimiento separado para "comunicaciones comerciales… de sus colaboradores" [ABIERTA, calculadora].

Lo no verificado o sin dato
- Precio por contacto de Cronoshare y de Certicalia; precio por lead de placas solares, abogados, residencias y dentistas en España.
- CPC España por keyword exacta en euros (todas las herramientas gratuitas bloquean el CPC); solo muestras USD de Semrush por dominio.
- Importes CPL de iSalud, Holaluz y Tarífalo (ocultos hasta aceptación); existencia de un programa CPL de alarmas (Securitas Direct/Verisure) en España.
- Resolución íntegra de la AEPD contra Más Sol Energía; texto del RD 88/2026.
- La reseña "15,33 por 9 trabajos… al día" (Trustpilot) es ambigua: puede ser 15,33 € por contacto o por lote.
- Tipo de cambio USD→EUR del día (se usó 0,90*).

---

## 6) URLs abiertas y estado

| URL | Estado | Uso |
|---|---|---|
| https://www.habitissimo.es/profesionales | 404 | — |
| https://www.habitissimo.es/premium | 200 [ABIERTA] | Modelo: suscripción con presupuesto semanal, sin cuotas ni comisión; documentación autónomo |
| https://habitissimo.es/calculadora-profesionales | 200 [ABIERTA] (HTTP y navegador) | 300 € → 9 (viviendas) / 24 (cocinas) contactos Madrid; mínimo 75 €; 100 contactos 1.222 €; cifras de plataforma |
| https://soporte.habitissimo.com/hc/es (+ /search y API articles.json) | 200 [ABIERTA] | Artículos: "¿Cuánto cuesta cada solicitud?" (12 € medio, 1/10), "Precios dinámicos", "Contacto no válido" (máx. 4 profesionales) |
| https://www.habitissimo.es/condiciones_de_contratacion | 200 [ABIERTA] | Sin precios |
| https://www.habitissimo.es/procenter/?p=3926 · ?p=228 | 200 (redirigen a guía de precios) | Sin datos |
| https://ayuda.habitissimo.es · /ayuda · /condiciones-generales-profesionales | 200 redirección / 404 / 404 | — |
| https://www.habitissimo.com.mx/premium | FAIL (ECONNRESET) | — |
| https://es.trustpilot.com/review/www.habitissimo.es (+?stars=1) | 403 HTTP; 200 con navegador [ABIERTA] | 4.742 opiniones, 3,7; reseñas de profesionales con importes |
| https://es.trustpilot.com/review/www.cronoshare.com?stars=1 | 403 HTTP; 200 con navegador [ABIERTA] | 4.531 opiniones, 4,7; quejas de profesionales |
| https://www.cronoshare.com/profesionales | 200 [ABIERTA] | Casos de éxito; sin precios |
| https://www.cronoshare.com/registrar-empresa | 200 [ABIERTA] | FAQ: pago por contacto en cronos, precio varía por servicio y zona |
| https://www.cronoshare.com/cronos | 200 [ABIERTA] | Packs, 30 € por invitado, sin caducidad |
| https://www.cronoshare.com/devoluciones | 200 [ABIERTA] | Garantía: devuelve la comisión, no los gastos de gestión |
| https://www.cronoshare.com/comunidad/comparativas/cronoshare-vs-habitissimo-espana | 200 [ABIERTA] | Recarga mínima 0,15 €; >30.000 peticiones/mes |
| https://www.cronoshare.com/atencion-cliente/dudas-precios-cronoshare (+ navegador) | 200 | Preguntas listadas, respuestas no renderizadas |
| https://www.cronoshare.com/atencion-cliente/es-fiable-seguro-cronoshare | 200 [ABIERTA] | Pago por adelantado; devolución en cronos |
| https://ayuda.cronoshare.com · https://cronoshare.zendesk.com/hc/es · /ayuda · /garantia · /soporte | 502 / 403 / 404 | — |
| https://es.gowork.com/cronosharecom-espana/9 · /2 (+ navegador) | 403 Cloudflare | Solo [FRAGMENTO] vía buscador |
| https://portaldaqueixa.com/…/155316326 · …/19387218 · …/56721621 | 200 [ABIERTA] | "a partir de 7 €", cargos de 51–58 €, política de no devolución |
| https://www.deco.proteste.pt/reclamar/…/5c73a228a3035a18c9 | 200 | Texto de la queja no extraído (25 € → 2 contactos solo [FRAGMENTO]) |
| https://www.certicalia.com/profesionales · /tecnicos | 403 Cloudflare | — |
| https://www.wordstream.com/blog/2025-google-ads-benchmarks | 200 [ABIERTA] | Benchmarks 2025 (16.000 campañas) |
| https://www.wordstream.com/blog/2026-google-ads-benchmarks | 200 [ABIERTA] | Tabla CPC y CTR 2026 por sector |
| https://www.searchenginejournal.com/what-are-good-google-ads-benchmarks/546995/ | 200 [ABIERTA] | CVR y CPL 2026 |
| https://megadigital.ai/en/blog/google-ads-benchmarks/ | 200 [ABIERTA] | Tabla completa 2026 (CPC, CVR, CTR, CPL) |
| https://lionelz.com/blog/cuanto-cuesta-google-ads/ | 200 [ABIERTA] | "España 20–40 % por debajo", sin dato primario |
| https://unbounce.com/conversion-benchmark-report/ (+ /legal-…, /finance-insurance-…, /professional-services-…) | 200 [ABIERTA]; /home-improvement-… 404 | Medianas por sector y canal |
| https://www.statista.com/statistics/1243710/spain-search-advertising-cpc | 200 | Cifras ocultas (pago) |
| https://es.semrush.com/blog/coste-keyword-google-ads | 200 | Sin cifras |
| https://www.semrush.com/analytics/keywordoverview/?q=placas%20solares%20precio&db=es (navegador) | 200 | "n/a" sin cuenta |
| https://www.semrush.com/website/{autosolar.es, habitissimo.es, certicalia.com, acierto.com, cuidum.com, sanitas.es, vitaldent.com, segurcaixaadeslas.es}/overview/ · https://zh.semrush.com/website/{autosolar.es, rastreator.com, legalitas.com}/overview | 200 [ABIERTA] | Top 5 keywords, volumen, CPC USD, tráfico de pago |
| Semrush overview de inforesidencias.com, miresi.es, mudanzas.com, sotysolar.es, otovo.es, presupuestos.com, vipreformas.es, certificadosenergeticos.com, gil-stauffer.com, abogadosherencias.com, mundojuridico.info, segurosdesalud.com, dentalia.es, flippers.es, residenciasymayores.com, abogadosdeherencias.com, segurosbroker.com | 404 | Dominios no indexados públicamente |
| https://ahrefs.com/keyword-generator/?country=es&input=… (navegador) · https://app.neilpatel.com/en/ubersuggest/overview?… (navegador) · https://keywordtool.io/… (navegador) · https://www.seobility.net/en/keywordresearch/… · https://seranking.com/free-tools/keyword-suggestion-tool.html… | 200 sin datos / 200 login / 200 (CPC solo Pro) / 404 / 404 | Sin CPC |
| https://www.energias-renovables.com/autoconsumo/las-bnsquedas-en-google-sobre-instalacion-de-20250203 | 200 [ABIERTA] | "instalar placas solares" 1.600→2.900/mes |
| https://adstransparency.google.com/?region=ES&domain={habitissimo.es, cronoshare.com, selectra.es, rastreator.com, solarmente.com, certicalia.com} (navegador) | 200 [ABIERTA] | 27 / 1 / ~600 / ~400 / 0 / ~500 anuncios |
| https://support.google.com/adspolicy/answer/9703665?hl=es · /2464998 · /12390454 · /6368661 · /9472930 | 200 [ABIERTA] | Políticas (verificación, financieros, destino, formularios) |
| https://support.google.com/adspolicy/answer/13263478?hl=es | 404 | — |
| https://blog.google/intl/es-es/productos/tecnologia/2022_10_verificacion-de-los-anunciantes-de/ | 200 [ABIERTA] | Verificación financiera España 24-01-2023 |
| https://www.vozpopuli.com/actualidad/adios-anuncios-cerrajeros-google-sd.html | 200 [ABIERTA] | Prohibición cerrajeros 04-11-2024 |
| https://asesor.legal/campanas-de-google-ads-para-abogados/ | 200 [ABIERTA] | Marco deontológico |
| https://www.awin.com/es/afiliados | 200 [ABIERTA] | Modelo creadores; 30.000 marcas |
| https://www.awin.com/es/preguntas-frecuentes | 404 | — |
| https://www.awin.com/gb/compliance-and-regulations/application-process-and-joining-fee | 200 [ABIERTA] | Depósito 5 £ |
| https://www.awin.com/docs.awin.com/Legal/Publisher+Terms/2025/ES_Awin-AG-Publisher-terms_August-2025.pdf | 200 [ABIERTA, PDF] | Lead aprobado; devolución del depósito |
| https://ui.awin.com/merchant-profile/15115 · /10548 | 200 [ABIERTA] | Allianz 8 % CPA; Lampara 5–8 % |
| https://affi.io/m/{aon-es-cpl, isalud, gana-energia-, holaluz, tarifalo} | ECONNRESET con pwfetch; 200 vía WebFetch [ABIERTA] | Payouts y validación |
| https://www.affilitizer.com/programs/allianz-assistance.es · /programs?country=ES · /search?q=españa+cpl | 200 | Redes por programa; listado dinámico sin importes |
| https://www.offervault.com/?query=spain (navegador) | 200 | Sin ofertas ES relevantes |
| https://adtraction.com/es/partners · /es/marcas · /es/brand-directory/ | 200 [ABIERTA] | Proceso de alta; directorio ES |
| https://www.tradedoubler.com/es/ · /es/afiliados/ | 200 / 404 | Sin directorio público |
| https://tradetracker.com/es/afiliados/ · https://affiliate.tradetracker.com/campaignDirectory | 200 / 404 | Sin directorio público |
| https://daisycon.com/es/campanas/ | 200 | Listado no renderizado |
| https://www.timeonegroup.com/es/ | 404 | — |
| https://www.leadsale.com/es/ · https://leadsale.com/ · https://www.netsalesmedia.com/ | 502 | Redes CPL españolas no accesibles |
| https://kimia.es/ | FAIL (redirecciones) | — |
| https://www.adsalsa.com/ · https://www.eficads.com/ · https://www.innovares.com/ | 200 | AdSalsa: agencia de lead generation con BBDD propia (30 M usuarios); Eficads: red CPL sin ofertas públicas; Innovares: no es red (farmacéutica italiana) |
| https://www.aepd.es/es/documento/reposicion-ps-00437-2022.pdf | 200 [ABIERTA, PDF] | 10.000 €, art. 6.1 |
| https://www.moncloa.com/2026/08/05/multa-aepd-spam-mas-sol-energia-3410709/ | 200 [ABIERTA] | 10.000 €, base comprada |
| https://www.economistjurist.es/?p=252000 · …/sancionada-con-90-000-euros-masluz-… | 200 [ABIERTA] (el primero con muro parcial) | Más Sol; MasLuz 90.000 € |
| https://www.legiscope.com/blog/aepd-sanciones-marketing-publicidad.html · …/aepd-sanciones-energia-utilities.html | 200 [ABIERTA] | PS/00135/2025; Endesa PS/00002/2023; reglas de compra de contactos |
| https://www.xatakahome.com/iluminacion-y-energia/multa-millonaria-a-endesa-… | 200 [ABIERTA] | 6,1 M€ |
| https://ecija.com/wp-content/uploads/2024/09/01_ECIJA_Nota_sancion_electrica_contratacion_2024-1.pdf | descarga HTML, no PDF (FAIL) | — |
| https://ahrefs.com/es/blog/visibilidad-seguros-salud-ia/ | 200 | Sin volúmenes extraíbles |
| https://arctic-shift.photon-reddit.com/api/… (r/spain, r/es, r/askSpain, r/autonomos, r/SpainFIRE; "habitissimo", "cronoshare", "leads") | 200 | Sin hilos relevantes |
