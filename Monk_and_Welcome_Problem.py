
n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
e=[]
for i in range(len(l1)):
    e.append(l1[i]+l2[i])
print(*e)