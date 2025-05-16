'''
Given an array arr containing equal number of positive and negative elements, arrange the array such that every positive element is followed by a negative element.

Input: arr[] = [-1, 2, -3, 4, -5, 6]
Output: [2, -1, 4, -3, 6, -5]'''

class Solution:
    def arranged(self,arr):
        positives=[]
        negatives=[]
        
        for num in arr:
            if num>0:
                positives.append(num)
            else:
                negatives.append(num)
                
        res=[]
        for p, n in zip(positives, negatives):
            res.append(p)
            res.append(n)
            
        return res
    
sol=Solution()
arr=[-1, 2, -3, 4, -5, 6]
print(sol.arranged(arr))  
