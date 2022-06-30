
n=int(input( ))
m=0
while(n!=0):
    d=n%10;
    n=n//10
    if(m<d):
        m=d;
print(m)