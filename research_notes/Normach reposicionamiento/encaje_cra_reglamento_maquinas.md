# Encaje entre el Reglamento de Ciberresiliencia (CRA, Reg. (UE) 2024/2847) y el Reglamento de Máquinas (Reg. (UE) 2023/1230), artículo por artículo

Fecha: 25-10-2026. Método: descarga del texto íntegro en español de ambos reglamentos desde EUR-Lex con Chromium (CRA: CELEX 32024R2847, 396.889 caracteres; Reglamento de Máquinas consolidado con la corrección de errores: CELEX 02023R1230-20230629, 316.406 caracteres) y búsqueda de todas las referencias cruzadas. Todo lo citado abajo está leído en el texto legal [ABIERTA]; lo que es interpretación mía va marcado como [INTERPRETACIÓN]. Ficheros de trabajo en el scratchpad de la sesión (`eurlex/cra_es.txt`, `eurlex/maq_es_consol.txt`).

## 0. Veredicto en cinco líneas

1. **No existe ningún artículo puente.** El CRA menciona al Reglamento de Máquinas una sola vez en todo su texto articulado y anexos: cero veces. La única mención es el **considerando 53** (más la nota al pie 24). Un considerando no crea derechos ni presunciones.
2. **Los dos se aplican acumulativamente** a una máquina con elementos digitales y conexión de datos. El considerando 53 lo dice literalmente: el fabricante "debe cumplir tanto los requisitos esenciales de ciberseguridad establecidos en el presente Reglamento como los requisitos esenciales de ciberseguridad de salud y seguridad establecidos en el Reglamento (UE) 2023/1230", y "debe seguir los procedimientos de evaluación de la conformidad aplicables establecidos en el presente Reglamento y en el Reglamento (UE) 2023/1230".
3. **La presunción de conformidad del Reglamento de Máquinas (art. 20.9) no cubre al CRA.** Solo presume conformidad con los puntos 1.1.9 y 1.2.1 del anexo III a quien tenga certificado o declaración bajo un **esquema europeo de certificación de ciberseguridad del Reglamento 2019/881**. Cumplir el CRA por autoevaluación (módulo A) no activa esa presunción.
4. **Dos expedientes técnicos, dos declaraciones UE, dos definiciones distintas de "modificación sustancial", dos relojes.** El CRA solo abre la puerta a integrar la evaluación de riesgos de ciberseguridad en la del otro acto para los productos del art. 12 (sistemas de IA de alto riesgo), no para la máquina corriente.
5. **Hay una obligación del CRA ya en vigor para máquinas conectadas en el mercado**: el art. 14 (notificación de vulnerabilidades explotadas e incidentes graves en 24 h / 72 h / 1 mes) se aplica desde el **11-09-2026** y, por el art. 69.3, alcanza a todos los productos con elementos digitales introducidos en el mercado antes del 11-12-2027.

## 1. Fechas de los dos reglamentos (texto legal)

| Hito | Fecha | Fuente |
|---|---|---|
| Reglamento de Máquinas aplicable | **20-01-2027** | Art. 54, párrafo 2, con corrección ►C1◄ (texto original decía 14-01-2027; corrección DOUE 04-07-2023) |
| Derogación de la Directiva 2006/42/CE | 20-01-2027 | Art. 52.2 |
| Productos introducidos conforme a la Directiva antes de esa fecha pueden seguir comercializándose | sin límite, salvo cap. VI (vigilancia) | Art. 53.1 |
| Régimen de sanciones comunicado por los Estados | 20-10-2026 | Art. 50.1 vía art. 54 b) |
| CRA en vigor | 10-12-2024 (20 días tras publicación) | Art. 71.1 |
| CRA: capítulo IV, notificación de organismos de evaluación (arts. 35-51) | 11-06-2026 | Art. 71.2 |
| **CRA: art. 14, notificación de vulnerabilidades explotadas e incidentes graves** | **11-09-2026** | Art. 71.2 |
| CRA aplicable en su totalidad | **11-12-2027** | Art. 71.2 |
| CRA: productos introducidos antes del 11-12-2027 | solo sujetos si sufren modificación sustancial después; **salvo el art. 14, que les aplica a todos** | Art. 69.2 y 69.3 |
| CRA: certificados de examen UE de tipo por ciberseguridad de otra legislación | válidos hasta 11-06-2028 | Art. 69.1 |

## 2. Ámbito: cuándo una máquina entra en el CRA

