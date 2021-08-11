#for only even numbers
print("The even numbers btw 12 to 22 are")
for num in range (12,22):
    if num % 2==0:
        print(num)
#or
evn_list=[num for num in range(22,32) if num % 2 == 0]
print("The list of even number",evn_list)