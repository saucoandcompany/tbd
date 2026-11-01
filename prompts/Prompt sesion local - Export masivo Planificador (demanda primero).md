# Prompt para la sesión local: export masivo del Planificador de Google Ads (demanda primero)

Objetivo: construir un conjunto de datos de demanda del universo, no de nuestras hipótesis. Hasta ahora cada ronda medía las 20-40 keywords que a un investigador se le ocurrían. Eso es muestreo con sesgo. Aquí se exportan decenas de miles de keywords con volumen, tendencia, competencia y puja, y el filtro se hace después, sobre datos, con el scorecard del repo.

Cuenta: saucoandcompany@gmail.com > Sauco MCC > cliente HerenciaClara (misma que el 4-10 y el 22-10-2026). No crear campañas ni tocar presupuestos; solo Herramientas > Planificador de palabras clave. Si al salir pide guardar un plan, descartar. Anotar cualquier efecto secundario como en las sesiones anteriores.

Tiempo estimado: 60-90 minutos. Resultado: ficheros CSV en la carpeta `data/planificador/` del repo, un commit por mercado.

## 1. Ajustes comunes antes de cada export

- Herramienta: "Descubre nuevas palabras clave".
- Mercado A: ubicación España, idioma español. Mercado B: ubicación Estados Unidos, idioma inglés. Hacer primero todo el mercado A.
- Periodo: últimos 12 meses (por defecto). No cambiar.
- Red: solo Google (desmarcar partners de búsqueda).
- Filtros dentro del Planificador: ninguno. El filtro lo hago yo después. Si la herramienta limita el número de ideas mostradas, dejar el máximo.
- Descarga: botón "Descargar ideas de palabras clave" > "Archivo CSV" (no Google Sheets). Debe incluir las columnas: palabra clave, promedio de búsquedas mensuales, cambio en 3 meses, cambio interanual, competencia, índice de competencia, puja parte superior rango bajo, puja parte superior rango alto, y las columnas de búsquedas por mes. Si aparece la opción "Incluir desglose mensual", marcarla.
- Nombre del fichero: `AA-MM-DD_mercado_semilla.csv`, por ejemplo `2026-11-02_ES_software.csv`.

## 2. Semillas del mercado A (España, español)

Cada semilla es un export independiente. Introducir las palabras de la semilla en el cuadro "Empieza con palabras clave" (máximo 10 por consulta). Donde pone "sitio web", usar la pestaña "Empieza con un sitio web" con "Usar todo el sitio".

### 2a. Modificadores de intención de herramienta (el núcleo del dataset)

| Semilla | Palabras a introducir |
|---|---|
| software | software, programa, programa para, software para, software gestión |
| plantilla | plantilla, plantilla excel, modelo de, formulario, ejemplo de |
| app | app, aplicación, app para, herramienta online, online gratis |
| calculadora | calculadora, calcular, simulador, comparador, generador |
| obligatorio | obligatorio, obligatorio 2027, nueva ley, normativa, reglamento |
| plazo | plazo, fecha límite, antes del, sanción, multa por |
| alternativa | alternativa a, alternativas, vs, mejor que, sustituto |
| precio | precio, cuánto cuesta, tarifa, presupuesto, cuota |

### 2b. Sitios web como semilla (categorías enteras de software y servicios)

| Semilla | Sitio |
|---|---|
| capterra | capterra.es |
| getapp | getapp.es |
| softwaredoit | softwaredoit.es |
| appvizer | appvizer.es |
| habitissimo | habitissimo.es |
| cronoshare | cronoshare.com |
| boe | boe.es (si el Planificador lo rechaza por tamaño, usar boe.es/legislacion) |
| aeat | sede.agenciatributaria.gob.es |
| seguridad social | seg-social.es |
| industria | industria.gob.es |
| aemps | aemps.gob.es |
| aepd | aepd.es |

### 2c. Sectores de tu experiencia (ingeniería, industria, calidad)

| Semilla | Palabras |
|---|---|
| máquinas | marcado ce, expediente técnico, declaración de conformidad, evaluación de riesgos, directiva máquinas, reglamento máquinas, seguridad de máquinas, normas armonizadas |
| calidad | iso 9001, iso 14001, iso 45001, iso 27001, auditoría interna, no conformidad, gestión documental calidad, calibración |
| industrial | plc, scada, mantenimiento industrial, gmao, cmms, automatización industrial, retrofit, ciberseguridad industrial |
| aeronáutica | en 9100, as9100, part 21, part 145, aeronáutica proveedor, nadcap, certificación aeronáutica |
| ue | cra, cyber resilience act, ai act, cbam, ppwr, pasaporte digital, due diligence, csrd |

