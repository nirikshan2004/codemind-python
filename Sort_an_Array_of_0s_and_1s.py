n=int(input())
c=0
a=list(map(int,input().split()))
for i in a:
    if(i==0):
        print(0,end=" ")
    else:
        c+=1
for i in range(c):
    print(1,end=" ")