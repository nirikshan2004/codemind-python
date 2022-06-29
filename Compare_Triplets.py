x = list(map(int,input().split()))
y = list(map(int,input().split()))
a=0
b=0
for i in range(len(x)):
    if x[i]<y[i]:
        a+=1
    elif x[i]==y[i]:
        pass
    else:
        b+=1
print(b,end=" ")
print(a)