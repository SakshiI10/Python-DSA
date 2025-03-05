def count(n):
    count=0
    while(n>0):
        rem=n%10
        count += 1
        n=n//10
    return count

n=9987
print(count(n))
