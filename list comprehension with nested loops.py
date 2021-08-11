# nested list
for a in [3, 4, 5]:
    for b in [9, 8, 7]:
        print(a, "*", b, "=", a * b)

# or
nestd_list = [x + y for x in [1, 2, 3] for y in [7, 8, 9]]
print("The nested list=", nestd_list)

nestd_list.insert(0, 100)
print(nestd_list)

