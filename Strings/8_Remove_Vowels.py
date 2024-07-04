class Solution:
    def removeVowels(self, S):
        vowels = set("aeiouAEIOU")  # Using a set for fast lookup
        result = ""
        
        for char in S:
            if char not in vowels:
                result += char
        
        return result

# Example usage:
sol = Solution()
S1 = "welcome to geeksforgeeks"
S2 = "what is your name ?"

print(sol.removeVowels(S1))  # Output: "wlcm t gksfrgks"
print(sol.removeVowels(S2))  # Output: "wht s yr nm ?"
