x=int(input())
l=list(map(int,input().split()))
s=[]
k=[]
for i in l:
    if i>0:
        s.append(i)
    else:
        k.append(i)
print(*(s+k))
    