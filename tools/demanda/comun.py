"""Funciones compartidas: clasificación de intención, núcleo de agrupación, exclusiones."""
import re
import unicodedata

HERRAMIENTA = re.compile(
    r"\b(software|programa|programas|app|apps|aplicaci[oó]n|herramienta|plataforma|online|en l[ií]nea|"
    r"gestor|gestión|gestion|calculadora|simulador|generador|comparador|automatizar|erp|crm|saas|"
    r"tool|tools|platform|calculator|generator|automate|tracker|dashboard|portal)\b", re.I)
PLANTILLA = re.compile(
    r"\b(plantilla|plantillas|modelo|modelos|formulario|ejemplo|ejemplos|excel|hoja de c[aá]lculo|word|pdf|"
    r"template|templates|spreadsheet|checklist|sample|form|forms|example)\b", re.I)
SERVICIO = re.compile(
    r"\b(gestor[ií]a|asesor[ií]a|asesor|consultor[ií]a|consultor|empresa de|empresas de|servicio|servicios|"
    r"contratar|abogado|abogados|ingenier[ií]a|certificadora|auditor|auditor[ií]a externa|outsourcing|"
    r"consultant|consulting|agency|service|services|lawyer|attorney|near me|cerca de m[ií])\b", re.I)
INFORMACION = re.compile(
    r"\b(qu[eé] es|que es|definici[oó]n|significado|wikipedia|c[oó]mo funciona|para qu[eé] sirve|"
    r"what is|meaning|definition|wiki|explained|history|historia)\b", re.I)
COMPRA_FISICA = re.compile(
    r"\b(comprar|amazon|aliexpress|segunda mano|wallapop|oferta|ofertas|outlet|barato|baratos|"
    r"buy|cheap|for sale|ebay|walmart|best buy)\b", re.I)
EMPLEO = re.compile(r"\b(empleo|trabajo|oposiciones|sueldo|salario|curso|cursos|m[aá]ster|grado|fp|"
                    r"jobs|salary|career|course|courses|degree|certification exam)\b", re.I)

RUIDO = re.compile(
    r"\b(isla de las tentaciones|gran hermano|supervivientes|operaci[oó]n triunfo|la voz|masterchef|eurovisi[oó]n|"
    r"real madrid|barcelona|atl[eé]tico|betis|sevilla fc|valencia cf|athletic|liga|champions|mundial|selecci[oó]n|"
    r"programa \d|programa \d+ de|cap[ií]tulo|episodio|temporada|serie|pel[ií]cula|netflix|hbo|"
    r"windows \d|windows xp|iphone \d|android \d|zip|rar|driver|drivers|bios|firmware|rom|emulador|"
    r"karaoke|dj|m[uú]sica|descargar v[ií]deos|youtube|spotify|torrent|crack|"
    r"ni[ñn]os de \d|cumplea[ñn]os|boda|navidad|halloween|"
    r"tv show|season \d|episode|movie|football|nfl|nba|mlb|fantasy|lineup|roster|"
    r"windows|iphone|android|xbox|playstation|minecraft|roblox|fortnite)\b", re.I)

EXCLUIR = re.compile(
    r"\b(ozempic|mounjaro|wegovy|semaglutida|tirzepatida|saxenda|zepbound|rybelsus|"
    r"porno|porn|xxx|sexo|casino|apuestas|bet365|crack|keygen|serial|torrent|descargar gratis full|"
    r"del sol|upv|uned|ucm|uam|uma|us\b|ub\b)\b", re.I)

MODIFICADORES = re.compile(
    r"\b(software|programa|programas|app|apps|aplicaci[oó]n|herramienta|plataforma|online|gratis|gratuito|gratuita|"
    r"plantilla|plantillas|modelo|formulario|ejemplo|excel|word|pdf|descargar|mejor|mejores|precio|precios|"
    r"cu[aá]nto cuesta|c[oó]mo|como|hacer|para|de|del|la|el|los|las|un|una|en|y|o|con|sin|2025|2026|2027|"
    r"tool|tools|template|templates|free|best|for|the|a|an|of|to|in|and|or|with|without|price|pricing|cost|how|"
    r"spreadsheet|checklist|generator|calculator|calculadora|simulador|generador|comparador)\b", re.I)


def quitar_tildes(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def intencion(kw):
    """Devuelve una de: herramienta, plantilla, servicio, informacion, compra_fisica, empleo, otra."""
    k = kw.lower()
    if EMPLEO.search(k):
        return "empleo"
    if COMPRA_FISICA.search(k):
        return "compra_fisica"
    if PLANTILLA.search(k):
        return "plantilla"
    if HERRAMIENTA.search(k):
        return "herramienta"
    if SERVICIO.search(k):
        return "servicio"
    if INFORMACION.search(k):
        return "informacion"
    return "otra"


def excluir(kw):
    return bool(EXCLUIR.search(kw.lower()))


def ruido(kw):
    return bool(RUIDO.search(kw.lower()))


def nucleo(kw):
    """Quita modificadores y deja el sustantivo del problema, para agrupar."""
    k = quitar_tildes(kw.lower())
    k = MODIFICADORES.sub(" ", k)
    k = re.sub(r"[^a-z0-9ñ ]", " ", k)
    toks = [t for t in k.split() if len(t) > 1]
    return " ".join(toks[:3]) if toks else quitar_tildes(kw.lower())
