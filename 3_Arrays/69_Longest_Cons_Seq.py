class Solution:
    def longest_cons_subseq(self, arr, n):
        for i in range(n):
            num = arr[i]
            count=1
            while num+1 in arr:
                count += 1
                num += 1
        return count
    
    def longest_cons_subseq2(self, arr):
        arr = list(set(arr)) 
        arr.sort()  

        longest = 1
        count = 1 
        last_smaller = arr[0]  
        n = len(arr)
        
        for i in range(n):
            if arr[i] == last_smaller + 1:  
                count += 1
            else:
                count = 1
            
            longest = max(longest, count)
            last_smaller = arr[i] 
        
        return longest

sol = Solution()
arr1 = [102, 4, 100, 1, 101, 3, 2, 1, 1]
print(sol.longest_cons_subseq(arr1, len(arr1)))  
print(sol.longest_cons_subseq2(arr1))  
