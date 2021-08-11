my_list = [12, 22, 33, 56, 78, 97]


def even_check(num):
    return num%2 == 0

def odd_check(num):
    return num%2 != 0
even_numbers=list(filter(even_check, my_list))
print(even_numbers)


filter_list=list(filter(odd_check,my_list))
print(filter_list)

#for lambda functions
square = lambda x : x * x
print(square(55))

sqr=list(map(lambda x : x**2,my_list))
print(sqr)