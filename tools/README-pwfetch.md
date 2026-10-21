# pwfetch.js: abrir páginas reales desde la sesión en la nube

Requisito: la red del entorno debe permitir el host (abierta el 21 oct 2026).

    NODE_EXTRA_CA_CERTS=/root/.ccr/ca-bundle.crt node tools/pwfetch.js <url>            # HTTP directo, páginas estáticas
    NODE_EXTRA_CA_CERTS=/root/.ccr/ca-bundle.crt node tools/pwfetch.js <url> --browser  # Chromium, páginas con JavaScript (ISO, Trends, apps)

Imprime STATUS y hasta 20.000 caracteres de texto. Si devuelve "Just a moment..." o 403, repetir con --browser.
