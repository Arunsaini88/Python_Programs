leap_year= int(input("whic year you check : "))
if leap_year%4==0:
    if leap_year%100==0: 
        if leap_year%400==0:
            print("leap year")

        else:
            print('not leap year')
    else:
        print(" leap year")
else:
    print("not leap year")


