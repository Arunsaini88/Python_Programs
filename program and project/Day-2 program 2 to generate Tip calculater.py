print('Welcome to the tip calculater!')
bill = float(input("What was the totla bill? $"))
Tip = int(input("What persentage tip would you like to give?10,12,or 15? :"))
Pepole = int(input('How many people to split he bill? '))

Pay_bill = Tip / 100 * bill + bill
Each_people_pay = Pay_bill/Pepole

final_bill = '{: .2f}'.format(Each_people_pay)

print(f'Each person should pay: {final_bill}')