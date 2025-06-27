'''
Given a number N. You can perform an operation on it multiple times, in which you can change digit 5 to 6 and vice versa.
You have to return the sum of the maximum number and the minimum number which can be obtained by performing such operations.

Input: N = 35
Output: 71'''

class Solution:
    def performOperation(self, n):
        n_str = str(n)

        max_str = ''
        for ch in n_str:
            if ch == '5':
                max_str += '6'
            else:
                max_str += ch
        max_num = int(max_str)

        min_str = ''
        for ch in n_str:
            if ch == '6':
                min_str += '5'
            else:
                min_str += ch
        min_num = int(min_str)

        return min_num + max_num

sol=Solution()
N=35
print(sol.performOperation(N))