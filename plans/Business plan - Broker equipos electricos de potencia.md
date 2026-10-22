# Business plan: intermediación de equipos eléctricos de potencia con plazo corto

Documento de estrategia y operación. Redactado desde la silla de CEO y Chief Strategy Officer del venture. Fecha: 22-10-2026. Nombre provisional del proyecto: "el broker" (la marca se registra solo si la prueba de 2 semanas da luz verde, ver sección 12).

**Regla de lectura.** Cada cifra lleva una de estas etiquetas:
- **[VERIFICADO]**: leído en la página de la fuente citada el 22-10-2026 (notas en `research_notes/Demanda voraz sin filtros 2026/verificacion_energia_red.md`).
- **[FRAGMENTO]**: visto solo en extracto de buscador o fuente secundaria no abierta.
- **[HIPÓTESIS]**: supuesto de trabajo del plan. No está confirmado. La prueba de 2 semanas y los primeros 90 días existen para sustituir cada hipótesis por un dato.

No hay ninguna cifra de ingresos, comisión, precio unitario, tasa de respuesta o CAC que esté verificada. Todas son hipótesis y se presentan con el cálculo a la vista para que puedas cambiar un supuesto y recalcular.

---

## 0. Resumen ejecutivo

**Qué es.** Un intermediario independiente, de una sola persona, que localiza transformadores de potencia y distribución, aparamenta de media y alta tensión y grupos electrógenos o turbinas con disponibilidad inferior a 12 meses, y los cruza con compradores que tienen un proyecto parado porque el fabricante les da 2 a 4 años de plazo. Cobra una comisión sobre la operación cerrada. No compra, no almacena, no fabrica, no transporta.

**Por qué ahora.** Plazos de transformadores GSU por encima de 160 semanas en el primer trimestre de 2026 frente a 143 en 2024 [VERIFICADO, Reuters vía AJOT 09-07-2026, citando a Wood Mackenzie]. Hitachi Energy en España: "cubiertos pedidos para, al menos, los próximos cuatro años"; plazo prepandemia 10-12 meses, hoy 3-4 años [VERIFICADO, El Español 23-06-2026]. Precios de transformadores de potencia +77 % y GSU +45 % desde 2019 [VERIFICADO, Wood Mackenzie vía POWER 02-01-2026]. Backlog de Siemens Energy Grid Technologies 51.000 M€ con book-to-bill 1,48 [VERIFICADO, nota oficial 05-08-2026]. La capacidad nueva de Hitachi (Gallman, Misisipi) no produce hasta 2029 [VERIFICADO, T&D World 16-09-2026]. La ventana de escasez dura, como mínimo, hasta 2029.

**Por qué Jorge.** Ingeniero con pasado en Airbus y Siemens; entiende una placa de características, un protocolo de ensayos y un pliego de subestación. Ya vende B2B por correo frío con Normach. Sin capex: el activo del negocio es la lista de necesidades concretas y la lista de equipos disponibles.

**Qué pedimos al mercado en 90 días.** Una operación cerrada con comisión cobrada. Una sola. Si se consigue, el negocio existe y se escala la máquina de prospección. Si no, se cierra con un gasto total inferior a 2.000 € (ver sección 9).

**Números de cabecera (todos [HIPÓTESIS], cálculo en sección 8):**

| Magnitud | Pesimista | Base | Optimista |
|---|---|---|---|
| Ticket medio de la operación intermediada | 120.000 € | 250.000 € | 450.000 € |
| Comisión media | 4 % | 5 % | 6 % |
| Ingreso por operación | 4.800 € | 12.500 € | 27.000 € |
| Operaciones cerradas, año 1 | 2 | 6 | 12 |
| Ingresos año 1 | 9.600 € | 75.000 € | 324.000 € |
| Costes fijos año 1 | 6.600 € | 8.450 € | 12.000 € |
| Resultado antes de IRPF, año 1 | 3.000 € | 66.550 € | 312.000 € |
| Operaciones cerradas, año 2 | 4 | 14 | 30 |
| Ingresos año 2 | 19.200 € | 175.000 € | 810.000 € |

Lectura honesta: el escenario pesimista no da para vivir. El base da un sueldo de ingeniero senior trabajando solo. El optimista exige inventario recurrente y un segundo buzón o una persona de apoyo. El plan está diseñado para saber en 90 días en qué escenario estamos, no para fingir que estamos en el optimista.

---

## 1. Tesis estratégica

### 1.1 El problema que compramos

Un promotor fotovoltaico, un EPC o un operador de centro de datos tiene un proyecto con fecha de conexión, financiación firmada y un transformador de 40 MVA pedido con 36 meses de plazo. Cada mes de retraso es coste financiero, penalizaciones y, en renovables, riesgo de perder el permiso de acceso. El fabricante no puede adelantar. El comprador pagaría más por tener el equipo en 6 meses, pero no sabe dónde buscarlo ni tiene tiempo para hacerlo.

Al mismo tiempo, en el mercado existen equipos que no llegan a su destino original: slots de fabricación cuyo proyecto se canceló, unidades de excedente de EPC, transformadores retirados por utilities en buen estado, equipo reacondicionado en taller con ensayos, grupos electrógenos de flotas de alquiler que se renuevan. Surplus Record, el marketplace de usado industrial de EE. UU., registró más de 5.000 consultas de transformadores en un año y más de 7.500 anuncios de transformadores trifásicos, con la demanda concentrada en 1-2,5 MVA [FRAGMENTO, ABNewswire 13-10-2026 y Transformer Magazine; no abiertas en página].

