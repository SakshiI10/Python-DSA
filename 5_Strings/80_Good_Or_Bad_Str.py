'''
In this problem, a String S is composed of lowercase alphabets and wildcard characters i.e. '?'. Here, '?' can be replaced by any of the lowercase alphabets. Now you have to classify the given String on the basis of following rules:

If there are more than 3 consonants together or more than 5 vowels together, the String is considered to be "BAD". A String is considered "GOOD" only if it is not “BAD”.

Input:
S = aeioup??
Output:
1 '''

class Solution:
    def isGoodorBad(self, s):
        vowels = set('aeiou')
        vowel_count = 0
        cons_count = 0

        for ch in s:
            if ch in vowels:
                vowel_count += 1
                cons_count = 0
            elif ch == '?':
                vowel_count += 1
                cons_count += 1
            else:
                cons_count += 1
                vowel_count = 0

            if vowel_count > 5 or cons_count > 3:
                return 0

        return 1
    
sol=Solution()
S = 'aeioup??'
print(sol.isGoodorBad(S))
