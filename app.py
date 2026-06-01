import job_roles
import learning_paths
from gtts import gTTS
import os
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename

import resume_parser
import skill_extractor
import gap_analyzer
import visualizer
import db_handler

app = Flask(__name__)
app.secret_key = "ai_resume_scanner_secret"

UPLOAD_FOLDER = os.path.join(app.root_path, 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = {'pdf', 'docx'}

db_handler.init_db()

JD_SKILLS = [
    "Python", "Flask", "SQL", "PostgreSQL", "Machine Learning", 
    "Deep Learning", "NLP", "TensorFlow", "PyTorch", "Scikit-Learn", 
    "Pandas", "NumPy", "Docker", "Kubernetes", "AWS", "Git", 
    "REST API", "CI/CD", "Communication", "Problem Solving", 
    "React", "TypeScript"
]

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', jd_skills=JD_SKILLS)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'resume' not in request.files:
        return "No resume file part in submission", 400
    file = request.files['resume']
    if file.filename == '':
        return "No file selected", 400
    if file and allowed_file(file.filename):
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        resume_text = resume_parser.extract_text(file_path)
        resume_skills = skill_extractor.extract_skills(resume_text)
        analysis = gap_analyzer.find_skill_gap(resume_skills, JD_SKILLS)
        db_handler.save_scan(filename, analysis)
        chart_path = visualizer.create_bar_chart(analysis['missing'])
        chart_url = '/' + chart_path if not chart_path.startswith('/') else chart_path
        weekly_plan = learning_paths.get_weekly_plan(analysis['missing'])
        tts_text = f"Your resume matches {analysis['match_percent']} percent. "
        tts_text += f"You matched {len(analysis['matched'])} skills. "
        tts_text += f"You are missing {len(analysis['missing'])} skills including "
        tts_text += ", ".join(analysis['missing'][:5])
        tts = gTTS(text=tts_text, lang='en')
        tts_path = os.path.join('static', 'result_audio.mp3')
        tts.save(tts_path)
        match = analysis['match_percent']
        if match >= 90:
            grade = "A+"
            grade_msg = "Excellent! 🏆"
            grade_color = "#00c853"
        elif match >= 70:
            grade = "A"
            grade_msg = "Very Good! 👍"
            grade_color = "#64dd17"
        elif match >= 50:
            grade = "B"
            grade_msg = "Good! Keep Learning! 📚"
            grade_color = "#ffd600"
        elif match >= 30:
            grade = "C"
            grade_msg = "Average! Work Hard! ⚠️"
            grade_color = "#ff6d00"
        else:
            grade = "D"
            grade_msg = "Needs Improvement! 💪"
            grade_color = "#dd2c00"
        role_suggestions = job_roles.suggest_roles(resume_skills)
        return render_template(
            'result.html',
            filename=filename,
            matched=analysis['matched'],
            missing=analysis['missing'],
            match_percent=analysis['match_percent'],
            chart_url=chart_url,
            weekly_plan=weekly_plan,
            audio_url='/static/result_audio.mp3',
            grade=grade,
            grade_msg=grade_msg,
            grade_color=grade_color,
            role_suggestions=role_suggestions
        )
    return "Unsupported file type. Only PDF and DOCX files are allowed.", 400

@app.route('/dashboard', methods=['GET'])
def dashboard():
    scans = db_handler.get_all_scans()
    scan_list = []
    for row in scans:
        scan_list.append({
            "id": row[0],
            "filename": row[1],
            "matched_skills": row[2] if row[2] else "None",
            "missing_skills": row[3] if row[3] else "",
            "match_percent": row[4] if row[4] else 0.0,
            "scan_date": row[5] if row[5] else ""
        })
    all_missing = []
    for scan in scan_list:
        if scan["missing_skills"]:
            skills = [s.strip() for s in scan["missing_skills"].split(',') if s.strip()]
            all_missing.extend(skills)
    chart_path = visualizer.create_bar_chart(all_missing)
    chart_url = '/' + chart_path if not chart_path.startswith('/') else chart_path
    return render_template('dashboard.html',
                         history=scan_list,
                         chart_url=chart_url)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)