Nadie en España y Portugal está, que sepamos, cruzando esas dos listas de forma sistemática para el tramo 1-100 MVA. No puedo confirmar que no exista; la prueba de 2 semanas lo medirá preguntando a los propios compradores a quién llaman hoy.

### 1.2 Lo que somos y lo que no somos

| Somos | No somos |
|---|---|
| Un buscador humano especializado con criterio técnico | Un marketplace con web y listados públicos (eso lo hacen Surplus Record, Machinio, Kitmondo, Exapro) |
| Un intermediario a comisión sobre éxito | Un distribuidor que compra para revender (eso exige capital y asume riesgo de inventario) |
| Un filtro técnico: validamos ficha, ensayos y estado antes de presentar | Un consultor de ingeniería que diseña la subestación |
| Un acelerador de plazo | Un competidor en precio frente al fabricante |

### 1.3 Ventaja competitiva defendible (y su límite)

La ventaja no es tecnológica ni de capital. Es tres cosas:

1. **Criterio técnico del fundador.** Un broker generalista no distingue un transformador con ensayo de calentamiento reciente de uno con papel degradado. Un comprador industrial sí paga por esa criba.
2. **Base de datos propietaria de necesidades y disponibilidades.** Cada respuesta a un correo es un dato que nadie más tiene. A los 6 meses, la lista de "quién necesita qué y para cuándo" vale más que cualquier operación individual.
3. **Velocidad.** Un fabricante tarda semanas en responder una consulta de un equipo que no va a poder servir. Nosotros respondemos en 24 horas con "sí tengo", "no tengo" o "tengo algo parecido".

Límite: la ventaja 1 no escala sin contratar ingenieros; la 2 la puede replicar un fabricante o un gran distribuidor si decide hacerlo. Nuestra ventana es 2026-2029, mientras los fabricantes están saturados y sin incentivo para montar este servicio.

---

## 2. Mercado

### 2.1 Tamaño: cálculo explícito y sus límites

Mercado global de transformadores de potencia ≈30.000 M€ [VERIFICADO, cifra citada en El Español 23-06-2026; es una estimación periodística, no un informe primario abierto].

No existe una cifra verificada del mercado secundario o de "equipo con plazo corto" en Iberia. Lo que sigue es un cálculo de orden de magnitud, no un dato:

**TAM (Iberia, equipo intermediable al año) [HIPÓTESIS]**
- Supuesto A: España y Portugal representan entre el 2 % y el 3 % del mercado global de transformadores de potencia (peso aproximado en PIB y en capacidad renovable instalada en la UE; no verificado).
- 30.000 M€ × 2,5 % = 750 M€/año de transformadores de potencia en Iberia.
- Añadir aparamenta MT/AT y gensets 1-50 MW: supuesto de +60 % sobre esa base → 750 × 1,6 = 1.200 M€/año de equipo en el alcance.

**SAM (parte que pasa por un canal secundario o acelerado) [HIPÓTESIS]**
- Supuesto B: entre el 3 % y el 8 % del equipo cambia de destino, se recoloca o se compra fuera del canal de fabricante estándar en un mercado con escasez. Tomamos 5 %.
- 1.200 M€ × 5 % = 60 M€/año de operaciones intermediables.

**SOM (lo que un intermediario de una persona puede tocar en 24 meses) [HIPÓTESIS]**
- Supuesto C: cuota del 2 % al 5 % del SAM en el año 2.
- 60 M€ × 3 % = 1,8 M€ de volumen intermediado en el año 2 → a 5 % de comisión = 90.000 € de ingresos.

Este SOM es coherente con el escenario base del año 2 (14 operaciones × 12.500 € = 175.000 €) solo si la cuota llega al 5-6 %. Lo señalo para que quede claro que el escenario base ya es ambicioso respecto al tamaño estimado del mercado iberico. Hay dos salidas si Iberia se queda corta: ampliar a Francia e Italia (mismo problema de plazos, misma normativa IEC/EN) o subir en ticket (equipos de 100-250 MVA).

### 2.2 Segmentos de comprador (demanda)

| Segmento | Por qué tiene urgencia | Equipo típico | Ticket estimado [HIPÓTESIS] | Prioridad |
|---|---|---|---|---|
| Promotores y EPC de fotovoltaica, eólica y almacenamiento con subestación propia | Fecha de acceso a red y de puesta en marcha; financiación con hitos | Transformador 10-60 MVA, 30/132 kV o 30/220 kV; celdas | 200.000-900.000 € | Alta |
| Operadores y promotores de centros de datos | Cliente final esperando; cada MW no entregado es ingreso perdido | Transformadores de 20-60 MVA, gensets 1-3 MW de respaldo | 150.000-1.500.000 € | Alta |
| Ingenierías y EPC industriales que ejecutan subestaciones para terceros | Penalizaciones contractuales | Transformadores 5-40 MVA, aparamenta | 100.000-600.000 € | Alta |
| Industrias electrointensivas en ampliación (metalurgia, química, papel, cemento, frío) | Parada de ampliación; equipo único en el proyecto | Transformadores 2-25 MVA, 10-66 kV | 60.000-500.000 € | Media |
| Distribuidoras pequeñas y cooperativas eléctricas | Reposición por avería o ampliación de red | Transformadores 1-10 MVA, celdas 20-30 kV | 30.000-250.000 € | Media |
| Hospitales, puertos, aeropuertos, Administración | Respaldo crítico; licitación con plazos rígidos | Gensets 0,5-3 MW | 100.000-600.000 € | Baja al inicio (licitación lenta) |

