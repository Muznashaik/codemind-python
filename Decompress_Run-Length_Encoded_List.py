x=int(input())
l=list(map(int,input().split()))
s=[]
for i in range(0,x-1,2):
    for j in range(l[i]):
        s.append(l[i+1])
print(*s)