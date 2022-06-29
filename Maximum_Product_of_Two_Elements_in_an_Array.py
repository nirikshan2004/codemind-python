m=0
a=list(map(int,input().split()))
for i in range(len(a)):
    for j in range(len(a)):
        if((a[i]-1)*(a[j]-1)>m and i!=j):
            m=(a[i]-1)*(a[j]-1)
print(m)