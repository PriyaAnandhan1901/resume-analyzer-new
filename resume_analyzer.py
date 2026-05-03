import spacy
import re
import sys
from pathlib import Path

# ─── Load spaCy model ────────────────────────────────────────────────────────
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("[INFO] Downloading spaCy model ...")
    import subprocess
    subprocess.run([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

# ─── Common Tech Skills Bank ─────────────────────────────────────────────────
SKILLS_BANK = {
    "python", "java", "c", "c++", "javascript", "typescript", "sql", "r",
    "tensorflow", "keras", "pytorch", "scikit-learn", "opencv", "numpy",
    "pandas", "matplotlib", "seaborn", "nltk", "spacy", "huggingface",
    "html", "css", "react", "nodejs", "flask", "django", "fastapi",
    "mysql", "postgresql", "sqlite", "mongodb", "firebase",
    "git", "github", "docker", "kubernetes", "aws", "azure", "gcp",
    "linux", "bash", "rest api", "graphql", "jupyter", "colab",
    "machine learning", "deep learning", "nlp", "computer vision",
    "data analysis", "data visualization", "neural network", "cnn", "rnn",
    "arduino", "iot", "embedded systems", "raspberry pi",
    "agile", "scrum", "jira", "postman", "figma",
}


def extract_text_from_file(filepath: str) -> str:
    """Read plain text or .txt resume files."""
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
    return path.read_text(encoding="utf-8", errors="ignore")


def extract_skills(text: str) -> set:
    """Extract skills from text using keyword matching + spaCy tokens."""
    text_lower = text.lower()
    found = set()

    # Direct keyword match
    for skill in SKILLS_BANK:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text_lower):
            found.add(skill)

    # spaCy noun chunks as potential skills
    doc = nlp(text_lower)
    for chunk in doc.noun_chunks:
        chunk_text = chunk.text.strip()
        if chunk_text in SKILLS_BANK:
            found.add(chunk_text)

    return found


def extract_email(text: str) -> str:
    match = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    return match.group(0) if match else "Not found"


def extract_phone(text: str) -> str:
    match = re.search(r"(\+?\d[\d\s\-().]{8,14}\d)", text)
    return match.group(0).strip() if match else "Not found"


def match_score(resume_skills: set, jd_skills: set) -> float:
    if not jd_skills:
        return 0.0
    return round(len(resume_skills & jd_skills) / len(jd_skills) * 100, 2)


def analyze(resume_path: str, jd_text: str):
    """
    Analyze a resume against a job description.

    Args:
        resume_path : path to resume .txt file
        jd_text     : job description as a string
    """
    print("\n" + "="*60)
    print("         RESUME ANALYZER — Powered by spaCy NLP")
    print("="*60)

    resume_text  = extract_text_from_file(resume_path)
    resume_skills = extract_skills(resume_text)
    jd_skills     = extract_skills(jd_text)

    matched  = resume_skills & jd_skills
    missing  = jd_skills - resume_skills
    score    = match_score(resume_skills, jd_skills)

    print(f"\n📧 Email   : {extract_email(resume_text)}")
    print(f"📞 Phone   : {extract_phone(resume_text)}")
    print(f"\n✅ Skills in Resume  : {len(resume_skills)}")
    print(f"📋 Skills in JD      : {len(jd_skills)}")
    print(f"🎯 Matched Skills    : {len(matched)}")
    print(f"❌ Missing Skills    : {len(missing)}")
    print(f"\n📊 Match Score       : {score}%")

    if score >= 75:
        print("🟢 Strong match! Go ahead and apply.")
    elif score >= 50:
        print("🟡 Moderate match. Consider upskilling in missing areas.")
    else:
        print("🔴 Low match. Resume needs significant improvement for this JD.")

    if matched:
        print(f"\n✅ Matched Skills:\n   {', '.join(sorted(matched))}")
    if missing:
        print(f"\n❌ Missing Skills (add these to improve your resume):\n   {', '.join(sorted(missing))}")

    print("\n" + "="*60)
    return {
        "score": score,
        "matched": sorted(matched),
        "missing": sorted(missing),
        "resume_skills": sorted(resume_skills),
    }


# ─── Entry Point ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Example usage — replace with your own resume and JD
    SAMPLE_JD = """
    We are looking for a Python developer with experience in machine learning,
    deep learning, TensorFlow, OpenCV, and SQL. Knowledge of Git, Docker,
    and REST APIs is a plus. Experience with data analysis using pandas and numpy
    is required. Good understanding of NLP and computer vision preferred.
    """

    resume_file = "sample_resume.txt"

    # Create a sample resume text file for demo
    sample_resume = """
    Priya A | priyaanandan682@gmail.com | +91 76959 52974
    Skills: Python, TensorFlow, OpenCV, CNN, Deep Learning, Git, GitHub,
    MySQL, SQLite, NumPy, Pandas, React, HTML, CSS, Arduino, IoT
    """
    Path(resume_file).write_text(sample_resume)

    result = analyze(resume_file, SAMPLE_JD)
