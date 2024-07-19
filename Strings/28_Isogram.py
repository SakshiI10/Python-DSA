'''
Given a string S of lowercase alphabets, check if it is isogram or not. An Isogram is a string in which no letter occurs more than once.

Input: S = machine
Output: 1
'''

# class Solution:
#     def isIsogram(self, s):
#         # Initialize an empty dictionary
#         count_dict = {}  
        
#         # Iterate through each character in the string
#         for char in s:  
#             # Check if the character is already in the dictionary
#             if char in count_dict:  
#                 # If yes, the string is not an isogram, return 0
#                 return 0  
#             else:
#                 # If no, add the character to the dictionary
#                 count_dict[char] = 1  
#         # If no duplicates are found, return 1
#         return 1  

# sol = Solution()
# print(sol.isIsogram("machine"))  
# print(sol.isIsogram("geeks"))    

class Solution:
    def isIsogram(self, s):
        # Initialize an empty set to keep track of seen characters
        seen = set()
        
        # Iterate through each character in the string
        for char in s:
            # Check if the character is already in the set
            if char in seen:
                # If yes, the string is not an isogram, return 0
                return 0
            else:
                # If no, add the character to the set
                seen.add(char)
        
        # If no duplicates are found, return 1
        return 1

# Example usage:
sol = Solution()
print(sol.isIsogram("machine"))  # Output: 1
print(sol.isIsogram("geeks"))    # Output: 0
