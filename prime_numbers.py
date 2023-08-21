''' THIS PROGROM FOR TO FIND PRIME NUMBERS BETWEEN 2 NUMBERS'''
lower=0 
end=100
for i in range(lower,end+1):
    if i>1:
        for j in range(2,i):
            if (i%j)==0:break
        
            
       
        else:print(i,end=" ") 
''' THIS PROGRAM FOR TO FIND PRIME NUMBERS IN A LIST ,ALSO IT MAKE SEPARATE LIST FOR NON PRIME NUMBERS'''
import math
def prime_(n):
    if n<=1:
        return False
    if n<=3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5,int(math.sqrt(n))+1,6):
        if n%i==0 or n%(i+2)==0:
            return False
            
    return True
    
            
            
def prime_list(numbers,size):
    prime=[]
    non_prime=[]
    
    for i in range(size):
        if prime_(numbers[i]):
            prime.append(numbers[i])
        else:
            non_prime.append(numbers[i])
    return '{}\n{}'.format(prime,non_prime)
            
            
user=[2,10,18,5,9,3]
lengt=len(user)
prime_list(user,lengt)
