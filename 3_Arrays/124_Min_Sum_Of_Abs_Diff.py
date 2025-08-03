'''
You are given two arrays A and B of equal length N. Your task is to pair each element of array A to an element in array B, such that the sum of the absolute differences of all the pairs is minimum.

Input:
N = 4
A = {4,1,8,7}
B = {2,3,6,5}
Output:
6
'''
class Solution:
    def findMinSum(self, A,B,N):
        A.sort()
        B.sort()
        total_sum=0
        
        for i in range(len(A)):
            total_sum += abs(A[i]-B[i])
            
        return total_sum
sol = Solution()
A = [4, 1, 8, 7]
B = [2, 3, 6, 5]
N = len(A)
print(sol.findMinSum(A, B, N))  
