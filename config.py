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
    {
        "tienda": "Lider",
        "nombre": "PS5 Digital Astro+GT7 00071171902355",
        "url": "https://www.lider.cl/ip/videojuegos/consola-playstation-5-edicion-digital-con-astro-bot-y-gran-turismo-7/00071171902355",
    },
    {
        "tienda": "Lider",
        "nombre": "PS5 Digital Astro+GT7 00071171902395",
        "url": "https://www.lider.cl/ip/videojuegos/consola-playstation-5-digital-con-astro-bot-y-gran-turismo-7/00071171902395",
    },
    {
        "tienda": "Lider",
        "nombre": "PS5 Slim Digital 00494887241591",
        "url": "https://www.lider.cl/ip/videojuegos/consola-sony-ps5-playstation-5-slim-edicion-digital-/00494887241591",
    },
]

# --- Metas por modelo Switch (cada producto puede traer su "meta") ---
META_SWITCH1 = 300000
META_OLED = 350000
META_SWITCH2 = 550000

PRODUCTS += [
    # Paris Switch
    {"tienda": "Paris", "nombre": "SW OLED Mario Wonder", "url": "https://www.paris.cl/consola-nintendo-switch-oled-super-mario-bros-wonder-3-meses-nso-207500999.html", "meta": META_OLED},
    {"tienda": "Paris", "nombre": "SW OLED MKF37DO7ZF", "url": "https://www.paris.cl/consola-nintendo-switch-oled-MKF37DO7ZF.html", "meta": META_OLED},
    {"tienda": "Paris", "nombre": "SW 32GB gris", "url": "https://www.paris.cl/consola-nintendo-switch-32gb-estandar-gris-MKY88VJ373.html", "meta": META_SWITCH1},
    {"tienda": "Paris", "nombre": "SW neon Wonder", "url": "https://www.paris.cl/consola-nintendo-switch-neon-super-mario-bros-wonder-3-meses-nso-207497999.html", "meta": META_SWITCH1},
    {"tienda": "Paris", "nombre": "SW2 142747999", "url": "https://www.paris.cl/consola-nintendo-switch-2-142747999.html", "meta": META_SWITCH2},
    {"tienda": "Paris", "nombre": "SW OLED blanco", "url": "https://www.paris.cl/consola-nintendo-switch-oled-blanco-MK39PEZGDL.html", "meta": META_OLED},
    # Ripley Switch
    {"tienda": "Ripley", "nombre": "SW2 StarFox bundle", "url": "https://simple.ripley.cl/consola-nintendo-switch-2-star-fox-sw2-bundle-exclusivo-mpm10003566410?s=mdco&pos=1&catPos=1&p=1&ps=48&cat=NO*vj_consolas_nint&orig=PLP&prodNavFullCategory=Tecno%20%3E%20Nintendo%20%3E%20Consolas", "meta": META_SWITCH2},
    {"tienda": "Ripley", "nombre": "SW2 2000406245874", "url": "https://simple.ripley.cl/consola-nintendo-switch-2-2000406245874p?color_80=Negro&s=mdco&pos=2&catPos=2&p=1&ps=48&cat=NO*vj_consolas_nint&orig=PLP&prodNavFullCategory=Tecno+%3E+Nintendo+%3E+Consolas", "meta": META_SWITCH2},
    {"tienda": "Ripley", "nombre": "SW 1.1 Wonder", "url": "https://simple.ripley.cl/nintendo-switch-11-super-mario-wonder-2000408339007p?color_80=Negro&s=mdco&pos=3&catPos=3&p=1&ps=48&cat=NO*vj_consolas_nint&orig=PLP&prodNavFullCategory=Tecno+%3E+Nintendo+%3E+Consolas", "meta": META_SWITCH1},
    {"tienda": "Ripley", "nombre": "SW2 mpm10002934494", "url": "https://simple.ripley.cl/consola-nintendo-switch-2-mpm10002934494?color_80=Negro&s=mdco&pos=4&catPos=4&p=1&ps=48&cat=NO*vj_consolas_nint&orig=PLP&prodNavFullCategory=Tecno+%3E+Nintendo+%3E+Consolas", "meta": META_SWITCH2},
    {"tienda": "Ripley", "nombre": "SW OLED Wonder", "url": "https://simple.ripley.cl/nintendo-switch-oled-white-super-mario-wonder-2000408339014p?color_80=Blanco&s=mdco&pos=5&catPos=5&p=1&ps=48&cat=NO*vj_consolas_nint&orig=PLP&prodNavFullCategory=Tecno+%3E+Nintendo+%3E+Consolas", "meta": META_OLED},
    {"tienda": "Ripley", "nombre": "SW OLED mpm10001493786", "url": "https://simple.ripley.cl/consola-nintendo-switch-oled-blanco-mpm10001493786?color_80=Blanco&s=mdco&pos=6&catPos=6&p=1&ps=48&cat=NO*vj_consolas_nint&orig=PLP&prodNavFullCategory=Tecno+%3E+Nintendo+%3E+Consolas", "meta": META_OLED},
    {"tienda": "Ripley", "nombre": "SW2 DK Bananza", "url": "https://simple.ripley.cl/consola-bundle-nintendo-switch-2-donkey-kong-bananza-sw2-mpm10002953688?s=mdco&pos=7&catPos=7&p=1&ps=48&cat=NO*vj_consolas_nint&orig=PLP&prodNavFullCategory=Tecno%20%3E%20Nintendo%20%3E%20Consolas", "meta": META_SWITCH2},
    {"tienda": "Ripley", "nombre": "SW2 Pokemon ZA", "url": "https://simple.ripley.cl/consola-nintendo-switch-2-poke-mon-legends-z-a-nsw-bundle-mpm10003675247?s=mdco&pos=9&catPos=9&p=1&cat=NO*vj_consolas_nint&orig=PLP&prodNavFullCategory=Tecno%20%3E%20Nintendo%20%3E%20Consolas", "meta": META_SWITCH2},
    # Falabella Switch
    {"tienda": "Falabella", "nombre": "SW2 SYSTEM", "url": "https://www.falabella.com/falabella-cl/product/17448346/HW-SWITCH-2-SYSTEM-LT2-SOLUS/17448346", "meta": META_SWITCH2},
    {"tienda": "Falabella", "nombre": "SW OLED Blanco", "url": "https://www.falabella.com/falabella-cl/product/123426296/Consola-Nintendo-Switch-Modelo-OLED-Blanco/123426297", "meta": META_OLED},
    {"tienda": "Falabella", "nombre": "SW 1.1 Neon Bund", "url": "https://www.falabella.com/falabella-cl/product/80627203/Consola%20Switch%201%201%20Neon%20Bund%20Nintendo/80627203", "meta": META_SWITCH1},
    {"tienda": "Falabella", "nombre": "SW OLED White", "url": "https://www.falabella.com/falabella-cl/product/80627204/Consola%20Switch%20Oled%20White%20Bu%20Nintendo/80627204", "meta": META_OLED},
    # Lider Switch
    {"tienda": "Lider", "nombre": "SW2 256GB", "url": "https://www.lider.cl/ip/tecnologia/consola-nintendo-switch-2-256gb-nintendo/00004549688584", "meta": META_SWITCH2},
    {"tienda": "Lider", "nombre": "SW2 DK Bananza", "url": "https://www.lider.cl/ip/videojuegos/consola-bundle-nintendo-switch-2-donkey-kong-bananza-sw2/03313938474855", "meta": META_SWITCH2},
    {"tienda": "Lider", "nombre": "SW2 elige tu juego", "url": "https://www.lider.cl/ip/videojuegos/consola-nintendo-switch-2-elige-tu-juego/00004549688667", "meta": META_SWITCH2},
    {"tienda": "Lider", "nombre": "SW OLED blanca", "url": "https://www.lider.cl/ip/videojuegos/consola-nintendo-switch-oled-blanca/00490237054849", "meta": META_OLED},
    {"tienda": "Lider", "nombre": "SW2 Pokemon ZA", "url": "https://www.lider.cl/ip/videojuegos/consola-nintendo-switch-2-videojuego-pokemon-z-a/03313938474151", "meta": META_SWITCH2},
    # Weplay Switch
    {"tienda": "Weplay", "nombre": "SW OLED Wonder", "url": "https://www.weplay.cl/consola-nintendo-switch-oled-mario-wonder.html", "meta": META_OLED},
    {"tienda": "Weplay", "nombre": "SW2", "url": "https://www.weplay.cl/consola-nintendo-switch-2.html", "meta": META_SWITCH2},
    {"tienda": "Weplay", "nombre": "SW neon Wonder", "url": "https://www.weplay.cl/consola-nintendo-switch-neon-mario-wonder.html", "meta": META_SWITCH1},
    {"tienda": "Weplay", "nombre": "SW OLED blanca", "url": "https://www.weplay.cl/consola-nintendo-switch-modelo-oled-blanca.html", "meta": META_OLED},
    {"tienda": "Weplay", "nombre": "SW OLED neon", "url": "https://www.weplay.cl/consola-nintendo-switch-modelo-oled-neon.html", "meta": META_OLED},
    {"tienda": "Weplay", "nombre": "SW2 choose game", "url": "https://www.weplay.cl/consola-nintendo-switch-2-choose-your-game-bundle.html", "meta": META_SWITCH2},
    {"tienda": "Weplay", "nombre": "SW2 Pokemon ZA", "url": "https://www.weplay.cl/consola-nintendo-switch-2-pokemon-legends-z-a-edition-bundle.html", "meta": META_SWITCH2},
    {"tienda": "Weplay", "nombre": "SW2 Mario Kart", "url": "https://www.weplay.cl/consola-nintendo-switch-2-mario-kart-world.html", "meta": META_SWITCH2},
    # Travel Switch
    {"tienda": "Travel", "nombre": "SW 1.1 neon Wonder", "url": "https://tienda.travel.cl/te-podr%C3%ADa-interesar-gamer-days/consola-nintendo-switch-11-neon-mario-wonder-bundle-3mo-nso/SKU131598", "meta": META_SWITCH1},
    {"tienda": "Travel", "nombre": "SW OLED Wonder", "url": "https://tienda.travel.cl/te-podr%C3%ADa-interesar-gamer-days/consola-nintendo-switch-oled-super-mario-bros-wonder-3-nso/SKU118707", "meta": META_OLED},
    {"tienda": "Travel", "nombre": "SW2 system", "url": "https://tienda.travel.cl/ofertas-destacadas/consola-nintendo-switch-2-system/SKU124047", "meta": META_SWITCH2},
]
