'''
Given two strings A and B consisting of lowercase english characters. Find the characters that are not common in the two strings. 

Input:
A = geeksforgeeks
B = geeksquiz
Output: fioqruz'''

class Solution:
    def UncommonChars(self, A, B):
        countA = {}
        countB = {}

        # Count frequency of characters in A
        for char in A:
            countA[char] = countA.get(char, 0) + 1

        # Count frequency of characters in B
        for char in B:
            countB[char] = countB.get(char, 0) + 1

        result = set()

        # Collect uncommon characters from A
        for char in countA:
            if char not in countB:
                result.add(char)

        # Collect uncommon characters from B
        for char in countB:
            if char not in countA:
                result.add(char)

        # Convert set to sorted list and then to string
        result = ''.join(sorted(result))

        return result

solution = Solution()
A = "geeksforgeeks"
B = "geeksquiz"
output = solution.UncommonChars(A, B)
print(output)  # Expected output: fioqruz
