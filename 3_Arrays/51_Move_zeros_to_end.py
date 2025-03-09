class Solution:
    def move(self, arr):
        n=len(arr)
        result=[]

        for i in range(n):
            if arr[i] != 0:
                result.append(arr[i])

        while len(result) < n:
            result.append(0)
            
        return result

sol=Solution()
arr=[1, 0, 2, 0, 3, 0, 4]
print(sol.move(arr))