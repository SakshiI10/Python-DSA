# Pascal Triangle:
#      1
#     1 1
#    1 2 1
#   1 3 3 1
#  1 4 6 4 1
# 1 5 10 10 5 1 

#  Three types of question
# 1. Given r and c, give the number at that place.
def nCr(n, r):
    res = 1
    for i in range(r - 1):  # Compute C(n-1, r-1)
        res = res * (n - 1 - i) // (i + 1)
    return res
print(nCr(4, 3))
print(nCr(5, 3))

# 2. Print nth row of pascal triangle
def nCr2(n):
    res2=[1]
    ans=1
    for i in range(1, n):
        ans=ans*(n-i)//i
        res2.append(ans)
    return res2
print(nCr2(4))
print(nCr2(5))

# 3. Given n, print the triangle
def pascal_triangle(r):
    res3 = []  
    for n in range(r):  
        row = [1]  
        ans = 1
        for i in range(1, n+1):  
            ans = ans * (n - i + 1) // i  
            row.append(ans)
        res3.append(row)
    for row in res3:
        print(" ".join(map(str, row)).center(r * 3)) 

pascal_triangle(5)
