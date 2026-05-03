# Resume Analyzer

A keyword-matching **Resume Analyzer** built with Python and **spaCy NLP** that extracts skills from resumes, compares them against job descriptions, and generates a **match score** with missing skills highlighted.

---

## Features

- Extracts skills from resume using spaCy NLP + keyword matching
- Parses job description for required skills
- Calculates a **match score (%)** between resume and JD
- Highlights **matched skills** and **missing skills**
- Extracts contact info (email, phone) automatically
- Color-coded result: Strong / Moderate / Low match

---

## Sample Output

```
============================================================
         RESUME ANALYZER — Powered by spaCy NLP
============================================================

📧 Email   : priyaanandan682@gmail.com
📞 Phone   : +91 76959 52974

✅ Skills in Resume  : 14
📋 Skills in JD      : 9
🎯 Matched Skills    : 7
❌ Missing Skills    : 2

📊 Match Score       : 77.78%
🟢 Strong match! Go ahead and apply.

✅ Matched Skills:
   deep learning, git, mysql, numpy, opencv, pandas, python, tensorflow

❌ Missing Skills (add these to improve your resume):
   docker, rest api
============================================================
```

---

## Tech Stack

- **Python 3.x**
- **spaCy** — NLP text processing
- **re** — regex for contact extraction
- **pathlib** — file handling

---

## Project Structure

```
resume-analyzer/
│
├── resume_analyzer.py   # Main script
├── requirements.txt     # Dependencies
└── README.md
```

---

## Setup & Run

### 1. Clone the repository
```bash
git clone https://github.com/PriyaAnandhan1901/resume-analyzer.git
cd resume-analyzer
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 3. Run the analyzer
```bash
python resume_analyzer.py
```

To analyze your own resume:
1. Save your resume as a `.txt` file
2. Update `resume_file` and `SAMPLE_JD` in the script
3. Run the script

---

## How It Works

1. **Text Extraction** — Reads resume from a `.txt` file
2. **Skill Extraction** — Matches text against a 60+ skills bank using regex + spaCy noun chunks
3. **JD Parsing** — Same extraction applied to the job description
4. **Match Score** — `(matched skills / JD skills) * 100`
5. **Output** — Displays score, matched skills, and missing skills

---

## Author

**Priya A**
- GitHub: [github.com/PriyaAnandhan1901](https://github.com/PriyaAnandhan1901)
- LinkedIn: [linkedin.com/in/priyaanandhan1901](https://linkedin.com/in/priyaanandhan1901)
- Email: priyaanandan682@gmail.com
