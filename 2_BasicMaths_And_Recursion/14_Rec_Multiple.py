# The Fibonacci problem.

def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    last=fibonacci(n-1)
    slast=fibonacci(n-2)
    return last+slast

n=5
print(fibonacci(n))
