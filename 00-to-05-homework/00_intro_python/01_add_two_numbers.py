def add_number():
    print("Add some numbers!")
    num1: str = input("Enter a number => ")
    num1 : int = int(num1)
    num2: str = input("enter second number => ")
    num2 : int = int(num2)
    total: int = num1 + num2
    print(f"The total is {total}")
add_number()