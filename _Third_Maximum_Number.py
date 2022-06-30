n=int(input())
l=list(map(int,input().split()))
s=list(set(l))
s.sort(reverse=True)
if len(s)>=3:
    print(s[2])
else:
    print(max(s))
