'''
Given an array arr[] and an integer x. You have to calculate the average for each element arr[i] and x and find out whether that number exists in the array. Do it for all the elements of the array and store the count result in another array for each index how many occurrences of average are present in the array.

Input : arr[] = [2, 4, 8, 6, 2] and x = 2
Output : [2, 0, 0, 1, 2]'''

class Solution:
    def countArray(self, arr, x):
        n = len(arr)
        result = []
        
        for i in range(n):
            avg = (arr[i] + x) // 2
            
            if avg in arr:
                result.append(arr.count(avg))
            else:
                result.append(0)
                
        return result

sol = Solution()
arr = [2, 4, 8, 6, 2]
x = 2
print(sol.countArray(arr, x)) 


'''
class Solution:
    def countArray (self, arr, x) : 
        count_map = {}
        for num in arr:
            count_map[num] = count_map.get(num, 0) + 1
        
        for i in range(n):
            avg = (arr[i] + x) // 2
            result.append(count_map.get(avg, 0))  
            
        return result'''