| Cuestión | Texto | Lectura para un fabricante de maquinaria |
|---|---|---|
| Definición de producto con elementos digitales | CRA art. 3.1: "producto consistente en programas informáticos o equipos informáticos y sus soluciones de procesamiento de datos remoto, incluidos los componentes… que se introduzcan en el mercado por separado" | Una máquina con PLC, HMI, variadores programables o firmware es un producto con elementos digitales. |
| Condición de conexión | CRA art. 2.1: aplicable a los productos "cuya finalidad prevista o uso razonablemente previsible incluya una conexión de datos directa o indirecta, lógica o física, a un dispositivo o red" | [INTERPRETACIÓN] Un puerto Ethernet, USB de diagnóstico, pasarela IoT, mantenimiento remoto o conexión a un SCADA basta. Una máquina puramente electromecánica sin ningún puerto de datos queda fuera. La zona gris es la máquina con puerto pero "no conectada": el criterio es el uso razonablemente previsible, no el uso real. |
| Exclusiones expresas | CRA art. 2.2 a 2.4: productos sanitarios (2017/745, 2017/746), vehículos (2019/2144), aviación (2018/1139), equipos marinos (2014/90) | La maquinaria industrial **no está excluida**. |
| Exclusión sectorial posible | CRA art. 2.5: la Comisión puede limitar o excluir por acto delegado la aplicación a productos regulados por otra norma de la Unión con protección equivalente | No consta en el texto ningún acto delegado para máquinas. No he verificado si se ha adoptado alguno fuera del texto. |
| Piezas de recambio idénticas | CRA art. 2.6: excluidas | Recambios a especificación idéntica no reabren el CRA. |
| Clasificación | CRA arts. 7 y 8 y anexos III y IV. El anexo III final (clases I y II) **no incluye sistemas de automatización industrial ni PLC**; el art. 7.1 añade que integrar un producto del anexo III no convierte a la máquina en producto importante | Una máquina es "producto por defecto": autoevaluación (módulo A, anexo VIII) por el art. 32.1 a). Si el fabricante vende por separado un componente de clase I o II (p. ej. un cortafuegos industrial), ese componente sí va a tercero. |

## 3. Requisitos esenciales: dónde se solapan y dónde no

Reglamento de Máquinas, anexo III (leído íntegro):

- **1.1.9 Protección contra la corrupción**: la conexión con otro dispositivo o remoto no debe provocar situaciones peligrosas; el hardware de conexión relevante para el software esencial de seguridad debe protegerse contra corrupción accidental o intencionada y **recoger pruebas de toda intervención legítima o ilegítima**; el software y los datos esenciales para la seguridad se **indicarán como tales** y se protegerán; la máquina **indicará el software instalado** necesario para funcionar con seguridad y lo hará accesible en todo momento; recogerá pruebas de toda intervención o modificación de ese software o su configuración.
- **1.2.1 Seguridad y fiabilidad de los sistemas de mando**, letra a): resistir "los intentos hostiles razonablemente previsibles de terceros de provocar una situación peligrosa"; letra b): un fallo del hardware o la lógica no debe provocar situaciones peligrosas.

CRA, anexo I (leído íntegro), Parte I (propiedades del producto) y Parte II (gestión de vulnerabilidades).

| Requisito del Reglamento de Máquinas | Requisito del CRA que cubre lo mismo | Lo que el CRA exige además y Máquinas no |
|---|---|---|
| 1.1.9: conexión no debe causar peligro; hardware de conexión protegido | Parte I 2 d) protección contra acceso no autorizado; 2 j) limitar superficies de ataque, incluidas interfaces externas; 2 i) no degradar otros dispositivos o redes | 2 h) disponibilidad frente a denegación de servicio; 2 e) confidencialidad y cifrado; 2 g) minimización de datos; 2 m) borrado seguro |
| 1.1.9: software y datos esenciales identificados y protegidos contra corrupción | Parte I 2 f) integridad de datos, comandos, programas y configuración, con aviso de corrupción | Parte I 2 a) sin vulnerabilidades explotables conocidas al comercializar; 2 b) configuración segura por defecto; 2 c) actualizaciones de seguridad, automáticas por defecto cuando proceda |
| 1.1.9: registro de intervenciones legítimas e ilegítimas y de cambios de software o configuración | Parte I 2 l) registro y seguimiento de la actividad interna, incluido acceso y modificación | El CRA exige un mecanismo de exclusión voluntaria para el usuario; Máquinas exige el registro sin excepción porque es seguridad |
| 1.1.9: la máquina indica el software instalado necesario para la seguridad | Parte II 1): identificar y documentar vulnerabilidades y componentes, con **nomenclatura de materiales de software (SBOM)** legible por máquina | El SBOM es un entregable nuevo que la maquinaria mecánica no tiene |
| 1.2.1 a): resistir intentos hostiles razonablemente previsibles | Parte I 1) nivel adecuado de ciberseguridad según riesgos; 2 k) reducir impacto de incidentes | Todo el bloque de **proceso**: Parte II 2) a 8): corregir vulnerabilidades sin demora, pruebas periódicas, divulgación pública de vulnerabilidades corregidas, **política de divulgación coordinada**, dirección de contacto para reportar, mecanismo seguro de distribución de actualizaciones, actualizaciones gratuitas |
| Sin equivalente en Máquinas | Art. 13.8: **período de soporte mínimo 5 años** (o la vida útil si es menor), fecha final indicada al comprar (art. 13.19); art. 13.9: cada actualización de seguridad disponible **10 años** | Convierte la conformidad en una obligación continua, no en un acto de puesta en el mercado |
| Sin equivalente en Máquinas | Art. 14: notificar a CSIRT coordinador y ENISA por la plataforma única: alerta temprana **24 h**, notificación **72 h**, informe final **1 mes** (incidentes graves) | Vigente desde el 11-09-2026 para todas las máquinas conectadas ya en el mercado (art. 69.3) |

