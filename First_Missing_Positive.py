x=int(input())
l=list(map(int,input().split()))
for i in range(1,10000):
    if i not in l:
        print(i)
        break