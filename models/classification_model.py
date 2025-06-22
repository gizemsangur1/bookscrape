import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

def train_and_evaluate_classification(input_csv_path: str):
    df = pd.read_csv(input_csv_path)

    X = df[["rating", "price"]]
    y = df["in_stock"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    clf = LogisticRegression(max_iter=1000)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    print("Sınıflandırma Modeli Performansı:")
    print(f"Doğruluk (Accuracy): {acc:.4f}")
    print("Classification Report:")
    print(report)

    sample = [[5, 30.0]]
    pred_stock = clf.predict(sample)[0]
    print(f"Örnek Stok Durumu Tahmini (rating=5, price=30): {pred_stock} (1=Stokta, 0=Stokta Değil)")

if __name__ == "__main__":
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    clean_data_path = os.path.join(BASE_DIR, "data", "books_clean.csv")

    train_and_evaluate_classification(clean_data_path)
