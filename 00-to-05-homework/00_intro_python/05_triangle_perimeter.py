def perimeter_triangle():
    print( "perimeter of the triangle")
    print("*" * 30)
    side1: float = float(input("What is the length of side 1? "))
    side2: float = float(input("What is the length of side 2? "))
    side3: float = float(input("What is the length of side 3? "))

    print(f"The perimeter of triangle is "  + str(side1 + side2 + side3))
perimeter_triangle()