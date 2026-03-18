"""
This code solves the second task from homework #7 "Bulls and cows"
"""

import random

while True:
    NUMBER = str(random.randint(1000, 9999))
    if len(set(NUMBER)) == 4:
        break

while True:
    GUESS = str(input('The number has been chosen. Try to guess it: '))
    if len(GUESS) != 4:
        print('Please enter a 4 digit number:')
        continue

    BULLS = 0
    COWS = 0
    for char in range(4):
        if GUESS[char] == NUMBER[char]:
            BULLS += 1

    for char in range(4):
        if GUESS[char] in NUMBER and GUESS[char] != NUMBER[char]:
            COWS += 1

    print(f'Bulles: {BULLS},cows: {COWS}')

    if BULLS == 4:
        print('You win!')
        break
