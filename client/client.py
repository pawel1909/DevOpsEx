import requests
import time

# Wysyłanie przykładowych danych do serwera
url = 'http://localhost:5000/data'
i = 0

while True:
    data = {'value': i}

    response = requests.post(url, json=data)
    print(f"Response: {response.status_code}, {response.json()}")

    # Pobieranie danych z serwera
    response = requests.get(url)
    print(f"Data from server: {response.json()}")

    i += 2
    if i > 2137:
        i = 0
    time.sleep(15)
