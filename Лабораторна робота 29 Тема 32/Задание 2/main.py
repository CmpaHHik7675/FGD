import pandas as pd

df = pd.read_csv('data.csv')

print("Перші 5 рядків даних:")
print(df.head())
print()
print("Описова статистика:")
print(df.describe())

