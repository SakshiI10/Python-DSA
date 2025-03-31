class Solution:
    def find(self, arr, target, n):
        first, last = -1, -1
        for i in range(n):
            if arr[i]==target:
                if(first==-1):
                    first=i
                last=i
        return first, last            

sol=Solution()
arr=[2, 4, 6, 8, 8, 8, 11, 11, 13]
n=len(arr)
target=8
print(sol.find(arr, target, n))