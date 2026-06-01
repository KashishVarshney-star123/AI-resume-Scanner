import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("resumes.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS scans (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT NOT NULL,
        matched_skills TEXT,
        missing_skills TEXT,
        match_percent REAL,
        scan_date TEXT
    )''')
    conn.commit()
    conn.close()

def save_scan(filename, result):
    conn = sqlite3.connect("resumes.db")
    c = conn.cursor()
    
    matched = ", ".join(result["matched"]) if result["matched"] else ""
    missing = ", ".join(result["missing"]) if result["missing"] else ""
    
    print(f"Saving scan: {filename}")  # Debug
    
    c.execute('''INSERT INTO scans 
                 (filename, matched_skills, missing_skills, match_percent, scan_date)
                 VALUES (?,?,?,?,?)''',
              (str(filename),
               matched,
               missing,
               result["match_percent"],
               datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

def get_all_scans():
    conn = sqlite3.connect("resumes.db")
    c = conn.cursor()
    c.execute("SELECT * FROM scans ORDER BY scan_date DESC")
    rows = c.fetchall()
    conn.close()
    return rows

def get_missing_skills_frequency():
    conn = sqlite3.connect("resumes.db")
    c = conn.cursor()
    c.execute("SELECT missing_skills FROM scans WHERE missing_skills != ''")
    rows = c.fetchall()
    conn.close()
    
    skill_count = {}
    for row in rows:
        if row[0]:
            skills = [s.strip() for s in row[0].split(",")]
            for skill in skills:
                if skill:
                    skill_count[skill] = skill_count.get(skill, 0) + 1
    
    sorted_skills = sorted(skill_count.items(), 
                          key=lambda x: x[1], reverse=True)[:5]
    return sorted_skills