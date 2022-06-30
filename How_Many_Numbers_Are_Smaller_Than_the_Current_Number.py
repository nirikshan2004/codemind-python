

n=int(input())
l=list(map(int,input().split()))
s=[]
for i in range(n):
    c=0
    for j in range(n):
        if l[i]>l[j]:
            c+=1
    s.append(c)
print(*s)