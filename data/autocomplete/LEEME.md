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

## Hojas de Google Sheets (03-11-2026)

Las listas prioritarias están también como Google Sheets de 2.000 filas en la carpeta de Drive "Demanda primero - Planificador" (cuenta saucoandcompany@gmail.com). Contenido idéntico a `*_para_planificador_ES_compacta_*.csv` y `*_US_compacta.csv`, troceado por orden alfabético. La hoja ES 2 lleva una keyword más (2.001) porque la última de la hoja ES 1 se pasó al principio de la 2.

| Hoja | Filas de keywords | Enlace |
|---|---|---|
| ES prioritaria 1 de 6 | 1.999 | https://docs.google.com/spreadsheets/d/1Hn0HTdBPv45K1yNDCw8hC4jXPrK3w9amhCyhqeS904o |
| ES prioritaria 2 de 6 | 2.001 | https://docs.google.com/spreadsheets/d/13XRH-N2F68bg6LdIDBGmXTAe6LKg5yuuGrQ91H-pF-E |
| ES prioritaria 3 de 6 | 2.000 | https://docs.google.com/spreadsheets/d/11i_-QqoPv8889uPTJBusoOUDWcnOV0puGFS46-Yf5fQ |
| ES prioritaria 4 de 6 | 2.000 | https://docs.google.com/spreadsheets/d/1TWdRUc55zEvMFPWXViqs6E4x4mj3_h6oIeiBXbyhFw8 |
| ES prioritaria 5 de 6 | 2.000 | https://docs.google.com/spreadsheets/d/1p6-c7KYiewi3BTJYxPks8nnGQPViyKB8TGv_UDg227Q |
| ES prioritaria 6 de 6 | 1.528 | https://docs.google.com/spreadsheets/d/1zFUoWOk8NELplTexyLHpPlIYVd65bEcqd9Q7gZiQDjY |
| US prioritaria 1 de 4 | 2.000 | https://docs.google.com/spreadsheets/d/1zN3SjsClcmQYY-_wsKRxRU2oSPGHJOnaRTkLOlUDxvA |
| US prioritaria 2 de 4 | 2.000 | https://docs.google.com/spreadsheets/d/1cCrSSDs2w6kuvxqNjaFBUhWS4ILbhdyIIf6ieyfQogs |
| US prioritaria 3 de 4 | 2.000 | https://docs.google.com/spreadsheets/d/1E_FhI00qSdHdBzISdMemkYdjukvOyqcmVFsHlnPvFXo |
| US prioritaria 4 de 4 | 1.584 | https://docs.google.com/spreadsheets/d/1c6oXL746ukXcf-09bCyCN35DtG5gh65w5JG3mHq1iD0 |

### Aviso de calidad: la lista "prioritaria" es de recall, no de precisión

Al copiarla a las hojas se vio que la lista es mucho más ruidosa de lo que decía el LEEME original: "intención herramienta, plantilla o servicio" se decide por una expresión regular sobre palabras como "app", "programa", "plantilla", "simulador", "generador" o "tool", y esas palabras abren consultas de consumo (plantillas de fútbol, programas de televisión, generadores eléctricos, canciones, zapatos de plataforma). El reparto por origen:

| Mercado | Keywords prioritarias | De semillas de dominio | De semillas genéricas |
|---|---|---|---|
| ES | 12.829 | 2.708 (21 %) | 10.121 (79 %) |
| US | 8.152 | 861 (11 %) | 7.291 (89 %) |

El ruido no estropea la medición (el Planificador da volumen a cada fila y el filtro duro del pipeline descarta lo que no tiene puja ni intención) pero sí cuesta tiempo de revisión. Por eso se generan además tres listas depuradas, solo con keywords que salieron de semillas de dominio (iso, marcado ce, cbam, cmms, gmao, modelo 303/390, registro horario, ppwr, nis2, cra, as9100, etc.):

- `universo/2026-11-01_depurada_dominio_ES_1.csv` (2.000) y `_ES_2.csv` (708)
- `universo/2026-11-01_depurada_dominio_US_1.csv` (861)

Limitación: ese filtro por procedencia deja fuera lo que solo sale de semillas genéricas, que es justo donde estaría un nicho que no hemos imaginado (por ejemplo "software para instaladores electricistas gratis"). Las listas completas siguen siendo la referencia para descubrir; las depuradas sirven para medir rápido lo que ya se sospecha.
