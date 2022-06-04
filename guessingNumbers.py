import random

introString=input('Guess a number between 1-9:')
print(introString)
number=random(1, 9)
chance=5

if (chance == number):
    print('Congratulations YOU WON!!!')
        break

if not (chance < 5):
    print('YOU LOSE!!! The number is', number)


print('Correct Number:')
print(number)

print('Chances you have:')
print(chance)