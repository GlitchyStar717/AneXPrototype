from flask import Flask, request, jsonify, session # type: ignore
from flask_cors import CORS # type: ignore
from main import final_object, recommend
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
    print("\n\n\nRESPONSES        :       ",responses,end='\n\n\n\n')
    session['responses'] = responses
    return jsonify({'message': 'Responses saved successfully'})

# Route to get predictions
@app.route('/predictions')
def get_predictions():
    responses = session.get('responses')
    predictions = recommend(responses)
    return jsonify({"predictions": predictions})

# def calculate_predictions(responses):
#     responses = session.get('responses')
#     print("\n\n\nRESPONSES        :       ",responses,end='\n\n\n\n')
#     return predicted_phones



if __name__ == '__main__':
    app.run(debug=True)
