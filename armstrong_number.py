''' ARMSTRONG NUMBER EXAMPLE 9,153
9=9^1
153=1^3+5^3+3^3
1634=1^4+6^4+3^4+4^4


'''
num=20
copy_num=str(num)
length=len(copy_num)
check=0
for i in range(0,length):
    
    check+=int(copy_num[i])**length
if check==num:print("{} is a armstrong number".format(num))
else:print("{} is not a armstrong number".format(num))


''' ARMSTRONG NUMBERS BETWEEN NUMBERS'''
arm=[]
till=10000
numbers=range(0,till)
for n in numbers:
    num=n
    copy_num=str(num)
    length=len(copy_num)
    check=0
    for i in range(0,length):
    
        check+=int(copy_num[i])**length
    if check==num:arm.append(n)
    
print("this are armstrong numbers between 0 to {}\n{}".format(till,arm))    
    

