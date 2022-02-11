"""
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string.
String traversal will take place from left to right, not from right to left.

Sample Input : ABCDCDC
               CDC
Sample Output : 2
"""

# Solution 
def count_substring(string, sub_string):
    l1 = len(string)
    l2 = len(sub_string)

    count = 0
    for i in range(0,l1 - l2 + 1):
        if sub_string == string[i:i + l2]:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
