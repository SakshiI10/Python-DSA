'''
Given an array arr of integers which may or may not contain duplicate elements. Your task is to remove duplicate elements.

Input: arr[] = [1, 2, 3, 1, 4, 2]
Output: [1, 2, 3, 4]'''

class Solution:
    def removeDuplicate(self, arr):
        seen=set()
        res=[]
        
        for num in arr:
            if num not in seen:
                seen.add(num)
                res.append(num)
                
        return res
    
sol=Solution()
arr=[1, 2, 3, 1, 4, 2]
print(sol.removeDuplicate(arr))