

#while
am_i_still_learning = "yes"
while am_i_still_learning == "yes" :
  print("still learning")
  am_i_still_learning = input("are you still learning")


#for

elements = [0,1,2,3,4,5]

for index in elements :
  print(f"elements {index}")

for index in range(10) :
  print(f"elements {index}")

for index in range(11 , 20) :
  print(f"elements {index}")

# for with list and tuples

name_age = [("vinoth",23),("others",45)]

for name, age in name_age :
  print(f"name {name} age {age}")

# dict

name_age_dic = {"vinoth":25, "ram":32}
for name, age in name_age_dic.items():
  print(f"name {name} age {age}")


#for with else

my_list = [1,2,3,4,5,6,7]

for index in my_list:
  if index==10 :
    print("got 6")
else:
  print("list don't have index")
