'''
Given two arrays arr1[], arr2[], and an integer k. The task is to check if after permuting both arrays in such a way, we get the sum of their corresponding element greater than or equal to k i.e. arr1i + arr2i >= k for all i (from 0 to n-1). Return true if possible, else false. 


Input: k = 10, arr1[] = [2, 1, 3], arr2[] = [7, 8, 9]. 
Output: true'''

class Solution:
    def isPossible(self, k, arr1, arr2):
        arr1.sort()
        arr2 = sorted(arr2)[::-1]
        
        for a, b in zip(arr1, arr2):
            if a + b < k:
                return False
        return True
    
sol=Solution()
k = 5
arr1 = [1, 2, 2, 1]
arr2 = [3, 3, 3, 4]
print(sol.isPossible(k, arr1, arr2))