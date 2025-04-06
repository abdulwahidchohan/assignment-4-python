def main():
    num: int = 7
    num = substract_seven(num)
    print("This should be zero:", num)

def substract_seven(num):
    num = num - 7
    return num

main()