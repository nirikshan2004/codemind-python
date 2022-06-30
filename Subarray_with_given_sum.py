T=int(input())

for i in range(T):

    n,k=map(int,input().split())

    li=[int(j) for j in input().split()]

    l=0

    x=0

    for r in range(len(li)):

        x=x+li[r]

        while(x>k and l<=r):

            x=x-li[l]

            l+=1

        if(x==k):

            print(l+1,r+1)

            break

        elif(r==len(li)-1):

            print("-1")
