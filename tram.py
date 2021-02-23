count=0
max=0
n=int(input())
for i in range(0,n):
    a,b=map(int,input().split())
    count=count-a
    count=count+b
    if(max<=count):
        max=count
print(max)