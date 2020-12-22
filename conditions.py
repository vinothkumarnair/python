

#simple conditions

user_name = input("enter your name")

if user_name == "vinoth" :
  print("its me")
elif user_name == "kumar" :
  print("its me again")
else:
  print("others")

print("done compare")

#compare with list

my_name_list = ["vinoth","kumar","nair"]

name_to_check = input("enter your name")

if name_to_check in my_name_list :
  print("name found")
else:
  print("not found")
  
# to check whether instance is of type
#if not isinstance(car,Car):
  #raise TypeError("something")
