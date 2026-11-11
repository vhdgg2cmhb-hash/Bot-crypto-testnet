from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from urllib.request import urlopen
from urllib.parse import urlencode
import json

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def accueil():
    return """
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Mon bot crypto</title>
    </head>
    <body style="font-family:Arial;text-align:center;padding:25px">
    <h1>🤖 Mon bot crypto</h1>
    <h2>Suivi BTC et ETH</h2>
    <p id="prix">Chargement des prix...</p>
    <script>
    fetch('/prix')
      .then(r => r.json())
      .then(d => {
        document.getElementById('prix').innerHTML =
          'Bitcoin : ' + d.BTC + ' €<br><br>' +
          'Ethereum : ' + d.ETH + ' €';
      })
      .catch(() => {
        document.getElementById('prix').innerText =
          'Prix indisponibles pour le moment';
      });
    </script>
    <p>Prix indicatifs fournis par CoinGecko.</p>
    <p>Aucun achat ni vente automatique.</p>
    </body>
    </html>
    """

@app.get("/prix")
def prix():
    url = "https://api.coingecko.com/api/v3/simple/price?"
    params = urlencode({
        "ids": "bitcoin,ethereum",
        "vs_currencies": "eur"
    })

    with urlopen(url + params, timeout=15) as response:
        data = json.loads(response.read().decode())

    return {
        "BTC": data["bitcoin"]["eur"],
        "ETH": data["ethereum"]["eur"]
    }
