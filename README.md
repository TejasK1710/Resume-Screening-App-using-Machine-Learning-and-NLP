# Resume Screening App using Machine Learning and NLP

## Description 📜
The Resume Screening App is an application that classifies resumes into predefined categories (e.g., Data Science, HR, Data Engineer) based on their content. It uses Machine Learning (SVM) and Natural Language Processing (NLP) techniques for text classification. The app allows users to upload a resume in .pdf or .txt format and receive a predicted category for the resume. 📂✨

---

## Features 🔥
-Upload resumes in PDF or TXT format. 📥
-Text extraction from PDF files. 📄➡️📝
-Preprocessing of resume text (cleaning and tokenization). 🧹🧠
-Prediction of the resume's category using a pre-trained SVM model. 🤖
-Display the predicted category. 🏷️

## Technologies Used ⚙️
Python 🐍: Programming language.

Streamlit 🌐: Web app framework.

PyMuPDF (fitz) 📚: PDF text extraction.

Scikit-learn 📊: For training and prediction with SVM.
---
```
```
## 📦 Dependencies
pandas
numpy
spacy
nltk
scikit-learn
transformers
pdfplumber
PyPDF2
docx2txt
streamlit (if using Streamlit for UI)
flask (if using Flask for UI)
```

---

## 🚀 Installation
1. Clone the repository:
```
git clone https://github.com/yourusername/resume-screening-app.git
```

2. Install dependencies:
```
pip install -r requirements.txt
```

---


```
python app.py
```
3. Upload resumes via the UI and view the screening results.

---
```
## 📈 Future Enhancements
- Add Named Entity Recognition (NER) for better skill extraction.
- Integrate with cloud-based storage.
- Add advanced NLP models like BERT for improved performance.


---

## How to Use 📚
Open the app in your browser (Streamlit should automatically open a browser window).

Upload your resume in .pdf or .txt format.

The app will process your resume and predict its category (e.g., Data Science, HR, Data Engineer).

View the predicted category displayed on the screen. 🧐
```
```
## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
```


