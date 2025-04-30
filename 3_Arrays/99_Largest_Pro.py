'''
Given an array arr and an integer k. You have to find the maximum product of k contiguous elements in the array. 

Input: arr[] = [1, 2, 3, 4] and k = 2
Output: 12 '''

class Solution:
    def findMaxProduct(self, arr, k):
        n=len(arr)
        arr.sort()
        product=1
        
        for i in range(n-k, n):
            product *= arr[i]
            
        return product
    
sol=Solution()
arr=[1, 2, 3, 4]
k = 3
print(sol.findMaxProduct(arr, k))