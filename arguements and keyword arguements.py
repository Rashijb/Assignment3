# *args and *kwargs
# arguements and keyword arguments

def monthly_expenses(a,b,c,d):
    print("Monthly expenses of",a,b,c,d,"=",sum((a,b,c,d)))


monthly_expenses(10000,2000,1300,600)

def kw_example(**kwargs):
    if 'animal' in kwargs:
        print(kwargs['animal'])
    else:
        print('No living things in the list')

kw_example(plant = 'banyan', animal ='tiger')
kw_example(nonliving = 'stone', animal ='panda')

kwargs = { 'plant': 'banyan','animal':'Lion'}
print(kwargs['animal'])
print(kwargs['plant'])

