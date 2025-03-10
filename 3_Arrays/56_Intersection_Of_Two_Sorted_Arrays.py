class Solution():
    def inter(self, arr1, arr2):
        i, j=0, 0
        n1=len(arr1)
        n2=len(arr2)
        result=[]

        while(i<n1 and j<n2):
            if arr1[i]<arr2[j]:
                i += 1
            elif arr2[j]<arr1[i]:
                j += 1
            else:
                result.append(arr1[i])
                i += 1
                j += 1
        return result

sol=Solution()
arr1=[1, 2, 2, 3, 3, 4, 5, 6]
arr2=[2, 3, 3, 5, 6, 6, 7]
print(sol.inter(arr1, arr2))
