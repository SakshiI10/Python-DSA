# Function to count occurrences of characters using hashing

class Solution():
    def count_occurences(self, arr):
        hash_table={}

        for char in arr:
            if char in hash_table:
                hash_table[char] += 1
            else:
                hash_table[char]=1
        return hash_table
    
sol=Solution()
arr="abcdabehf"
print(sol.count_occurences(arr))
