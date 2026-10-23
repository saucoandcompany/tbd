# Barrido de negocios autoservicio sin reuniones: el CAC manda

Fecha: 23-10-2026. Encargo de Jorge: "no pasa filtro, tengo que hacer reuniones, yo no soy closer… vamos a explorar bien las cosas… lo que importa es el CAC". Restricciones aplicadas: cero reuniones y cero llamadas de venta; sin capital; sin LinkedIn (cuenta nueva); el cliente llega por anuncio o búsqueda y paga solo en la web. Presupuesto de anuncios no fijado por Jorge: se calculan los tres escenarios 300 / 1.000 / 2.000 €/mes.

Cinco investigadores en paralelo, uno por tipo de negocio, con obligación de abrir páginas (≥30 cada uno; 41-70 páginas útiles por nota) y de marcar cada dato como [ABIERTA], [FRAGMENTO], [INTERNO] (datos del Planificador de Google Ads sacados en tu sesión local del 4-10-2026) o "sin dato". Notas completas con tablas de URLs en `research_notes/Autoservicio sin reuniones 2026/`.

Convención de cálculo en todo el informe: **CAC = CPC / conversión**; clientes al mes = presupuesto / CAC; margen = clientes × margen bruto por venta − presupuesto − fijos. Los supuestos sin fuente llevan asterisco en las notas.

---

## 1. Veredicto en una tabla

| Fila | Mejor caso verificable | CAC (€) | Ticket o margen por venta (€) | CAC / ticket | ¿Cuadra con anuncios? | Qué lo salvaría |
|---|---|---|---|---|---|---|
| Kits B2B normativos (tipo Advisera) | Kit transición ISO 9001:2026, puja real 2,34 € [INTERNO], conv. 1 % supuesta | 234 | 249 (590 si se vende a consultoras) | 0,94 (0,40) | No con cliente final; sí solo si CPC ≤1,4 € y conv. ≥1,5 % | Volumen: todo el bloque ISO 9001 son 320 búsquedas/mes en España; ni se podrían gastar 1.000 €/mes. El canal real es orgánico (así creció Advisera desde 2009) |
| Captación B2C y venta de leads | Reforma integral Madrid, CPC 2,2 €, conv. 8 %, Habitissimo cobra 33,3 €/contacto | 27,5 por lead | 33,3 por lead | 0,83 | Solo en el mejor caso: +63 / +212 / +424 €/mes. Caso típico (CPL 150 €): −233 / −778 / −1.556 € | Nada: vender el lead a un profesional exige llamarle (reunión encubierta) y la cesión de datos sin consentimiento tiene multas AEPD de 5.000 a 90.000 € |
| Afiliación y CPA en redes (sin vender tú) | Energía 3,2 €/lead, seguros 3,5 €/lead (programa cerrado) | CPL 10-31 | 3,2-3,5 por lead | 3-9 | No en ninguna categoría | Nada con los payouts públicos españoles |
| Ecommerce de nicho (dropshipping UE) | Aire acondicionado portátil ~350 €, CPC Shopping 0,34 € mediana europea, conv. 1 %, margen 15 %* | 34 | 52,5 de margen bruto (37,5 si el envío voluminoso cuesta 15 €) | 0,65 (0,91) | Frágil: +48 / +428 / +973 €/mes, pero cae a −85 / −13 / +90 con el envío. Pedidos B2B eléctricos ≥110-120 €: +140 / +737 / +1.590 € | Verificar tarifas y envío de BigBuy (bloqueado, 403) y aceptar que una tienda nueva paga CPC por encima de la mediana |
| Afiliación SaaS B2B y comparadores | Semrush: 200 $ por venta, ingreso 0,63-1,13 € por visita | CPC 2,3-4,5 € por visita | 0,05-1,13 € por visita | 2-45 | No en ningún vertical; solo Semrush empata si el clic cuesta ≤1 € | Nada: Hostinger y Kinsta prohíben PPC, Semrush exige aprobar cada campaña, casi todos vetan pujar por marca |
| Newsletter B2B patrocinada | Bonilista 599 €/envío con 18.000 suscriptores (33 €/1.000) | Coste de llegar a 10.000 suscriptores: sin dato | 330-510 €/envío a 10.000 suscriptores → 600-2.000 €/mes | — | No es un modelo de anuncios | Exige audiencia previa que no tienes |
| Micro-SaaS autoservicio | Precio 35-50 €/mes, churn ≤5 %, prueba con tarjeta (25 % pasan a pago), CPC ≤3 € | 240 (120 si CPC 1,5 €) | LTV 700-1.667 | LTV/CAC 2,9-13,9 | Sí en ese caso: 4-8 clientes/mes con 1.000 € y 83-417 € de MRR añadido al mes. Caso base (20 €/mes, churn 8 %, sin tarjeta): CAC 600 €, LTV 250 €, se pierde dinero por cliente | Construir algo que un profesional pague 35-50 €/mes y mantenga; recuperar el CAC tarda 5-7 meses |
| Marketplaces de apps (Shopify, Chrome, Atlassian) | Coste por instalación ≈0 | ≈0 en euros | Mediana de entrada 9,99 $/mes; TrustMRR: mediana 169 $/mes entre los que cobran | — | No hay anuncios: es SEO del marketplace y reseñas | Shopify: 22.546 apps, 51 % sin reseñas, el 1 % superior se lleva ≈72 % de los ingresos; 584-1.588 apps nuevas al mes |

