a=input('please input:')
countstr=0
countnumber=0
countspace=0
cother=0
for c in a:
    if c.isalpha():#中英文字符
        countstr+=1
    elif c.isdigit():#数字
        countnumber+=1
    elif c.isspace():#空格
        countspace+=1
    else:
        cother+=1
print('中英文字母',countstr)
print('空格',countspace)
print('数字',countnumber)
print('其他',cother)