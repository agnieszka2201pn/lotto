import random


def choose_numbers():
# """
# function takes numbers from the player and creates a sorted list
# """
    list_of_user_numbers = []
    for i in range(6):
        a = int(input("Choose number: "))
        if a in range(1, 50):
            list_of_user_numbers.append(a)

        else:
            print("Choose number from range 1-49")
    return sorted(list_of_user_numbers)

my_numbers = choose_numbers()
print(my_numbers)

def drawn_numbers():
# """
# function provides sorted list of numbers drawn by computer
# """
    computer_list = random.sample(range(1, 50), 6)
    return sorted(computer_list)

computer_numbers = drawn_numbers()
print(computer_numbers)

def comparison():
    user_choice = my_numbers
    computer_choice = computer_numbers
    common_numbers = []
    for item in user_choice[::]:
        if item in computer_choice[::]:
            common_numbers.append(item)
    return common_numbers

print(comparison())