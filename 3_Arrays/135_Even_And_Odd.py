'''
Given an array arr[] of size N containing equal number of odd and even numbers. Arrange the numbers in such a way that all the even numbers get the even index and odd numbers get the odd index.
Note: There are multiple possible solutions, Print any one of them. Also, 0-based indexing is considered.

Input:
N = 6
arr[] = {3, 6, 12, 1, 5, 8}
Output:
1
'''

class Solution:
    def reArrange(self, arr, n):
        even_idx = 0
        odd_idx = 1
        res = [0] * n  
        
        for num in arr:
            if num % 2 == 0:
                res[even_idx] = num
                even_idx += 2
            else:
                res[odd_idx] = num
                odd_idx += 2
        
        for i in range(n):
            arr[i] = res[i]
        
        return 1
    
sol=Solution()
n = 6
arr = [3, 6, 12, 1, 5, 8]
print(sol.reArrange(arr, n))
 