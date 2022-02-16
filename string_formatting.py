"""
Given an integer, n , print the following values for each integer i from 1 to n:

1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary

Prints

The four values must be printed on a single line in the order specified above for each i from 1 to number. 
Each value should be space-padded to match the width of the binary value of number and the values should be separated by a single space.
"""

# SOLUTION
def print_formatted(number):
    # your code goes here
    width = len("{0:b}".format(n))
    for i in range(1,n+1):
        print(('{0:d}'.format(i)).rjust(width), end=" ")
        print(('{0:o}'.format(i)).rjust(width), end=" ")
        print(('{0:X}'.format(i)).rjust(width), end=" ")
        print(('{0:b}'.format(i)).rjust(width), end=" ")
        print()

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
