#list comprehension
#unique way to create a list
#alternative for creating a list with for loop and apppend method from typing import List, Any

msg="awaken"
list3=[]
for char in msg:
    list3.append(char)
print(list3)

#or

mymsg="sleepy"
list2=[char for char in mymsg ]
print("List2=",list2)

#another example
for num in range(1,5):
    num=num**2
    print(num)
print("another method")
sqrs=[num**2 for num in range(0,5)]
print(sqrs)


