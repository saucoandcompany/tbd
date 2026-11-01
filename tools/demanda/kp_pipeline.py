#!/usr/bin/env python3
"""Pipeline demanda primero sobre exports del Planificador de Google Ads.

Uso: python3 -I tools/demanda/kp_pipeline.py <carpeta_csv> <salida_prefijo>

Lee todos los .csv de la carpeta (formato de descarga del Planificador: UTF-16 o UTF-8, tabulador,
dos líneas de preámbulo, cabeceras en español o inglés), une, deduplica por (mercado, keyword),
aplica el filtro duro, clasifica intención, agrupa por núcleo y puntúa 0-10 con criterios de datos.
El mercado se toma del nombre del fichero: contiene "_ES_" o "_US_".

Salidas: <prefijo>_keywords.csv (todas las filas con columnas normalizadas y filtros),
         <prefijo>_grupos.csv y <prefijo>_grupos.md (grupos que pasan el filtro, ordenados por nota).
"""
import csv
import glob
import io
import os
import re
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comun import excluir, intencion, nucleo, ruido  # noqa: E402

UMBRAL = {  # por mercado
    "ES": {"vol_min": 200, "puja_min": 1.0},
    "US": {"vol_min": 2000, "puja_min": 1.0},
}
COLS = {
    "keyword": ["palabra clave", "keyword"],
    "vol": ["prom. de búsquedas mensuales", "promedio de búsquedas mensuales", "avg. monthly searches"],
    "c3m": ["cambio en tres meses", "three month change"],
    "yoy": ["cambio interanual", "yoy change"],
    "comp": ["competencia", "competition"],
    "comp_idx": ["competencia (valor indexado)", "competition (indexed value)"],
    "puja_baja": ["puja de la parte superior de la página (intervalo bajo)", "top of page bid (low range)"],
    "puja_alta": ["puja de la parte superior de la página (intervalo alto)", "top of page bid (high range)"],
}


def leer_csv(path):
    raw = open(path, "rb").read()
    if raw[:2] in (b"\xff\xfe", b"\xfe\xff"):
        text = raw.decode("utf-16")
    else:
        try:
            text = raw.decode("utf-8-sig")
        except UnicodeDecodeError:
            text = raw.decode("latin-1")
    lines = text.splitlines()
    # saltar preámbulo hasta la cabecera
    start = 0
    for i, l in enumerate(lines[:10]):
        low = l.lower()
        if ("keyword" in low or "palabra clave" in low) and (low.count("\t") >= 3 or low.count(",") >= 3):
            start = i
            break
    delim = "\t" if "\t" in lines[start] else ","
    reader = csv.DictReader(io.StringIO("\n".join(lines[start:])), delimiter=delim)
    rows = []
    for r in reader:
        rows.append({k.strip().lower(): (v or "").strip() for k, v in r.items() if k is not None and isinstance(v, str) or (k is not None and v is None)})
    return rows


def col(row, key):
    for name in COLS[key]:
        if name in row:
            return row[name]
    return ""


def num(s):
    s = s.replace("%", "").replace("€", "").replace("$", "").replace(" ", "").strip()
    if not s or s in ("-", "—", "–"):
        return None
    s = s.replace(".", "").replace(",", ".") if re.search(r"\d,\d\d$", s) or ("," in s and "." not in s) else s.replace(",", "")
    try:
        return float(s)
    except ValueError:
        return None


def mercado_de(path):
    n = os.path.basename(path).upper()
    if "_US_" in n or n.startswith("US_") or "_US." in n:
        return "US"
    return "ES"


