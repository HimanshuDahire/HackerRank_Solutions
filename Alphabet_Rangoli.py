"""
You are given an integer, N. Your task is to print an alphabet rangoli of size N.

size 3
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

size 5
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

"""

# SOLUTION :
def print_rangoli(size):
    import string
    letters = string.ascii_lowercase

    ls = []
    for i in range(size):
        s = "-".join(letters[i:size])
        ls.append((s[::-1]+s[1:]).center(4*size-3, "-"))
    return print('\n'.join(ls[:0:-1]+L))
