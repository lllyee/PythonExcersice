import math
counti=0
for i in range (100,1000):
    i=str(i)
    j=int(i[0])
    k=int(i[1])
    m=int(i[2])
    j=math.pow(j,3)
    k=math.pow(k,3)
    m=math.pow(m,3)
    if(int(i)==int((j+k+m))):
        counti+=1
print(counti)

