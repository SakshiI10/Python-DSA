class Solution:
    def findMissing(self, a, n):
        freq={}
        repeating, missing = -1, -1

        for num in a:
            freq[num]=freq.get(num, 0)+1

        for i in range(n+1):
            if i not in freq:
                missing=i   
            elif freq[i]>1:
                repeating=i
        return missing, repeating

sol = Solution()
A = [4, 3, 6, 2, 1, 1]
N = len(A)
output = sol.findMissing(A, N)
print(output)