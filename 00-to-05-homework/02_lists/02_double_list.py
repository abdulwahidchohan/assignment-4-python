def double_list():
    numbers: list = [1, 2, 3, 4]

    for i in range(len(numbers)):
        numbers[i] = numbers[i] * 2

    print(numbers)

double_list()