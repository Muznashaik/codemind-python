x=int(input())
l=list(map(int,input().split()))
k=set(l)
s=0
for i in k:
    z=l.count(i)
    if z>s:
        s=z
        h=i
print(h)