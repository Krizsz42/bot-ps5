# 🎮 Bot PS5 Cyber Day Chile

Rastrea Falabella, Paris, Ripley, PC Factory cada 2 min y te avisa a Telegram si baja de $400.000.

Probado: Paris se lee ok sin navegador ($799.990 actual).

## 1. Crear alerta Telegram (5 min, gratis)

1. En Telegram busca `@BotFather` → `/newbot` → te da un TOKEN
2. Busca `@userinfobot` → te da tu CHAT_ID (número)
3. Edita `.env`:
```
TELEGRAM_BOT_TOKEN=123456:ABC...
TELEGRAM_CHAT_ID=12345678
```
4. Mándale `/start` a tu bot para activarlo.

## 2. Correr local (PC)

```
pip install -r requirements.txt
python tracker.py
```

- Revisa cada `INTERVALO_SEGUNDOS` en `config.py` (default 120s = 2 min).
- Puedes bajarlo a 60s. Menos de 60s = riesgo de bloqueo IP.
- Deja el PC encendido el lunes.

## 3. Poner tus links exactos

Edita `config.py` → `PRODUCTS`. Pega el link del producto puntual, no del buscador.
Ejemplo: si ves una PS5 a $450.000 en Ripley, pega esa URL.

## 4. Nube gratis 24/7

Opción A - GitHub Actions (gratis, pero mínimo 5 min por límite de GitHub):
- Sube esta carpeta a GitHub, agrega secrets TELEGRAM_BOT_TOKEN y TELEGRAM_CHAT_ID.

Opción B - Render.com free + UptimeRobot (permite 1-2 min):
- Crea Web Service con `python tracker.py` como worker.
- UptimeRobot hace ping cada 5 min para que no se duerma.

Para el Cyber Day te recomiendo PC local a 1-2 min, es más rápido e instantáneo.

## Archivos
- `tracker.py` : cerebro
- `config.py` : tiendas, umbral $400.000, intervalo
- `state.json` : se crea solo, guarda último precio
- `.env` : tus claves Telegram (no subir a GitHub)
