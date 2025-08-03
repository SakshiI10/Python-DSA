'''
Given an integer array arr[], check if the array contains any duplicate value.

Input: arr = [4, 5, 6, 4]
Output: true'''

class Solution:
    def checkDuplicates(self, arr):
        # seen = set()
        # for num in arr:
        #     if num in seen:
        #         return True 
        #     seen.add(num)
        # return False

        # If you want to print duplicates
        seen = set()
        duplicates = set()
        for num in arr:
            if num in seen:
                duplicates.add(num)
            else:
                seen.add(num)

        if duplicates:
            return list(duplicates)  
        else:
            return False
    
sol=Solution()
arr = [4, 5, 6, 4]
print(sol.checkDuplicates(arr))
