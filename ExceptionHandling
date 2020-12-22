#exception handling

class Customer:
  def __init__(self,name,age):
    self.name=name
    self.age=age


  def throw_error(self):
    raise NotImplementedError("not implemented")

  def throw_custom_error(self):
    raise MyCustomError("customer error not implemented",500)

class MyCustomError(TypeError):
  def __init__(self,message,code):
    super().__init__(f" {message} {code}")
    self.code=code

  


customer_object=Customer("vinoth",25)
#print(customer_object.throw_error())
print(customer_object.throw_custom_error())





