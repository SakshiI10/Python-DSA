'''Red OR Green
Difficulty: BasicAccuracy: 72.22%Submissions: 29K+Points: 1
Given a string of length N, made up of only uppercase characters 'R' and 'G', where 'R' stands for Red and 'G' stands for Green.Find out the minimum number of characters you need to change to make the whole string of the same colour.

Input: N=5
S="RGRGR"
Output: 2'''

class Solution:
    def RedOrGreen(self, N, S):
        count_G = S.count('G')
        return count_G


sol = Solution()
N = 5
S = "RGRGR"
print(sol.RedOrGreen(N, S))  
N = 7
S = "GGGGGGR"
print(sol.RedOrGreen(N, S)) 