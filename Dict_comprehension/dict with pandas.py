student_dict =  {
    "student":["Angla","James","Lily"],
    "score":[56,76,98]
}
import pandas

student_data_fram = pandas.DataFrame(student_dict)
# print(student_data_fram)
for (index,row) in student_data_fram.iterrows():
    # print(index)
    # print(row)
    if row.student == "Angla":
        print(row.score)