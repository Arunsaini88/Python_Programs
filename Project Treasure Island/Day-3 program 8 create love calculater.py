print('welcome to love calculator!')
name1 = input('What is your name?\n')
name2 = input('What is their name?\n')
c_string = (name1 + name2).lower()

t = c_string.count('t')
r = c_string.count('r')
u = c_string.count('u')
e = c_string.count('e')
true = t + r + u + e

l = c_string.count('l')
o = c_string.count('o')
v = c_string.count('v')
e = c_string.count('e')

love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f'your score is {love_score}, you go together like coke and mentos.')

elif (love_score >= 40) or (love_score <= 50):
    print(f'your score is {love_score}, you are alright together.')

else:
    print(f'your score is {love_score}.')