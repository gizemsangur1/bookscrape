import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def train_and_evaluate_regression(input_csv_path: str):
    df = pd.read_csv(input_csv_path)

    X = df[["rating", "in_stock"]]
    y = df["price"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Regresyon Modeli Performansı:")
    print(f"Mean Squared Error (MSE): {mse:.4f}")
    print(f"R² Skoru: {r2:.4f}")

    # Burada sample'ı DataFrame olarak verdik, kolon isimleriyle
    sample = pd.DataFrame([[5, 1]], columns=["rating", "in_stock"])
    predicted_price = model.predict(sample)[0]
    print(f"Örnek Tahmini Fiyat (rating=5, in_stock=1): £{predicted_price:.2f}")

if __name__ == "__main__":
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    clean_data_path = os.path.join(BASE_DIR, "data", "books_clean.csv")

    train_and_evaluate_regression(clean_data_path)
