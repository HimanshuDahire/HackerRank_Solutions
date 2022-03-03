"""
Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string S.

For Example:
String S = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

"""

# SOLUTION
def minion_game(string):
    # your code goes here
    length = len(string)
    vowels = "AEIOU"
    stuart_count = 0       
    kevin_count = 0
    for j in range(length):
        if s[j] in vowels:
            kevin_count += length - j
        else:
            stuart_count += length - j
        
    if stuart_count > kevin_count:
        return print("Stuart " + str(stuart_count))
    elif stuart_count == kevin_count:
        return print("Draw")
    else:
        return print("Kevin " + str(kevin_count))
