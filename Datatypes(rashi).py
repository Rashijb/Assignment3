# the print command
print("Assignment3")
# To perform arithmetic operations
print("2 + 2 =", 2 + 2)
print("20 - 5 =", 20 - 5)
print("20 / 5 =", 20 / 5)
print("20 * 5 =", 20 * 5)

# modula operator (gives remainder)
print("20 % 2 =", 20 % 2)
print("23 % 2 =", 23 % 2)

# for exponents
print("11 ** 2 =", 11 ** 2)

# to check order of preferance (bodmas applied)
print("2 + 2 * 15 - 5  =", 2 + 2 * 15 - 5)

# when you want to give prefernce to set of functions of choice then use brackets
print("(2 + 2) * (15 - 5) =", (2 + 2) * (15 - 5))

# variables to perform operations
a = 22
v = 33
sum = a + v
print("a =", a)
print("v =", v)
print("a + v = ", sum)
my_name = "rashi"
print(my_name)

# to check the datatype of variables
print (type(my_name))
print (type(a))

#example performing logic using variable names
Total_marks = 200
marks = 165
percentage = ( marks / Total_marks ) * 100
print ( "marks =", marks)
print ( "Total marks =", Total_marks)
print ( "Percentage =", percentage)

#strings
planet = "mars"
star = 'brunomars'
print ( planet,star)

#replacing a letter in a string
print ("name = ", planet)
#slicing
print (planet[1:4])
print("c" + planet[1:4])
new="c" + planet[1:3] + "d"
print("new=",new)

yes="hello from the other side"
print(yes)
print(yes [0:5])
print(yes [0:19:3])
#indexing
new_1=new[0]
print(new_1)

#string concatination
wow=new + planet
print(wow)

#to repeat a string multiple times
group= planet * 10
print(group)

#string methods
#to print in upper/lower case
print(new)
print(new.upper())
cool="HOUSE"
print(cool)
print(cool.lower())

#to split a sentece
sentence="see you in 2050"
print(sentence)
print(sentence.split())
print(sentence.split('0'))

#print formatting
print(sentence)
year="2051"
print(f'see you in {year}')


