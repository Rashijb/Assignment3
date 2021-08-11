#range increment
for a in range(0,10,2):
    print("List =",a)

#slicing
list1=[11,22,33,44,55,66]
print("\n List1=",list1)
index = 0
for item in list1[0::2]:
        index = index + 2
        print("at index", index, "element =", item)