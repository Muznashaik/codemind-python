x=input()
k=list(x)
c=0
for i in range(len(k)):
    s=k.count(k[i])
    if s==1:
        c+=1
        print(i)
        break
if(c==0):
    print("-1")