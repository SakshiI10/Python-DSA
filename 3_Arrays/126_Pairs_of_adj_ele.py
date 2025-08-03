'''
Given an array arr[] of positive integers. The task is to count consecutive pairs of adjacent elements. A pair is said to be consecutive if the second element in the pair is greater than the first element by 1. For example, (4,5) is a pair of consecutive elements.

Input: arr = [5, 7, 6, 7, 4]
Output: 1'''

class Solution:
    def adjacentPairs(self,arr):
        n=len(arr)
        count=0
        res=[]
        
        for i in range(n-1):
            if arr[i+1] == arr[i] + 1:
                count += 1
                res.append((arr[i], arr[i+1]))
        return count, res
    
sol=Solution()
arr = [1, 2, 3, 4]
print(sol.adjacentPairs(arr))
