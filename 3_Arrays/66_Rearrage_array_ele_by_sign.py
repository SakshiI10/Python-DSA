class Solution:
    #Brute Force
    def rearrange(self, arr):
        n=len(arr)
        pos=[]
        neg=[]
        result=[]

        for i in range(n):
            if arr[i]>0:
                pos.append(arr[i])
            else:
                neg.append(arr[i])

        i, j= 0, 0
        while i<len(pos) and j<len(neg):
            result.append(pos[i])
            result.append(neg[i])
            i += 1
            j += 1
        
        return result
            
sol=Solution()
arr=[3, 1, -2, -5, 2, -4]
arr2=[1, 2, -4, -5]
print(sol.rearrange(arr))
print(sol.rearrange(arr2))
