def add_copies(my_list, data):
    for i in range(3):
     my_list.append(data)

def copy_message():
    message = input("Enter Message to Copy: ")    
    my_list = []
    print("List Before: ", my_list)
    add_copies(my_list,message)
    print("List After:", my_list)

copy_message()  