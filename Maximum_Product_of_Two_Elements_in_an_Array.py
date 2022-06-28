l=list(map(int,input().split()))
s=sorted(l)
k=[]
h=1
s=s[::-1]
for i in range(0,2):
    k.append(s[i]-1)
for i in k:
    h=h*i
print(h)