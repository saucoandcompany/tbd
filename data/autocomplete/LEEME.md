# Universo de demanda por autocompletado de Google (01-11-2026)

Qué es: todas las sugerencias que el autocompletado de Google (client=chrome) devuelve para 111 semillas en España (hl=es, gl=es) y 51 en EE. UU. (hl=en, gl=us), cada semilla sola y con 36 sufijos (" a".." z", " 0".." 9"). 6.051 consultas, 1 error de red, 0 bloqueos. Rastreo en 6 procesos paralelos con pausa de 0,7 s (`tools/demanda/autocomplete_crawl.py`).

Qué NO es: volumen de búsquedas. El autocompletado dice qué consultas existen y en qué orden las propone Google (relevancia 0-1000). El volumen lo da el Planificador de Google Ads a partir de estas listas.

## Ficheros

| Fichero | Contenido |
|---|---|
| `semillas_ES.txt`, `semillas_US.txt` | Semillas (modificadores de intención, sectores de Jorge, pyme España; en inglés las equivalentes) |
| `sugerencias_*.tsv` | Datos brutos: mercado, semilla, consulta, posición, sugerencia, relevancia (76.372 filas) |
| `universo/2026-11-01_universo.csv` | 68.441 sugerencias únicas (ES 44.984, US 23.457) con frecuencia, relevancia media, intención, exclusión y núcleo |
| `universo/2026-11-01_grupos.csv` | 16.038 núcleos (agrupación por sustantivo del problema) |
| `universo/2026-11-01_resumen.md` | Recuento por intención y 60 núcleos con más keywords por mercado |
| `universo/*_para_planificador_ES_compacta_1.csv` (5.800) y `_2.csv` (5.728) | **Lista prioritaria España**: intención herramienta, plantilla o servicio, sin ruido, variantes de relleno colapsadas |
| `universo/*_para_planificador_US_compacta.csv` (7.584) | **Lista prioritaria EE. UU.**, mismo criterio |
| `universo/*_para_planificador_ES_todo_1..5.csv`, `_US_todo_1..3.csv` | Listas completas (todas las intenciones, incluida "otra": síntoma y obligación), en tramos de 10.000 |

## Recuento por intención

| Intención | ES | US |
|---|---|---|
| otra (síntoma, obligación, marca, pregunta) | 30.258 | — |
| herramienta | 7.470 | — |
| plantilla | 5.410 | — |
| servicio | 661 | — |
| empleo | 611 | — |
| información | 438 | — |
| compra física | 136 | — |

(Ver `universo/2026-11-01_resumen.md` para EE. UU.)

## Cómo medir el volumen en el Planificador

1. Google Ads > Herramientas > Planificador de palabras clave > **Consulta el volumen de búsquedas y las previsiones**.
2. Pegar el contenido de una lista (columna Keyword) o usar "Subir un archivo" con el CSV. Un fichero por consulta; límite de 10.000 keywords por consulta.
3. Ubicación España e idioma español para las listas ES; Estados Unidos e inglés para las US. Red: solo Google.
4. En la pestaña "Métricas históricas", descargar CSV (incluir desglose mensual si se ofrece). Guardar en `data/planificador/` con nombre `AAAA-MM-DD_ES_compacta_1.csv` (o `_US_...`).
5. Empezar por las tres listas prioritarias (dos ES, una US). Las ocho listas "todo" son opcionales y añaden la demanda de síntoma ("verifactu obligatorio", "cuota autónomos 2027") que no lleva palabra de herramienta.

Después: `python3 -I tools/demanda/kp_pipeline.py data/planificador reports/universo` produce la tabla ordenada por nota de datos (0-7) con el filtro duro (volumen ≥200 ES / ≥2.000 US, tendencia a 3 meses ≥0, puja alta ≥1 €, intención útil). Los tres criterios que no salen de datos (foso de retención, construible solo, sin título) se revisan a mano sobre los grupos resultantes.

## Límites

- Las semillas siguen siendo una elección. Los sitios web como semilla (Capterra, Habitissimo, BOE, AEAT) del prompt solo pueden usarse dentro del Planificador, no en el autocompletado; esa parte queda para la sesión local.
- El autocompletado está sesgado hacia lo que Google quiere sugerir (filtra marcas, adultos, salud sensible) y mezcla portugués en algunas semillas.
- La clasificación de intención es por expresiones regulares: "programa" captura programas de TV y "plantilla" captura plantillas de fútbol; el filtro de ruido quita lo obvio, el resto lo elimina el volumen o la revisión manual.
- Frecuencia y relevancia no son volumen y no deben usarse para ordenar candidatos finales.
