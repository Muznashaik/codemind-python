x=int(input())
a=0
b=0
c=0
e=0
f=0
g=0
h=0
i=0
j=0
k=0
while x:
    d=x%10
    x=x//10
    if(d==1):
        a+=1
    if(d==2):
        b+=1
    if(d==3):
        c+=1
    if(d==4):
        e+=1
    if(d==5):
        f+=1
    if(d==6):
        g+=1
    if(d==7):
        h+=1
    if(d==8):
        i+=1
    if(d==9):
        j+=1
    if(d==0):
        k+=1
if(a>1 or b>1 or c>1 or e>1 or f>1 or g>1 or h>1 or i>1 or j>1 or k>1):
    print("Not Unique Number")
else:
    print("Unique Number")
        
        