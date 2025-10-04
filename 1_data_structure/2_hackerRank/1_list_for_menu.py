# Start with an empty list
my_list = []

def print_menu():
    print("\nChoose an operation:")
    print("1. insert i e   -> Insert integer e at position i")
    print("2. print        -> Print the list")
    print("3. remove e     -> Delete the first occurrence of integer e")
    print("4. append e     -> Insert integer e at the end")
    print("5. sort         -> Sort the list")
    print("6. pop          -> Pop the last element")
    print("7. reverse      -> Reverse the list")

# Read how many commands we will get
N = int(input("number of commands needed:"))

# Run a loop N times to process each command
for _ in range(N):
    print_menu()
    
    command = input("enter your commands:").split()
    
    # The first word is always the command name
    if command[0] == "insert":
        # insert i e → command[1] = i, command[2] = e
         # Prompt the user to input the index and element separately
        index = int(input("Enter the index where you want to insert: "))
        element = int(input("Enter the element value you want to insert: "))
        my_list.insert(index, element)
        print(my_list)

    elif command[0] == "print":
        print(my_list)

    elif command[0] == "remove":
       element = int(input("Enter the element to remove: "))
       if element in my_list:
            my_list.remove(element)
       else:
            print(f"{element} not found in the list.")
        
    elif command[0] == "append":
        # append e → command[1] = e
        element = int(input("Enter the element to append: "))
        my_list.append(element)
        print(my_list)
        

    elif command[0] == "sort":
        if my_list:
            my_list.sort()
            print(my_list)    
        else:
            print("cannot sort the list because list is empty")

    elif command[0] == "pop":
        
        if my_list:  # Check if the list is not empty
         my_list.pop()
         print(my_list)  
        else:
         print("Cannot pop from an empty list.")


    elif command[0] == "reverse":
        if my_list:  # Check if the list is not empty
         my_list.reverse()
        print(my_list)  
    else:
        print("unknown command:",command[0])

    
