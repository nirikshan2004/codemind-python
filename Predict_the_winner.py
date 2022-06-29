
n=int(input())
x=0
y=0
a=list(map(int,input().split()))
for i in range(n):
    if(i%2==0):
        x=x+a[i]
    else:
        y=y+a[i]
if (x-y)%4==0:
    print("X")
else:
    print("Y")