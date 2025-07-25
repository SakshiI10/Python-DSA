'''
Print first letter of every word in the string
Difficulty: BasicAccuracy: 71.6%Submissions: 45K+Points: 1
Given a string S, the task is to create a string with the first letter of every word in the string.

Input: S = "geeks for geeks"
Output: gfg '''

class Solution:
    def firstAlphabet(self, S):
        res=""
        words=S.split()
        for word in words:
            res += word[0]
        return res

solution = Solution()
S = "geeks for geeks"
print(solution.firstAlphabet(S))  
S = "bad is good"
print(solution.firstAlphabet(S))  