Los tickets son órdenes de magnitud de mercado del fundador y de referencias generales; no se ha leído ninguna lista de precios en página. Se validan con las tres primeras ofertas reales.

### 2.3 Fuentes de oferta

| Fuente | Qué ofrece | Facilidad de acceso [HIPÓTESIS] |
|---|---|---|
| Fabricantes ibéricos (Gedelsa, Jesiva, Ormazabal, Imefy, Cotradis, Alkargo, Efacec) | Slots cancelados, unidades de stock, pedidos anulados | Media: quieren vender, pero protegen su cliente directo |
| Utilities y distribuidoras que renuevan parque | Unidades retiradas en buen estado, con historial | Baja al principio: procesos de desinversión lentos; alta si entras por el asset manager |
| EPC y promotores con proyectos cancelados o retrasados | Equipo pedido que ya no necesitan, a veces ya fabricado | Alta: tienen capital inmovilizado y quieren salir |
| Talleres de reparación y reacondicionamiento | Unidades reacondicionadas con ensayos | Alta: son vendedores naturales y necesitan canal |
| Brokers y marketplaces europeos y de EE. UU. (Surplus Record, Machinio, Kitmondo, Exapro) | Inventario listado, frecuentemente en EE. UU. con tensiones y frecuencia de 60 Hz | Alta para listar, baja para equipo compatible con 50 Hz y tensiones europeas |
| Alquiladores de gensets (Aggreko, Genesal, Himoinsa canal alquiler) | Disponibilidad inmediata en alquiler; venta de flota renovada | Media: alternativa al cliente más que fuente; útil como solución puente |

Riesgo de oferta: es la variable menos verificada del plan. Si en 2 semanas no aparecen al menos 3 vendedores con equipo real, el negocio no es "broker" sino "agente de compras" (ver pivotes en sección 12).

### 2.4 Competencia y sustitutos

- **Marketplaces de usado industrial** (Surplus Record, Machinio, Kitmondo, Exapro): listan, no cualifican técnicamente ni acompañan la operación. Son fuente de oferta para nosotros tanto como competencia.
- **Brokers especializados en transformadores** en EE. UU. y Reino Unido: existen, pero operan en 60 Hz y en sus mercados. No he verificado ninguno con actividad en Iberia. No puedo confirmar que no los haya.
- **Fabricantes con stock o canal de reacondicionado propio**: Siemens Energy cobra "reservation fees" para asegurar slots [VERIFICADO, nota 05-08-2026]. Esto confirma que el plazo tiene precio, pero también que el fabricante monetiza la escasez directamente.
- **Alquiler** (Aggreko, Genesal): sustituto para gensets; para transformadores de potencia el alquiler de subestación móvil existe (Ormazabal e Ingeteam para Iberdrola "para asegurar plazos" [FRAGMENTO]) pero es caro y temporal.
- **El propio comprador buscando en LinkedIn**: el sustituto real. Nuestra respuesta: le ahorramos 40 horas y le filtramos la chatarra.

---

## 3. Propuesta de valor y oferta

### 3.1 Para el comprador

"Te digo en 72 horas si existe en Europa un equipo compatible con tu especificación disponible en menos de 12 meses, con ficha técnica, ensayos y precio. Si no existe, te lo digo también y no te cobro nada."

### 3.2 Para el vendedor

"Te traigo un comprador cualificado con proyecto, presupuesto y fecha, para un equipo que tienes parado. Cobro solo si se firma."

### 3.3 Catálogo de servicios (fase 1 y fase 2)

| Servicio | Fase | Precio [HIPÓTESIS] | Quién paga |
|---|---|---|---|
| Intermediación a éxito | 1 | 4-6 % del precio de venta del equipo; mínimo 3.000 € | Vendedor por defecto; comprador si el vendedor no acepta comisión |
| Búsqueda bajo mandato (retainer) | 1 si no hay oferta | 1.500-3.000 € por búsqueda, descontable de la comisión si se cierra | Comprador |
| Inspección técnica previa (visita, revisión de ensayos, informe) | 2 | 1.200-2.500 € + desplazamiento | Comprador |
| Gestión de la operación (contrato, Incoterms, transporte, puesta en marcha con tercero) | 2 | 1-2 % adicional | Comprador |
| Representación comercial de un vendedor con stock recurrente | 2 | 3-5 % con exclusividad por zona | Vendedor |

La comisión 4-6 % es hipótesis construida así: por debajo del 3 % no compensa el tiempo por operación (ver 8.4); por encima del 8 % el comprador prefiere buscar solo. Se fija por escrito en el primer cruce y se ajusta con los datos de las 3 primeras operaciones.

---

## 4. Modelo de negocio y flujo de una operación

### 4.1 Flujo tipo (de la necesidad a la comisión)

1. **Captación de necesidad** (correo frío, LinkedIn, referidos). Dato mínimo: tipo, potencia, tensiones, grupo de conexión, fecha límite, acepta reacondicionado sí/no, presupuesto orientativo.
2. **Registro** en la hoja de necesidades. Un identificador por necesidad.
3. **Búsqueda** en la hoja de disponibilidades y, si no hay, correo dirigido a vendedores con la especificación anonimizada.
4. **Pre-cualificación técnica** del equipo candidato: ficha, protocolo de ensayos en fábrica, historial de carga, fecha de fabricación, aceite, estado de aislamiento (en reacondicionados), compatibilidad de tensiones y frecuencia, normativa (IEC 60076 para transformadores; IEC 62271 para aparamenta; ISO 8528 para gensets).
5. **Presentación** al comprador con ficha anonimizada del vendedor (hasta que haya acuerdo de comisión firmado, no se revelan nombres: es la única protección real del intermediario).
6. **Acuerdo de intermediación** firmado con la parte que paga (modelo en 6.2).
7. **Puesta en contacto** y llamada a tres. El cierre comercial lo hacen comprador y vendedor; nosotros resolvemos las dudas técnicas y empujamos el calendario.
8. **Firma de compraventa** entre comprador y vendedor.
9. **Facturación de la comisión** al hito pactado: 50 % a la firma del contrato de compraventa y 50 % a la entrega, o 100 % a la firma si el vendedor lo acepta. Nunca a la puesta en marcha: no controlamos esa fecha.

