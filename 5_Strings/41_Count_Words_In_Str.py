'''
You are given a string s consisting of multiple words. You need to count the total words in the string. Words are separated by a single space.
Note: It is guaranteed that the last character of the given string is not a white space.

Input: s = "Geeks"
Output: 1
Input: s = "World is hello"
Output: 3'''

class Solution:
    def countWords(self,s):
        words=s.split()
        count=0
        
        for char in words:
            count += 1
            
        return count
    
sol=Solution()
print(sol.countWords("Geeks")) 
print(sol.countWords("World is hello"))
