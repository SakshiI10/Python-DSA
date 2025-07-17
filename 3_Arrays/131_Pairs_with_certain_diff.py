'''
Given an array of integers, arr[] and a number, K.You can pair two numbers of the array if the difference between them is strictly less than K. The task is to find the maximum possible sum of such disjoint pairs (i.e., each element of the array can be used at most once). The Sum of P pairs is the sum of all 2P elements of pairs.

Input  : 
arr[] = {3, 5, 10, 15, 17, 12, 9}
K = 4
Output : 
62'''

class Solution:
    def maxSumPairWithDifferenceLessThanK(self, arr, N, K): 
        arr.sort()
        sum=0
        i=N-1
        
        while i>0:
            if arr[i] - arr[i-1] < K:
                sum += arr[i] + arr[i-1]
                i -= 2  
            else:
                i -= 1  
        
        return sum
    
sol=Solution()
arr = [3, 5, 10, 15, 17, 12, 9]
K=4
print(sol.maxSumPairWithDifferenceLessThanK(arr, len(arr), K))
