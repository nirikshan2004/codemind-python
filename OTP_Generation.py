s=input()
b=[]
a=list(s)
for i in range(len(a)):
    if int(a[i])%2!=0:
        b.append(int(a[i])**2)
for i in b:
    print(i,end='')