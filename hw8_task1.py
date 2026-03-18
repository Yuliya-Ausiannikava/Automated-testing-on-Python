"""
This code solves the second task from homework #7 "Bulls and cows"
"""

import random

while True:
    NUMB = str(random.randint(1000, 9999))
    if (NUMB[0] != NUMB[1] and NUMB[0] != NUMB[2] and NUMB[0] != NUMB[3]
        and NUMB[1] != NUMB[2] and NUMB[1] != NUMB[3] and NUMB[2] != NUMB[3]):
        break
while True:
    guess_numb = str(input('The number has been chosen. Try to guess it: '))
    if len(guess_numb) != 4:
        print('Please enter a 4 digit number:')
        continue

    bulls = 0
    cows = 0
    for char in range(4):
        if guess_numb[char] == NUMB[char]:
            bulls += 1

    for char in range(4):
        if guess_numb[char] in NUMB and guess_numb[char] != NUMB[char]:
            cows += 1

    print(f'Bulles: {bulls},cows: {cows}')

    if bulls == 4:
        print('You win!')
        break
