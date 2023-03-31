def fibonacci(x):
    first = 0
    second = 1
    print(first)
    print(second)
    count=x
    while count>0:
        third = first + second
        first, second = second, third
        count-=1
        print(third)
    

n = int(input("Enter nth term: "))
fibonacci(n)

