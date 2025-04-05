import streamlit as st
import joblib
import fitz  # PyMuPDF for PDF handling
import os

# Load the trained model and TF-IDF vectorizer
svm_classifier = joblib.load('svm_model.pkl')
tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Function to extract text from PDF files
import io

# Function to extract text from PDF files
def extract_text_from_pdf(pdf_file):
    # Convert the Streamlit file object to bytes
    pdf_bytes = pdf_file.read()
    # Create a PyMuPDF document from the byte stream
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    text = ''
    # Extract text from each page
    for page in doc:
        text += page.get_text()
    return text

import re
import nltk
from nltk.corpus import stopwords

# Download the stopwords corpus
nltk.download('stopwords')

# Define preprocessing function
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove special characters and digits (keep only alphabetic words)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Tokenize the text (split it into words)
    words = text.split()
    
    # Remove stopwords (commonly used words that do not contribute much meaning)
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    
    # Join the words back into a string
    cleaned_text = " ".join(words)
    
    return cleaned_text

# Function to preprocess and predict resume category
def predict_category(resume_text):
    # Preprocess the resume text
    cleaned_resume = preprocess_text(resume_text)
    
    # Transform the text into TF-IDF features
    resume_vectorized = tfidf_vectorizer.transform([cleaned_resume]).toarray()
    
    # Predict the category
    prediction = svm_classifier.predict(resume_vectorized)
    
    return prediction[0]

# Streamlit UI
st.title("Resume Screening App")
st.write("Upload your resume (PDF or TXT) for category prediction.")

# Upload resume file
uploaded_file = st.file_uploader("Choose a file", type=["pdf", "txt"])

if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        resume_text = extract_text_from_pdf(uploaded_file)
    else:
        resume_text = str(uploaded_file.read(), 'utf-8')
    
    # Display the extracted text (optional, can be removed later)
    st.subheader("Extracted Resume Text")
    st.write(resume_text[:1000])  # Show the first 1000 characters

    # Predict the category
    if st.button('Predict Category'):
        category = predict_category(resume_text)
        st.subheader(f"Predicted Category: {category}")
