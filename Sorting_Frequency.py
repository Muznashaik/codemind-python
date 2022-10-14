x=int(input())
l=list(map(int,input().split()))
k=set(l)
k=list(k)
z=[]
m=[]
n=[]
h=[]
w=[]
for i in k:
    j=l.count(i)
    if j==1:
        n.append(i)
    else:
        z.append(i)
        h.append(j)
for i in range(len(z)):
    r=max(h)
    p=h.index(r)
    w.append(z[p])
    h[p]=-1
for i in n:
    w.append(i)
for t in w:
    print(t,end=" ")