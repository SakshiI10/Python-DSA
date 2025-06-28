'''
Given two integer number n and d. The task is to find the number between 0 to n which contain the specific digit d.

Input
n = 20
d = 5
Output
5 15 '''

class Solution:

    def solve(self, n, d):
        res = []
        d = str(d)
        
        for i in range(n + 1):
            if d in str(i):
                res.append(str(i))

        if res:
            return ' '.join(res)  
        else:
            return '-1'

sol=Solution()
n=1
d=2
print(sol.solve(n, d))