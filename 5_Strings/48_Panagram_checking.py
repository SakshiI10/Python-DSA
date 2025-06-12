'''
You are given a string s. You need to find if the string is a panagram or not.
A panagram contains all the letters of english alphabet at least once.

Input: s = "Thequickbrownfoxjumpsoverthelazydog"
Output: 1
'''

class Solution:
    def isPanagram(self,s):
        letters = set()
        s = s.lower()
        
        for char in s:
            if char.isalpha():
                letters.add(char)
                
        if len(letters) == 26:
            return 1
        else:
            return 0

sol=Solution()
s = "Thequickbrownfoxjumpsoverthelazydog"
print(sol.isPanagram(s))  