x=int(input())
for i in range(x):
    k=[]
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    s=list(map(int,input().split()))
    for i in l:
        k.append(i)
    for i in s:
        k.append(i)
    print(*(sorted(k)))