def main():
    for i in range(10):
        if is_odd(i):
            print(f"{i} odd")
        else:
            print(f"{i} even")

def is_odd(value : int):
    remainder = value % 2
    return remainder == 1            

main()