x=int(input())
l=list(map(int,input().split()))
l=set(l)
l=sorted(l)
k=len(l)
if k>=3:
    print(l[-3])
else:
    print(l[-1])