### 2d. Pyme y autónomo España

| Semilla | Palabras |
|---|---|
| fiscal | verifactu, factura electrónica, modelo 303, modelo 390, autónomo gastos, cuota autónomos 2027, notificaciones electrónicas, certificado digital |
| laboral | registro horario, nómina, convenio, despido, baja médica, prevención riesgos laborales, plan de igualdad, protocolo acoso |
| gestoría | gestoría online, asesoría, contable, programa gestoría, software asesoría, portal cliente gestoría |

## 3. Semillas del mercado B (Estados Unidos, inglés)

Solo después de terminar el mercado A. Las mismas lentes traducidas; los sitios cambian.

| Semilla | Palabras o sitio |
|---|---|
| software | software, software for, tool, tool for, platform, app for |
| template | template, template excel, spreadsheet, checklist, generator, calculator |
| compliance | compliance, required by law, deadline, regulation, penalty, new rule 2027 |
| alternative | alternative to, alternatives, vs, replace, cheaper than |
| capterra | capterra.com |
| g2 | g2.com |
| producthunt | producthunt.com |
| machinery | ce marking, machinery regulation, risk assessment iso 12100, declaration of conformity, technical file, ul 508a, nfpa 79 |
| quality | iso 9001, as9100, calibration software, cmms, quality management, nonconformance |
| eu | cyber resilience act, eu ai act, cbam, eudr, ppwr, digital product passport, nis2 |

## 4. Después de cada export

1. Guardar el CSV en `data/planificador/` con el nombre indicado.
2. Al terminar un mercado: `git add data/planificador/ && git commit -m "Planificador: export masivo mercado A (España)" && git push`.
3. Anotar en un fichero `data/planificador/LEEME.md`: fecha, cuenta, mercado, número de filas por fichero, y cualquier aviso del Planificador (límite de ideas, semilla rechazada).

## 5. Lo que hago yo con los datos (para que sepas qué sale de esto)

Pipeline sobre todos los CSV unidos y sin duplicados:

1. Filtro duro: volumen España ≥200/mes (EE. UU. ≥2.000), cambio a 3 meses ≥0 %, puja alta ≥1 € (hay alguien pagando por ese clic: intención comercial), competencia de anuncios baja o media. Quitar marcas registradas y términos de medicamentos con receta.
2. Clasificación de intención por palabra: herramienta, plantilla, servicio, información, compra. Solo pasan herramienta, plantilla y servicio.
3. Comprobación de oferta: para cada grupo que pase, abro los 10 primeros resultados y anoto si existe autoservicio con tarjeta, su precio, y si el líder tiene reseñas. "Sin oferta autoservicio" es la señal, no "sin competencia".
4. Scorecard de 10 criterios con umbral (demanda, tendencia, intención comercial, puja, ausencia de autoservicio, fecha o disparador, foso de retención, construible solo, sin reuniones, sin título requerido). Cada candidato recibe una nota numérica, no un juicio de investigador.
5. Entrega: tabla con todos los grupos que pasen el filtro duro, ordenada por nota, con las keywords, volúmenes y la oferta encontrada. Normach reposicionada entra en la misma tabla como un candidato más.

## 6. Límites de este método, para no engañarnos

- El Planificador agrupa volúmenes en tramos y promedia 12 meses; para keywords con menos de 1.000 búsquedas el redondeo es grueso.
- "Competencia baja" mide anunciantes, no resultados orgánicos ni productos.
- Demanda alta no significa demanda desatendida; el paso 3 es el que separa una cosa de otra.
- Una herramienta que nadie busca por nombre puede tener demanda enorme por su síntoma. Por eso las semillas incluyen "obligatorio", "plazo", "multa", "alternativa a".
- Si quieres el universo completo de verdad, hace falta una base de datos de keywords de pago (Semrush o Ahrefs, 100-130 €/mes, o DataForSEO por consumo, céntimos por mil keywords). El Planificador con 40-50 semillas se acerca sin coste.
