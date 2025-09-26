def print_menu():
    print("\nChoose an operation:")
    print("1. insert i e   -> Insert integer e at position i")
    print("2. print        -> Print the list")
    print("3. remove e     -> Delete the first occurrence of integer e")
    print("4. append e     -> Insert integer e at the end")
    print("5. sort         -> Sort the list")
    print("6. pop          -> Pop the last element")
    print("7. reverse      -> Reverse the list")
    print("8. exit         -> Quit the program")


if __name__ == '__main__':
    my_list = []
    N = int(input("Enter the number of operations: "))

    for _ in range(N):
        print_menu()
        command = input("\nEnter command:(Eg: insert 0(value) 5(position)) ").split()
        operation = command[0]
        args = command[1:]

        if operation == "insert":
            i, e = map(int, args)
            my_list.insert(i, e)
        elif operation == "print":
            print("Current list:", my_list)
        elif operation == "remove":
            e = int(args[0])
            if e in my_list:
                my_list.remove(e)
            else:
                print(f"{e} not found in list.")
        elif operation == "append":
            e = int(args[0])
            my_list.append(e)
        elif operation == "sort":
            my_list.sort()
        elif operation == "pop":
            if my_list:
                my_list.pop()
            else:
                print("List is empty, nothing to pop.")
        elif operation == "reverse":
            my_list.reverse()
        elif operation == "exit":
            print("Exiting early. Final list:", my_list)
            break
        else:
            print("Invalid command. Try again!")

    print("\nProgram finished. Final list:", my_list)
