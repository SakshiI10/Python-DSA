def print_divisors(n):
    for i in range(1, n+1): #start from 1, to avoid 0
        if (n % i==0):
            print(i)

n=36
print_divisors(n)