Lectura: con tráfico frío de pago, **ninguna de las cinco filas cubre el CAC con la primera venta usando solo datos verificados**. Los casos positivos (aire acondicionado, pedidos B2B eléctricos, SaaS a 35-50 €, kit ISO 9001 con CPC bajo) dependen todos de uno o dos supuestos sin fuente marcados con asterisco.

## 2. Qué dice el CAC, fila por fila

### 2.1 Kits normativos
- Hay ≥8 vendedores autoservicio en español, pero casi todos son SaaS mensuales baratos (Cumpleo 4,5-30 €/mes, EticAlert 9-39 €/mes, iubenda 19,99 €/mes) o servicio con abogado (Ático34 120-280 €/año). Kits puros de 50-1.000 €: Advisera (229-997 USD, con web en español, 6.000 empresas, 110 países), the9000store (en inglés), Gumroad (56 USD con 7 reseñas).
- Advisera ya vende en español y anuncia "AI-Powered Toolkits". El hueco no es "Advisera en español", sino producto hiperlocal con fecha límite.
- CPC real (puja superior del Planificador, tu cuenta, 4-10-2026): ISO 9001 2,34 €; Verifactu 4,99 €; ISO 27001 11,26 €; Cyber Resilience Act 15,59 €. Ciberseguridad queda fuera por CPC: CAC 1.126-1.559 €.
- Fechas verificadas en fuente oficial: Reglamento de Máquinas aplicable el 14-01-2027 (no el 20-01 que yo había escrito); CRA notificación 11-09-2026 y resto 11-12-2027; Ley 2/2023 desde 50 trabajadores; NIS2 en España sin transponer; registro horario digital sin Real Decreto a octubre de 2026; Verifactu −63 % de búsquedas y, según el investigador, nota de la AEAT del 5-10-2026 que lo aplaza a 2028 pendiente de BOE [FRAGMENTO: no lo he comprobado yo].
- Tasa base de conversión a compra de productos digitales: Littledata mediana 1,4 %, Gumroad 3,2 % modelado, Etsy 1-5 %. Para un kit de 150-900 € con tráfico frío uso 1 %.

Cálculo central: 2,34 € / 1 % = 234 € de CAC frente a 249 € de ticket. Con 300 €/mes compras 1,3 clientes; con 2.000 €/mes, 8,5. Pero las 320 búsquedas/mes del bloque, al 50 % de cuota y 5 % de CTR, son 8-16 clics al mes: 0,1-0,2 ventas. El presupuesto no se puede gastar.

