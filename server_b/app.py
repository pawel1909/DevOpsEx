from flask import Flask

app = Flask(__name__)

@app.route('/')
def response_b():
    return "Dobry wieczór! To jest serwer B."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
