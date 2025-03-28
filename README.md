# Resume Screening App using Machine Learning and NLP

## 📌 Project Description
The Resume Screening App is an AI-powered application designed to **automatically analyze and filter resumes** based on predefined criteria like skills, experience, education, etc. It helps recruiters quickly identify the most suitable candidates for a job by leveraging techniques from Natural Language Processing (NLP) and Machine Learning.

---

## ✅ Features
- Extracts text from resumes (PDF, DOCX).
- Cleans and preprocesses text data.
- Extracts key information such as skills, experience, and education.
- Uses NLP models for keyword matching and semantic understanding.
- Classifies resumes as "Suitable" or "Not Suitable" based on requirements.
- Provides a simple user interface for uploading resumes and displaying results.
- Can be expanded with advanced features like Named Entity Recognition (NER).

---

## 📂 Project Structure
```
├── README.md
├── app.py                 # Main application file (if using Flask/Streamlit)
├── requirements.txt       # Dependencies
├── data/                  # Folder for storing resumes (PDFs, DOCX)
├── models/                # Trained models
├── utils/                 # Helper functions (text extraction, preprocessing, etc.)
├── static/                # CSS/JS files (if using Flask)
├── templates/             # HTML files (if using Flask)
└── notebooks/             # Jupyter notebooks for experimentation
```

---

## 📦 Dependencies
```
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
git clone https://github.com/your-username/resume-screening-app.git
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Download pre-trained models (if needed, e.g., Spacy models):
```
python -m spacy download en_core_web_sm
```

---

## 📊 Usage
1. Add resumes to the `data/` folder.
2. Run the application:
```
python app.py
```
3. Upload resumes via the UI and view the screening results.

---

## 📈 Future Enhancements
- Add Named Entity Recognition (NER) for better skill extraction.
- Integrate with cloud-based storage.
- Add advanced NLP models like BERT for improved performance.

---

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

