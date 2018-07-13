counti=0
for i in range(101,201):
    leap = 1
    for j in range(2,i):
        if(i%j==0):
            leap=0
            break
    if(leap==1):
        print(i)
        counti+=1
print('共有:',counti)
