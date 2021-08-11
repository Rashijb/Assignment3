#combining two lists
list_1=['a','b','c','d']
print("Mylist 1 =",list_1)
list_2=[1,2,3,4]
print("Mylist 2 =",list_2)
for item in zip(list_1,list_2):
    print (item)
else: print('Okay')
list_3=[11,22,33,44]
for a,b,c in zip(list_1,list_2,list_3):
    print(a,b,c)
    print(b)


