x=int(input())
for i in range(x):
    k=input()
    if k==k[::-1]:
        if len(k)%2==0:
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")