import requests
import datetime

def test_main_server():
    # Adres głównego serwera (w Docker Compose będzie to localhost:5000)
    main_server_url = "http://localhost:5000"

    print(f"Test klienta rozpoczęty: {datetime.datetime.now()}")
    try:
        # Wysyłanie zapytania GET do głównego serwera
        response = requests.get(main_server_url)

        # Wyświetlanie odpowiedzi
        print(f"Status: {response.status_code}")
        print(f"Odpowiedź z serwera: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Błąd podczas połączenia z serwerem: {e}")

if __name__ == "__main__":
    test_main_server()
