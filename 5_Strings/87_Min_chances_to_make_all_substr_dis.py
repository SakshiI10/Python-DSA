'''
Given a string s consisting only lower case alphabets, find the minimum number of changes required to it so that all substrings of the string become distinct.
Note: length of the string is at most 26.

Input: S = "aab"
Output: 1'''

class Solution:
    def minChange(self,S):
        n1=len(S)
        unique_set=set(S)
        n2=len(unique_set)
        n=abs(n1-n2)
        return n
    
sol=Solution()
S = "aab"
print(sol.minChange(S))
