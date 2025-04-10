import streamlit as st  # <-- Cette ligne manquait !
import os
import pandas as pd
from utils import load_data

# Configuration de la page
st.set_page_config(page_title="Dashboard Phosphorique", layout="wide")

# Chemin absolu vérifié
EXCEL_PATH = r"C:\Users\Timo\jfc1-phosphorique-optimisation\data\ABD_PRO.xlsx"

# Debug (visible dans la console)
print(f"Chemin utilisé : {EXCEL_PATH}")

try:
    # Chargement des données
    df = load_data(EXCEL_PATH)
    
    # Affichage Streamlit
    st.title("📊 Dashboard JFC1")
    st.metric("Fichier chargé", "Succès !")
    st.dataframe(df.head())
    
except Exception as e:
    st.error(f"Erreur de chargement : {str(e)}")
    st.warning(f"Chemin essayé : {EXCEL_PATH}")