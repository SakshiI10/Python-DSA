'''
Input: s = "Geeks for Geeks"
Output: 5
Explanation: The last word is "Geeks" of length 5.'''

class Solution:
    def findLength(self, s):
        words=s.split()
        return len(words[-1])
    
sol=Solution()
print(sol.findLength("Geeks for Geeks"))  