### 4.2 Qué no hacemos nunca

- No tomamos posesión del equipo ni facturamos el equipo. Ni riesgo de inventario, ni IVA sobre 300.000 €, ni responsabilidad de producto.
- No garantizamos el equipo. La garantía es del vendedor o del taller que reacondiciona. Nuestro informe es una opinión técnica, y así se escribe en el contrato.
- No cobramos de las dos partes sin que ambas lo sepan (doble comisión oculta: riesgo legal y reputacional).
- No enviamos desde los dominios de Normach.

---

## 5. Go-to-market

### 5.1 Canal principal: correo frío cualificado

Es lo que Jorge ya hace. Reglas heredadas del HANDOFF (12-10-2026): 25 correos al día por buzón, calentamiento de 2 semanas, SPF, DKIM y DMARC configurados, un contacto por empresa, verificación de correo antes de enviar.

Capacidad mensual por buzón: 25 correos/día × 22 días laborables = **550 correos nuevos al mes** (sin contar seguimientos). Con seguimientos (1 por contacto), la carga real es 1.100 envíos/mes, que excede el límite de 25/día. Por tanto, con un buzón: **275 contactos nuevos al mes + 275 seguimientos**. Con dos buzones (misma persona, dos dominios o dos cuentas en el mismo dominio): 550 contactos nuevos al mes.

Plantillas: las dos del plan de 2 semanas (`plans/Prueba broker equipos electricos - 2 semanas.md`, sección 4). Sin marca, firmadas por Jorge como ingeniero.

### 5.2 Canal secundario: LinkedIn

- Perfil de Jorge reorientado: titular "Ingeniero. Localizo transformadores, celdas y gensets con plazo inferior a 12 meses para proyectos parados por el fabricante".
- 2 publicaciones a la semana con un dato verificado y una pregunta ("¿Cuántos meses de plazo os están dando hoy para un 40 MVA?"). El objetivo no es viralidad sino que el comprador que recibe el correo vea un perfil coherente.
- Sales Navigator para la lista de compradores (cargos de compras y proyectos en EPC, renovables y data centers).

### 5.3 Canal terciario (a partir del mes 3): referidos y asociaciones

- Cada operación cerrada: pedir dos presentaciones.
- Asociaciones sectoriales (UNEF para fotovoltaica, AEE para eólica, Spain DC para centros de datos; sin verificar sus programas de proveedores): asistir, no patrocinar.
- Talleres de reacondicionamiento: acuerdo de representación informal; son el mejor origen de inventario recurrente.

### 5.4 Mensaje y posicionamiento

Posicionamiento en una frase: **"El ingeniero que encuentra el transformador que el fabricante no puede entregar."**

Lo que no decimos: "marketplace", "plataforma", "digital". Los compradores de esta categoría desconfían de las plataformas y confían en las personas con criterio técnico.

### 5.5 Embudo y métricas [HIPÓTESIS, con cálculo]

Tasas supuestas para correo frío B2B industrial muy segmentado, firmado por un ingeniero, sin pedir reunión:

| Etapa | Tasa supuesta | Sobre 550 contactos/mes (2 buzones) |
|---|---|---|
| Entregado | 95 % | 522 |
| Abierto | 45 % | 235 |
| Respuesta (cualquier tipo) | 6 % de entregados | 31 |
| Respuesta con necesidad o equipo concreto | 40 % de respuestas | 12,5 |
| Cruce necesidad-equipo viable | 20 % de necesidades concretas | 2,5 |
| Operación cerrada | 25 % de cruces viables | 0,6 operaciones/mes |

0,6 operaciones/mes × 12 = **7 operaciones en año 1** si el embudo funciona desde el mes 1, lo que no ocurrirá: los dos primeros meses son calentamiento y construcción de listas, y el ciclo de cierre es de 2 a 4 meses. Por eso el escenario base del año 1 fija **6 operaciones**, no 7, y las concentra en los meses 5 a 12.

Si la tasa de respuesta real es del 2 % en vez del 6 % (plausible en frío sin marca), el embudo cae a 0,2 operaciones/mes → 2 al año: ese es el escenario pesimista. La prueba de 2 semanas mide la tasa de respuesta real con 100 contactos; es el dato más importante del plan.

---

## 6. Operaciones, legal y riesgo técnico

### 6.1 Forma jurídica y fiscalidad (España) [verificar con gestoría antes de facturar]

