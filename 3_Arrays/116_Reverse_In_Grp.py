'''
Given an array arr of positive integers. Reverse every sub-array group of size k.

Input: arr[] = [1, 2, 3, 4, 5], k = 3
Output: [3, 2, 1, 5, 4]
'''

class Solution:
    def reverseInGroups(self, arr, k):
        n = len(arr)
        
        if k >= n:
            arr[:] = arr[::-1]  
        else:
            for i in range(0, n, k):
                arr[i:i+k] = arr[i:i+k][::-1]
        return arr
    
sol = Solution()
arr = [1, 2, 3, 4, 5]   
k = 3
print(sol.reverseInGroups(arr, k)) 
