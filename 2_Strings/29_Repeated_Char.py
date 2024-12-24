'''
Given a string consisting of lowercase english alphabets. Find the repeated character present first in the string.

Input: S = "geeksforgeeks"
Output: g'''

class Solution:
    def firstRep(self, s):
        count_dict = {}  # Dictionary to keep track of character counts
        
        for char in s:
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1
        
        # Iterate again to find the first character with a count greater than 1
        for char in s:
            if count_dict[char] > 1:
                return char
        
        return '#'  # Return '#' if no repeated characters are found

sol = Solution()
print(sol.firstRep("geeksforgeeks"))  # Output: g
print(sol.firstRep("abcde"))          # Output: #
