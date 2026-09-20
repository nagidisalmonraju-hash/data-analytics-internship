import pandas as pd

df = pd.read_csv("data/books.csv")

print("Dataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())
print("\nAverage price:")
print(df["Price"].mean())

print("\nMinimum price:")
print(df["Price"].min())

print("\nMaximum price:")
print(df["Price"].max())
print("\nBooks by rating:")
print(df["Rating"].value_counts().sort_index())
import matplotlib.pyplot as plt

rating_counts = df["Rating"].value_counts().sort_index()

plt.bar(rating_counts.index, rating_counts.values)

plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.title("Books by Rating")

plt.savefig("images/books_by_rating.png")

plt.show()
plt.hist(df["Price"], bins=10)

plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.title("Price Distribution of Books")
plt.savefig("images/price_distribution.png")
plt.show()
print("\nTop 10 Most Expensive Books:")
top_10_expensive = df.sort_values("Price", ascending=False).head(10)

print(top_10_expensive[["Title", "Price", "Rating"]])
print("\nTop 10 Cheapest Books:")

top_10_cheapest = df.sort_values("Price", ascending=True).head(10)

print(top_10_cheapest[["Title", "Price", "Rating"]])
print("\nAverage Price by Rating:")

average_price_by_rating = df.groupby("Rating")["Price"].mean()

print(average_price_by_rating)
average_price_by_rating = df.groupby("Rating")["Price"].mean()

plt.bar(
    average_price_by_rating.index,
    average_price_by_rating.values
)

plt.xlabel("Rating")
plt.ylabel("Average Price (£)")
plt.title("Average Book Price by Rating")
plt.savefig("images/average_price_by_rating.png")

plt.show()