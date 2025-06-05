'''
Given a string consisting of lowercase english alphabets. Find the repeated character present first in the string.

Input: S = "geeksforgeeks"
Output: g'''

# Returns character
# class Solution:
#     def firstRep(self, s):
#         count_dict = {} 
        
#         for char in s:
#             if char in count_dict:
#                 count_dict[char] += 1
#             else:
#                 count_dict[char] = 1
        
#         for char in s:
#             if count_dict[char] > 1:
#                 return char
        
#         return '#'

# Returns index
class Solution:
    def repeatingCharacter(self,s):
        freq = {} 
        
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        index = 0
        for char in s:
            if freq[char] > 1:
                return index 
            index += 1

        return -1

sol = Solution()
print(sol.firstRep("geeksforgeeks"))  # Output: g
print(sol.firstRep("abcde"))          # Output: #
