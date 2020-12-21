# inheritance and decorator

class Customer:

  def __init__(self,name,age):
    self.name=name
    self.age=age

  #decorator
  @property
  def get(self):
    return f"name {self.name} age {self.age}"

class StaffCustomer(Customer):

  def __init__(self,name,age,staffid):
    super().__init__(name,age)
    self.staffid=staffid
 

  def __repr__(self):
    return f"id is {self.staffid}"

  @classmethod
  def myname(cls):
    print(f"my name is {cls.__name__}")

  @staticmethod
  def hi():
    print("static method called")

staff_customer_object=StaffCustomer("vinoth",25,44)
print(staff_customer_object.get) # becuase of decorator we don't have to () for get
print(staff_customer_object)

staff_customer_object.myname()
StaffCustomer.hi()
