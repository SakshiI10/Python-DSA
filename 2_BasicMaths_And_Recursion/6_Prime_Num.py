def prime_num(n):
    count=0
    for i in range(1, int(n**0.5)+1):
        if (n%i==0):
            count += 1
            if n//i != i:
                count += 1
    if count==2:
        print("Yes")
    else:
        print("No")

m=4
n=5
prime_num(m)
prime_num(n)
