'''
Given a string S and array of strings, find whether the array contains a string with one character different from the given string.

Input :
N = 4
arr[] = {"bana","apple","banaba","bonanzo"}
S = "banana"
Output :
True'''

class Solution:
    def isOneMismatch(self, arr, S):
        for word in arr:
            if len(word) != len(S):
                continue

            count=0
            for i in range(len(S)):
                if word[i] != S[i]:
                    count += 1
                    if count > 1:
                        break
            
            if count == 1:
                return True
        return False
    
sol = Solution()
print(sol.isOneMismatch(["bana", "apple", "banaba", "bonanzo"], "banana"))  
