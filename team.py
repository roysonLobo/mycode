n=int(input())
count=0
for i in range(n):
    a, b, c=(map(int,input().split()))
    sum=a+b+c
    if sum >=2:
        count+=1
    
    #print(type(team),team)
print(count)