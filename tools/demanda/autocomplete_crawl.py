#!/usr/bin/env python3
"""Expande semillas con el autocompletado de Google (client=chrome) y guarda las sugerencias.

Uso: python3 -I tools/demanda/autocomplete_crawl.py <mercado ES|US> <fichero_semillas> <salida.tsv> [pausa_s]

- Cada semilla se consulta sola y con 36 sufijos (" a".." z", " 0".." 9").
- Guarda: mercado, semilla, consulta, posicion, sugerencia, relevancia (google:suggestrelevance).
- Reanudable: si la salida existe, salta las consultas ya hechas.
- Proxy: usa HTTPS_PROXY del entorno y el CA bundle de /root/.ccr/ca-bundle.crt.
"""
import csv
import json
import os
import ssl
import sys
import time
import urllib.parse
import urllib.request

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36")
MARKETS = {"ES": ("es", "es"), "US": ("en", "us")}
SUFFIXES = [""] + [" " + c for c in "abcdefghijklmnopqrstuvwxyz0123456789"]


def fetch(q, hl, gl, ctx):
    url = ("https://www.google.com/complete/search?client=chrome&hl=%s&gl=%s&q=%s"
           % (hl, gl, urllib.parse.quote(q)))
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": hl})
    with urllib.request.urlopen(req, timeout=20, context=ctx) as r:
        data = json.loads(r.read().decode("utf-8", "replace"))
    sugg = data[1] if len(data) > 1 else []
    meta = data[4] if len(data) > 4 and isinstance(data[4], dict) else {}
    rel = meta.get("google:suggestrelevance", [None] * len(sugg))
    return list(zip(sugg, rel))


def main():
    market, seeds_path, out_path = sys.argv[1], sys.argv[2], sys.argv[3]
    pause = float(sys.argv[4]) if len(sys.argv) > 4 else 1.0
    hl, gl = MARKETS[market]
    ctx = ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt")
    seeds = [l.strip() for l in open(seeds_path, encoding="utf-8") if l.strip() and not l.startswith("#")]
    done = set()
    import glob
    for prev in glob.glob(os.path.join(os.path.dirname(out_path) or ".", "sugerencias_%s*.tsv" % market)):
        with open(prev, encoding="utf-8") as f:
            for row in csv.reader(f, delimiter="\t"):
                if len(row) >= 3:
                    done.add(row[2])
    new = not os.path.exists(out_path) or os.path.getsize(out_path) == 0
    errors = 0
    with open(out_path, "a", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        if new:
            w.writerow(["mercado", "semilla", "consulta", "posicion", "sugerencia", "relevancia"])
        total = len(seeds) * len(SUFFIXES)
        n = 0
        for seed in seeds:
            for suf in SUFFIXES:
                q = seed + suf
                n += 1
                if q in done:
                    continue
                try:
                    pairs = fetch(q, hl, gl, ctx)
                    errors = 0
                except Exception as e:  # noqa: BLE001
                    errors += 1
                    sys.stderr.write("ERR %s: %s\n" % (q, e))
                    if errors >= 5:
                        sys.stderr.write("5 errores seguidos: pausa de 120 s\n")
                        time.sleep(120)
                        errors = 0
                    continue
                if not pairs:
                    w.writerow([market, seed, q, 0, "", ""])
                for i, (s, r) in enumerate(pairs, 1):
                    w.writerow([market, seed, q, i, s, r if r is not None else ""])
                f.flush()
                if n % 50 == 0:
                    sys.stderr.write("%d/%d consultas\n" % (n, total))
                time.sleep(pause)
    sys.stderr.write("fin: %d consultas\n" % total)


if __name__ == "__main__":
    main()
