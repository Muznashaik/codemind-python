import math
x=int(input())
temp=x
k=1
s=0
while x>0:
    d=x%10
    x=x//10
    k=math.factorial(d)
    s=s+k
if(s==temp):
    print("The number %d is a strong number" %temp)
else:
    print("The number %d is not a strong number" %temp)