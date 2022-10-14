n=int(input())
y=[]
while n>0:
    r=n%10
    y.append(r)
    n=n//10
a=[]
for i in y:
    if i not in a:
        a.append(i)
if(a==y):
    print('Unique Number')
else:
    print('Not Unique Number')