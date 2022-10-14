x=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(len(l)):
    for j in range(i,len(l)):
        if l[i]<l[j]:
            l[i]=l[j]
l.append("-1")
for i in range(1,len(l)):
    print(l[i],end=" ")