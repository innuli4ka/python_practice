# Create the students dictionary
students = {
    "Alice": {"grade": 85, "age": 20},
    "Bob": {"grade": 90, "age": 21},
    "David": {"grade": 78, "age": 19}
}

# Add a new student
students["David"] = {"grade": 88, "age": 22}

# Update the grade of an existing student
students["Alice"]["grade"] = 92

# Remove a student
del students["Charlie"]

# Calculate and print the average grade
total_grades = 0
for student in students:
    total_grades += students[student]["grade"]

average_grade = total_grades / len(students)
print("Average grade:", average_grade)

# Find and print the student with the highest grade
highest_grade = -1
top_student = ""

for name in students:
    if students[name]["grade"] > highest_grade:
        highest_grade = students[name]["grade"]
        top_student = name

print("Top student:", top_student)
