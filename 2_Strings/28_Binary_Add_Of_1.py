'''
You are given a binary string s of length n. You have to perform binary addition of the string with '1'.

Input: n = 4
s = 1010
Output: 1011'''

class Solution:
    def binaryAdd(self, n, s):
        # Convert the binary string to an integer
        num = int(s, 2)
        # Add 1 to the integer
        num += 1
        # Convert the integer back to a binary string, removing the '0b' prefix
        result = bin(num)[2:]
        # Ensure the result has the correct length by padding with leading zeros if necessary
        if len(result) < n:
            result = '0' * (n - len(result)) + result
        return result

sol = Solution()
print(sol.binaryAdd(4, "1010"))  
print(sol.binaryAdd(3, "111"))   
print(sol.binaryAdd(22, "0000000000001111111110")) 
