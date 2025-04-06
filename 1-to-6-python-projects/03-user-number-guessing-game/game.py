import random

print("""Welcome To User Number Guessing Game!!!
      Guess a Number Between 1 to 20""")

def game():

 user = int(input("Enter A Number:"))

 if user != random.randint(1,20):
    print("not a correct number")

 else:
    print("yay! you guess correct number")

game()
