'''
Given a string S. Count the characters that have ‘N’ number of occurrences. If a character appears consecutively it is counted as 1 occurrence.

Input:
S = "abc", N = 1
Output: 3'''

class Solution:
    def getCount(self, S, N):
        count_dict = {}
        prev_char = None
        
        for char in S:
            if char != prev_char:
                if char in count_dict:
                    count_dict[char] += 1
                else:
                    count_dict[char] = 1
                prev_char = char
        
        result_count = 0
        for char, count in count_dict.items():
            if count == N:
                result_count += 1
        
        return result_count

S = "abc"
N = 1
solution = Solution()
print(solution.getCount(S, N))  # Output: 3
