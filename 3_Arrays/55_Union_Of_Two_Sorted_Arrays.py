class Solution:
    def union(self, arr1, arr2):
        unique_element=set()
        n1=len(arr1)
        n2=len(arr2)
        for i in range(n1):
            if arr1[i] not in unique_element:
                unique_element.add(arr1[i])
        for i in range(n2):
            if arr2[i] not in unique_element:
                unique_element.add(arr2[i])
        return unique_element

sol=Solution()
arr1=[1, 1, 2, 3, 4, 5]
arr2=[2, 3, 4, 4, 5, 6]
print(sol.union(arr1, arr2))
