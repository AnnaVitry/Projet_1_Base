from fastapi import FastAPI
from maths.mon_module import add

app = FastAPI(title="Toolbox IA API")

# Simulation d'une base de données en mémoire
fake_db = []


@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API de la Toolbox IA ʕ•ᴥ•ʔ"}


@app.get("/compute/add")
def compute_add(a: int, b: int):
    """Expose la fonction add du Projet 1 via une URL."""
    result = add(a, b)
    return {"operation": "addition", "a": a, "b": b, "result": result}


@app.post("/data")
def create_data(item: dict):
    """Route POST pour sauvegarder des données"""
    fake_db.append(item)
    return {"status": "success", "added": item}


@app.get("/data")
def get_all_data():
    """Route GET pour récupérer les données"""
    return {"database_content": fake_db}
