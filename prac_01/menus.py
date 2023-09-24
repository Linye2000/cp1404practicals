name = input("Enter name: ")
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")
choice = input(">>> ").upper()

while choice != 'Q':
    if choice == 'H':
        print("Hello", name)
    elif choice == 'G':
        print("Goodbye", name)
    else:
        print("nothing ")

    # Display the menu again
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    choice = input(">>> ").upper()

    print("Finish.")
