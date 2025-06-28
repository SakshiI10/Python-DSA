'''
Given an integer N represented in the form of a string, remove consecutive repeated digits from it.

Input:
N = 1224
Output: 124'''

class Solution:
    def modify(self, N):          
        arr = list(str(N))
        n = len(arr)
        res = ''
        
        for i in range(n - 1):
            if arr[i] != arr[i + 1]:   
                res += arr[i]
        res += arr[-1]  
        
        return res
    
sol=Solution()
N=1224
print(sol.modify(N))