"""
This code solves the second task from homework #7 "Level Up"
"""

XP = input('Write the number of experience points before killing the monster?:')
XP = float(XP)
reward = input('How much experience did you get as a reward for killing a monster?:')
reward = float(reward)
threshold = 15
sum = XP + reward
if sum >= threshold:
    print(True)
if sum < threshold:
    print(False)

