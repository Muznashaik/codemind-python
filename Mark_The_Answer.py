a,b=map(int,input().split())
l=list(map(int,input().split()))
c=0
k=0
for i in l:
    if k==2:
        break
    if b>=i:
        c+=1
    else:
        k+=1
print(c)