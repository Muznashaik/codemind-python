x=int(input())
i=x
y=x
while True:
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            break
    else:
        g=i
        break
    i+=1
while True:
    for j in range(2,int(y**0.5)+1):
        if y%j==0:
            break
    else:
        h=y
        break
    y-=1
s=abs(x-g)
t=abs(x-h)
if s>=t:
    print(t)
else:
    print(s)
