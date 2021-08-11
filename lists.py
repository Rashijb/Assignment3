#lists
list_num=[10,9,8,7,6,5,4,3,2,1,0]
print(list_num)
list_mixed=['Hope',2021,'is','great']
print(list_mixed)

#indexing and slicing in list
print(list_mixed[2])
print(list_mixed[2:5])
print(list_num[6:10])

#step in list
print(list_num[2::2])

#concatenation
list_1=['my','name',]
list_2=['is','peace']
list_3= list_1 + list_2
print(list_1)
print(list_2)
print(list_3)

#lists are mutable unlike strings
list_1[0] = 'My'
print(list_1)

#adding elements to the list
list_4=[6,9,3,1]
print(list_4)
list_4.append(11)
print(list_4)
print(list_4.pop())
print(list_4)
print(list_4.pop(2))
print(list_4)

#sorting the list
list_nmb=[12,45,21,35,77,33,99]
print(list_nmb)
list_nmb.sort()
print(list_nmb)

#lenght of the list
print(len(list_nmb))

#reverse
list_nmb.reverse()
print(list_nmb)


