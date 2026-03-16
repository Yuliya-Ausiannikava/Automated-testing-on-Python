"""
This code solves the second task from homework #7 "Bulls and cows"
"""

import random

while True:
    numb = str(random.randint(1000, 9999))
    if numb[0] != numb[1] and numb[0] != numb[2] and numb[0] != numb[3] and numb[1] != numb[2] and numb[1] != numb[3] and numb[2] != numb[3]:
        break
while True:
    i = str(input('The number has been chosen. Try to guess it: '))
    if len(i) != 4:
        print('Please enter a 4 digit number:')
        continue
    bulls = 0
    cows = 0
    if numb[0] == i[0]:
        bulls += 1
    if numb[1] == i[1]:
        bulls += 1
    if numb[2] == i[2]:
        bulls += 1
    if numb[3] == i[3]:
        bulls += 1
    if i[0] == numb[1] or i[0] == numb[2] or i[0] == numb[3]:
        cows += 1
    if i[1] == numb[0] or i[1] == numb[2] or i[1] == numb[3]:
        cows += 1
    if i[2] == numb[0] or i[2] == numb[1] or i[2] == numb[3]:
        cows += 1
    if i[3] == numb[0] or i[3] == numb[1] or i[3] == numb[2]:
        cows += 1
    print(f'Bulles:{bulls},cows:{cows}')

    if bulls == 4:
        print('You win!')
    else:
        print('Try again:')
        break
