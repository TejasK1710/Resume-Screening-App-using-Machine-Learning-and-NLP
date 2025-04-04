# -*- coding: utf-8 -*-
"""Resume_ Screening_App.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1j3RKDmkTwqOZ9ESnLVAVooRO3n4Qd7mD

# Data Preprocessing

First, we need to clean the resume text data. Here's how we will process it:
1.   Remove Special Characters and Punctuation.
2.  Convert text to lowercase.
*   Remove stopwords (common words that do not add much meaning).
*   Tokenize (split the text into individual words).
"""

import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# Download NLTK stopwords
nltk.download('punkt_tab')
nltk.download('stopwords')

# Function for cleaning the text
def preprocess_text(text):
    # Remove non-alphabetic characters (special characters, digits)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Convert text to lowercase
    text = text.lower()
    # Tokenize the text
    tokens = word_tokenize(text)
    # Remove stopwords
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    return ' '.join(tokens)

# Example dataset (use your own CSV with 'category' and 'resume' columns)
df = pd.read_csv('/content/UpdatedResumeDataSet.csv')
# Apply preprocessing to the 'resume' column
df['cleaned_resume'] = df['Resume'].apply(preprocess_text)

# Check the cleaned data
print(df.head())

"""# **What this does:**
It removes any characters that aren’t alphabetic.
Converts everything to lowercase.
Tokenizes the text into individual words and removes common stopwords.

#Feature Extraction with TF-IDF
We’ll use TF-IDF (Term Frequency - Inverse Document Frequency) to convert the cleaned resume text into numerical features that the SVM model can understand. TF-IDF helps capture the importance of a word in a document relative to a set of documents (corpus).
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import joblib

# Create TF-IDF Vectorizer
tfidf_vectorizer = TfidfVectorizer(max_features=5000)

# Fit and transform the cleaned resume text data
X = tfidf_vectorizer.fit_transform(df['cleaned_resume']).toarray()

# Prepare target variable (labels)
y = df['Category']  # This should be the 'category' column in your dataset

# Split data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the SVM classifier (with linear kernel)
svm_classifier = SVC(kernel='linear')
svm_classifier.fit(X_train, y_train)

# Predict on the test set
y_pred = svm_classifier.predict(X_test)

# Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

# Save the model and vectorizer for later use
joblib.dump(svm_classifier, 'svm_model.pkl')
joblib.dump(tfidf_vectorizer, 'tfidf_vectorizer.pkl')