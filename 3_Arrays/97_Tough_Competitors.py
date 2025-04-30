# Given an array arr[] of non-negative integers representing the skill levels of competitors, determine the minimum absolute difference between the skills of any two competitors. Competitors are considered tough if their skill difference is the smallest among all possible pairs.

# Input: arr[] = [9, 4, 12, 6]
# Output: 2

class Solution:
    def minDiff(self, arr):
        n=len(arr)
        arr.sort()
        min_diff=float('inf')
        
        for i in range(1, n):
            diff=abs(arr[i] - arr[i-1])
            if diff<min_diff:
                min_diff=diff
        return min_diff

sol=Solution()    
arr=[9, 4, 12, 6]
print(sol.minDiff(arr))
