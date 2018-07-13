a=int(input('input number:'))
c=a
b=[]
while(c>1):
    for i in range(2, c+1):
        if c % i == 0:
            b.append(i)
            c =int(c / i)
            break
if len(b)==1:
    print('1*',a)
else:
    print(a,'=',end='')
    for i in range (len(b)-1):
        print(b[i],'*',end='')
    print(b[-1])








