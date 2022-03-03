"""
You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
For example, alison heck should be capitalised correctly as Alison Heck.

Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Sample Input : chris alan
Sample Output : Chris Alan
"""

# SOLUTION:
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    import string
    small = string.ascii_lowercase
    capital = string.ascii_uppercase
    num = string.digits

    y=re.findall('.\S*',s)

    for i in range(len(y)):
        st = ''
        count = 0
        for j in y[i]:
            if ((j in small) or (j in capital) or (j in num)) and count == 0:
                st = st + j.capitalize()
                count += 1
            else:
                st = st + j
        y[i] = st

    z = "".join(y)
    return z
  
# solution 2
def solve(s):
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return s
