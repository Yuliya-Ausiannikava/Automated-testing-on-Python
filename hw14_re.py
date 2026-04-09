"""
Programs that work using regular expressions.
"""

import re

# Finds all dates in the text in the format "dd.mm.yyyy"
with open('hw14_text.txt', 'r', encoding='utf-8') as file:
    for line in file:
        dt = re.findall(r'\d{2}.\d{2}.\d{4}', line)
        dt_str = ', '.join(dt)
        print(dt_str)
print('______________________________________')

# Checks the correctness of passwords
password = input('Enter your password: ')

if len(password) < 8:
    print('Password is too short')
if not re.search(r'[a-z]', password):
    print('Password must contain at least one lowercase letter')
if not re.search(r'[A-Z]', password):
    print('Password must contain at least one uppercase letter')
if not re.search(r'[0-9]', password):
    print('Password must contain at least one number')
if re.search(r'\s', password):
    print('Password cannot contain spaces')
if re.search(r'[^a-zA-Z0-9]', password):
    print('Password can only contain letters and numbers')
else:
    print('Password is valid')
print('______________________________________')

# Corrects repetitions of words in the text
MESSAGE = ('Довольно распространённая ошибка ошибка — это лишний повтор повтор слова слова. '
           'Смешно, не не правда ли? Не нужно портить хор хоровод.')
PATTERN = r'\b(\w+)\s+\1\b'
corrected_message = re.sub(PATTERN, r'\1', MESSAGE, flags=re.IGNORECASE)
print(corrected_message)
