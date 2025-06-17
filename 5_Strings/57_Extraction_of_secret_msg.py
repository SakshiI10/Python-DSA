'''
You are given an encoded string S of length N. The encoded string is mixed with some number of substring "LIE" and some secret message. You have to extract secret message from it by removing all the "LIE" substrings.

Input: S = "LIEILIEAMLIELIECOOL"
Output: "I AM COOL"
'''

class Solution:

    def ExtractMessage(self, s):
        words=s.split('LIE')
        
        char=[]
        for word in words:
            if word != "":
                char.append(word)
        return " ".join(char)
    
sol=Solution()
print(sol.ExtractMessage("LIEILIEAMLIELIECOOL"))  