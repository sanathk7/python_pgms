lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
greeting_doubled=list(map(lambda y:2*y,lst))
print(greeting_doubled)


or

def transform(x):
  return 2*x
lst= [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
greeting_doubled=list(map(transform,lst))
print(greeting_doubled)                      
