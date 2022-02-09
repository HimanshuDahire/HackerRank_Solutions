"""
Consider a list (list = []). You can perform the following commands:

--> insert i e: Insert integer r at position i.
--> print: Print the list.
--> remove e: Delete the first occurrence of integer e.
--> append e: Insert integer e at the end of the list.
--> sort: Sort the list.
--> pop: Pop the last element from the list.
--> reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above.
Iterate through each command in order and perform the corresponding operation on your list.
"""

# SOLUTION

if __name__ == '__main__':
    N = int(input())
ls = []    
for i in range(N):
    command = input().split()
    if command[0] == "insert":
        ls.insert(int(command[1]), int(command[2]))
    if command[0] == "print":
        print(ls)
    if command[0] == "remove":
        ls.remove(int(command[1]))
    if command[0] == "append":
        ls.append(int(command[1]))
    if command[0] == "sort":
        ls.sort()
    if command[0] == "pop":
        ls.pop()
    if command[0] == "reverse":
        ls.reverse()
