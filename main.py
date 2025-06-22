import os
from scraping import book_scrape
from preprocessing import data_process
from models import regression_model, classification_model
import pandas as pd

def main():
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    data_dir = os.path.join(BASE_DIR, "data")
    os.makedirs(data_dir, exist_ok=True)

    print("Veri çekiliyor...")
    df_raw = book_scrape.scrape_books_selenium(page_limit=30)
    raw_csv_path = os.path.join(data_dir, "books_selenium.csv")
    df_raw.to_csv(raw_csv_path, index=False)
    print(f"Ham veri kaydedildi: {raw_csv_path}")

    print("Veri temizleniyor...")
    df_clean = data_process.load_and_clean_data(raw_csv_path)
    clean_csv_path = os.path.join(data_dir, "books_clean.csv")
    df_clean.to_csv(clean_csv_path, index=False)
    print(f"Temizlenmiş veri kaydedildi: {clean_csv_path}")

    print("\nRegresyon model eğitiliyor...")
    regression_model.train_and_evaluate_regression(clean_csv_path)

    print("\nSınıflandırma model eğitiliyor...")
    classification_model.train_and_evaluate_classification(clean_csv_path)

if __name__ == "__main__":
    main()
