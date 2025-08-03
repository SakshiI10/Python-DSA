class Solution:
    def Learning(self, arr, n):
        positive_count, negative_count, zero_count=0, 0, 0
        res=[]
        
        for i in range(n):
            if arr[i]>0:
                positive_count += 1
            elif arr[i]<0:
                negative_count += 1
            else:
                zero_count += 1
        
        def format_result(value):
            rounded = round(value, 5)
            return int(rounded) if rounded == int(rounded) else rounded

        res.append(format_result(n / positive_count) if positive_count else 'inf')
        res.append(format_result(n / negative_count) if negative_count else 'inf')
        res.append(format_result(n / zero_count) if zero_count else 'inf')
        
        return res
    
sol=Solution()
arr=[7, 7, 7, 7, 7, 7, -9, -9, -9, 0]
print(sol.Learning(arr, len(arr)))
