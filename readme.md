# CV–Job Matching API

A Flask-based NLP system that matches candidate CVs with job descriptions using TF–IDF and cosine similarity.

---

## Overview

This project automatically matches candidate resumes to relevant job descriptions.
It uses **TF–IDF vectorization** to convert text into feature vectors and **cosine similarity** to measure how closely a CV aligns with each job role.

Ideal for recruitment automation, HR analytics, or intelligent resume screening.

---

## Features

* Uses **TF–IDF + cosine similarity** for accurate text-based matching
* Extracts text from **PDF, DOCX, and TXT** resumes
* Cleans and preprocesses both CV and job description text
* Returns **top 5 best-matched jobs** for each resume
* Simple RESTful **Flask API endpoint**

---

## Project Structure

```
cv_job_matcher/
│
├── app.py                   # Main Flask application
├── job_descriptions.csv      # Job descriptions dataset
├── cv_files/                 # Folder with CVs
│   ├── candidate1.pdf
│   ├── candidate2.docx
│   └── ...
└── README.md
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/cv-job-matcher.git
cd cv-job-matcher
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```
Flask
pandas
pdfplumber
python-docx
scikit-learn
```

---

## How It Works

1. Extracts text from all CVs in the `cv_files` directory.
2. Cleans and vectorizes text from both CVs and job descriptions.
3. Calculates **cosine similarity** between each CV and all job roles.
4. Returns the **top 5 most relevant jobs** for a given CV text input.

---

## API Endpoint

### POST `/match`

**Request JSON:**

```json
{
  "cv_text": "Experienced data scientist with background in Python, ML, and NLP..."
}
```

**Response JSON:**

```json
{
  "matched_jobs": [
    "Data Scientist",
    "Machine Learning Engineer",
    "AI Research Associate",
    "Data Analyst",
    "NLP Engineer"
  ]
}
```

---

## Example Usage (Python)

```python
import requests

url = "http://127.0.0.1:5000/match"
cv_text = open("my_resume.txt").read()

response = requests.post(url, json={"cv_text": cv_text})
print(response.json())
```

---

## Dataset Format

**job_descriptions.csv**

| job_title      | job_description                                        |
| -------------- | ------------------------------------------------------ |
| Data Scientist | Analyze large datasets to extract actionable insights. |
| ML Engineer    | Build and optimize machine learning pipelines.         |

---

## Future Improvements

* Use **BERT or spaCy embeddings** for semantic similarity
* Add **keyword weighting** and **skill extraction**
* Develop a **Streamlit or React-based dashboard** for HR teams
* Include **candidate scoring and ranking**

---

## Author

* **Mauli Patel**
* Data Science and AI Enthusiast
* LinkedIn: [linkedin.com/in/maulipatel](https://linkedin.com/in/maulipatel)
* Email: [maulipatel@example.com](mailto:maulipatel@example.com)
