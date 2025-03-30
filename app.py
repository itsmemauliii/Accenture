from flask import Flask, request, jsonify
import pandas as pd
import os
import re
import pdfplumber
from docx import Document
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

CV_FOLDER = "cv_files/"  # Folder containing 200 CVs

# Function to extract text from CVs
def extract_text(file_path):
    text = ""
    if file_path.endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            text = " ".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    elif file_path.endswith(".docx"):
        doc = Document(file_path)
        text = " ".join([para.text for para in doc.paragraphs])
    elif file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
    return text.strip()

# Load all CVs into a dataframe
cv_data = []
for file in os.listdir(CV_FOLDER):
    file_path = os.path.join(CV_FOLDER, file)
    if file.endswith((".pdf", ".docx", ".txt")):
        text = extract_text(file_path)
        if text:
            cv_data.append({"filename": file, "cv_text": text})

cv_df = pd.DataFrame(cv_data)

# Load Job Descriptions
job_data = pd.read_csv("job_descriptions.csv")

# Text Cleaning
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text

cv_df["cleaned_cv"] = cv_df["cv_text"].apply(clean_text)
job_data["cleaned_job"] = job_data["job_description"].apply(clean_text)

# Convert text to vectors
vectorizer = TfidfVectorizer()
cv_vectors = vectorizer.fit_transform(cv_df["cleaned_cv"])
job_vectors = vectorizer.transform(job_data["cleaned_job"])

@app.route("/match", methods=["POST"])
def match_cv():
    data = request.json
    cv_text = clean_text(data["cv_text"])
    cv_vector = vectorizer.transform([cv_text])
    scores = cosine_similarity(cv_vector, job_vectors).flatten()
    top_jobs = scores.argsort()[-5:][::-1]
    matched_jobs = job_data.iloc[top_jobs]["job_title"].tolist()

    return jsonify({"matched_jobs": matched_jobs})

if __name__ == "__main__":
    app.run(debug=True)
