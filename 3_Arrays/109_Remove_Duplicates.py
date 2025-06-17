'''
Given an array arr of integers which may or may not contain duplicate elements. Your task is to remove duplicate elements.

Input: arr[] = [1, 2, 3, 1, 4, 2]
Output: [1, 2, 3, 4]'''

class Solution:
    def removeDuplicate(self, arr):
        seen=set()
        
        for num in arr:
            if num not in seen:
                seen.add(num) 
        return list(seen)
    
    def checkDuplicates(self, arr):
        seen = set()

        for num in arr:
            if num in seen:
                return 'true'
            seen.add(num)
        return 'false'
    
sol=Solution()
arr=[1, 2, 3, 4]
print(sol.removeDuplicate(arr))
print(sol.checkDuplicates(arr))  
