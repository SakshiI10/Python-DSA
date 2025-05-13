'''
Given an unsorted array arr[] and two elements num1 and num2. The task is to count the number of elements that occur between the given elements (excluding num1 and num2). If there are multiple occurrences of num1 and num2, we need to consider the leftmost occurrence of num1 and the rightmost occurrence of num2.

Input: arr[] = [4, 2, 1, 10, 6], num1 = 4, and num2 = 6
Output: 3'''

class Solution:
    def getCount(self, arr, num1, num2):
        n=len(arr)
        res=[]
        
        low = arr.index(num1)  
        high = len(arr) - 1 - arr[::-1].index(num2)

        for i in range(n):
            if i > low and i < high:
                res.append(arr[i])

        return len(res)
    
sol=Solution()
arr = [4, 2, 1, 10, 6]
num1, num2 = 4, 6
print(sol.getCount(arr, num1, num2))
