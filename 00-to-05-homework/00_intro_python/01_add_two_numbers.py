def add_number():
    print("Let's add some numbers!")
    num1: str = input("enter a number: ")
    num1 : int = int(num1)
    num2: str = input("enter second number: ")
    num2 : int = int(num2)
    total: int = num1 + num2
    print(f"The total is {total}")
add_number()