def print_divisors(n):
    for i in range(1, n+1): #start from 1, to avoid 0
        if (n % i==0):
            print(i)

result=[]
def print_divisors2(n):
    for i in range(1, int(n**0.5)+1):
        if (n%i==0):
            result.append(i)
            if n//i != i:
                result.append(n//i)
    result.sort()
    print(result)

n=36
print_divisors(n)
print_divisors2(n)
