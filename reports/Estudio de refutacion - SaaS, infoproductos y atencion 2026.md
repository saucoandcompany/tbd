# Estudio de refutación: ¿está sesgado el analista hacia "servicio normativo B2B"?

Fecha: 23-10-2026. Encargo de Jorge: comprobar si la recomendación de "servicio productizado B2B con fecha legal" es un sesgo del analista o lo que dicen los datos, buscando activamente la evidencia a favor de SaaS, infoproductos y negocios de atención (webs con anuncios, YouTube, apps). Seis investigadores independientes con la orden de refutar; ≈400 páginas, PDF, CSV y 10-K abiertos. Notas con tablas de URL en `research_notes/Refutacion SaaS infoproductos 2026/`.

## 1. Veredicto sobre el sesgo

**Había sesgo, y en tres sitios concretos. Pero la conclusión sobrevive.**

| Afirmación del analista | Veredicto | Lo que dicen los datos |
|---|---|---|
| "Solo el 2-5 % de SaaS indie supera 100 k$/año" | CONFIRMADA | 4,8 % de fundadores solos con ingresos verificados por Stripe en Indie Hackers supera 10 k$ MRR (n=970); TrustMRR (7.378 proyectos Stripe): 5,1 % acumula >100 k$; mediana 169 $/mes; 48-61 % a cero |
| "...porque los que ganan tenían audiencia previa" | **REFUTADA** | 54 % de los fundadores con ingresos verificados tiene <1.000 seguidores; correlación ingresos-seguidores r=0,25; ingresos-antigüedad r=0,47. La variable es **distribución prestada** (marketplace, open source, SEO de nicho, tienda de apps) **más tiempo** (mediana 2,2 años hasta 100 k$), no audiencia |
| "Infoproductos: mediana cero, ley de potencias, lotería" | CONFIRMADA en cifras, MATIZADA en "lotería" | Gumroad (n=45.917): mediana 70 $/año, 0,39 % >100 k$. Udemy 10-K FY2025: 168 M$ entre >91.000 instructores, media 1.846 $/año. Patreon: mediana 31 $/mes. Pero no es azar: número de productos, lista de correo y antigüedad (solo 13 % de los >1 k$ está en su primer año) explican quién gana |
| "Un SaaS B2B no se vende por correo frío" | **MATIZADA** | Sí se vende, pero nunca "solo correo": abre la puerta y detrás hay llamada corta, migración manual o prueba con datos del cliente (ConvertKit, Upsales con 80-90 % de ingresos por outbound, Cloutly, Tocoway). Y los compradores industriales convierten a lead 2-4× más que los de software (Sopro: ingeniería civil 3,68 %, construcción 3,03 %, automatización industrial 1,91 % vs software 0,83 %) |
| "Gumroad retiró su dato de mediana" | **ERROR DEL ANALISTA** | La página de Gumroad de 2020 sigue publicada; no hubo retractación. La cifra (mediana 70 $) es válida y primaria |
| "Webs con anuncios ya no son vía" | CONFIRMADA | CTR orgánico −34,5 % con AI Overviews (Ahrefs, 300 k keywords); HouseFresh −91 %, Retro Dodo −85 %, Travel Lemming −94 %; Ezoic exige 250.000 usuarios/mes desde feb-2026; Raptive prioriza tráfico anglosajón; en español, RPM de YouTube 1,65 $ vs 5,64 $ en inglés. Para 100 k€/año en español: ≈3 M páginas vistas al mes |
| "YouTube infantil replicado" | CONFIRMADA | Política de YouTube 15-07-2025: contenido "mass-produced, generic, repetitive" no monetiza. "Made for kids" sin anuncios personalizados (COPPA): RPM de canal infantil fuerte ≤1 $; Cocomelon ≈2,3 $. Para 100 k€/año: ≈9 M vistas al mes |
| "Apps: ley de potencias extrema" | **MATIZADA** | RevenueCat 2026 (apps de suscripción): 17,3 % llega a 1.000 $/mes y **4,6 % a 10.000 $/mes en 2 años**. Es la misma tasa que el SaaS, sin depender de Google ni de YouTube. Condiciones: suscripción, categorías foto/vídeo, salud, juegos; audiencia estadounidense; precio alto |
| "El servicio B2B productizado tiene probabilidad mucho mayor y techo más bajo" | CONFIRMADA en dirección, MATIZADA en magnitud | Estimación del investigador, P(>100 k€/año a 24 meses, solo, sin capital): infoproducto ≈1 % [0,3-3]; SaaS B2B ≈4 % [2-8]; servicio productizado por correo frío a empresas con obligación ≈15 % [8-25], techo 100-250 k€. La prima por "obligación legal" no está cuantificada en ninguna fuente; es inferencia |
| "En el mercado hispano no hay casos solos >100 k€ sin audiencia" | MATIZADA | Hay SaaS españoles bootstrapped sin audiencia que llegaron a millones (Metricool, Quaderno, Hevy, SumaCRM), pero todos con 2-3 fundadores o equipo, 2-4 años, y canal producto gratuito, SEO o tiendas. Caso hispano con cifras basado en correo frío: NO ENCONTRADO. Infoproductor hispano verificable >100 k€ sin audiencia: NO ENCONTRADO |

## 2. Dónde estaba el sesgo

1. **Confundí audiencia con distribución.** Decía "sin audiencia no hay SaaS ni infoproducto". Los datos dicen que lo que hace falta es un canal prestado donde ya hay búsqueda o compradores (marketplace de Shopify, tienda de apps, Etsy, Udemy, Google de nicho, comunidad open source), y 2-4 años. La audiencia propia es una de las vías, no la condición.
2. **Subestimé las apps de suscripción.** 4,6 % a 10 k$/mes en 24 meses no es "lotería extrema"; es la misma tasa base que el SaaS B2B, con la ventaja de que la tienda hace la distribución.
3. **Cité un dato falso** (la retractación de Gumroad). Lo retiro.

