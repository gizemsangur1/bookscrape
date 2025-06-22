import pandas as pd
df = pd.read_csv("books_selenium.csv")

df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df = df.dropna(subset=["price"])
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
df = df.dropna(subset=["rating"])
df["in_stock"] = df["availability"].apply(lambda x: 1 if "In stock" in str(x) else 0)

df.drop(columns=["title", "url", "availability"], inplace=True)



print(df.head())
