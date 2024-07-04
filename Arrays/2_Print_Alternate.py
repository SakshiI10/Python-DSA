'''
You are given an array A of size N. You need to print elements of A in alternate order (starting from index 0).

Input:
N = 4
A[] = {1, 2, 3, 4}
Output:
1 3'''

class Solution:
    def printAl(self, arr, n):
        for i in range(0, n, 2):
            print(arr[i], end=" ")

sol=Solution()
n=4
arr=[1,2,3,4]
sol.printAl(arr,n)
