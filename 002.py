money=int(input("输入利润:"))
wan=10000
ProPercent=[0,0.1,0.075,0.05,0.03,0.015,0.1]
ProMoney=[0,10,20,40,60,100]
profit=0
for i in range(1,len(ProMoney)):
    if money>=ProMoney[i]:
        profit=(ProMoney[i]-ProMoney[i-1])*ProPercent[i]+profit
    else:
        profit=(money-ProMoney[i-1])*ProPercent[i]+profit
        break
print(int(profit*10000))