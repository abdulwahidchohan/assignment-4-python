def read_phone_numbers():
    phonebook = {}

    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number

    return phonebook

def print_phonebook(phonebook):
    for name, number in phonebook.items():
        print(f"{name}  -> {number}")   

def lookup_numbers(phonebook):
   while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name in phonebook:
            print(phonebook[name])  # Print the number
        else:
            print(name + " is not in the phonebook")


def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)     
    lookup_numbers(phonebook)                   

main()   