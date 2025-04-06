import random

def play():

    print("Welcome to Rock, Paper, Scissors!")
    print("Instructions:")
    print("- Type 'r' for Rock")
    print("- Type 'p' for Paper")
    print("- Type 's' for Scissors")

    user = input("Enter Your Choice").lower()
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'Its a tie'
    
    if is_win(user,computer):
        return 'You Won yay!!'
    
    return 'You Lost'
    

def is_win(player,opponent):

    if player =='r' and opponent == 's' or player == 's' and opponent == 'p' \
    or player == 'p' and opponent == 'r':
        return True

print(play())