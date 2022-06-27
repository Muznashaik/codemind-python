n=int(input())
k=0
if(n<=9):
    if(n==1):
        print(True)
    else:
        print(False)
else:
    while n:
        d=n%10
        n=n//10
        k=k+d*d
        if k<=9 and n==0:
            if(k==1):
                print(True)
            else:
                print(False)
        elif(k>9 and n==0):
            n=k
            k=0
        