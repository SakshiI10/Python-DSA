'''
You are given an array arr[] of integers. Your task is to find the count of elements before which all the elements are smaller. The first element is always counted as there are no elements before it.

Input: arr[] = [10, 40, 23, 35, 50, 7]
Output: 3'''

class Solution:
    def count_elements(self, arr):
        n=len(arr)
        count=1
        max_count=arr[0]
        
        for i in range(1, n):
            if arr[i]>max_count:
                count += 1
                max_count=arr[i]
        return count
    
sol=Solution()
arr=[10, 40, 23, 35, 50, 7]
print(sol.count_elements(arr))
