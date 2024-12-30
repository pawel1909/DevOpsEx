#!/usr/bin/env python3

import urllib.request
import time

while True:
    try:
        # Wysyłanie zapytania do serwera
        fp = urllib.request.urlopen("http://localhost:1234/")
        encodeContent = fp.read()
        decodedContent = encodeContent.decode("utf8")

        print(decodedContent)
        fp.close()

        # Odczekanie 5 sekund przed kolejnym zapytaniem
        time.sleep(5)

    except KeyboardInterrupt:
        print("Zatrzymano klienta.")
        break
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
        with open('log.txt', 'w') as f:
            f.writelines(e)
        time.sleep(5)
