'''
Given an array arr, the goal is to find out the smallest number that is repeated exactly ‘k’ times.
Note: If there is no such element then return -1.

Input: arr[] = [2, 2, 1, 3, 1], k = 2
Output: 1'''

class Solution:
    def findDuplicate(self, arr, k):
        freq={}
        
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
                
        res=[]
        
        for num, count in freq.items():
            if count==k:
                res.append(num)
                
        if res:
            return min(res)
        else:
            return -1
        
sol=Solution()
arr=[2, 2, 1, 3, 1]
k=2
arr2=[3, 5, 3, 2]
k2=1
print(sol.findDuplicate(arr, k))
print(sol.findDuplicate(arr2, k2))