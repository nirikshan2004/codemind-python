n=int(input())
while n:
    s=int(input())
    l=list(map(int,input().split()))
    c=0
    s=set(l)
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if l[i]+l[j] in s:
                c=c+1
    if c==0:
        print(-1)
    else:
        print(c)