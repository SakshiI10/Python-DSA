'''
Given a string s of lowercase alphabets. The task is to find the maximum occurring character in the string s. If more than one character occurs the maximum number of times then print the lexicographically smaller character.

Input: s = "testsample"
Output: 'e' '''

class Solution:
    def getMaxOccurringChar(self, s):
        freq={}
        
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        max_freq = 0
        max_char = ''
        
        for char in sorted(freq):
            if freq[char] > max_freq:
                max_freq = freq[char]
                max_char = char
                
        return max_char
    
sol = Solution()
s = "testsample"
print(sol.getMaxOccurringChar(s))  