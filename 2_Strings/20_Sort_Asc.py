'''
Given a string consisting of lowercase letters, arrange all its letters in ascending order. 

Input:
S = "edcab"
Output: "abcde"'''

class Solution:
    def sort(self, s):
        return ''.join(sorted(s))

sol = Solution()
sorted_string = sol.sort("edcab")
print(sorted_string)  # Output: "abcde"
