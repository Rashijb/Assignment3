#range funtion
print("Number from range 2 to 7")
for a in range(2,7):
      print(a)

print("Odd number from 1 to 10")
for b in range(1,10,2):
    print(b)
else:
    print(list(range(b)))

#range ennumerate
my_message='Feeling happy'
print(my_message)
for char in my_message:
    print(char)
else:
    print("Range enumeration")

#index count
name='gdragon'
print("name=",name)
print("index count of name =")
index_count=0
for cha in name:
    print(cha,"at index ",index_count)
    index_count=index_count+1
else: print("Index count")
