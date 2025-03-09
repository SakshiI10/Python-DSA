def armstrong_num(n):
    dup=n
    sum=0
    len_digit=len(str(n))

    while(n>0):
        num=n%10
        sum += num ** len_digit
        n = n//10
    
    if (sum==dup):
        print("Yes")
    else:
        print("No")

n=371
armstrong_num(n)
m=1634
armstrong_num(m)
