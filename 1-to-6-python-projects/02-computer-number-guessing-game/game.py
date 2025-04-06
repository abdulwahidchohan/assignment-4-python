import random


def computer_guessing(x):
    print("""welcome to computer number guessing game🎊
          think of number betwwen 1 to 30 💭🤔""")
    low = 1
    high = x
    feedback = ""

    while feedback != "c":
      if low == high:
         guess = low
      else:
         guess = random.randint(low, high)

      feedback = input(f"Is {guess} too high (H), too low (L) or correct (C)").lower()  

      if feedback == 'h':
       high = guess - 1
      elif feedback == 'l':
        low = guess + 1
        
    
    
    print(f"yay! the computer guessed your number, {guess} correctly🥳")

computer_guessing(30)            
