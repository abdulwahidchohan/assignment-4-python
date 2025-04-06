def height_for_ride():
    
    minimum_height = 50

    user_height = int(input("How tall are you? "))

    if (user_height >= minimum_height):
        print("You're tall enough to ride! Enjoy your ride 🥳")
    else:
        print("You're not tall enough to ride, but maybe next year!")    

height_for_ride()        