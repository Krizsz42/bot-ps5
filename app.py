"""Modo nube (Render free): servidor web anti-sleep + bot en segundo plano."""
import os
import threading
import asyncio
from flask import Flask

app = Flask(__name__)

@app.get("/")
def health():
    return "Bot PS5 activo", 200

def run_bot():
    from tracker import main
    asyncio.run(main())

if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    port = int(os.getenv("PORT", "10000"))
    app.run(host="0.0.0.0", port=port)
