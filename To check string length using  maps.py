list_string = ['RM','V','Jimin','JK','Suga','Jhope','Jin']

def even_check(string):
    if len(string) %2 == 0:
        return "Even"
    else:
        return "Odd"

even_check('Jaebom')

string_count = list(map(even_check,list_string))
print(string_count)