'''
Given a string S which consists of alphabets , numbers and special characters. You need to write a program to split the strings in three different strings S1, S2 and S3 such that the string S1 will contain all the alphabets present in S , the string S2 will contain all the numbers present in S and S3 will contain all special characters present in S.  The strings S1, S2 and S3 should have characters in same order as they appear in input.

Input:
S = geeks01for02geeks03!!!
Output:
geeksforgeeks
010203
!!!'''

class Solution:
    def splitString(ob, S): 
        S1, S2, S3 = '', '', ''  
        
        for char in S:
            if char.isalpha():  
                S1 += char
            elif char.isdigit(): 
                S2 += char
            else:  
                S3 += char
                
        return S1, S2, S3

S = "geeks01for02geeks03!!!"
sol = Solution()
S1, S2, S3 = sol.splitString(S)
print(S1)  # Output: geeksforgeeks
print(S2)  # Output: 010203
print(S3)  # Output: !!!