def main():
    carpeta, prefijo = sys.argv[1], sys.argv[2]
    filas = {}
    for path in sorted(glob.glob(os.path.join(carpeta, "*.csv"))):
        m = mercado_de(path)
        for r in leer_csv(path):
            kw = col(r, "keyword")
            if not kw:
                continue
            vol = num(col(r, "vol"))
            if vol is None:
                continue
            key = (m, kw.lower())
            if key in filas:
                continue
            filas[key] = {
                "mercado": m, "keyword": kw, "vol": int(vol),
                "c3m": num(col(r, "c3m")), "yoy": num(col(r, "yoy")),
                "comp": col(r, "comp"), "comp_idx": num(col(r, "comp_idx")),
                "puja_baja": num(col(r, "puja_baja")), "puja_alta": num(col(r, "puja_alta")),
                "fichero": os.path.basename(path),
            }
    if not filas:
        sys.exit("No se encontraron filas. ¿Está la carpeta vacía o el formato no es el del Planificador?")

    # filtro duro y clasificación
    for f in filas.values():
        u = UMBRAL[f["mercado"]]
        f["intencion"] = intencion(f["keyword"])
        f["excluida"] = excluir(f["keyword"]) or ruido(f["keyword"])
        f["nucleo"] = nucleo(f["keyword"])
        motivos = []
        if f["vol"] < u["vol_min"]:
            motivos.append("volumen")
        if f["c3m"] is not None and f["c3m"] < 0:
            motivos.append("tendencia")
        if (f["puja_alta"] or 0) < u["puja_min"]:
            motivos.append("puja")
        if f["intencion"] not in ("herramienta", "plantilla", "servicio"):
            motivos.append("intencion:" + f["intencion"])
        if f["excluida"]:
            motivos.append("excluida")
        f["pasa"] = not motivos
        f["motivos"] = ";".join(motivos)

    with open(prefijo + "_keywords.csv", "w", encoding="utf-8", newline="") as out:
        w = csv.DictWriter(out, fieldnames=list(next(iter(filas.values())).keys()))
        w.writeheader()
        for f in sorted(filas.values(), key=lambda x: -x["vol"]):
            w.writerow(f)

    # agrupación por núcleo y mercado
    grupos = defaultdict(list)
    for f in filas.values():
        if f["pasa"]:
            grupos[(f["mercado"], f["nucleo"])].append(f)
    tabla = []
    for (m, nuc), fs in grupos.items():
        vol = sum(f["vol"] for f in fs)
        pujas = [f["puja_alta"] for f in fs if f["puja_alta"]]
        c3 = [f["c3m"] for f in fs if f["c3m"] is not None]
        comp_idx = [f["comp_idx"] for f in fs if f["comp_idx"] is not None]
        puja = sorted(pujas)[len(pujas) // 2] if pujas else 0
        tend = sum(c3) / len(c3) if c3 else 0
        cidx = sum(comp_idx) / len(comp_idx) if comp_idx else None
        # nota de datos (7 criterios, 0-7); los otros 3 (foso, construible solo, sin título) son revisión manual
        n = 0
        n += 1 if vol >= (UMBRAL[m]["vol_min"] * 5) else 0          # demanda
        n += 1 if vol >= (UMBRAL[m]["vol_min"] * 25) else 0         # demanda alta
        n += 1 if tend >= 0 else 0                                   # tendencia no negativa
        n += 1 if tend >= 20 else 0                                  # crece
        n += 1 if puja >= 1 else 0                                   # intención comercial
        n += 1 if puja >= 3 else 0                                   # alguien paga caro el clic
        n += 1 if (cidx is not None and cidx <= 66) else 0           # competencia de anuncios no alta
        inten = sorted({f["intencion"] for f in fs})
        tabla.append({
            "mercado": m, "nucleo": nuc, "n_keywords": len(fs), "vol_total": vol,
            "tendencia_3m_media": round(tend, 1), "puja_alta_mediana": round(puja, 2),
            "comp_idx_media": round(cidx, 0) if cidx is not None else "",
            "intenciones": "|".join(inten), "nota_datos_0a7": n,
            "ejemplos": " | ".join(sorted(fs, key=lambda x: -x["vol"])[:4][i]["keyword"] for i in range(min(4, len(fs)))),
        })
    tabla.sort(key=lambda t: (-t["nota_datos_0a7"], -t["vol_total"]))
    with open(prefijo + "_grupos.csv", "w", encoding="utf-8", newline="") as out:
        w = csv.DictWriter(out, fieldnames=list(tabla[0].keys()) if tabla else ["vacio"])
        w.writeheader()
        for t in tabla:
            w.writerow(t)
    with open(prefijo + "_grupos.md", "w", encoding="utf-8") as out:
        total = len(filas)
        pasan = sum(1 for f in filas.values() if f["pasa"])
        out.write("# Universo de demanda (Planificador): grupos que pasan el filtro duro\n\n")
        out.write("Filas leídas: %d. Pasan el filtro duro: %d (%.1f %%). Grupos: %d.\n\n" % (total, pasan, 100.0 * pasan / total, len(tabla)))
        out.write("Filtro duro por mercado: volumen ≥%d (ES) / ≥%d (US), cambio a 3 meses ≥0, puja alta ≥1, intención herramienta/plantilla/servicio, sin exclusiones.\n\n" % (UMBRAL["ES"]["vol_min"], UMBRAL["US"]["vol_min"]))
        out.write("Nota de datos 0-7: demanda (≥5× y ≥25× umbral), tendencia (≥0 y ≥20 %), puja (≥1 y ≥3), competencia de anuncios ≤66. Los tres criterios restantes del scorecard (foso de retención, construible solo, sin título requerido) se revisan a mano sobre los grupos de esta tabla.\n\n")
        out.write("| # | Mercado | Núcleo | Keywords | Volumen total | Tend. 3 m | Puja alta mediana | Comp. idx | Intenciones | Nota datos | Ejemplos |\n|---|---|---|---|---|---|---|---|---|---|---|\n")
        for i, t in enumerate(tabla, 1):
            out.write("| %d | %s | %s | %d | %d | %s %% | %s | %s | %s | %d/7 | %s |\n" % (
                i, t["mercado"], t["nucleo"], t["n_keywords"], t["vol_total"], t["tendencia_3m_media"],
                t["puja_alta_mediana"], t["comp_idx_media"], t["intenciones"], t["nota_datos_0a7"], t["ejemplos"]))
    print("filas %d, pasan %d, grupos %d -> %s_grupos.md" % (len(filas), sum(1 for f in filas.values() if f["pasa"]), len(tabla), prefijo))


if __name__ == "__main__":
    main()
