# Task: 
"""
Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

Sample Input 0 : 1990

Sample Output 0 : False

Explanation 0 : 1990 is not a multiple of 4 hence it's not a leap year.
"""

Solution : 
def is_leap(year):
    leap = False
    
    # Write your logic here
    if  year % 100 == 0:
        if year % 400 == 0:
            leap = True
    elif year % 4 == 0:
        leap = True
    return leap

year = int(input())
print(is_leap(year))
