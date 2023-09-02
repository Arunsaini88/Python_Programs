while True:
    print()
    N = int(input("Which program wiil you run at a time 4 or 5: "))
    print()
    print('Chose an optint , for run this program "y",OR Exit this program "exit"')
    option = input("Put your option\n")
    if option == 'y':
        if N == 4:

            height = float(input('enter your hight in m: '))
            weight = int(input('enter your weight in kg: '))
            BMI = int(weight / height ** 2)
            if BMI < 18.5:
                print(f"your BMI is {BMI}, you are underweight.")
            elif BMI <= 25:
                print(f"your BMI is {BMI}, you are normal weight.")
            elif BMI <= 30:
                print(f"Your BMI is {BMI}, you are overweight.")
            elif BMI <= 35:
                print(f"Your BMi is {BMI}, you are obese.")
            else:
                print(f"Your BMI is {BMI}, you are cliniclly obese.")




        # program 5 calculate remaning age
        else:

            age = int(input('What is your current age: '))

            years_remaning = 90 - age
            days_remaning = years_remaning * 365
            weeks_remaning = years_remaning * 52
            month_remaning = years_remaning * 12

            print(
                f'your  have {days_remaning} daye, {weeks_remaning} weeks,  {month_remaning} months, and  {years_remaning} years')
    else:
        break
