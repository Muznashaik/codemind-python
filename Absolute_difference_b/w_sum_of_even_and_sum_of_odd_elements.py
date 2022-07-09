x=int(input())
l=list(map(int,input().split()))
s=0
k=0
for i in l:
    if i%2==0:
        k=k+i
    else:
        s=s+i
print(abs(s-k))