from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import ccxt
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def accueil():
    return """
    <html>
    <head><meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Mon bot crypto</title></head>
    <body style="font-family:Arial;text-align:center;padding:25px">
    <h1>🤖 Mon bot crypto</h1>
    <h2>Mode TESTNET uniquement</h2>
    <p>Bot connecté à Binance en lecture des prix.</p>
    <p>Aucun ordre réel ne sera passé.</p>
    <p id="prix">Chargement du prix BTC...</p>
    <script>
    fetch('/prix').then(r=>r.json()).then(d=>{
      document.getElementById('prix').innerText =
      'Bitcoin : ' + d.prix + ' USDT';
    }).catch(()=> {
      document.getElementById('prix').innerText='Prix indisponible';
    });
    </script>
    </body></html>
    """

@app.get("/prix")
def prix():
    exchange = ccxt.binance()
    ticker = exchange.fetch_ticker("BTC/USDT")
    return {"prix": ticker["last"]}
