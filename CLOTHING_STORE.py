def function(arr,n):
    count=0
    arr.sort()
    i=0
    while i<(n-1):
        if(arr[i]==arr[i+1]):
            count+=1
            i=i+2
        else:
            i+=1
    return count
n=int(input())
arr=list(map(int,input().split()))
print(function(arr,n))