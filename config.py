# Bot PS5 Cyber Day Chile
# Rastrea precios en Falabella, Paris, Ripley, PC Factory y avisa por Telegram

# --- Umbral: avisa si precio <= este valor (tu meta: 400.000) ---
PRECIO_OBJETIVO = 400000

# --- Cada cuántos segundos revisar? MODO MINIMO ---
# 60s es lo mínimo seguro. Con 9 productos cada ronda tarda ~30s,
# así que cada producto se revisa aprox cada 90s.
INTERVALO_SEGUNDOS = 60

# --- Detección de cupones: exige la palabra + un precio $ cerca ---
# Se ignoran contextos de "juego" (cupón de juego del bundle), footers y legales.
CUPON_KEYWORDS = [
    "cupon",
    "cupon de descuento",
    "codigo de descuento",
    "codigo promocional",
    "con cupon",
    "cupon cyber",
    "descuento extra",
]
CUPON_EXCLUIR = ["juego", "devolucion", "gift card", "juguete", "boleta"]

# --- Productos a vigilar (9 links exactos del usuario) ---
PRODUCTS = [
    {
        "tienda": "Paris",
        "nombre": "PS5 Slim Digital 825GB Astro+GT7",
        "url": "https://www.paris.cl/consola-ps5-slim-digital-825gb-con-astro-bot-y-gran-turismo-7-316547999.html?commune=13201",
    },
    {
        "tienda": "Paris",
        "nombre": "PS5 Slim Digital MK208523YL",
        "url": "https://www.paris.cl/consola-sony-ps5-playstation-5-slim-edicion-digital-MK208523YL.html?commune=13201",
    },
    {
        "tienda": "Paris",
        "nombre": "PS5 Standard Astro+GT7",
        "url": "https://www.paris.cl/consola-ps5-standard-con-astro-bot-y-gran-turismo-7-316545999.html?commune=13201",
    },
    {
        "tienda": "Ripley",
        "nombre": "PS5 Digital 825GB Astro+GT7",
        "url": "https://simple.ripley.cl/consola-playstation-5-edicion-digital-825gb-astro-bot-gran-turismo-7-2000408796497p?color_80=Blanco&s=mdco&pos=2&catPos=2&p=1&ps=48&cat=NO*vj_playstation&orig=PLP&prodNavFullCategory=Tecno+%3E+Playstation",
    },
    {
        "tienda": "Ripley",
        "nombre": "PS5 Slim Digital MPM10001386412",
        "url": "https://simple.ripley.cl/consola-sony-ps5-playstation-5-slim-edicion-digital-mpm10001386412?color_80=Blanco&s=mdco&pos=1&catPos=1&p=1&ps=48&cat=NO*vj_playstation&orig=PLP&prodNavFullCategory=Tecno+%3E+Playstation",
    },
    {
        "tienda": "Ripley",
        "nombre": "PS5 1TB Astro+GT7",
        "url": "https://simple.ripley.cl/consola-playstation-5-1tb-astro-bot-gran-turismo-7-2000408941743p?color_80=Blanco&s=mdco&pos=3&catPos=3&p=1&ps=48&cat=NO*vj_playstation&orig=PLP&prodNavFullCategory=Tecno+%3E+Playstation",
    },
    {
        "tienda": "Falabella",
        "nombre": "PS5 HW Digital GT7",
        "url": "https://www.falabella.com/falabella-cl/product/80648266/Consola%20PS5%20HW%20Digital%20GT7%20A%20Sony/80648266",
    },
    {
        "tienda": "Falabella",
        "nombre": "PS5 Slim Digital 126614389",
        "url": "https://www.falabella.com/falabella-cl/product/126614389/Consola-Sony-PS5-PlayStation-5-Slim-(Edicion-Digital)/126614390",
    },
    {
        "tienda": "Falabella",
        "nombre": "PS5 HW Standard GT7",
        "url": "https://www.falabella.com/falabella-cl/product/80648267/Consola%20PS5%20HW%20Standard%20GT7%20Sony/80648267",
    },
]
