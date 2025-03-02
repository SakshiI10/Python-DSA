'''
You are given a string S, convert it into a magical string.
A string can be made into a magical string if the alphabets are swapped in the given manner: a->z or z->a, b->y or y->b, and so on.  
 
Note: All the alphabets in the string are in lowercase.

Input: S = varun
Output: ezifm'''

class Solution:
    def magicalString (ob,S):
        n=len(S)
        for i in range(n):result = []
        for char in S:
            if 'a' <= char <= 'z':
                reciprocal_char = chr(ord('z') - (ord(char) - ord('a')))
                result.append(reciprocal_char)
        return ''.join(result)