Lectura: el solape real es el núcleo de **integridad, acceso y registro** (1.1.9 y 1.2.1 a) frente a Parte I 2 d, f, j, l). Ahí el considerando 53 reconoce que cumplir el CRA "podría facilitar" cumplir Máquinas, y pide a la Comisión y a los organismos de normalización coherencia y orientaciones. Fuera de ese núcleo, el CRA es un reglamento de **proceso durante toda la vida del producto** y Máquinas es un reglamento de **estado en la puesta en el mercado**. No se sustituyen.

## 4. Procedimientos, documentación y declaraciones

| Elemento | Reglamento de Máquinas | CRA | Encaje |
|---|---|---|---|
| Evaluación de la conformidad | Art. 25: anexo I parte A (incluye **componentes de seguridad y máquinas con aprendizaje automático que garanticen funciones de seguridad**, puntos 5 y 6) → tercero obligatorio (módulos B+C, H o G); parte B → módulo A solo si se aplican normas armonizadas completas; resto → módulo A | Art. 32.1: módulo A por defecto; clase I con normas armonizadas → A, sin ellas → B+C o H; clase II → tercero; anexo IV → certificación 2019/881 | Una máquina conectada "normal": módulo A en los dos. Una máquina con IA en función de seguridad: tercero por Máquinas y, si es IA de alto riesgo, procedimiento del art. 43 del AI Act por el art. 12 del CRA |
| Evaluación de riesgos | Anexo IV A b): evaluación de riesgos de seguridad con lista de requisitos esenciales y medidas | Art. 13.2-13.4: evaluación de riesgos de ciberseguridad, documentada y **actualizada durante el período de soporte**, incluida en la documentación técnica | Art. 13.4 permite integrarla en la evaluación de otro acto **solo** para productos del art. 12 (IA de alto riesgo). Para la máquina corriente son dos evaluaciones; en la práctica pueden compartir el análisis de amenazas [INTERPRETACIÓN], pero cada una debe cubrir sus requisitos |
| Documentación técnica | Anexo IV parte A, letras a) a o): incluye m) código fuente o lógica del software de seguridad a petición motivada, n) descripción de datos de sensores en máquinas autónomas o controladas a distancia | Anexo VII: descripción con versiones de software, arquitectura, **procesos de gestión de vulnerabilidades y SBOM**, evaluación de riesgos de ciberseguridad, justificación del período de soporte, normas aplicadas, informes de pruebas, copia de la declaración | Dos expedientes distintos. Comparten planos, arquitectura y versiones de software; el resto no se solapa |
| Conservación | Art. 10.3: documentación técnica y declaración UE **10 años** desde la introducción en el mercado; declaraciones digitales accesibles en línea 10 años (art. 10.?, líneas 805 y 815 del texto) | Art. 13.13: **10 años** o el período de soporte si es mayor; art. 13.9: actualizaciones disponibles 10 años | Mismo plazo, dos repositorios obligatorios |
| Declaración UE de conformidad | Anexo V parte A | Anexo V del CRA | Dos declaraciones. Ninguna de las dos admite al otro reglamento como presunción |
| Presunción de conformidad | Art. 20.1 normas armonizadas; **art. 20.9 solo esquemas de certificación 2019/881** para 1.1.9 y 1.2.1 | Art. 27 normas armonizadas, especificaciones comunes y esquemas 2019/881 | Autoevaluar el CRA **no** da presunción de 1.1.9 y 1.2.1. Un certificado bajo esquema 2019/881 (p. ej. EUCC) sí la daría, pero son esquemas pensados para productos TIC, no para máquinas [INTERPRETACIÓN] |
| Modificación sustancial | Art. 3: modificación "por medios físicos o digitales" no prevista por el fabricante que afecte a la **seguridad** generando un nuevo peligro o aumentando un riesgo | Art. 3: cambio que afecta al cumplimiento de los requisitos de **ciberseguridad** del anexo I parte I o modifica la finalidad evaluada | Una actualización de software puede ser sustancial para uno y no para el otro. Un retrofit de conectividad en una máquina antigua puede abrir los dos a la vez |
| Instrucciones | Anexo III 1.7.4; art. 10.7 permite formato digital con condiciones | Art. 13.18 y anexo II: información de ciberseguridad al usuario, fecha fin de soporte visible al comprar (art. 13.19) | Dos bloques de instrucciones; pueden ir en el mismo manual |

