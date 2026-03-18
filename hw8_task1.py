"""
This code solves the second task from homework #7 "Bulls and cows"
"""

import random

while True:
    number = str(random.randint(1000, 9999))
    if len(set(number)) == 4:
        break

while True:
    guess = str(input('The number has been chosen. Try to guess it: '))
    if len(guess) != 4:
        print('Please enter a 4 digit number:')
        continue

    bulls = 0
    cows = 0
    for char in range(4):
        if guess[char] == number[char]:
            bulls += 1

    for char in range(4):
        if guess[char] in number and guess[char] != number[char]:
            cows += 1

    print(f'Bulles: {bulls},cows: {cows}')

    if bulls == 4:
        print('You win!')
        break
