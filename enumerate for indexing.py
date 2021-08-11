str1="euphoria"
print("Message=",str1)
index=0
for char in str1:
    print(char,"Index is",index)
    index=index+1
else:
    print("done")

    #or

for char in enumerate(str1):
    print(char)




