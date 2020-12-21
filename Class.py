
#class and object
class Calculator:
  def __init__(self,num1,num2):
    self.num1=num1
    self.num2=num2

  def add(self,buffer):
    return self.num1+self.num1+buffer

calculator_object1=Calculator(5,6)

calculator_object2=Calculator(10,6)

print(calculator_object1.add(10))
print(calculator_object2.add(10))

print(Calculator.add(calculator_object1,10))

# MAJIC METHODS - if len and getitem implemented then
#the object is iterable

#__init__  like constructor automatically called
#__len__ to get lenth of some property
#__getitem__ to get a pariticular item from property
#__repr__ (retrun a formatter)for debugger to give info an object
#__str__ (retrun a formatter)to directly print the object as string
#__doc__ will print the command above the method which are in 3 single quotes
