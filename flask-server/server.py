from flask import Flask, request, jsonify, session # type: ignore
from flask_cors import CORS # type: ignore
from main import final_object, recommended_phones

app = Flask(__name__)
app.secret_key = 'My secret key'
CORS(app)  # Enable CORS for all routes
responses = {}

@app.route('/questions')
def questions():
    return final_object

@app.route('/submit-responses', methods=['POST'])
def submit_responses():

    responses = request.json
    print(responses)
    session['responses'] = responses
    return {'message': 'Responses saved successfully'}

# Route to get predictions
@app.route('/predictions')
def get_predictions():
    responses = session.get('responses')
    predictions = calculate_predictions(responses)
    return jsonify({"predictions": predictions})

def calculate_predictions(responses):
    predicted_phones = ["Samsung A20", "Iphone 11", "Nokia 3310", "Samsung S20", "OnePlus 8"]
    return predicted_phones


if __name__ == '__main__':
    app.run(debug=True)
