'''
Given a string S. Count the characters that have ‘N’ number of occurrences. If a character appears consecutively it is counted as 1 occurrence.

Input: S = "abc", N = 1
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
                
        result_count = sum(1 for count in count_dict.values() if count == N)
        
        return result_count

solution = Solution()
S = "abc"
N = 1
output = solution.getCount(S, N)
print(output)  
