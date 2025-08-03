class Solution:
    def merge_arr(self, arr1, arr2):
        n1=len(arr1)
        n2=len(arr2)
        left, right=0, 0
        arr3=[]

        while(left<n1 and right<n2):
            if(arr1[left] <= arr2[right]):
                arr3.append(arr1[left])
                left += 1
            else: 
                arr3.append(arr2[right])
                right += 1

        while left < n1:
            arr3.append(arr1[left])
            left += 1

        while right < n2:
            arr3.append(arr2[right])
            right += 1

        return arr3
    
sol = Solution()
arr1 = [1, 3, 5, 7]
arr2 = [0, 2, 6, 8, 9]
print(sol.merge_arr(arr1, arr2)) 
