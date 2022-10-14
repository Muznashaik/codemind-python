a,b=map(int,input().split())
l=list(map(int,input().split()))
t=[]
for i in range(b):
    l.append(l[i])
    l[i]=-1
for i in l:
    if i==-1:
        pass
    else:
        t.append(i)
print(*t)