def reverse_num(n):
    rev_num=0
    while(n>0):
        num=n%10
        rev_num=(rev_num*10)+num
        n=n//10
    return rev_num

n=9987
print(reverse_num(n))