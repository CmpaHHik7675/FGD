import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Отримані дані:")
    print(data)
else:
    print("Помилка при запиті.")
