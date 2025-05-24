class Solution:
    def nonRepeating(self, arr):
        freq = {}

        for ch in arr:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        for i in range(len(arr)):
            if freq[arr[i]] == 1:
                return i

        return -1
    
sol=Solution()
str="welcometoaccolite"
print(sol.nonRepeating(str))
