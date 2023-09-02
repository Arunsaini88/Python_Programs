numbers = [1,1,2,3,4,8,13,21,34,55]
# square = [num**2 for num in numbers]
# print(square)
result = [num for num in numbers if num%2==0]
print(result)