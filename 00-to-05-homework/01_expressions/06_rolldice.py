import random 

dice_num = 6

def diceroll():
    dice1 : int = random.randint(1,dice_num)
    dice2 : int = random.randint(1,dice_num)

    total : int = dice1 + dice2


    print("Dice have", dice_num, "sides each.")
    print("First die:", dice1)
    print("Second die:", dice2)
    print("Total of two dice:", total)

diceroll()