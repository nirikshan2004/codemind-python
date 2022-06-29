n=int(input( ))
sq=n*n
c=0
while(sq!=0):
    d=sq%10;
    sq=sq//10;
    c=c+d;
if(c==n):
    print("Neon Number");
else:
    print("Not Neon Number")
