
n=int(input())
c=0
for i in range(1,n+1):
    for j in range(2,n):
        for k in range(2,n):
            if(i%k!=0 and i%j!=0):
                if(k*j==n):
                    p=j
                    q=k
                    c+=1
                    break
if(c==0):
    print("-1")
else:
    print(q,p)
