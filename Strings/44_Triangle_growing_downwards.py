'''
Input:
str = "geeks"

Output:
....g
...ge
..gee
.geek
geeks
'''

class Solution:
    def printTriangleDownwards(self, s: str):
        n = len(s) 
        for i in range(n):
            print('.' * (n - i - 1) + s[:i + 1])

solution = Solution()
s = "geeks"
solution.printTriangleDownwards(s)
