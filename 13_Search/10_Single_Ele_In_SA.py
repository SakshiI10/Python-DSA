class Solution:
    def find(self, arr, target, n):
        if n==1:
            return arr[0]         
        
        for i in range(n):
            if i==0:
                if (arr[i] != arr[i+1]):
                    return arr[i]
            elif i==n-1:
                if (arr[i] != arr[i-1]):
                    return arr[i]
            else:
                if (arr[i] != arr[i-1] and arr[i] != arr[i+1]):
                    return arr[i]


sol=Solution()
arr=[1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
n=len(arr)
target=8
print(sol.find(arr, target, n))