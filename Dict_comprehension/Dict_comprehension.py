student_dis = {
    "Alex": 51,
    "Beth": 72,
    "Caroline": 62,
    "Dave": 81,
    "Eleanor": 38,
    "Freddie": 89
}

passed_student = {student: mark for (student, mark) in student_dis.items() if mark >= 60}
print(passed_student)