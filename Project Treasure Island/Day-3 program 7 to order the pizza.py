print('Welcome to Python Pizza Deliveries!')
size = (input('What size pizza do you wnat? S,L.or M\n')).upper()
add_pepproni = (input('Do you want papperoni? Y,N\n')).upper()

extra_cheese = (input('Do you want extra cheese? Y ,N\n')).upper()
bill = 0
if size == 'S':
    bill += 15
    print('Small pizza prise=$15')
elif size == 'M':
    bill += 20
    print('Mediam pizza prise=$20')
else:
    bill += 25
    print('larg pizza prise=$25')
if add_pepproni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3
if extra_cheese == 'Y':
    bill += 1
print(f'Your final bill is: ${bill}')