import random
print("==================")
print(" GUESS MY NUMBER   ")
print(" By Russell        ")
print("==================")
print(" ")

name = input("what is your name? ")
the_number = random.randint(0,100)

guess = -1
print(" ")
print ("i'm thinking of an integer between 0 and 100")

while guess != the_number:

    guess_text = input("what is your guess?")
    guess =int(guess_text)
    if guess < the_number:
        print(f" sorry,{name} but your guess is to LOW. Try again")

    elif guess > the_number:
        print(f"sorry,{name} but your guess is to HIGH Try again")

    else:
        print(f"You guessed it! Congratulation, {name} ")