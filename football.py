football=(input())
a=b=c=0
for i in range(len(football)):
    if (football[i]=='1'):
        a+=1
        b=0
    else:
        b+=1
        a=0
    if (a>=7 or b>=7):
        c=1
if c==1:
    print("YES")
else:
    print("NO")
    


