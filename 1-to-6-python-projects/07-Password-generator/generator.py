import random
import string

def generate_strong_password(length=12):
    """Generate a strong password that is simple yet secure."""
    if length < 6:
        print("Password length should be at least 6 characters for better security.")
        return None
    
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    print("Welcome to the Password Generator!")
    try:
        num_passwords = int(input("How many passwords do you want to generate? "))
        length = int(input("Enter desired password length (minimum 6): "))
        
        for i in range(num_passwords):
            password = generate_strong_password(length)
            if password:
                print(f"Password {i+1}: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
