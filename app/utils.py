import pandas as pd
import os

def load_data(path):
    """Version ultra-robuste"""
    try:
        if not os.path.isfile(path):
            raise FileNotFoundError(
                f"Fichier {path} introuvable. "
                f"Contenu du dossier : {os.listdir(os.path.dirname(path))}"
            )
        return pd.read_excel(path, sheet_name="Feuil1")
    except Exception as e:
        raise Exception(f"Erreur avec le fichier {path} : {str(e)}")