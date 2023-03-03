import pandas as pd

df = pd.read_csv("note11.csv")

print("first 5 Rows:")
print(df.head(5))

print("\nlast 5 Rows:")
print(df.tail(5))

