from flask import Flask
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def route_request():
    current_hour = datetime.now().hour
    if 6 <= current_hour < 18:  # W godzinach 6-18 kierujemy na serwer A
        response = requests.get('http://server_a:5001')
    else:  # Poza tym czasem kierujemy na serwer B
        response = requests.get('http://server_b:5002')
    return response.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
