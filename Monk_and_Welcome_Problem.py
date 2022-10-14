x=int(input())
l=list(map(int,input().split()))
n=list(map(int,input().split()))
z=[]
for i in range(len(l)):
    for j in range(len(n)):
        if i==j:
            k=l[i]+n[j]
            z.append(k)
print(*z)