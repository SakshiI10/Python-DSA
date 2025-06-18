'''
Given a string S, find whether it fulfills the following criteria. 
When split from the middle, the string should give two halves having the same characters and same frequency of each character. If the number of characters in the string is odd, ignore the middle character.

Input: S = "abcdbca"
Output: YES
'''

class Solution:
    def passed(self, s):
        n = len(s)
        mid = n // 2
        
        if n % 2 == 0:
            left = s[:mid]
            right = s[mid:]
        else:
            left = s[:mid]
            right = s[mid+1:]

        def count_freq(substring):
            freq = {}
            for char in substring:
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] = 1
            return freq

        left_count = count_freq(left)
        right_count = count_freq(right)

        if len(left_count) != len(right_count):
            return "NO"

        for key in left_count:
            if key not in right_count or left_count[key] != right_count[key]:
                return "NO"

        return "YES"

sol=Solution()
S="bvas"
print(sol.passed(S)) 
