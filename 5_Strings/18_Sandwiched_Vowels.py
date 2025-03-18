'''
For a given string S, comprising of only lowercase English alphabets, eliminate the vowels from the string that occur between two consonants(sandwiched between two immediately adjacent consonants). Print the updated string on a new line.

Input : S = "bab"
Output : bb'''

class Solution():
    def Sandwiched_Vowel(self, s):
        vowels = set('aeiou')
        n = len(s)
        result = []

        for i in range(n):
            if i > 0 and i < n - 1:
                if s[i - 1] not in vowels and s[i] in vowels and s[i + 1] not in vowels:
                    continue
            result.append(s[i])
        return ''.join(result)

sol = Solution()
S = "bab"
print(sol.Sandwiched_Vowel(S))  # Output: bb