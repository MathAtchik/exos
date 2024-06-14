from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    question = request.data.decode('utf-8')
    # Simuler une réponse à la question
    response = f"La réponse à votre question '{question}' est 42."
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)