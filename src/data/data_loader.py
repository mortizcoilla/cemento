import os
import pandas as pd

def load_data():
    """
    Carga el conjunto de datos desde la ubicación especificada.
    """
    raw_data_path = os.path.join(os.getcwd(), "data/raw/concrete_data.csv")
    if not os.path.exists(raw_data_path):
        raise FileNotFoundError(f"Archivo no encontrado en: {raw_data_path}")
    data = pd.read_csv(raw_data_path)
    print("Datos cargados correctamente.")
    return data
