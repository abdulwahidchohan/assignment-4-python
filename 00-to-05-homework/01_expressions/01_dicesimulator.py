import random 

dice_num = 6

def diceroll():
    dice1 : int = random.randint(1,dice_num)
    dice2 : int = random.randint(1,dice_num)

    print(f"rolled: {dice1}  {dice2}")

print("Rolling two dice three times:")
for dice in range(3):
    diceroll()