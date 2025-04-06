def average(a: float, b: float):

    sum = a + b
    return sum / 2

def main():
    avg1 = average(0,10)
    avg2 = average(8,10)

    final = average(avg1, avg2)
    print("avg1", avg1)
    print("avg2", avg2)
    print("final", final)

main()    