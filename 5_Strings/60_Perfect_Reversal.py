'''
You are given a string ‘str’, the task is to check that reverses of all possible substrings of ‘str’ are present in ‘str’. If yes then the answer is 1, otherwise, the answer will be 0.

Input: n = 2, str = "ab"
Output: 0'''

class Solution:
    def isReversible(self, str, n):
        for i in range(n // 2):
            if str[i] != str[n - 1 - i]:
                return 0
        return 1

sol=Solution()
S='abcdba'
print(sol.isReversible(S, len(S)))