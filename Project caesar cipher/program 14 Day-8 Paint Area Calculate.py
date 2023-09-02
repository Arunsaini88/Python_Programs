from math import *

def paint_calc(height,width,cover):
    area = height * width
    num_of_cans = ceil(area / cover)
    print(f"You'll need {num_of_cans} cans of paint")

test_h = int(input("Hight of wall :"))
test_w = int(input('width of wall:'))
coverage = 5
paint_calc(height=test_h,width=test_w,cover=coverage)