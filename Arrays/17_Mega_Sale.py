'''
Mr. Geek is a greedy seller. He has a stock of N laptops which comprises of both useful and useless laptops. Now, he wants to organize a sale to clear his stock of useless laptops. The prices of N laptops are Ai each consisting of positive and negative integers (-ve denoting useless laptops). In a day, he can sell atmost M laptops. Mr. Geek being a greedy seller want to earn maximum profit out of this sale. So, help him maximizing his profit by selling useless laptops.

Input:N=4, M=3, A[] = {-6, 0, 35, 4}
Output: 6'''

def maxProfit(a, n, m):
    a.sort()
    sum = 0
    
    for i in range(n):
        if a[i] < 0 and m > 0:
            sum += a[i]
            m -= 1
        elif m == 0:
            break
    
    return -sum

N = 4
M = 3
A = [-6, 0, 35, 4]
print(maxProfit(A, N, M))  # Output: 6