## 5. Puente con el AI Act

- Reglamento de Máquinas, anexo I parte A puntos 5 y 6: componentes de seguridad y máquinas con comportamiento autoevolutivo por aprendizaje automático que garanticen funciones de seguridad van a tercero (art. 25.2).
- CRA art. 12: si el producto es sistema de IA de alto riesgo (art. 6 del Reg. 2024/1689), cumplir el anexo I del CRA se considera cumplir la ciberseguridad del art. 15 del AI Act, y el procedimiento es el del art. 43 del AI Act con sus organismos notificados.
- Fechas del AI Act de alto riesgo: aplazadas al 02-12-2027 y 02-08-2028 por el Reglamento 2026/1744 según la nota `research_notes/Herramientas odiadas con disparador 2026-2027/regulacion_ue.md` (verificado por el investigador en EUR-Lex el 23-10-2026; no reabierto hoy).

## 6. Lo que no está en el texto y no he verificado

- Si la Comisión ha publicado ya las orientaciones que el considerando 53 le encomienda para fabricantes sujetos a ambos reglamentos.
- Si existe algún acto delegado del art. 2.5 del CRA que limite su aplicación a maquinaria.
- Estado de las normas armonizadas del CRA (CEN/CENELEC) y su relación con las normas de Máquinas para 1.1.9 y 1.2.1.
- Si algún esquema europeo de certificación 2019/881 publicado en el DOUE es aplicable a máquinas a efectos del art. 20.9.

## 7. Implicaciones para el reposicionamiento de Normach

1. **La escalera de fechas para el mismo comprador existe y es más densa de lo que decía**: 11-09-2026 (CRA art. 14, ya en vigor para máquinas conectadas en el mercado), 20-01-2027 (Máquinas), 11-06-2028 (fin de validez de certificados de tipo por ciberseguridad de otra legislación), 11-12-2027 (CRA completo), 02-12-2027 y 02-08-2028 (AI Act alto riesgo).
2. **La falta de puente legal es trabajo, no obstáculo.** Al no haber presunción cruzada, el fabricante necesita dos evaluaciones de riesgos, dos expedientes y dos declaraciones con un núcleo técnico común. Eso es exactamente lo que un servicio puede empaquetar: una sola evaluación de amenazas que alimente los dos expedientes, con trazabilidad a 1.1.9 y 1.2.1 por un lado y al anexo I del CRA por otro.
3. **El CRA obliga a un proceso continuo durante al menos cinco años** (gestión de vulnerabilidades, SBOM vivo, actualizaciones, política de divulgación, notificación en 24 h). Un fabricante de maquinaria con un PLC y una pasarela no tiene nada de eso. Es la base legal de un modelo recurrente: no es que Normach quiera vender suscripción, es que la norma exige mantenimiento documental durante el soporte.
4. **El art. 14 ya vigente es el gancho de entrada hoy**, antes del 20 de enero: cualquier fabricante con máquinas conectadas en campo tiene desde el 11-09-2026 la obligación de poder notificar en 24 horas una vulnerabilidad explotada. Casi ninguno sabe que le aplica. Es verificable en el texto (arts. 14, 69.3 y 71.2) y no depende de interpretaciones de alcance salvo la de "conexión".
5. **Límite del mercado**: máquinas sin ningún puerto de datos quedan fuera del CRA; máquinas con IA en funciones de seguridad son otro producto (tercero obligatorio) y otro precio.
