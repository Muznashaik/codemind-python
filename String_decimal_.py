x=int(input())
c=0
for i in range(x):
    k=input()
    for i in k:
        if i in "1234567890":
            c+=1
    if len(k)==c:
        print("True")
    else:
        print("False")
    c=0