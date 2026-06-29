from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "status": "online",
        "mensagem": "API de DevOps e Observabilidade - Unidade 4",
        "timestamp": time.time()
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)