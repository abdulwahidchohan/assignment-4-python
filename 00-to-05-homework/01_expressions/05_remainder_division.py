def division():
    q1 = int(input("Please enter an integer to be divided: "))
    q2 = int(input("Please enter an integer to divide by:"))

    division = int (q1 / q2 )
    remainder  = int (q1 % q2 )
    
    print("*" * 55)
    result = print(f"The result of this division is {division} with a remainder of {remainder}")
    print("*" * 55)
    
division()