- **Arranque como autónomo** (empresario individual), epígrafe IAE de intermediarios del comercio (agrupación 51 del IAE, "agentes comerciales e intermediarios"; confirmar epígrafe exacto con la gestoría). Pasar a SL cuando la facturación anual supere los 60.000-80.000 € o cuando un cliente grande exija contratar con sociedad.
- **IVA**: la comisión de intermediación es una prestación de servicios al 21 % en España. Si el cliente que paga está en otro Estado miembro y es empresario, aplica la inversión del sujeto pasivo (factura sin IVA, con mención a la regla de localización). Fuera de la UE, no sujeto. Confirmar con gestoría caso a caso.
- **Situación personal de Jorge.** Jorge está actualmente de baja. Iniciar una actividad económica y facturar durante una incapacidad temporal o un permiso por nacimiento puede ser incompatible con la prestación y tener consecuencias con la Seguridad Social. No puedo confirmar su situación concreta ni la compatibilidad. **Es el primer punto a resolver con la gestoría antes de emitir la primera factura.** Hasta entonces, la prueba de 2 semanas puede hacerse (no factura nada), pero el cierre de una operación con cobro, no.
- **Cuota de autónomos**: en 2026 existe una tarifa reducida para nuevos autónomos durante los primeros 12 meses (importe a confirmar en la Seguridad Social; en 2025 era de 80 €/mes). El plan usa 90 €/mes el año 1 y 320 €/mes el año 2 [HIPÓTESIS].

### 6.2 Contrato de intermediación (lo que protege el ingreso)

La figura en España es el contrato de mediación o corretaje, atípico, reconocido por la jurisprudencia del Tribunal Supremo: el mediador cobra si la operación se perfecciona por su gestión, aunque no intervenga en la firma. Si la relación con un vendedor se hace estable y continuada, pasa a ser contrato de agencia (Ley 12/1992), con indemnización por clientela al finalizar: evitarlo salvo que se quiera deliberadamente.

Cláusulas mínimas del modelo (redactar con abogado; coste estimado 400-800 € una sola vez [HIPÓTESIS]):
1. Identificación de la operación (equipo, número de serie si existe, partes).
2. Comisión: porcentaje, base (precio del equipo sin IVA, sin transporte), mínimo, hitos de pago.
3. **Protección frente al rodeo**: la comisión se devenga si comprador y vendedor presentados por el intermediario cierran entre sí en los 18 meses siguientes a la presentación, aunque sea otro equipo.
4. Confidencialidad bidireccional hasta la firma del acuerdo de comisión.
5. Exclusión de responsabilidad sobre el estado del equipo: el informe técnico es opinión; la garantía es del vendedor.
6. Ley española y tribunales de Madrid (o arbitraje si la operación es internacional).

### 6.3 Seguro

Responsabilidad civil profesional para actividad de intermediación y asesoramiento técnico, 300.000-600.000 € de cobertura: prima estimada 600-1.500 €/año [HIPÓTESIS, pedir tres cotizaciones]. No contratar hasta que la prueba dé luz verde.

### 6.4 Due diligence técnica mínima por equipo

Transformadores:
- Placa de características completa y protocolo de ensayos de fábrica (IEC 60076): relación, pérdidas en vacío y en carga, impedancia, ensayos dieléctricos.
- Año de fabricación, horas o años en servicio, historial de carga y de averías.
- En usados: análisis de aceite (gases disueltos, humedad, acidez), factor de potencia del aislamiento, relación de transformación, resistencia de arrollamientos. Si el vendedor no los tiene, se encargan a un laboratorio a cargo del comprador (300-1.500 € [HIPÓTESIS]).
- Compatibilidad: tensiones, grupo de conexión, frecuencia 50 Hz, regulación, nivel de ruido si hay límite municipal, dimensiones y peso para transporte.

Aparamenta MT/AT:
- Tensión asignada, corriente de cortocircuito, tipo de aislamiento (SF6 frente a aire o vacío: restricciones crecientes al SF6 en la UE, verificar el reglamento de gases fluorados vigente antes de intermediar aparamenta con SF6).

Gensets y turbinas:
- Potencia PRP y standby (ISO 8528), horas, fabricante del motor y del alternador, cumplimiento de emisiones (Stage V en la UE para motores nuevos; equipos usados pueden no cumplir y limitar su uso).

### 6.5 Logística y comercio

- Incoterms recomendados: EXW o FCA en el origen. El transporte de un transformador de 40 MVA es un transporte especial (peso, permisos de ruta); lo contrata el comprador con un transportista especializado. Nosotros solo lo ponemos en contacto.
- Importación desde fuera de la UE (EE. UU., Turquía, China): aranceles, marcado CE (los transformadores de potencia están bajo la Directiva de Baja Tensión y el Reglamento de Ecodiseño 548/2014 para transformadores nuevos puestos en el mercado de la UE; un equipo de 60 Hz no sirve). Al principio, limitar el alcance a equipo ya en la UE y a 50 Hz.

### 6.6 Herramientas de operación

| Herramienta | Uso | Coste mensual [HIPÓTESIS] |
|---|---|---|
| Dominio propio (.com o .es) | Correo | 1-2 € (anual prorrateado) |
| Google Workspace, 1-2 buzones | Correo y hojas | 7-14 € |
| Apollo (plan de pago básico) | Listas, verificación, secuencias | 50-100 € |
| LinkedIn Sales Navigator | Lista de compradores | 90-110 € |
| Herramienta de calentamiento de buzón | Entregabilidad | 20-40 € |
| Hoja de cálculo o Notion | Registro de necesidades y disponibilidades | 0 |
| Firma electrónica (para contratos de comisión) | Cierre | 0-15 € |
| **Total herramientas** | | **170-280 €/mes** |

---

## 7. Equipo y organización

**Año 1: Jorge solo.** Dedicación estimada: 10-15 horas semanales durante la prueba y los primeros 90 días; 20-30 horas semanales a partir de la primera operación cerrada.

Reparto de tiempo semanal en régimen (20 h) [HIPÓTESIS]:
- Prospección y seguimiento de correos: 6 h.
- Cualificación técnica de equipos y necesidades: 5 h.
- Llamadas de 15 minutos con compradores y vendedores: 4 h.
- Gestión de operaciones en curso y contratos: 3 h.
- LinkedIn y contenido: 2 h.

