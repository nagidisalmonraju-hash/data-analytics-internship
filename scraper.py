import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

book_data = []

page = 1

while True:

    url = base_url.format(page)

    response = requests.get(url)

    if response.status_code != 200:
        break

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    if not books:
        break

    for book in books:

        title = book.h3.a["title"]

        book_url = book.h3.a["href"]

        price = book.find("p", class_="price_color").text

        rating = book.find("p", class_="star-rating")["class"][1]

        availability = book.find(
            "p", class_="instock availability"
        ).text.strip()

        book_data.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability,
            "URL": book_url
        })

    print("Scraped page:", page)

    page += 1


# Create DataFrame
df = pd.DataFrame(book_data)


# Clean Price
df["Price"] = df["Price"].str.replace(r"[^\d.]", "", regex=True)
df["Price"] = pd.to_numeric(df["Price"])

# Clean Rating
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating"] = df["Rating"].map(rating_map)


# Check total books
print("\nTotal books:", len(df))


# Show first 5 rows
print(df.head())


# Show data types
print("\nData types:")
print(df.dtypes)
df.to_csv("data/books.csv", index=False)

print("\nDataset saved successfully!")
# Verify saved dataset
df_check = pd.read_csv("data/books.csv")

print("\nDataset shape:")
print(df_check.shape)

print("\nFirst 5 rows:")
print(df_check.head())

print("\nMissing values:")
print(df_check.isnull().sum())
print("\nColumns:")
print(df_check.columns.tolist())

print("\nFirst URL:")
print(df_check["URL"].iloc[0])
