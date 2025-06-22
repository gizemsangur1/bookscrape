import pandas as pd
import os

def load_and_clean_data(input_path: str) -> pd.DataFrame:
    df = pd.read_csv(input_path)

    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df = df.dropna(subset=["price"])

    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
    df = df.dropna(subset=["rating"])

    df["in_stock"] = df["availability"].apply(lambda x: 1 if "In stock" in str(x) else 0)

    df.drop(columns=["title", "url", "availability"], inplace=True)

    return df

if __name__ == "__main__":
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    input_file = os.path.join(BASE_DIR, "data", "books_selenium.csv")
    df_clean = load_and_clean_data(input_file)

    clean_path = os.path.join(BASE_DIR, "data", "books_clean.csv")
    df_clean.to_csv(clean_path, index=False)

    print("Temizlenmiş veri kaydedildi:", clean_path)
    print(df_clean.head())
