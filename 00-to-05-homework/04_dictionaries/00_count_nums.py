def count_numbers():
    count_dict = {}

    while True:
        num = input("Enter a number (or 'q' to quit)")
        if num.lower() == "q":
            break
        if num.isdigit():
           num = int(num)
           count_dict[num] = count_dict.get(num, 0) + 1
        else:
            print("Please enter a valid number or 'q' to quit.")  

    for number, count in count_dict.items():
        print(f"{number} appears {count} times.")    

count_numbers()