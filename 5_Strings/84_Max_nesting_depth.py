'''
Input: s = " ((5+2)(3+4)((6))) "
Output: 3
Explanation: Character '6' is inside three nested parentheses.'''

class Solution:
    def maxDepth(self, s):
        max_depth=0
        current_depth=0
        
        for char in s:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
                
        return max_depth

sol=Solution()
s = " ((5+2)(3+4)((6))) "
print(sol.maxDepth(s))
