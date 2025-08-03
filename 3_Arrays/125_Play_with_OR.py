'''
You are given an array arr[] of length n, you have to re-construct the same array arr[] in-place. The arr[i] after reconstruction will become arr[i] OR arr[i+1], where OR is bitwise or. If for some i, i+1 does not exists, then do not change arr[i].

Input :
n = 5
arr[] = {10, 11, 1, 2, 3}
Output :
11 11 3 3 3'''

class Solution:
    def game_with_number (self, arr,  n) : 
        res = []
        
        for i in range(n - 1):
            num = arr[i] | arr[i + 1]
            res.append(num)
        res.append(arr[n - 1]) 
        
        return res
    
sol=Solution()
arr=[10, 11, 1, 2, 3]
n = len(arr)
print(sol.game_with_number(arr, n))  
