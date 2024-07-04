class Solution:
    def countCamelCase(self, S):
        count = 0
        
        for char in S:
            if char.isupper():
                count += 1
        
        return count
    
# Example usage:
sol = Solution()
S1 = "ckjkUUYII"
S2 = "CamelCaseExample"
S3 = "lowerUpperLower"

print(sol.countCamelCase(S1))  # Output: 5
print(sol.countCamelCase(S2))  # Output: 2
print(sol.countCamelCase(S3))  # Output: 1
