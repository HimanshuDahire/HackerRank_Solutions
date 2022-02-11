"""
Task : You are given a string 'S'.
Your task is to find out if the string 'S' contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Output Format : 
--> In the first line, print True if 'S' has any alphanumeric characters. Otherwise, print False.
--> In the second line, print True if 'S' has any alphabetical characters. Otherwise, print False.
--> In the third line, print True if 'S' has any digits. Otherwise, print False.
--> In the fourth line, print True if 'S' has any lowercase characters. Otherwise, print False.
--> In the fifth line, print True if 'S' has any uppercase characters. Otherwise, print False.

Sample Input : qA2
Sample Output : 
True
True
True
True
True
"""

# Solution

if __name__ == '__main__':
    s = input()
    
a = b = c = d = e = False

for i in s:
    if a == False:
        a = i.isalnum()
    if b == False:
        b = i.isalpha()
    if c == False:
        c = i.isdigit()
    if d == False:
        d = i.islower()
    if e == False:
        e = i.isupper()

print(a)
print(b)
print(c)
print(d)
print(e)
