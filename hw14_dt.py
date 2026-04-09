"""
Programs using the module datetime
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta

# Counts the number of days between dates
date_1 = input('Enter the first date in the format YYYY-MM-DD: ')
date_2 = input('Enter the second date in the format YYYY-MM-DD: ')
format_date_1 = datetime.strptime(date_1, "%Y-%m-%d").date()
format_date_2 = datetime.strptime(date_2, "%Y-%m-%d").date()
result = relativedelta(format_date_2, format_date_1)
print(result)
print('___________________________________________________________')

# Checks whether a date is past or future
date = input("Enter a date in the format YYYY-MM-DD: ")
format_date = datetime.strptime(date, "%Y-%m-%d").date()
today = datetime.today().date()
if today > format_date:
    print("The date entered is in the past")
elif today < format_date:
    print("The date entered is in the future")
elif today == format_date:
    print("The date entered is today")
