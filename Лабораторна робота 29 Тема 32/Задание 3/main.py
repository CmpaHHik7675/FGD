import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.figure(figsize=(8, 4))
plt.plot(x, y, marker='o', label="Прості числа")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Лінійний графік")
plt.legend()
plt.grid(True)
plt.show()

df = pd.read_csv('data.csv')
plt.figure(figsize=(8, 4))
sns.histplot(data=df, x="DDD", kde=True)
plt.title("Гістограма для 'DDD'")
plt.xlabel("Значення")
plt.ylabel("Частота")
plt.show()
