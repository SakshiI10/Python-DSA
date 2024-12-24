'''
Given a string S contains 0's, 1's, and 2's, the task is to find the number of goals on the penalty.

 '1' stands for "goal".
 '0' stands for "no goal".
 '2' stands for a foul which gives a penalty.

 Input: S = "1012012112110"
Output: 2'''

class Solution:
    def penaltyScore(self, S):
        count = 0
        for i in range(len(S) - 1):
            if S[i] == '2' and S[i + 1] == '1':
                count += 1
        return count

sol = Solution()
S = "1012012112110"
print(sol.penaltyScore(S))  # Output: 2
