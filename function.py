
def add(x, y=3):
  return x+y

print(add(6,2))
print(add(2))

#lambda

result = lambda x,y :x+y
print(result(2,4)) 

# first class functions

add_function =add

print(add_function(4,5))

# pass function as arg (higher order fucntion)

def supper_function(sub):
  print("in supper")
  sub()
  print("in end of supper")

def sub():
  print("in sub")

supper_function(sub)
