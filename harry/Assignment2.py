import string

def is_pangram(s):

# Returns True if the given string is a pangram, False otherwise.

    alphabet = string.ascii_lowercase
    for char in alphabet:
        if char not in s.lower():
            return False
    return True

def list_even_positions(numbers):

#Returns a list of the positions of the even numbers in the given list.

    return [i for i, x in enumerate(numbers) if x % 2 == 0]

def encrypt_string(input_string):
    # Use slicing to encrypt the input string
    reversed_string = input_string[::-1]
    encrypted_string = reversed_string + input_string
    return encrypted_string


def intersect_lists(list1, list2):
    """
    Returns a list of the elements that are present in both of the given lists.
    """
    return list(set(list1) & set(list2))

while True:
    # Display menu options
    print("*******************************", "\n")
    print("1 : Check Pangram String")
    print("2 : List of positions of even numbers")
    print("3 : Encrypt the String")
    print("4 : Intersection of lists")
    print("0 : Exit","\n")
    print("*******************************", "\n")
    # Read user choice
    choice = input("Enter your choice: ")

    if choice == "1":
        # Check if a string is a pangram
        s = input("Enter a string: ")
        if is_pangram(s):
            print("The string is a pangram.")
        else:
            print("The string is not a pangram.")

    elif choice == "2":
        # List positions of even numbers
        numbers = input("Enter a list of numbers separated by spaces: ")
        numbers = [int(x) for x in numbers.split()]
        even_positions = list_even_positions(numbers)
        print("Even numbers are at positions:", even_positions)

    elif choice == "3":
        input_string = input("Enter a string: ")
        encrypted_string = encrypt_string(input_string)
        print("Encrypted String : ", encrypted_string)

    elif choice == "4":
        # Find intersection of two lists
        list1 = input("Enter the first list separated by spaces: ")
        list1 = [int(x) for x in list1.split()]
        list2 = input("Enter the second list separated by spaces: ")
        list2 = [int(x) for x in list2.split()]
        intersection = intersect_lists(list1, list2)
        print("Intersection of the lists:", intersection)

    elif choice == "0":
        # Exit the program
        print("Goodbye!")
        break

    else:
        # Invalid input
        print("Invalid input. Please enter a number from 0 to 4.")