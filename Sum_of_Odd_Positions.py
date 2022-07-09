x=int(input())
l=list(map(int,input().split()))
k=0
for i in range(len(l)):
    if i%2==1:
        k=k+l[i]
print(k)
