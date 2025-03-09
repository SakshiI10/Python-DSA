def GCD(m, n):
    gcd=1
    for i in range(1, min(m, n)+1):
        if (m%i ==0 and n%i==0):
            gcd=i
            
    return gcd

m=12
n=9
print(GCD(m, n))
