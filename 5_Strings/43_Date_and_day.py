'''
Given the date, month and year. Find what weekday it was. 

Input:
Date = 17
Month = 03 
Year = 2017
Output:
FRIDAY
'''

import datetime

def find_day(date, month, year):
    dt = datetime.date(year, month, date)
    return dt.strftime("%A").upper()

print(find_day(17, 3, 2017))  # Output: FRIDAY
