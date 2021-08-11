# syntax
def name_of_function():
    print('sunshine')
    print(2 + 2)


name_of_function()


# passing parameters or arguements to a method
def print_name(name):
    print(f'Hello {name}')


print_name('JaeBeom')
print_name('Jin')


def sum_num():
    x = input('Enter first number: ')
    y = input('Enter second number: ')
    sum = float(x) + float(y)
    print("sum=", sum)


sum_num()


def odev_num(nbr):
    if nbr % 2 == 0:
        print(nbr,'is even')
    else:
        print(nbr,'is odd')


odev_num(23)

#to check if even/odd number present in a list
def chk_num(list1):
    for num in list1:
        if num%2 > 0:
            return True
        else:
            return False


list1 = [2,3,4,5,6,7]
chk_num(list1)
