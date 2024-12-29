import requests

# Wysyłanie przykładowych danych do serwera
url = 'http://localhost:5000/data'
i = int(input("Wprowadź liczbę: "))
data = {'value': i}

response = requests.post(url, json=data)
print(f"Response: {response.status_code}, {response.json()}")

# Pobieranie danych z serwera
response = requests.get(url)
print(f"Data from server: {response.json()}")
