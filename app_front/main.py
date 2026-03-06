import os

import requests
import streamlit as st
from dotenv import load_dotenv

# Charge les variables
load_dotenv()
API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

st.set_page_config(page_title="Toolbox IA", page_icon="ʕ•ᴥ•ʔ")
st.title("Toolbox IA - Interface")

# --- Calculateur ---
st.header("Calculateur Magique")
a = st.number_input("Nombre A", value=0.0)
b = st.number_input("Nombre B", value=0.0)

if st.button("Calculer"):
    try:
        res = requests.get(f"{API_URL}/compute/add", params={"a": a, "b": b})
        if res.status_code == 200:
            st.success(f"Résultat : {res.json().get('result')}")
        else:
            st.error("L'API a répondu avec une erreur.")
    except Exception as e:
        st.error(f"Erreur de connexion à l'API : {e}")

# Remplacement de st.divider() pour éviter l'AttributeError
st.markdown("---")

# --- Historique ---
st.header("Historique")
if st.button("Afficher la base de données"):
    try:
        res = requests.get(f"{API_URL}/data")
        st.table(res.json())
    except Exception:  # Remplace le except: vide par except Exception:
        st.warning("Impossible de récupérer l'historique.")
