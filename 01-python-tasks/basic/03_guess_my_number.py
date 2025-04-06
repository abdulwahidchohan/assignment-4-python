import random

def main():
    secret_number : int = random.randint(1,50)
    print("Think of number between 1 to 50")

    guess = int(input("enter a number:"))

    while guess != secret_number:
        if guess < secret_number:
         print("your guess is too low")

        else:
         print("your guess is too high")

        print()
        guess = int(input("enter a number:"))

    print(f"congrats your guess number is :" + str(secret_number))

main()

