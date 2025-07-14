'''
Given a string, find the number of pairs of characters that are same. Pairs (s[i], s[j]), (s[j], s[i]), (s[i], s[i]), (s[j], s[j]) should be considered different.

Input:
S = "air"
Output: 3'''

class Solution:
    def equalPairs (self,s):
        freq={}
        
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
                
        total_pairs=0
        for char, count in freq.items():
            total_pairs += count*count
            
        return total_pairs
    
sol=Solution()
S='geek'
print(sol.equalPairs(S))