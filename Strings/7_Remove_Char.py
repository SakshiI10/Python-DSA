class Solution:
    def removeCharacters(self, S):
        result = ""
        
        for char in S:
            if char.isdigit():
                result += char
        
        return result

# Example usage:
sol = Solution()
S1 = "AA1d23cBB4"
S2 = "a1b2c3"

print(sol.removeCharacters(S1))  # Output: "1234"
print(sol.removeCharacters(S2))  # Output: "123"
