def armstrong_num(n):
    dup=n
    sum=0
    len_digit=len(str(n))
    while(n>0):
        rem=n%10
        sum += rem ** len_digit
        n=n//10
    if (sum==dup):
        print("Yes")
    else:
        print("No")

n=371
armstrong_num(n)
m=1634
armstrong_num(m)
