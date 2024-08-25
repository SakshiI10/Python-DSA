'''
Given a string S, write a program to count the occurrence of Lowercase characters, Uppercase characters, Special characters and Numeric values in the string.

Input:
S = "#GeeKs01fOr@gEEks07"
Output:
5
8
4
2 '''

class Solution:
    def countCharacters(self, S):
        upper_count = 0
        lower_count = 0
        special_count = 0
        digit_count = 0
        
        for char in S:
            if char.islower():
                lower_count += 1
            elif char.isupper():
                upper_count += 1
            elif char.isdigit():
                digit_count += 1
            else:
                special_count += 1
        
        return lower_count, upper_count, special_count, digit_count

sol = Solution()
S = "#GeeKs01fOr@gEEks07"
lower, upper, special, digits = sol.countCharacters(S)

print(upper)   # Output: 8
print(lower)   # Output: 5
print(special) # Output: 4
print(digits)  # Output: 2
