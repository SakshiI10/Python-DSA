'''
Given a string s, extract all the integers from s.

Input:
s = "1: Prakhar Agrawal, 2: Manish Kumar Rai, 
     3: Rishabh Gupta56"
Output: 1 2 3 56'''

class Solution:
    def extractIntegerWords(self, s: str) -> list:
        result = []
        current_int = ''

        for ch in s:
            if ch.isdigit():
                current_int += ch
            elif current_int:   #current_int has accumulated digits, it means we've reached the end of an integer in the string.
                result.append(current_int)
                current_int = ''
        
        if current_int:
            result.append(current_int)

        if not result:
            result.append("No Integers")

        return result

sol = Solution()
s = "1: Prakhar Agrawal, 2: Manish Kumar Rai, 3: Rishabh Gupta56"
print(sol.extractIntegerWords(s))
