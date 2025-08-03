'''Given a positive integer x and an array arr of positive integers. We need to find the farthest index at which x is present. If any occurrence of x doesn't exist, then return -1.

Input: arr[] = [7, 42, 5, 6, 42, 8, 7, 5, 3, 6, 7] and x = 7
Output: 11
'''

class Solution:
    def findIndex(self, arr, x):
        n=len(arr)
        
        for i in range(n - 1, -1, -1): 
            if arr[i] == x:
                return i + 1  
        return -1 

sol=Solution()
arr=[7, 42, 5, 6, 42, 8, 7, 5, 3, 6, 7] 
x=7
print(sol.findIndex(arr, x))