### 2.2 Captación B2C y venta de leads
- Habitissimo cobra al profesional 7-33,3 € por contacto (media 12 €, bono mínimo 75 €) y vende cada solicitud a hasta 4 profesionales. Cronoshare no publica el precio por contacto.
- Conversión de landing a lead realista 3-8 % (Unbounce 2024 mediana 6,6 %; WordStream 2026 hogar 8,05 %, abogados 5,55 %, seguros 2,64 %), no 5-15 %.
- CPC España publicado solo en Semrush (sep-2026, USD): "comparador seguros coche" 7,15 $; "abogado penalista" 5,26 $; "reforma cerca de mi" 2,40 $; "cedula de habitabilidad" 1,38 $.
- Payouts CPA en redes españolas: Gana Energía 2,2 $/lead + 14 $/venta; Aon 3,5 €/lead (cerrado); MyLead solo paga con venta. Por debajo de cualquier coste por lead plausible.
- Habitissimo tiene 320 visitas de pago al mes frente a 2 millones orgánicas: los incumbentes ganan con SEO y marca, no con Ads. Google exige verificación de anunciante, restringe servicios financieros en España desde 2023 y vetó cerrajeros en noviembre de 2024.
- AEPD: sanciones por cesión de leads sin consentimiento de 5.000 € (PS/00135/2025), 10.000 € (PS/00437/2022; Más Sol Energía 2026) y 90.000 € (MasLuz 2023); Endesa 6,1 M€ y Vodafone 8,15 M€ por casos relacionados.

Solo reformas integrales da margen positivo, y solo en el mejor caso: +5,8 € por lead. Y hay que vender ese lead a un reformista: llamada o reunión. Fila descartada por tu restricción, no solo por el CAC.

### 2.3 Ecommerce de nicho
- Conversión España: Flat 101 1,20 % (edición 2023, no hay posterior) con ticket 196,89 €; Littledata oct-2026 mediana 1,4 % (suplementos 2,4 %, hogar 1,0 %, belleza 2,9 %).
- CPC: no hay dato público por categoría en España. Mejor proxy: smec (650 M€ de gasto ecommerce europeo, 19-10-2026) mediana Shopping 0,34 €, Search 0,47 €. Es la mediana de anunciantes consolidados; una tienda nueva paga más.
- BigBuy (fuente secundaria, el oficial dio 403): 89 €/mes plan ecommerce, 119 € marketplace, 89 € de alta; margen bruto ≈26 % en un PVP de 50 €. Printful 0-24,99 $/mes, camiseta 10,75 $ + 4,99 $ de envío. Amazon.es: 39 €/mes, 8-15 % de referencia, ACoS medio 28,8 %.
- Supervivencia: 34 % de las tiendas Shopify sigue activa al año (dato de 2022 vía Store Leads). Jungle Scout 2024: 58 % de vendedores Amazon rentables en el primer año.
- Suplementos de menopausia: margen 5,7-9,9 € por pedido frente a CAC 14-20 €. Solo cuadra con 2-3 recompras por cliente, dato no verificado, y Amazon.es ya tiene 97 resultados con marcas farmacéuticas de 600-1.500 reseñas.

Positivos solo con ticket alto: aire acondicionado portátil (ticket 350 €, margen 15 %*: 52,5 € frente a CAC 34-47 €) y pedidos B2B de material eléctrico ≥110-120 €. El primero oscila entre −13 y +428 €/mes a 1.000 € de gasto según cueste el envío de un bulto de 25-30 kg: negocio de céntimos, estacional y con >20.000 resultados en Amazon.es.

