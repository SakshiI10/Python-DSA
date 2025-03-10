# Using Brute Force - Dictionary method
class Solution():
    def find(self, arr):
        freq={}

        for num in arr:
            freq[num]=freq.get(num, 0)+1
        for key, value in freq.items():
            if value==1:
                return key

# Using xor      
    def find2(self, arr):
        xorr=0
        n=len(arr)

        for i in range(n):
            xorr=xorr^arr[i]
        return xorr

sol=Solution()
arr=[1, 1, 2, 3, 3, 4, 4]
print(sol.find(arr))
print(sol.find2(arr))