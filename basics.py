

#basics
age = input("please enter your age")
month = int(age) * 12
half_age=int(age)/2
half_age_int=int(age)//2

print(f"half of the age in float is {str(half_age)}")
print(f"half of the age in int is {str(half_age_int)}")

print("total month "+ str(month))

print(f"total month {month}")

#list
name_list = ["vinoth","kumar"]
formated_name_list=", ".join(name_list)
name_list.append(2)
name_list.append(2.2)



print(name_list[0])

print(len(name_list))

print(f"formated name list {formated_name_list}")

print("int in the list : "+ str(name_list[2]))

name_list.remove(2.2)

print("len after remove"+ str(len(name_list)))

""" tuples - can't add or remove. it always produces a new tuples """

friends = ("vinoth","kumar")
friends = friends + ("john",)

print(friends)

#sets - no order maintained and and no duplicate allowed
# very easy to compare two sets
my_set = {"vinoth","kunar","jj"}
my_set.add("ram")
my_set.remove("jj")
print(my_set)

#dictionaries
# you can convert list to dictionarie by using dict(list)
my_friends_age = {"vinoth":25,"ram":45}
my_friends_age["newkey"]=77
print(my_friends_age["newkey"])
