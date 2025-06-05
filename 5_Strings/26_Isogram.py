'''
Given a string S of lowercase alphabets, check if it is isogram or not. An Isogram is a string in which no letter occurs more than once.

Input: S = machine
Output: 1
'''

class Solution:
    def isIsogram(self, s):
        count_dict = {}  
        
        for char in s:  
            if char in count_dict:  
                return 0  
            else:
                count_dict[char] = 1  
        return 1  

sol = Solution()
print(sol.isIsogram("machine"))  
print(sol.isIsogram("geeks"))    

# class Solution:
#     def isIsogram(self, s):
#         seen = set()
        
#         for char in s:
#             if char in seen:
#                 return 0
#             else:
#                 seen.add(char)

#         return 1

# sol = Solution()
# print(sol.isIsogram("machine"))  # Output: 1
# print(sol.isIsogram("geeks"))    # Output: 0
