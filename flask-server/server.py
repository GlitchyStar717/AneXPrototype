# import pandas as pd
from flask import Flask, request, jsonify, session # type: ignore
from flask_cors import CORS # type: ignore
from main import question_list, recommend
app = Flask(__name__)
app.secret_key = 'My secret key'
CORS(app)  # Enable CORS for all routes
responses = {}

@app.route('/questions')
def questions():
    final_object = question_list()
    return final_object

@app.route('/submit-responses', methods=['POST'])
def submit_responses():
    global responses
    responses = request.json
    print("\n\n\nRESPONSES        :       ",responses,end='\n\n\n\n')
    return jsonify({'message': 'Responses saved successfully'})

# Route to get predictions
@app.route('/predictions')
def get_predictions():
    # responses = session.get('responses')
    global responses
    print("\n\n\nRESPONSES        :       ",responses,end='\n\n\n\n')
    predictions = recommend(responses)
    return jsonify({"predictions": predictions})

# def calculate_predictions(responses):
#     responses = session.get('responses')
#     print("\n\n\nRESPONSES        :       ",responses,end='\n\n\n\n')
#     return predicted_phones

if __name__ == '__main__':
    app.run(debug=True, port=5001)
