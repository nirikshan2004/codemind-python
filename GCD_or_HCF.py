a,b=map(int,input().split())
res=0
while(b):
    res=a%b
    a=b
    b=res
print(a)