'''
Given a string S, remove all consonants and print the modified string that contains vowels only.

Input: S = "abEkipo"
Output: aEio'''

class Solution:
    def removeConsonants(self, s):
        vowels = set("aeiouAEIOU")  
        result = ""
        
        for char in s:
            if char in vowels:
                result += char
        if not result:
            return "No Vowel"
            
        return result

sol = Solution()
print(sol.removeConsonants("abEkipo"))  # Output: aEio
print(sol.removeConsonants("vgty"))     # Output: No Vowel