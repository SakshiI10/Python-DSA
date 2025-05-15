'''Given two sorted arrays arr1 and arr2 of distinct elements. Given a value x. The problem is to count all pairs from both arrays whose sum equals x.
Note: The pair has an element from each array.

Input: x = 10, arr1[] = [1, 3, 5, 7], arr2[] = [2, 3, 5, 8] 
Output: 2'''

class Solution:
    def countPairs(self,arr1, arr2, x):
        s = set(arr2)
        count = 0

        for num in arr1:
            if (x - num) in s:
                count += 1

        return count
    
sol=Solution()
arr1= [1, 3, 5, 7]
arr2= [2, 3, 5, 8]  
x=10
print(sol.countPairs(arr1, arr2, x)) 