**Lo que no se delega:** la llamada técnica. Es donde se gana la confianza y donde se detecta que el "transformador disponible" es chatarra. Jorge ha dicho que le falta el closer; en este negocio el closer es el ingeniero, porque el comprador cierra cuando confía en la ficha, no cuando le presionan.

**Año 2, solo si hay ≥8 operaciones cerradas en año 1:** una persona a tiempo parcial (10-15 h/semana, 600-900 €/mes) para prospección y mantenimiento de listas, o un segundo ingeniero a comisión (30 % de la comisión de las operaciones que origine) para ampliar a Francia e Italia.

---

## 8. Finanzas: unit economics, CAC, escenarios

### 8.1 Costes fijos

| Partida | Año 1 (€) | Año 2 (€) | Nota |
|---|---|---|---|
| Herramientas (sección 6.6), 12 meses | 2.700 | 3.300 | 225 €/mes medio año 1; 275 € año 2 con 2 buzones |
| Cuota de autónomos | 1.080 | 3.840 | 90 €/mes tarifa reducida año 1; 320 €/mes año 2 [HIPÓTESIS, confirmar] |
| Gestoría | 900 | 1.200 | 75-100 €/mes |
| Seguro RC profesional | 900 | 1.200 | Solo tras luz verde |
| Abogado: modelo de contrato | 600 | 0 | Una vez |
| Desplazamientos a inspecciones | 1.200 | 2.400 | 4-8 visitas/año a 300 € |
| Dominio, web de una página, LinkedIn Premium incluido en SN | 300 | 300 | |
| Imprevistos (10 %) | 770 | 1.220 | |
| **Total fijos** | **8.450** | **13.460** | Coincide con la cabecera |

Escenario pesimista año 1 (sin seguro ni abogado porque no se cierra): 6.600 €. Optimista año 1 (segundo buzón, más viajes): 12.000 €.

### 8.2 Costes variables por operación

