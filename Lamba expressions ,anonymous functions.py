def addition(n):
    return n*n

numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print("Numbers",numbers)
print("Square of the numbers",list(result))



