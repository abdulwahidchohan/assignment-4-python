import random

words: list = ["Code", "Data", "App", "Server", "Cache", "Cookie", "python", "Database", "developer", "hangman"]

word = random.choice(words).lower()  
word_letters = set(word)
guessed_letters = set()
attempts = 6

print(f"Welcome to Hangman!\nLet's see if you can guess the word. It has {len(word)} letters.")
print(" ".join(["_" for _ in word]))

hangman_levels = [
    " 😵💀  ",   
    "  😨|   ",   
    "  😰/|  ",   
    "  🥶/|\\ ",  
    "  🫣/|\\ ",  
    "  😱/|\\ /  " 
]

while attempts > 0 and word_letters:
    guess = input("Guess a Letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a **single letter**, not a word or number!")
        continue  
    if guess in guessed_letters:
        print("❗ You already guessed that letter! Try again.")
        continue

    guessed_letters.add(guess)

    if guess in word_letters:
        word_letters.remove(guess)
        print("✅ Correct!")
    else:
        attempts -= 1
        print(f"❌ Wrong! You have {attempts} attempts left.")
        if attempts < 6:
            print(hangman_levels[5 - attempts])  

    display_word = [letter if letter in guessed_letters else "_" for letter in word]
    print(" ".join(display_word))

if not word_letters:
    print(f"🎉 Congratulations! You guessed the word: {word.upper()} 🏆")
else:
    print(f"💀 Game Over! The correct word was: {word.upper()}")