### 2.4 Afiliación, comparadores y newsletters
- Programas con pago alto y abiertos desde España: HubSpot 30 % recurrente 12 meses; Semrush 200-300 $ por venta; Kinsta 50-500 $ + 10 % de por vida; NordVPN 40 % + 30 % en renovaciones; SiteGround 50-100 $; Raiola 25 % recurrente; monday hasta 100 % del primer año; Pipedrive 33 % durante 12 meses.
- Conversión referido→venta medida por Rewardful (68,4 M$ en programas SaaS): 0,8 %; solo el 1,28 % de los afiliados genera una venta.
- Ingreso por visita a una página comparativa: 0,05-1,13 €. CPC sectorial software en Europa 2,30-4,50 €. Todo pierde; Semrush empata si el clic baja a 1 €.
- SERP español de comparativas: 26 de 29 dominios del top 5 son fabricantes, agregadores de pago por lead (Capterra, GetApp, SoftDoit) o medios grandes. "X vs Y" es 100 % Gartner Digital Markets.
- Comisiones recortadas 2023-2026: Amazon −50 % en categorías; Hostinger de 60 % a "desde 40 %"; Semrush cerró el 40 % de por vida en 2023; Notion cerrado.
- Newsletters en español con tarifa pública: Bonilista 599 €/envío (18.000 suscriptores), Tendenci@s 400 € (7.800), Kapital 333 €/inserción (25.000). Con 10.000 suscriptores, 600-2.000 €/mes vendiendo 2-4 envíos. El cuello de botella es llegar a 10.000.

### 2.5 Micro-SaaS y apps
- Único benchmark primario de CAC abierto (First Page Sage, enero 2026): CAC pagado B2B SaaS 341 $, orgánico 205 $, Engineering SaaS 551 $.
- Embudo con fuentes: visita→registro 5 % en trial y 9 % en freemium (OpenView/Lenny, >1.000 productos); trial→pago mediana 8 %, 4-6 % sin tarjeta, 25-35 % con tarjeta (ChartMogul 2026, 200 productos). Churn mensual medio 4,8 %, cuartiles 2,9-8,5 % (Recurly); con ARPU <100 $, 6-9 %.
- Distribución prestada: Shopify 22.546 apps, 51 % sin reseñas, el 1 % superior ≈72 % de los ingresos, 584-1.588 apps nuevas al mes, comisión 0 % hasta 1 M$; Atlassian sube la comisión de Connect del 15 al 20 % en 2026; ExtensionPay ha pagado 800.000 $ en total desde 2021 a todos sus desarrolladores; Freemius convierte free→pago 2-5 %. Casos de Reddit 2026 a un año: 100-210 $ de MRR.
- Oferta disparada: Product Hunt 18.385 lanzamientos en 30 días y récord de 1.382 en un día (20-10-2026) frente a 800-1.600 al mes antes de 2024; Shopify +81 % de apps interanual.
- SaaS técnicos autoservicio existen (Steel Beam Calculator 40-50 £/mes con 2 socios; WebStructural 29 $/mes; ClearCalcs 79-149 $/mes; SkyCiv desde 69 $/mes). Ningún fundador solo con ingresos públicos verificado.

Caso base (CPC 3 €, 5 %, 10 %, 20 €/mes, churn 8 %): CAC 600 €, LTV 250 €, LTV/CAC 0,42. Caso que sí cuadra: 35-50 €/mes, churn ≤5 %, tarjeta en la prueba, CPC ≤3 €: CAC 240 €, LTV 700-1.667 €, payback 5-7 meses, 4-8 clientes nuevos al mes con 1.000 €.

## 3. Lo que esto significa, sin edulcorar

