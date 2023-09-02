# Chose max value in list
student_score = input('Enter the list of  student heights\n').split()
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)

higher_score = 0
for score in student_score:
    if score > higher_score:
        higher_score = score
print(f'The higher score is {higher_score}')

lowest_score = score
for lscore in student_score:
    if lscore < lowest_score:
        lowest_score = lscore
print(f"The lowest score is {lowest_score}") 
