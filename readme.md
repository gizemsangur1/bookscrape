# Book Price Scraping & Machine Learning Project

Unlock the power of real-world data scraping and predictive modeling with this end-to-end project that combines web scraping, data preprocessing, and machine learning — all focused on predicting book prices!

---

## 🚀 Project Overview

This project demonstrates how to:

- **Scrape** dynamic, real-world data from the [Books to Scrape](http://books.toscrape.com/) website using Selenium automation.
- **Clean and preprocess** raw scraped data for reliable analysis.
- **Build and evaluate** machine learning models:
  - A **Regression model** to predict book prices based on features like customer rating and availability.
  - A **Classification model** to predict stock availability (note: limited by dataset imbalance).

By working with live scraped data, this project bridges the gap between raw web data and actionable business insights through machine learning.

---

## 🔍 Why This Project?

- **Hands-on scraping experience:** Learn how to automate data extraction from real websites using Selenium.
- **Data science pipeline:** See the full flow from data collection, cleaning, to model training and evaluation.
- **Practical machine learning:** Understand regression and classification tasks with interpretable results.
- **Expandability:** Easily extend this framework to other datasets or add advanced ML models.


---

## ⚙️ Setup & Usage

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/book_price_project.git
cd book_price_project

```

2. **Create and activate a virtual environment**

```

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

````

3. **Install dependencies**

```

pip install -r requirements.txt

````
4. **Run the pipeline**

```

python main.py

````

## Results & Insights
The regression model provides a baseline attempt to predict book prices using features like rating and stock availability. However, current results show limited predictive power, indicating room for improvement.

The classification model attempts to predict stock status, but due to the dataset containing almost exclusively in-stock samples, its accuracy is not meaningful.

Both models can be significantly enhanced with better feature engineering, hyperparameter tuning, and more diverse and balanced datasets.