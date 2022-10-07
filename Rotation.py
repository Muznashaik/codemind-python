x=int(input())
for i in range(x):
    a,k=map(int,input().split())
    l=list(map(int,input().split()))
    for i in range(k):
        f=l[a-1]
        l.remove(f)
        l=l[::-1]
        l.append(f)
        l=l[::-1]
    print(*l)