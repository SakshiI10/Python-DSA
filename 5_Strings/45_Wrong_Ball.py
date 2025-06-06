'''
There is a table on which N balls are kept starting from index 1 to N in horizontal direction. Each ball is either of  red (denoted by 'R') or of blue (denoted by 'B') color. Any red ball which is placed on even indices and blue balls placed on odd indices is considered as wrongly placed. You need return the number of balls placed wrong on the table.

Input:
S = "RRBB"
Output: 2 '''

class Solution:
    def countWrongPlacedBalls(self, s):
        count = 0
        
        for i in range(len(s)):
            index = i + 1
            if index % 2 == 0 and s[i] == 'R':
                count += 1
            elif index % 2 != 0 and s[i] == 'B':
                count += 1
        return count
    
sol = Solution()
s = "RRBB"
print(sol.countWrongPlacedBalls(s)) 