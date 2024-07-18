'''
Given two arrays arr1 and arr2 of equal size, the task is to find whether the given arrays are equal. Two arrays are said to be equal if both contain the same set of elements, arrangements (or permutations) of elements may be different though.

Input: arr1[] = [1, 2, 5, 4, 0], arr2[] = [2, 4, 5, 0, 1]
Output: true
'''

class Solution:
    def check(self, arr1, arr2) -> bool:
        arr1.sort()
        arr2.sort()
        
        if len(arr1) != len(arr2):
            return False
        
        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                return False
        
        return True
    
sol = Solution()
arr1 = [1, 2, 5, 4, 0]
arr2 = [2, 4, 5, 0, 1]
print(sol.check(arr1, arr2)) 