"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:
- Www.HackerRank.com → wWW.hACKERrANK.COM
- Pythonist 2 → pYTHONIST 2

Sample Input 0 :
HackerRank.com presents "Pythonist 2".

Sample Output 0 :
hACKERrANK.COM PRESENTS "pYTHONIST 2".
"""

# Solution
def swap_case(s):
    ns = ""
    for i in s:
        if ord(i) > 64 and ord(i) < 91:
            ns = ns + chr(ord(i) + 32)
        elif ord(i) > 96 and ord(i) < 123:
            ns = ns + chr(ord(i) - 32)
        else:
            ns = ns + i
    return ns

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
