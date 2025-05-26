'''
Given an array arr[] containing positive elements. A and B are two numbers defining a range. The task is to check if the array contains all elements in the given range (inclusive).

Input: n = 7, A = 2, B = 5, arr[] =  {1, 4, 5, 2, 7, 8, 3}
Output: True=

Input: n = 7, A = 2, B = 6, arr[] = {1, 4, 5, 2, 7, 8, 3}
Output: False'''

class Solution:
    def check_elements(self, arr, A, B):
        for num in range(A, B+1):
            if num not in arr:
                return False
        return True
    
sol = Solution()
arr= [1, 4, 5, 2, 7, 8, 3]
A1, B1=2, 5
A2, B2=2, 6
print(sol.check_elements(arr, A1, B1))  
print(sol.check_elements(arr, A2, B2))
