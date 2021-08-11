#first list of cups
list_cups = ['','0','']
from random import shuffle
shuffle(list_cups)

def shuffle_list(list_cups):
    return shuffle(list_cups)
result = shuffle_list(list_cups)

#ask for guess
def get_guess():
    guess = ''
    guess = input("Pic the cup 0,1,2")
    print(guess)
    return int(guess)

guess = get_guess()
#now to check if the guess is right or wrong
def check_guess(list_cups,guess):
 if list_cups[guess] == '0':
     print("Correct guess")
 else:
     print("Wrong guess")
     print(list_cups)

check_guess(list_cups,guess)

