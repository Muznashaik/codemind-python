x,y,z=map(int,input().split())
ci=x*pow((1+y/100),z)
print("{:.2f}".format(ci))