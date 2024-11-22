from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
tfidf_vectorizer=pickle.load(open('tfidf_vectorizer.pkl','rb'))

def detect(input_text):
    #vectorize the text
    vectorized_text=tfidf_vectorizer.transform([input_text])
    #prediction by model
    result=model.predict(vectorized_text)
    return "PLAGIARISM DETECTED" if result[0]==1 else "NO PLAGIARISM"

@app.route('/', methods=['GET'])
def handle_get():
    if request.method == 'GET':
        return jsonify({'message': 'GET request received'})

@app.route('/predict', methods=['POST'])
def predict():

    # Get the text input from the request
    text_input = request.get_json().get('text', None)
    
    if not text_input:
        return jsonify({'error': 'No text input provided'}), 400
    
    # Predict the output using the model
    prediction = detect(text_input)
    
    # Send the prediction back as a response
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)