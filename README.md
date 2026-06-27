# 🤖 AI Resume Scanner & Skill Gap Predictor

A Flask-based web application that analyzes resumes using NLP and ML to identify skill gaps and suggest personalized learning paths.

---

## ✨ Features

- 📄 PDF/DOCX Resume Upload with OCR Support
- 🧠 NLP-based Skill Extraction using Sentence-BERT
- 📊 Skill Gap Analysis with Match Score
- 🏆 Resume Grading System (A+/A/B/C/D)
- 💼 Job Role Suggester with Salary Insights
- 📅 Weekly Learning Path Recommendations
- 🔊 Voice Summary using Text-to-Speech
- 📈 Visual Charts for Missing Skills
- 🌓 Dark/Light Mode Toggle
- 💾 Scan History Dashboard

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Primary Language |
| Flask | Web Framework |
| Sentence-BERT | Semantic Similarity |
| spaCy | NLP Processing |
| PyMuPDF | PDF Text Extraction |
| Tesseract OCR | Image PDF Support |
| SQLite | Database |
| Matplotlib | Charts |
| gTTS | Text-to-Speech |

---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/KashishVarshney-star123/AI-resume-Scanner.git
cd AI-resume-Scanner
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 3. Install Tesseract OCR
- Download: https://github.com/UB-Mannheim/tesseract/wiki
- Install and add to PATH

### 4. Install Poppler
- Download: https://github.com/oschwartz10612/poppler-windows/releases/
- Extract to C:\poppler

### 5. Run the App
```bash
python app.py
```

### 6. Open Browser
```
http://127.0.0.1:5000
```

---

## 🚀 How It Works

```
1. Upload Resume (PDF/DOCX)
        ↓
2. Text Extraction (PyMuPDF + OCR)
        ↓
3. Skill Extraction (spaCy + NLP)
        ↓
4. Gap Analysis (Sentence-BERT)
        ↓
5. Results + Grade + Job Roles
        ↓
6. Learning Path + Voice Summary
        ↓
7. Save to Database → Dashboard
```

---

## 👩‍💻 Author

**Kashish Varshney**
- GitHub: [@KashishVarshney-star123](https://github.com/KashishVarshney-star123)

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).