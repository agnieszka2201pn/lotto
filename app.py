import random


def choose_numbers():
    """ function takes numbers from the player and creates a sorted list"""

    list_of_user_numbers = []

    for i in range(6):
        try:
            a = int(input("Choose number: "))
            if a in range(1, 50):
                list_of_user_numbers.append(a)
            else:
                print("Choose number from range 1-49")

        except ValueError:
            print("This is not a number")

    return sorted(list_of_user_numbers)


def drawn_numbers():
    """ function provides sorted list of unique numbers drawn by computer from range 1-49"""

    computer_list = random.sample(range(1, 50), 6)
    return sorted(computer_list)


def comparison():
    """
    functions compares numbers drawn by computer with numbers chosen by user
    """
    my_numbers = choose_numbers()
    computer_numbers = drawn_numbers()
    common_numbers = []
    print("Drawn numbers are: " + str(computer_numbers))
    print("Your numbers are: " + str(my_numbers))

    for item in my_numbers[::]:
        if item in computer_numbers[::]:
            common_numbers.append(item)
    return "You guessed: " + str(len(common_numbers)) + " numbers"


print(comparison())
