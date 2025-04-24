# Given an array arr[] of integers. Write a program to check whether an arithmetic progression can be formed using all the given elements. 
# Input: arr[] = [0, 12, 4, 8]
# Output: true

class Solution:
    def checkIsAP(self, arr):
        arr.sort()
        n=len(arr)
        
        if n<2:
            return 'true'
            
        diff=arr[1]-arr[0]
        
        for i in range(1, n-1):
            if arr[i + 1] - arr[i] != diff:
                return False
        
        return True
    
sol=Solution()
arr=[0, 12, 4, 8]
print(sol.checkIsAP(arr))