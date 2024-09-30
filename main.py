import random

min_val=0
max_val=10
secret_number=random.randint(min_val, max_val)
guess=None

print("Welcome in guessing game!")
print("I think about a number from "+str(min_val)+" to "+str(max_val)+ ", can you guess it?")
print("You can end the game by giving up, press -1 to quit.")
print(secret_number)

while(True):
    try:
        guess=int(input("Your guess is: "))
        if(guess==-1):
            print("Too bad, you haven't guessed it :(")
            break
        if(guess==secret_number):
            print("Hooray, you found it! Our secret number was: "+str(secret_number))
            break
        else:
            print("Try again!")
    except ValueError:
     print("Please enter a integer!")



