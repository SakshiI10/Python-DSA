'''
Given a string S, find whether it fulfills the following criteria. 
When split from the middle, the string should give two halves having the same characters and same frequency of each character. If the number of characters in the string is odd, ignore the middle character.

Input: S = "abcdbca"
Output: YES
'''

from collections import Counter
class Solution:
    def passed(self, s):
        n = len(s)
        mid = n // 2
        
        if n % 2 == 0:
            left = s[:mid]
            right = s[mid:]
        else:
            left = s[:mid]
            right = s[mid+1:]

        if Counter(left) == Counter(right):
            return "YES"
        else:
            return "NO"

sol=Solution()
S="bvas"
print(sol.passed(S)) 
