"""
This code solves the second task from homework #7 "Time"
"""

n = int(input("Write how many minutes the motorcycle timer shows:"))
hour = (n//60)%24
minutes = n%60

if hour < 10 and minutes < 10:
    s = f'0{hour}:0{minutes}'
    print(s)
    total = int(s[0]) + int(s[1]) + int(s[3]) + int(s[4])
    print(total)
elif hour >= 10 and minutes < 10:
    s = f'{hour}:0{minutes}'
    print(s)
    total = int(s[0]) + int(s[1]) + int(s[3]) + int(s[4])
    print(total)
elif hour < 10 and minutes >= 10:
    s = f'0{hour}:{minutes}'
    print(s)
    total = int(s[0]) + int(s[1]) + int(s[3]) + int(s[4])
    print(total)
elif hour >= 10 and minutes >= 10:
    s = f'{hour}:{minutes}'
    print(s)
    total = int(s[0]) + int(s[1]) + int(s[3]) + int(s[4])
    print(total)


