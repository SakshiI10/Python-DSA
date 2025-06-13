'''
Given two strings S1 and S2 . Return "1" if both strings are anagrams otherwise return "0" .

Note: An anagram of a string is another string with exactly the same quantity of each character in it, in any order.

Input: S1 = "cdbkdub" , S2 = "dsbkcsdn"
Output: 0 
Explanation: Length of S1 is not same
as length of S2.'''

class Solution:
    def areAnagram(ob, S1, S2):
        if len(S1) != len(S2):
            return 0

        for char in S1:
            if S1.count(char) != S2.count(char):
                return 0

        return 1
    
sol=Solution()
S1 = "cdbkdub"
S2 = "dsbkcsdn"
print(sol.areAnagram(S1, S2))  