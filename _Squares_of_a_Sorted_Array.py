n=int(input())
a=list(map(int,input().split()))
c=[]
for i in a:
    c.append(i*i)
c.sort()
print(*c)