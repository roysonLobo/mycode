n=int(input())
str_int=str(n)
for i in str_int:
    a=str_int.count('4')
    b=str_int.count('7')
    c=a+b
if (c==4 or c==7) :
    print("YES")
else:
    print("NO")
