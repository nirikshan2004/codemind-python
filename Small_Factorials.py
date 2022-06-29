T=int(input())
for i in range(T):
    N=int(input())
    count=1
    for i in range(N,0,-1):
        count=count*i
    print(count)