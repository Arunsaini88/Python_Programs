
student_marks = {
    "Harry" : 81,
    "Ram":78,
    "Hermione":99,
    "Draco":74,
    "Neville":62,

}

student_grades = {}

for student in student_marks:
    score = student_marks[student]
    if score > 90:
        student_grades[student] = 'Outstanding'
    elif score > 80:
        student_grades[student]  = 'Exceed Expectations'
    elif score > 70:
        student_grades[student] = 'Accepting'
    else:
        student_grades[student] = 'Fail'

print(student_grades)