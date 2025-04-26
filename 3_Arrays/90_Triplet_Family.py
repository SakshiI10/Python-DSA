# Given an array arr of integers. First sort the array then find whether three numbers are such that the sum of two elements equals the third element.

# Input: arr[] = [1, 2, 3, 4, 5]
# Output: true

class Solution:

    def findTriplet(self, arr):
        n = len(arr)
        arr.sort()
        for i in range(n - 1, -1, -1):
            j = 0
            k = i - 1
            while j < k:
                if arr[i] == arr[j] + arr[k]:
                    return True
                elif arr[i] > arr[j] + arr[k]:
                    j += 1
                else:
                    k -= 1
        return False
sol=Solution()
arr=[1, 2, 3, 4, 5]
print(sol.findTriplet(arr))