- Laboratorio o inspección externa: pagada por el comprador; si la anticipamos, 300-1.500 €.
- Comisión a terceros que aporten el contacto (finder's fee): 10-20 % de nuestra comisión cuando aplique.
- Tiempo: ver 8.4.

### 8.3 CAC: coste de adquisición por operación cerrada

Definición usada: coste en dinero de prospección y herramientas dividido por operaciones cerradas en el periodo, sin valorar el tiempo del fundador. Cálculo con el embudo de 5.5 en escenario base:

- Coste mensual de prospección (herramientas + calentamiento + verificación): 225 €.
- Operaciones por mes en régimen: 0,6.
- **CAC monetario = 225 / 0,6 = 375 € por operación cerrada.**

Con el tiempo valorado a 50 €/h [HIPÓTESIS, coste de oportunidad de un ingeniero senior]:
- Horas de prospección y cualificación al mes: 11 h/semana × 4,3 = 47 h → 2.365 €.
- **CAC con tiempo = (225 + 2.365) / 0,6 = 4.317 € por operación.**

Comparado con el ingreso base por operación (12.500 €): ratio ingreso/CAC con tiempo = 2,9. Es un negocio viable si la tasa de respuesta se sostiene; si cae al 2 %, el CAC con tiempo sube a 12.950 € y el negocio deja de pagar el tiempo del fundador. Esa es la frontera de muerte.

### 8.4 Horas por operación y comisión mínima

Horas estimadas por operación cerrada (cualificación, llamadas, contrato, seguimiento hasta entrega): 25-40 h [HIPÓTESIS]. A 50 €/h: 1.250-2.000 €. Más la parte proporcional del CAC. Por eso el **mínimo de comisión es 3.000 €** aunque el equipo sea pequeño: por debajo, se pierde dinero en tiempo.

Operación de 60.000 € (transformador 2,5 MVA usado) a 5 % = 3.000 €: justo en el mínimo. Operación de 400.000 € a 5 % = 20.000 €: aquí está el negocio. Consecuencia estratégica: **priorizar necesidades ≥10 MVA y gensets ≥1 MW**; aceptar pequeñas solo para alimentar la base de datos y la reputación.

### 8.5 Escenarios a 24 meses (cálculo)

Supuestos por escenario:

| Variable | Pesimista | Base | Optimista |
|---|---|---|---|
| Tasa de respuesta a correo frío | 2 % | 6 % | 9 % |
| Operaciones año 1 | 2 | 6 | 12 |
| Operaciones año 2 | 4 | 14 | 30 |
| Ticket medio | 120.000 € | 250.000 € | 450.000 € |
| Comisión media | 4 % | 5 % | 6 % |
| Ingreso por operación | 4.800 € | 12.500 € | 27.000 € |

Resultados:

| | Pesimista | Base | Optimista |
|---|---|---|---|
| Ingresos año 1 | 2 × 4.800 = 9.600 € | 6 × 12.500 = 75.000 € | 12 × 27.000 = 324.000 € |
| Fijos año 1 | 6.600 € | 8.450 € | 12.000 € |
| Resultado año 1 | 3.000 € | 66.550 € | 312.000 € |
| Ingresos año 2 | 4 × 4.800 = 19.200 € | 14 × 12.500 = 175.000 € | 30 × 27.000 = 810.000 € |
| Fijos año 2 | 9.000 € | 13.460 € | 13.460 € + 10.800 € (apoyo a tiempo parcial) = 24.260 € |
| Resultado año 2 | 10.200 € | 161.540 € | 785.740 € |

Advertencias sobre la tabla:
- El optimista supone 30 operaciones en un año con una persona y media: 2,5 cierres al mes con tickets de 450.000 €. Exige inventario recurrente (talleres o un fabricante representado) y, probablemente, salir de Iberia. Lo incluyo para marcar el techo, no como objetivo.
- El base del año 2 supera el SOM calculado en 2.1 (90.000 €). Una de las dos estimaciones está mal; sabremos cuál en el mes 6.
- Ningún escenario incluye IRPF. Sobre 66.550 € de rendimiento neto, el IRPF de un autónomo en Madrid sin otras rentas estaría en torno al 25-30 % efectivo [HIPÓTESIS, depende de la situación personal; calcular con gestoría].

### 8.6 Caja y punto de equilibrio

- Inversión inicial antes del primer cobro: herramientas 3 meses (675 €) + dominio (15 €) = **~700 €**. Si hay luz verde: + abogado (600 €) + seguro (900 €) = **2.200 € acumulados** antes de la primera comisión.
- Punto de equilibrio sobre fijos del año 1 (8.450 €): 8.450 / 12.500 = **0,7 operaciones base**. Una operación cubre el año. El riesgo no es de caja; es de tiempo del fundador sin retorno.
- Cobro: 50 % a la firma de la compraventa, 50 % a la entrega. Con ciclos de 2-4 meses, la primera caja llega en el mes 4-6 desde el inicio. Jorge necesita otra fuente de ingresos (Normach) hasta entonces; el plan lo asume.

---

## 9. Riesgos y mitigación

| Riesgo | Probabilidad [HIPÓTESIS] | Impacto | Mitigación |
|---|---|---|---|
| No aparece oferta accesible (vendedores no responden o no tienen equipo) | Alta | Mata el modelo broker | Pivote a agente de compras con retainer (sección 12); representar talleres de reacondicionado |
| Tasa de respuesta de compradores <2 % | Media | Embudo insuficiente | Cambiar canal a LinkedIn + llamada; pedir presentaciones a contactos de Airbus/Siemens; aumentar segmentación |
| Rodeo: comprador y vendedor cierran sin pagar | Media | Pérdida de la comisión | Anonimato hasta firma del acuerdo; cláusula de 18 meses; cobrar 50 % a la firma |
| Equipo defectuoso tras la venta y reclamación al intermediario | Baja-media | Legal y reputacional | Contrato con exclusión expresa; informe como opinión; seguro RC; no intermediar sin protocolo de ensayos |
| Incompatibilidad con la situación de baja de Jorge | Desconocida | Legal y económico personal | Consultar gestoría antes de facturar; la prueba no factura |
| Fabricantes alivian plazos antes de lo previsto | Baja hasta 2029 | Cierra la ventana | Capacidad nueva de Hitachi en 2029 [VERIFICADO]; ampliar a gensets y data centers, donde el ciclo es más largo |
| Dependencia de un solo canal (correo frío) y de la entregabilidad | Media | Para la prospección | Dos buzones, calentamiento, LinkedIn en paralelo |
| Confusión con Normach o uso de sus activos | Baja | Marca y deliverability | Dominio y cuentas separados desde el día 1 |
| Jorge sin tiempo (recién nacido, Normach, baja) | Alta | Ejecución | Plan de 10-15 h/semana; umbrales de cierre claros; no empezar si no hay 10 h/semana garantizadas |

---

## 10. Plan de 90 días

### Días 1-14: prueba de 2 semanas (ya definida en `plans/Prueba broker equipos electricos - 2 semanas.md`)
- Registrar dominio, crear buzón, configurar SPF/DKIM/DMARC, iniciar calentamiento.
- Construir listas en Apollo y Sales Navigator desde la sesión local: 50 compradores + 50 vendedores.
- Consultar a la gestoría la compatibilidad de la actividad con la situación de baja.
- Al terminar el calentamiento, enviar los 100 correos (25/día durante 4 días) y seguimientos al cuarto día.
- **Decisión día 14** según umbrales: ≥5 compradores con necesidad concreta y ≥3 vendedores con equipo real → seguir.

### Días 15-45: primer cruce y contrato
- Redactar y firmar el modelo de contrato de intermediación (abogado).
- Cerrar el primer cruce: llamada técnica con cada parte, ficha, presentación anonimizada, acuerdo de comisión firmado.
- Escalar prospección a 275 contactos nuevos al mes (1 buzón) y empezar el segundo buzón.
- Primeras 4 publicaciones en LinkedIn.
- KPI al día 45: 1 acuerdo de comisión firmado; ≥15 necesidades registradas; ≥8 equipos disponibles registrados.

### Días 46-90: primera operación y máquina
- Acompañar la compraventa del primer cruce hasta la firma. Facturar el 50 %.
- Contratar seguro RC.
- Formalizar relación con 2 talleres de reacondicionado o 1 fabricante con stock.
- Segundo buzón operativo: 550 contactos nuevos al mes.
- Definir nombre y marca (solo ahora).
- KPI al día 90: 1 operación con compraventa firmada y 50 % cobrado; ≥30 necesidades; ≥15 equipos; tasa de respuesta medida sobre ≥500 correos.

---

## 11. KPIs y cuadro de mando

Semanal:
- Correos enviados, entregados, respondidos (tasa de respuesta real frente al 6 % supuesto).
- Necesidades nuevas registradas y equipos nuevos registrados.
- Cruces viables identificados.

Mensual:
- Acuerdos de comisión firmados.
- Operaciones con compraventa firmada.
- Comisión facturada y cobrada.
- Ticket medio y comisión media reales (sustituyen a las hipótesis de la sección 8).
- Horas dedicadas (para recalcular el CAC con tiempo).

Trimestral:
- Revisión de escenario: ¿pesimista, base u optimista? Ajustar el plan al que digan los datos, no al que apetezca.

---

## 12. Criterios de continuación, pivote y cierre

| Momento | Señal | Decisión |
|---|---|---|
| Día 14 | ≥5 compradores con necesidad concreta Y ≥3 vendedores con equipo real | Seguir con el plan |
| Día 14 | Compradores sí, vendedores no | Pivote A: agente de compras. El comprador paga retainer 1.500-3.000 € por búsqueda; se busca en marketplaces y fabricantes europeos |
| Día 14 | Vendedores sí, compradores no | Pivote B: representación comercial de 1-2 vendedores con stock, a comisión con exclusividad por zona |
| Día 14 | Ninguno | Cerrar. Gasto total <700 €. Siguiente prueba de venta: idea 2 |
| Día 90 | Ninguna compraventa firmada pero ≥2 acuerdos de comisión en curso | Extender 60 días; no ampliar gasto |
| Día 90 | Ninguna compraventa firmada y ningún acuerdo de comisión | Cerrar o pivotar a A o B según dónde haya respuesta |
| Mes 12 | <3 operaciones cerradas | Cerrar o reducir a actividad oportunista sin herramientas de pago |
| Mes 12 | ≥8 operaciones cerradas | Contratar apoyo; ampliar a Francia e Italia; estudiar SL |

---

## 13. Lo que necesito de Jorge para arrancar (en este orden)

1. Confirmar con la gestoría la compatibilidad de la actividad con la baja. Si no es compatible, la prueba de 2 semanas sigue siendo válida (no factura), pero el calendario de cierre se desplaza al fin de la baja.
2. Dominio nuevo, buzón de Workspace, SPF/DKIM/DMARC y calentamiento. Dos semanas.
3. Exportar 50 + 50 contactos verificados desde Apollo y Sales Navigator en la sesión local, con el ICP del plan de 2 semanas (sección 3).
4. Comprometer la llamada de 15 minutos con cada parte cuando haya cruce. Sin esto, no hay negocio.
5. Diez horas a la semana durante 90 días.

---

## 14. Fuentes verificadas en página (22-10-2026)

| Dato | Fuente | URL |
|---|---|---|
| GSU >160 semanas 1T 2026 vs 143 en 2024; interruptores AT 125 vs 77 | Reuters vía AJOT, 09-07-2026, citando a Wood Mackenzie | ver `verificacion_energia_red.md`, fila A1 |
| Precios +77 % potencia, +45 % GSU desde 2019; 128/144 semanas en 2T 2025 | POWER, 02-01-2026 | https://www.powermag.com/transformers-in-2026-shortage-scramble-or-self-inflicted-crisis |
| Precios EE. UU. +79 %; plazos ≥100 MVA más que duplicados | pv magazine Latam, 27-02-2026 (BNEF) | https://www.pv-magazine-latam.com/2026/02/27/la-transicion-energetica-mundial-se-enfrenta-a-un-cuello-de-botella-en-el-hardware/ |
| Hitachi Energy "cubiertos al menos cuatro años"; 10-12 meses → 3-4 años; mercado ≈30.000 M€ | El Español/Invertia, 23-06-2026 | https://www.elespanol.com/invertia/empresas/energia/20260623/congestion-fabricantes-material-red-electrica-completo-pedidos-proximos-anos/1003744295811_0.html |
| Siemens Energy Grid Technologies backlog 51.000 M€, book-to-bill 1,48; reservation fees | Nota oficial Siemens Energy, 05-08-2026 | ver `verificacion_energia_red.md` |
| GE Vernova Electrification pedidos 6.300 M$ (+66 %), backlog 40.600 M$; 116 GW turbinas vs 20 GW/año | 8-K GE Vernova, 22-07-2026 | https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000147/gevpressrelease2q26.htm |
| Eaton backlog 22.800 M$, 68 % en 12 meses; backlog eléctrico +43 % | 10-Q 1T 2026 y 8-K 2T 2026 Eaton | https://www.sec.gov/Archives/edgar/data/0001551182/000155118226000013/etn-20260331.htm ; https://www.sec.gov/Archives/edgar/data/0001551182/000155118226000027/etn06302026exhibit99.htm |
| Caterpillar Power Generation +29 % a 3.098 M$, 212 M$ de precio | 8-K Caterpillar, 04-08-2026 | https://www.sec.gov/Archives/edgar/data/0000018230/000001823026000040/ex991toformcat2q2026earnin.htm |
| Hitachi Energy fábrica Gallman 528 M$, producción desde 2029 | T&D World, 16-09-2026 | https://www.tdworld.com/utility-business/news/55405686/hitachi-energy-selects-mississippi-for-528m-transformer-factory-to-bolster-us-manufacturing-grid-capacity |
| Precios de turbinas +10-20 puntos $/kW en un semestre; 600 $/kW a fin de 2027 | Power Engineering, 23-04-2026 | ver `verificacion_energia_red.md`, fila B3 |

No verificado en página y usado como contexto: Surplus Record >5.000 consultas y >7.500 anuncios [FRAGMENTO]; Cummins "pedidos hasta 2028" [FRAGMENTO]; Ormazabal/Ingeteam subestaciones móviles para Iberdrola [FRAGMENTO].

Ninguna cifra de precio unitario de equipo, comisión de mercado, tasa de respuesta, coste de herramientas, cuota de autónomos o prima de seguro ha sido verificada. Son hipótesis de trabajo y así están marcadas.
