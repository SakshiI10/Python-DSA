# Concept: gcd(m, n)=gcd(m-n, n) or gcd(m, n)=gcd(m%n, n)
# id (0, x): if one of them is 0 then, another one is the gcd

def euclidean_algo(m, n):
    while(m>0 and n>0):
        if(m>n):
            m=m%n
        else:
            n=n%m
    if m==0:
        return n
    else:
        return m

m=12
n=9
print(euclidean_algo(m, n))
