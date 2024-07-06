'''
Given a string, remove the vowels from the string.

Input: S = "welcome to geeksforgeeks"
Output: wlcm t gksfrgks'''

class Solution:
    def removeVowels(self, S):
        vowels = set("aeiouAEIOU")  
        result = ""
        
        for char in S:
            if char not in vowels:
                result += char
        
        return result

sol = Solution()
S1 = "welcome to geeksforgeeks"
S2 = "what is your name ?"
print(sol.removeVowels(S1))  # Output: "wlcm t gksfrgks"
print(sol.removeVowels(S2))  # Output: "wht s yr nm ?"
