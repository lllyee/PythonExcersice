a,b=input('input number and times:').split()
a=int(a)
b=int(b)
asum=a
c=str(a)
for i in range(1,b):
    a=str(a)
    a=a+c
    a=int(a)
    asum=a+asum
print(asum)

