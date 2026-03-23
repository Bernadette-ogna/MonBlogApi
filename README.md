# MonBlogApi
# Installation
1. Prérequis
Python 3.8 ou plus récent
pip (gestionnaire de paquets Python)
2. Créer un environnement virtuel (optionnel mais recommandé)
python -m venv venv
3. Installer FastAPI et Uvicorn
pip install fastapi uvicorn

# Endpoints
1. Endpoint GET simple
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

 Exemple :

GET /items/5
2. Endpoint avec paramètres de requête
@app.get("/search/")
def search(q: str = None):
    return {"query": q}

 Exemple :

GET /search/?q=fastapi
3. Endpoint POST
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
def create_item(item: Item):
    return {"item": item}

 Exemple JSON :

{
  "name": "Ordinateur",
  "price": 1200
}
 Documentation automatique

FastAPI génère automatiquement une documentation interactive :

Swagger UI :
http://127.0.0.1:8000/docs
ReDoc :
http://127.0.0.1:8000/redoc
 Exemple complet
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.get("/")
def home():
    return {"message": "API fonctionne"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

@app.post("/users/")
def create_user(user: User):
    return {"user": user}

    Exemples d’utilisation
# Utilisation avec un navigateur

Si ton serveur tourne (uvicorn main:app --reload), tu peux accéder directement :

Page d’accueil :
http://127.0.0.1:8000/
Exemple :
http://127.0.0.1:8000/items/10

Réponse :

{
  "item_id": 10
}
2. Utilisation avec Swagger UI (interface graphique)

FastAPI fournit une interface interactive :

http://127.0.0.1:8000/docs

Tu peux :

Tester les endpoints directement
Envoyer des requêtes GET / POST
Voir les réponses automatiquement
💻 3. Utilisation avec curl (ligne de commande)
🔹 Requête GET
curl -X GET "http://127.0.0.1:8000/items/5"

 Réponse :

{
  "item_id": 5
}
🔹 Requête POST
curl -X POST "http://127.0.0.1:8000/items/" \
-H "Content-Type: application/json" \
-d '{"name": "Téléphone", "price": 500}'

 Réponse :

{
  "item": {
    "name": "Téléphone",
    "price": 500
  }
}
🐍 4. Utilisation avec Python (requests)

Installer requests :

pip install requests
🔹 Exemple GET
import requests

response = requests.get("http://127.0.0.1:8000/items/3")
print(response.json())
🔹 Exemple POST
import requests

data = {
    "name": "Laptop",
    "price": 1500
}

