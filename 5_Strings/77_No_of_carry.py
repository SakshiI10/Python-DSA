'''
Given two numbers A and B, the task is to find the number of carry operations required when two numbers are added

Input:
A = 1234
B = 5678
Output: 
2'''

class Solution:
    def countCarry(self, A , B):
        A = str(A)[::-1]
        B = str(B)[::-1]
        
        carry = 0
        count = 0
        
        for i in range(len(A)):
            total = int(A[i]) + int(B[i]) + carry
            if total >= 10:
                carry = 1
                count += 1
            else:
                carry = 0
        
        return count
    
sol=Solution()
A = 1234
B = 5678
print(sol.countCarry(A, B))