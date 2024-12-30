from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint do odbioru danych
@app.route('/data', methods=['POST'])
def save_data():
    data = request.json
    if not data or 'value' not in data:
        return jsonify({'error': 'Invalid data'}), 400
    
    # Zapisz dane do pliku
    with open('data.txt', 'a') as f:
        f.write(f"{data['value']}\n")
    
    return jsonify({'message': 'Data saved'}), 200

# Endpoint do odczytu zapisanych danych
@app.route('/data', methods=['GET'])
def get_data():
    try:
        with open('data.txt', 'r') as f:
            lines = f.readlines()
        return jsonify({'data': [line.strip() for line in lines]}), 200
    except FileNotFoundError:
        return jsonify({'data': []}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
