# Create the students dictionary
students = {
    "Alice": {
        "age": 20,
        "subjects": ["Math", "English", "Biology"],
        "grades": {85, 90, 78}
    },
    "Bob": {
        "age": 21,
        "subjects": ["History", "Math", "Physics"],
        "grades": {88, 92, 80}
    }
}

# 1. Add a new student
students["Charlie"] = {
    "age": 19,
    "subjects": ["English", "Art"],
    "grades": {75, 83}
}

# 2. Update grades of an existing student
students["Alice"]["grades"].add(95)

# 3. Remove a subject from a student's subjects list
students["Bob"]["subjects"].remove("Math")

# 4. Find the average grade of a specific student
grades_list = list(students["Alice"]["grades"])
average_grade = sum(grades_list) / len(grades_list)
print("Average grade for Alice:", average_grade)

# 5. Find the student with the highest average grade
highest_avg = -1
top_student = ""

for name, info in students.items():
    grades = list(info["grades"])
    avg = sum(grades) / len(grades)
    if avg > highest_avg:
        highest_avg = avg
        top_student = name

print("\nTop student:")
print("Name:", top_student)
print("Age:", students[top_student]["age"])
print("Subjects:", students[top_student]["subjects"])

# 6. Create tuples for each student (name, age, number of subjects)
student_tuples = []

for name, info in students.items():
    student_tuples.append((name, info["age"], len(info["subjects"])))

# Sort by number of subjects
student_tuples.sort(key=lambda x: x[2])

print("\nStudent tuples sorted by number of subjects:")
for t in student_tuples:
    print(t)
