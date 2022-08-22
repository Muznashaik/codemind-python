x=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
s=[]
for i in range(len(l)):
    if l[i]>=a and l[i]<=b:
        s.append(l[i])
    else:
        continue
k=len(s)
if k==0:
    print("-1")
else:
    print(min(s))