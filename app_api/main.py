from fastapi import Depends, FastAPI
from maths.mon_module import add
from models.models import Base, Calcul
from modules.connect import engine, get_db
from sqlalchemy.orm import Session

# Création des tables (pour le test local en SQLite)
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/compute/add")
def compute_add(a: float, b: float, db: Session = Depends(get_db)):
    """Fait  le calcule l'addition de deux nombres et enregistre le résultat."""
    res = add(a, b)
    # On enregistre en base de données
    nouveau_calcul = Calcul(a=a, b=b, resultat=res)
    db.add(nouveau_calcul)
    db.commit()

    return {"result": res, "saved": True}


@app.get("/data")
def get_history(db: Session = Depends(get_db)):
    """Récupère l'historique des calculs."""
    return db.query(Calcul).all()
