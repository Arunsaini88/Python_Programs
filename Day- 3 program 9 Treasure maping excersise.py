row1 = ["0", "0", "0"]
row2 = ["0", "0", "0"]
row3 = ["0", "0", "0"]

mape = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
#  row = 1,2,3 and column = 1,2,3 give the input combination of row and column.
# Eg:32 or 23 etc.
position = input("Where do you want to put the treasure?\n")
# write the row code

horizontal = int(position[0])
vertical = int(position[1])

mape[vertical - 1][horizontal - 1] = "❌"

print(f"{row1}\n{row2}\n{row3}")
