''' THIS PROGRAM IS USED TO FIND THE SUM OF n TH NUMBER
    EX: IF n=3 THEN OUTPUT WILL BE 3+2+1=6
    THIS IS USING RECURSION METHOD ,SO THAT USER CAM FIND UPTO 1000 TERM '''

def sum_of(n):
    if n==0:
        return 0 
    return n+sum_of(n-1)
    
print(sum_of(5))

''' THIS IS OTHER METHOD USING WHILE LOOP, HERE USER CAN FIND MORE THAN THE ABOVE PROGRAM
    '''
def sum_of_previous(n):
    sum_=0
    if n==0:
        return 0
    
    while n>=1:
        sum_+=n
        n-=1# -*- coding: latin-1 -*-
    return sum_
    
print(sum_of_previous(10000))
