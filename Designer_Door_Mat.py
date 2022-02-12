"""
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
  - Mat size must be 'N' X 'M'. (N) is an odd natural number, and M is 3 times N.)
  - The design should have 'WELCOME' written in the center.
  - The design pattern should only use |, . and - characters.
  
  
Sample Input : 9 27
Sample Output :

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------

"""

# solution :

# printing dash and pattern for upper trangle
i = 1
while i <= n//2:
    for j in range((m - (3 * (2 * i -1)))//2):
        print(dash, end="")
    for k in range(i * 2 -1):
        print(pattern,end="")
    for l in range((m - (3 * (2 * i -1)))//2):
        print(dash,end="")         
    print()
    i += 1

# Printing welcome
for ii in range((m - 7)//2):
    print(dash,end="")
print("WELCOME",end="")
for jj in range((m - 7)//2):
    print(dash,end="")
print()
# printing dash and pattern for lower trangle
while i < n:
    for r in range((m - (6 * (n - i) - 3))//2):
        print(dash,end="")
    for s in range(2 * (n - i) - 1):
        print(pattern,end="")
    for r in range((m - (6 * (n - i) - 3))//2):
        print(dash,end="")
    print()
    i += 1
