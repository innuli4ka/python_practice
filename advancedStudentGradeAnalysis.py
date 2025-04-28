# 1. Create a list of student dictionaries
students = [
    {"name": "Daniel", "grades": [80, 90, 85]},
    {"name": "Jenya", "grades": [40, 50]},
    {"name": "Noya", "grades": [100, 95, 98]},
    {"name": "Mika", "grades": []}  # Mika has no grades
]

# 2.1 Calculate average grade for each student using map()
def calculate_average(student):
    if len(student["grades"]) == 0:
        return {"name": student["name"], "average": None}
    avg = sum(student["grades"]) / len(student["grades"])
    return {"name": student["name"], "average": avg}

students_with_averages = list(map(lambda student: calculate_average(student), students))

print("\nAverage grades:")
for student in students_with_averages:
    if student["average"] is None:
        print(student["name"], "- No grades available")
    else:
        print(student["name"], "-", f"{student['average']:.2f}")

# 2.2 Find students who passed (average >= 50)
passed_students = list(filter(lambda s: s["average"] is not None and s["average"] >= 50, students_with_averages))

print("\nStudents who passed:")
for student in passed_students:
    print(student["name"], "-", f"{student['average']:.2f}")

# 2.3 Sort students by average grade descending
sorted_students = sorted(
    filter(lambda s: s["average"] is not None, students_with_averages),
    key=lambda s: s["average"],
    reverse=True
)

print("\nStudents sorted by average grade:")
for student in sorted_students:
    print(student["name"], "-", f"{student['average']:.2f}")

# 2.4 Increase each student's grades by 5 points (max 100)
print("\nGrades after adding 5 points (max 100):")
for student in students:
    updated_grades = list(map(lambda g: g+5 if g+5 <= 100 else 100, student["grades"]))
    student["grades"] = updated_grades
    print(student["name"], "-", updated_grades)

# 2.5 Handle students with no grades
# (Already handled earlier by checking if "average" is None)

# 2.6 Summary Report
summary = [(student["name"], student["average"]) for student in students_with_averages if student["average"] is not None]

# Find highest grade in the class
highest_grade = max([grade for student in students for grade in student["grades"]], default=None)

# Find student(s) who achieved the highest grade
top_students = [student["name"] for student in students if highest_grade in student["grades"]]

print("\nSummary Report:")
print("Highest grade in the class:", highest_grade)
print("Student(s) with the highest grade:", ", ".join(top_students))
