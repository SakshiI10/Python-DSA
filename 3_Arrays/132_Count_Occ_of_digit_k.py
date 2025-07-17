'''
Given an array arr[]. Your task is to return an integer denoting the total number of times digit k appears in the array.

Input: k=1, arr[] = [11, 12, 13, 14, 15]
Output: 6 '''

class Solution:
    def num(self, k, arr):
        count=0
        k=str(k)
        
        for num in arr:
            for digit in str(num):
                if digit == k:
                    count += 1
                    
        return count
    
sol=Solution()
arr=[11, 12, 13, 14, 15]
k=1
print(sol.num(k, arr))
