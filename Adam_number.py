n=int(input( ))
sq=n*n
rev=0
yrs=0
while(n!=0):
    d=n%10;
    n=n//10
    rev=rev*10+d
qs=rev*rev
while(qs!=0):
    s=qs%10
    qs=qs//10
    yrs=yrs*10+s
if(sq==yrs):
    print("True")
else:
    print("False")