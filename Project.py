# personalized_course_recommender.py

# A basic personalized course recommender using content-based filtering

# Sample student data
students = {
    "student1": {
        "interests": ["AI", "ML", "Python"],
        "grades": {"AI": 85, "Python": 90, "DBMS": 70}
    },
    "student2": {
        "interests": ["Web Development", "CSS", "JavaScript"],
        "grades": {"HTML": 88, "CSS": 82, "DSA": 60}
    }
}

# Sample course catalog
courses = [
    {"name": "Advanced Python", "tags": ["Python", "OOP", "Development"]},
    {"name": "Intro to Machine Learning", "tags": ["ML", "AI", "Data"]},
    {"name": "Full Stack Web Dev", "tags": ["HTML", "CSS", "JavaScript"]},
    {"name": "Database Systems", "tags": ["SQL", "DBMS", "Data"]},
    {"name": "Data Structures", "tags": ["DSA", "Algorithms", "Logic"]}
]

def recommend_courses(student_id):
    student = students.get(student_id)
    if not student:
        return "Student not found."

    interest_set = set(student["interests"])
    recommended = []

    for course in courses:
        match_score = len(interest_set.intersection(course["tags"]))
        if match_score > 0:
            recommended.append((course["name"], match_score))

    # Sort by match score (higher is better)
    recommended.sort(key=lambda x: x[1], reverse=True)

    return [course for course, score in recommended]

# Example usage
student_id = "student1"
print(f"Recommended courses for {student_id}:")
for course in recommend_courses(student_id):
    print("-", course)
