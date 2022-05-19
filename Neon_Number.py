x=int(input())
z=x*x
s=0
while(z):
    v=z%10
    s=s+v
    z=z//10
if(s==x):
    print("Neon Number")
else:
    print("Not Neon Number")
