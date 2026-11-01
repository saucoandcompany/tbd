#!/usr/bin/env python3
"""Convierte las sugerencias de autocompletado en (a) un universo deduplicado con intención y núcleo,
(b) listas listas para pegar en el Planificador ("Consulta el volumen de búsquedas") y (c) un resumen.

Uso: python3 -I tools/demanda/autocomplete_universe.py <carpeta data/autocomplete> <salida_prefijo> [max_por_lista=10000]

Frecuencia = número de consultas distintas (semilla+sufijo) que devolvieron la sugerencia.
Relevancia = media de google:suggestrelevance. Ninguna de las dos es volumen: son proxies de existencia e intensidad.
"""
import csv
import glob
import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comun import excluir, intencion, nucleo, ruido  # noqa: E402


def main():
    carpeta, prefijo = sys.argv[1], sys.argv[2]
    max_lista = int(sys.argv[3]) if len(sys.argv) > 3 else 10000
    univ = {}
    consultas = defaultdict(set)
    for path in glob.glob(os.path.join(carpeta, "sugerencias_*.tsv")):
        with open(path, encoding="utf-8") as f:
            for row in csv.DictReader(f, delimiter="\t"):
                s = row["sugerencia"].strip().lower()
                if not s:
                    continue
                key = (row["mercado"], s)
                consultas[key].add(row["consulta"])
                u = univ.setdefault(key, {"mercado": row["mercado"], "keyword": s, "rel_sum": 0.0, "rel_n": 0,
                                          "semillas": set(), "mejor_pos": 99})
                u["semillas"].add(row["semilla"])
                try:
                    u["rel_sum"] += float(row["relevancia"]); u["rel_n"] += 1
                except ValueError:
                    pass
                u["mejor_pos"] = min(u["mejor_pos"], int(row["posicion"]))
    filas = []
    for key, u in univ.items():
        filas.append({
            "mercado": u["mercado"], "keyword": u["keyword"],
            "frecuencia": len(consultas[key]), "n_semillas": len(u["semillas"]),
            "relevancia_media": round(u["rel_sum"] / u["rel_n"], 0) if u["rel_n"] else "",
            "mejor_posicion": u["mejor_pos"],
            "intencion": intencion(u["keyword"]), "excluida": excluir(u["keyword"]) or ruido(u["keyword"]), "nucleo": nucleo(u["keyword"]),
            "semillas": "|".join(sorted(u["semillas"]))[:200],
        })
    filas.sort(key=lambda r: (r["mercado"], -r["frecuencia"], -(float(r["relevancia_media"]) if r["relevancia_media"] != "" else 0)))
    with open(prefijo + "_universo.csv", "w", encoding="utf-8", newline="") as out:
        w = csv.DictWriter(out, fieldnames=list(filas[0].keys()))
        w.writeheader()
        w.writerows(filas)

    # listas para el Planificador: solo intención herramienta/plantilla/servicio y no excluidas
    for m in ("ES", "US"):
        kws = [r["keyword"] for r in filas if r["mercado"] == m and not r["excluida"]
               and r["intencion"] in ("herramienta", "plantilla", "servicio")]
        for i in range(0, len(kws), max_lista):
            parte = kws[i:i + max_lista]
            with open("%s_para_planificador_%s_%d.csv" % (prefijo, m, i // max_lista + 1), "w", encoding="utf-8", newline="") as out:
                w = csv.writer(out)
                w.writerow(["Keyword"])
                for k in parte:
                    w.writerow([k])
        # también la lista completa (todas las intenciones) por si se quiere medir informacion/compra
        with open("%s_para_planificador_%s_todo.csv" % (prefijo, m), "w", encoding="utf-8", newline="") as out:
            w = csv.writer(out)
            w.writerow(["Keyword"])
            for r in filas:
                if r["mercado"] == m and not r["excluida"]:
                    w.writerow([r["keyword"]])

    # resumen por núcleo (solo intenciones útiles)
    grupos = defaultdict(list)
    for r in filas:
        if not r["excluida"] and r["intencion"] in ("herramienta", "plantilla", "servicio"):
            grupos[(r["mercado"], r["nucleo"])].append(r)
    tabla = []
    for (m, nuc), rs in grupos.items():
        tabla.append({"mercado": m, "nucleo": nuc, "n_keywords": len(rs), "frecuencia_total": sum(r["frecuencia"] for r in rs),
                      "intenciones": "|".join(sorted({r["intencion"] for r in rs})),
                      "ejemplos": " | ".join(r["keyword"] for r in sorted(rs, key=lambda x: -x["frecuencia"])[:4])})
    tabla.sort(key=lambda t: (t["mercado"], -t["n_keywords"], -t["frecuencia_total"]))
    with open(prefijo + "_grupos.csv", "w", encoding="utf-8", newline="") as out:
        w = csv.DictWriter(out, fieldnames=list(tabla[0].keys()))
        w.writeheader()
        w.writerows(tabla)
    with open(prefijo + "_resumen.md", "w", encoding="utf-8") as out:
        for m in ("ES", "US"):
            fm = [r for r in filas if r["mercado"] == m]
            por_int = defaultdict(int)
            for r in fm:
                por_int[r["intencion"]] += 1
            out.write("## %s: %d sugerencias únicas\n\n" % (m, len(fm)))
            out.write("| Intención | Keywords |\n|---|---|\n")
            for k, v in sorted(por_int.items(), key=lambda x: -x[1]):
                out.write("| %s | %d |\n" % (k, v))
            out.write("\n### Núcleos con más keywords de herramienta/plantilla/servicio (%s)\n\n" % m)
            out.write("| # | Núcleo | Keywords | Frecuencia | Intenciones | Ejemplos |\n|---|---|---|---|---|---|\n")
            for i, t in enumerate([t for t in tabla if t["mercado"] == m][:60], 1):
                out.write("| %d | %s | %d | %d | %s | %s |\n" % (i, t["nucleo"], t["n_keywords"], t["frecuencia_total"], t["intenciones"], t["ejemplos"]))
            out.write("\n")
    print("universo %d keywords; grupos %d" % (len(filas), len(tabla)))


if __name__ == "__main__":
    main()
