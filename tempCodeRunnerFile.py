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

plt.show()
plt.hist(df["Price"], bins=10)

plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.title("Price Distribution of Books")

plt.show()