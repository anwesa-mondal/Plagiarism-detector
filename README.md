**Plagiarism Detector**

A machine learning-based application designed to detect plagiarism in text documents. This tool analyzes text content and identifies potential similarities using natural language processing (NLP) techniques.
A robust and user-friendly Chrome extension powered by a machine learning model to detect plagiarism in text. The extension integrates a Flask-based backend and leverages a pre-trained model (model.pkl) to analyze input text and provide predictions.


**Features**

Text Detection: Analyze text for plagiarism using a trained machine learning model.
Chrome Integration: Interact with the system directly through a browser extension.
Flask Backend: A lightweight REST API for model inference.
Preprocessing: Automatic text preprocessing for accurate predictions.
User-Friendly Interface: Simple and intuitive Chrome extension UI for entering and analyzing text.


**Technologies Used**

Python: For backend and model integration.
Flask: To create the REST API and for deployment.
NLP: Scikit-learn, NLTK, string
Scikit-learn: For training and saving the model (model.pkl).
Data Processing: Pandas, NumPy
Chrome Extension: For a user-friendly interface.
HTML/CSS/JavaScript: To build the extension UI.
Vectorization: TF-IDF

**Working**

Backend:

The Flask server (app.py) hosts an endpoint (/detect) to receive and process text input.
It loads the machine learning model from model.pkl and uses the detect(input_text) function to make predictions.

Chrome Extension:

Users enter text in the Chrome extension interface (a popup).
The extension sends the input to the Flask server via a POST request.
The server processes the input and returns the prediction, which is displayed in the extension.


**Future Enhancements**

Deploy the Flask backend to the cloud for global access.
Add support for real-time plagiarism checking in text editors (e.g., Google Docs, Word).
Enhance the UI for better user interaction.
Add multilingual text analysis capabilities.
