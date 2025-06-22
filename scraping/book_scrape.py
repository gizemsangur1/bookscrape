from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
import os

RATING_MAP = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

def get_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)
    return driver

def scrape_books_selenium(page_limit=5):
    driver = get_driver()
    base_url = "http://books.toscrape.com/catalogue/page-{}.html"
    data = []

    for page in range(1, page_limit + 1):
        url = base_url.format(page)
        print(f"Scraping page {page} ...")
        driver.get(url)
        time.sleep(1)

        books = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")

        for book in books:
            try:
                title = book.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a").get_attribute("title")
                price = book.find_element(By.CSS_SELECTOR, "p.price_color").text.replace("\u00a3", "").strip()
                price = float(price)

                availability = book.find_element(By.CSS_SELECTOR, "p.instock.availability").text.strip()
                rating_class = book.find_element(By.CSS_SELECTOR, "p.star-rating").get_attribute("class").split()[-1]
                rating = RATING_MAP.get(rating_class, 0)

                detail_url = book.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a").get_attribute("href")

                data.append({
                    "title": title,
                    "price": price,
                    "availability": availability,
                    "rating": rating,
                    "url": detail_url
                })
            except Exception as e:
                print("Hata:", e)
                continue

        time.sleep(1)

    driver.quit()
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = scrape_books_selenium(page_limit=30)
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    data_dir = os.path.join(BASE_DIR, "data")
    os.makedirs(data_dir, exist_ok=True)

    csv_path = os.path.join(data_dir, "books_selenium.csv")
    df.to_csv(csv_path, index=False)
    print(f"Veri başarıyla kaydedildi: {csv_path}")
