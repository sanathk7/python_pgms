def abs(x):
    if '.' in x:
        x=float(x)
    else:
        x=int(x)
    if x>=0:
        return x
        
    else:
        return -x

        
number=input('enter a number: ')
print(abs(number))

