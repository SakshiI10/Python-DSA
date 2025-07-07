'''
Given a string S. Count the characters that have ‘N’ number of occurrences. If a character appears consecutively it is counted as 1 occurrence.

Input:
S = "abc", N = 1
Output: 3'''

class Solution:
    def getCount (self,S, N):
        freq = {}
        prev = None
        
        for char in S:
            if char != prev:
                freq[char] = freq.get(char, 0) + 1
            prev = char
        
        res = 0
        for count in freq.values():
            if count == N:
                res += 1
                
        return res
    
sol=Solution()
S = "abc"
N = 1
print(sol.getCount(S, N))