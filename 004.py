from datetime import  datetime
import time
i=str(input("请输入时间(xxxx-xx-xx):"))
j=datetime.strptime(i,"%Y-%m-%d")#str-datetime
result=datetime.timetuple(j)#datetime-datetuple
print(result.tm_yday)