1. **Para un recién llegado, el tráfico de pago es un impuesto, no un canal.** En las cinco filas el CAC monetario con datos verificados iguala o supera la primera venta. Los incumbentes que citan los investigadores (Advisera, Habitissimo, Selectra, Capterra) no compran su tráfico: lo tienen por SEO y marca acumulados durante 10-15 años. Su CAC real fue tiempo, no euros.
2. **Lo que baja el CAC es, por este orden: ticket alto, recurrencia, canal propio o prestado.** Los únicos casos positivos del barrido tienen ticket ≥110 € o suscripción ≥35 €/mes. Nada con ticket <60 € sobrevive al CPC con tráfico frío.
3. **La restricción "cero reuniones" es la que más te encarece el CAC.** El canal donde tu credibilidad de ingeniero reduce el coste de adquisición es la conversación de 20 minutos con otro ingeniero; la has vetado. Lo digo porque es el dato que sale del barrido, no para discutir tu decisión: sin voz, compites con tarjeta de crédito contra quien lleva una década acumulando enlaces.
4. **Los presupuestos de prueba de 300 €/mes no miden nada.** Con CPC de 2-6 €, son 50-150 clics: 0-2 ventas, ruido estadístico. Los datos de agencias dicen que la optimización empieza en 600-800 €/mes. Con 2.000 €/mes se mide, pero en el caso base se pierde la mayor parte.
5. **No puedo confirmar el CPC real de ninguna keyword española concreta** salvo las cuatro que ya sacaste del Planificador. Todas las herramientas gratuitas bloquearon (Ubersuggest, Semrush, Ahrefs, Sistrix, WordStream, Google Trends 429). Tienes el instrumento en tu cuenta de Google Ads y cuesta 0 €.

## 4. Lo que sobrevive, por orden de probabilidad, y qué medir antes de gastar

| Candidato | Por qué sobrevive | Dato que lo mata o lo confirma | Cómo medirlo gratis |
|---|---|---|---|
| Micro-SaaS para profesionales a 35-50 €/mes con prueba con tarjeta | Única fila con LTV/CAC >2,5 con supuestos de cuartil normal, no heroicos | CPC real de las keywords del problema ≤3 €; que exista un problema que un profesional pague mensualmente | Planificador de Google Ads con 20 keywords del problema (sesión local); 10 conversaciones por correo con usuarios potenciales, sin llamada |
| Tienda B2B de material eléctrico con pedido ≥110 € | CPC Shopping bajo (0,34-0,47 €) y margen 30 %* dan +737 €/mes a 1.000 € | Margen real del proveedor (BigBuy u otro distribuidor UE con dropshipping) y ticket medio real | Pedir tarifa y condiciones de envío a 3 proveedores por correo; ver precios de referencia en Amazon.es y RS/Farnell |
| Kit de transición ISO 9001:2026 vendido a consultoras (590 €) | CAC 234 € frente a 590 €: ratio 0,40; coincide con la línea de Normach pero el cliente es distinto (consultoras, no empresas) | Que las consultoras compren un kit en vez de hacerlo ellas; volumen de búsqueda de 320/mes limita todo a orgánico | Lista de consultoras ISO en España (Apollo lookup gratis) y una página de venta; la demanda se mide por correo, que tú asumes en Normach |
| Aire acondicionado portátil | Ticket 350 € cubre el CAC | Coste de envío de 25-30 kg y margen real del proveedor; estacional (mayo-agosto) | Tarifa de BigBuy o de un mayorista de climatización por correo |

Fuera: venta de leads B2C (exige vender a profesionales y riesgo AEPD), afiliación de pago (pierde en todos los verticales y lo prohíben los programas), ecommerce con ticket <60 €, infoproducto genérico, newsletter sin audiencia.

## 5. Confianza y límites

- Alta confianza: fórmula y signo de los resultados en las filas de leads, afiliación y ecommerce de ticket bajo; las fechas legales; las tarifas públicas de Habitissimo, Bonilista, los programas de afiliación y las sanciones de la AEPD.
- Media: CAC de SaaS y de kits (benchmarks con muestra pero no específicos de España ni del nicho).
- Baja: CPC por keyword española (solo 4 datos reales, de tu cuenta); márgenes y envíos de dropshipping (BigBuy bloqueado); LTV por recompra en suplementos; existencia de fundadores solos rentables en SaaS técnico.
- Error mío corregido: la fecha de aplicación del Reglamento de Máquinas es el 14-01-2027, no el 20-01-2027.

Notas fuente: `kits_b2b_normativos_cac.md`, `leadgen_b2c_y_afiliacion_cac.md`, `ecommerce_nicho_cac.md`, `saas_app_autoservicio_cac.md`, `afiliacion_comparadores_newsletters_cac.md`, todas en `research_notes/Autoservicio sin reuniones 2026/`.
