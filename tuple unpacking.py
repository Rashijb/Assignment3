# tuple unpacking
tup_nbr = (4, 5, 8, 9)
for item in tup_nbr:
    print(item)
list_tpl = [(4, 5), (8, 9)]
for item in list_tpl:
    print(item)

list1 = [(2, 3, 4), (9, 8, 7), (1, 5, 6)]
for item in list1:
    print(item)
else:
    print("list printed")

for a, b, c in list1:
    print(a)

# for loop for dictionary
dict_1 = {'bts': 2013, 'got7': 2014, 'bigbang': 2006}
print(dict_1)
for item in dict_1.items():
    print(item)
else:print("dict unpacked")
for x,y in dict_1.items():
    print(x)
    print(y)

#pass
print("practice of pass")
list2=[5,6,7,8,9]
print(list2)
for num in list2:
    pass
print(list2)

#continue
print("practice of continue")
list_2=[2,3,4,5]
print(list_2)
for num in list_2:
    if num == 2:
        continue
    print(num)

#break
print("practice of break")
list_3=[9,8,7,6,5]
print(list_3)
for num in list_3:
    if num == 6:
        break
    print(num)

print('outside the for loop')

#break in while loop
r=0
while(r<10):
    print(r)
    r=r+2

    s=10
    while(s>0):
        print(s)
        s=s-2

        



