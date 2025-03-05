def reverse_num(n):
    rev_num=0
    dup=n
    while(n>0):
        num=n%10
        rev_num=(rev_num*10)+num
        n=n//10

    if(rev_num==dup):
        print("true")
    else:
        print("false")

n=9987
reverse_num(n)
m=303
reverse_num(m)