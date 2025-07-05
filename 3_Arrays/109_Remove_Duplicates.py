'''
Given an array arr of integers which may or may not contain duplicate elements. Your task is to remove duplicate elements.

Input: arr[] = [1, 2, 3, 1, 4, 2]
Output: [1, 2, 3, 4]'''

class Solution:
    def removeDuplicate(self, arr):
        unique_ele=set(arr)
        return list(unique_ele)
    
    def checkDuplicates(self, arr):
        unique_ele = set()

        for num in arr:
            if num in unique_ele:
                return 'true'
            unique_ele.add(num)
        return 'false'
    
sol=Solution()
arr=[1, 2, 3, 4]
print(sol.removeDuplicate(arr))
print(sol.checkDuplicates(arr))  
