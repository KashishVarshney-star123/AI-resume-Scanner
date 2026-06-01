LEARNING_PATHS = {
    "python": {
        "course": "Python for Everybody - Coursera",
        "link": "https://www.coursera.org/specializations/python",
        "time": "4 weeks"
    },
    "flask": {
        "course": "Flask Web Development - YouTube",
        "link": "https://www.youtube.com/watch?v=Z1RJmh_OqeA",
        "time": "1 week"
    },
    "sql": {
        "course": "SQL for Beginners - W3Schools",
        "link": "https://www.w3schools.com/sql/",
        "time": "2 weeks"
    },
    "postgresql": {
        "course": "PostgreSQL Tutorial",
        "link": "https://www.postgresqltutorial.com/",
        "time": "2 weeks"
    },
    "machine learning": {
        "course": "ML Crash Course - Google",
        "link": "https://developers.google.com/machine-learning/crash-course",
        "time": "6 weeks"
    },
    "deep learning": {
        "course": "Deep Learning Specialization - Coursera",
        "link": "https://www.coursera.org/specializations/deep-learning",
        "time": "8 weeks"
    },
    "nlp": {
        "course": "NLP with Python - Udemy",
        "link": "https://www.udemy.com/course/nlp-natural-language-processing-with-python/",
        "time": "5 weeks"
    },
    "tensorflow": {
        "course": "TensorFlow Developer - Coursera",
        "link": "https://www.coursera.org/professional-certificates/tensorflow-in-practice",
        "time": "6 weeks"
    },
    "pytorch": {
        "course": "PyTorch Tutorials - Official",
        "link": "https://pytorch.org/tutorials/",
        "time": "4 weeks"
    },
    "docker": {
        "course": "Docker for Beginners - YouTube",
        "link": "https://www.youtube.com/watch?v=fqMOX6JJhGo",
        "time": "2 weeks"
    },
    "aws": {
        "course": "AWS Cloud Practitioner - AWS",
        "link": "https://aws.amazon.com/training/",
        "time": "4 weeks"
    },
    "git": {
        "course": "Git & GitHub - YouTube",
        "link": "https://www.youtube.com/watch?v=RGOj5yH7evk",
        "time": "1 week"
    },
    "react": {
        "course": "React JS - Full Course",
        "link": "https://www.youtube.com/watch?v=bMknfKXIFA8",
        "time": "4 weeks"
    },
    "typescript": {
        "course": "TypeScript Tutorial - W3Schools",
        "link": "https://www.w3schools.com/typescript/",
        "time": "2 weeks"
    },
    "kubernetes": {
        "course": "Kubernetes for Beginners",
        "link": "https://www.youtube.com/watch?v=X48VuDVv0do",
        "time": "3 weeks"
    },
    "pandas": {
        "course": "Pandas Tutorial - Kaggle",
        "link": "https://www.kaggle.com/learn/pandas",
        "time": "1 week"
    },
    "numpy": {
        "course": "NumPy Tutorial - W3Schools",
        "link": "https://www.w3schools.com/python/numpy/",
        "time": "1 week"
    },
    "scikit-learn": {
        "course": "Scikit-Learn Tutorial - Official",
        "link": "https://scikit-learn.org/stable/tutorial/",
        "time": "3 weeks"
    },
    "rest api": {
        "course": "REST API Tutorial",
        "link": "https://restfulapi.net/",
        "time": "2 weeks"
    },
    "ci/cd": {
        "course": "CI/CD Pipeline - YouTube",
        "link": "https://www.youtube.com/watch?v=R8_veQiYBjI",
        "time": "2 weeks"
    },
    "communication": {
        "course": "Business Communication - Coursera",
        "link": "https://www.coursera.org/learn/wharton-communication-skills",
        "time": "3 weeks"
    },
    "problem solving": {
        "course": "Problem Solving - HackerRank",
        "link": "https://www.hackerrank.com/domains/algorithms",
        "time": "Ongoing"
    }
}

def get_learning_path(skill):
    skill_lower = skill.lower()
    if skill_lower in LEARNING_PATHS:
        return LEARNING_PATHS[skill_lower]
    return {
        "course": f"Search '{skill}' on Coursera/YouTube",
        "link": f"https://www.coursera.org/search?query={skill}",
        "time": "2-4 weeks"
    }

def get_weekly_plan(missing_skills):
    plan = []
    week = 1
    for skill in missing_skills[:8]:  # Top 8 skills
        path = get_learning_path(skill)
        plan.append({
            "week": week,
            "skill": skill,
            "course": path["course"],
            "link": path["link"],
            "time": path["time"]
        })
        week += 1
    return plan