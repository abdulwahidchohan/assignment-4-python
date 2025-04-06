import random

def guess_my_number():

    secret_number = random.randint(1,99)

    user_guess = int(input("Enter A number!!!"))

    while user_guess != secret_number:
       if user_guess < secret_number:
           print("your guessed is too low")
       else:
           print("Your guess is too high")   

        
       user_guess = int(input("ENter a new guess: "))
        
    print("WOW, Congratulations 🥳 you guessed right number, the number was " + str(secret_number))   

guess_my_number()   