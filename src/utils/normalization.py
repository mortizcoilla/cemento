from sklearn.preprocessing import StandardScaler

def normalize_data(X):
    """
    Normaliza las características X utilizando StandardScaler.
    """
    scaler = StandardScaler()
    X_normalized = scaler.fit_transform(X)
    return X_normalized
