'''
Given an array arr, write a program segregating even and odd numbers. The program should put all even numbers first in sorted order, and then odd numbers in sorted order.

Input: arr[] = [12, 34, 45, 9, 8, 90, 3]
Output: [8, 12, 34, 90, 3, 9, 45]'''

class Solution:
    def segregateEvenOdd(self,arr):
        n=len(arr)
        evens=[]
        odds=[]
        
        for i in range(n):
            if arr[i]%2==0:
                evens.append(arr[i])
                
        for i in range(n):
            if arr[i]%2 != 0:
                odds.append(arr[i])
                
        evens.sort()
        odds.sort()
        
        for i in range(len(evens)):
            arr[i] = evens[i]
        for i in range(len(odds)):
            arr[i + len(evens)] = odds[i]

        return arr

sol=Solution()
arr=[12, 34, 45, 9, 8, 90, 3]   
print(sol.segregateEvenOdd(arr))  