## 3. Dónde no había sesgo

- Las tasas base del 2-5 % para SaaS y <1 % para infoproductos son correctas y vienen de datos primarios (Stripe, 10-K de Udemy, Gumroad, estudios académicos de Patreon).
- Webs con anuncios y YouTube infantil replicado están cerrados para quien empieza en 2026 en español: la propia plataforma lo dice por escrito y las caídas de tráfico están medidas.
- Stripe Atlas: los fundadores solos B2B ganan más de 4× que los B2C a 24 meses; retención en el mes 2: 30 % frente a 8 %. B2B no era mi gusto; es el dato.
- El servicio productizado es 2-5× más probable que el SaaS y 4-15× más que el infoproducto. Techo bajo, también confirmado.

## 4. Lo que los datos sí abren para Jorge (fuera de Normach)

El patrón que aparece en los casos verificados para un perfil "solo, sin capital, vende por outbound" no es "SaaS desde el día 1" ni "servicio para siempre". Es una secuencia:

**Servicio productizado por outbound → producto.** Cold Email Studio 0→10 k$ MRR en 3,5 meses como servicio; Instantly y Gojiberry nacieron de agencias que convirtieron su proceso en software; Upsales vendió con lista de 1.500 cuentas y outbound. El servicio paga las facturas y descubre qué automatizar; el producto llega con clientes ya dentro.

Aplicado a lo que hemos investigado estos dos días, hay dos candidatos que cumplen "B2B, outbound, tu oficio, no es Normach":

| Candidato | Fase servicio (meses 1-12) | Fase producto (meses 12-36) | Dato que lo sostiene | Riesgo principal |
|---|---|---|---|---|
| **Inteligencia de plazos y precios de equipo eléctrico** | Informe mensual a medida para 10-20 compradores (EPC, promotores, CPD): plazos reales por fabricante, precios de excedentes, inventario europeo; 300-600 €/mes | Índice de suscripción con alertas y API | Nadie vende un índice independiente (Wood Mackenzie y Rystad lo tienen dentro de research opaco; Turner lo regala trimestral); compradores industriales convierten 2-4× más a lead por correo frío; ImportGenius cobra 183-449 $/mes self-serve | Precio: 100-500 €/mes es "tierra de nadie" (Cummings); el dato agregado trimestral vale cero; cobrable solo granularidad, frecuencia y alertas |
| **Salida del SF6 en instalaciones de MT** | Inventario y plan de sustitución por instalación, 3-8 k€ | Herramienta de inventario y calendario normativo por instalación | Prohibiciones escalonadas 2026-2032 verificadas en el reglamento; decenas de miles de centros de transformación | Demanda no medida; posible competencia de mantenedores e ingenierías |

Ambos arrancan como servicio con los mismos 100 correos de prueba, y el segundo paso solo se da si el servicio paga.

## 5. Lo que los datos cierran para Jorge en 2026

- Webs con anuncios en español (3 M páginas vistas al mes para 100 k€; CTR hundido; redes premium cerradas).
- YouTube infantil replicado (política explícita; RPM ≤1 $).
- Infoproductos sin canal de búsqueda (0,4 % >100 k$; en B2B por correo frío, ningún caso con cifras).
- Intermediar capital (regulado, visto antes).
- Planes de nutrición para menopausia (búsqueda en caída, credibilidad y canal ajenos, visto antes).

Lo que queda abierto pero no es "demanda voraz": apps de suscripción (4,6 % a 10 k$/mes en 2 años, audiencia estadounidense, 2 años sin ingresos) y creador de fitness 40-55 (12-24 meses sin ingresos).

## 6. Recomendación revisada

Sin cambio de dirección, con cambio de argumento y de secuencia:

1. **Servicio productizado B2B vendido por correo frío** sigue siendo el arranque con mayor probabilidad (≈15 % frente a ≈4 % y ≈1 %). No porque sea "lo que ya tienes", sino porque es la única vía donde los datos muestran ingresos antes de 12 meses para alguien solo y sin capital.
2. **El servicio es el primer año, no el destino.** Los casos verificados que escalan convierten el servicio en producto con los clientes dentro. El plan debe nacer con esa segunda fase escrita.
3. **De los dos candidatos fuera de Normach, el índice de plazos y precios de equipo eléctrico es el que tiene hueco sin competidor directo y compradores que responden al correo.** Su riesgo es el precio, y se resuelve en la fase servicio preguntando cuánto pagan por el informe mensual.
4. El broker queda como tercera opción: mismas listas, mismos correos, pero ingresos por comisión e inventario perecedero. Puede convivir con el índice: el índice se vende a los mismos compradores y el broker monetiza los cruces que aparezcan.

## 7. Errores y lagunas de este estudio

- Sin cohortes a 24 meses por modelo de negocio: Stripe y Carta tienen el dato y no lo publican. Las probabilidades de la sección 1 son estimaciones del investigador a partir de tasas base de stock, no de cohortes.
- Indie Hackers está sesgado al éxito; TrustMRR y Stripe Atlas corrigen parcialmente.
- Casos hispanos con correo frío como canal: no encontrados; puede ser ausencia de documentación, no de casos.
- La AEAT publicó el 05-10-2026 una previsión de ampliación del plazo de Verifactu: cualquier negocio ligado a esa fecha carga riesgo de aplazamiento.
