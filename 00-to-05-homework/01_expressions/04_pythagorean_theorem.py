import math

def pythagorean_theorem():
    ab : float = float(input("Enter the length of AB: "))
    ac : float = float(input("Enter the length of AC: "))

    bc : float = math.sqrt(ab**2 + ac**2)
    print("The length of BC (the hypotenuse is: " + str(bc))

pythagorean_theorem()