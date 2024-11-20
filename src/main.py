import os
from src.data.data_loader import load_data
from src.utils.normalization import normalize_data
from src.models.train_model import build_model
from src.models.evaluate_model import evaluate_model

def main():
    # Cargar los datos
    data = load_data()
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]

    # Normalizar los datos
    X_normalized = normalize_data(X)

    # Evaluar configuraciones
    print("\nPaso A: Modelo básico")
    mean_a, std_a = evaluate_model(X, y, model_fn=lambda: build_model(layers=1), epochs=50)
    print(f"Media del MSE: {mean_a}, Desviación estándar: {std_a}")

    print("\nPaso B: Normalización")
    mean_b, std_b = evaluate_model(X_normalized, y, model_fn=lambda: build_model(layers=1), epochs=50)
    print(f"Media del MSE: {mean_b}, Desviación estándar: {std_b}")

    print("\nPaso C: 100 épocas")
    mean_c, std_c = evaluate_model(X_normalized, y, model_fn=lambda: build_model(layers=1), epochs=100)
    print(f"Media del MSE: {mean_c}, Desviación estándar: {std_c}")

    print("\nPaso D: 3 capas ocultas")
    mean_d, std_d = evaluate_model(X_normalized, y, model_fn=lambda: build_model(layers=3), epochs=50)
    print(f"Media del MSE: {mean_d}, Desviación estándar: {std_d}")

if __name__ == "__main__":
    main()
