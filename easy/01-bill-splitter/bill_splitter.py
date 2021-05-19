import sys


def number_of_friends():
    n_friends = int(input("Enter the number of friends joining (including you): "))
    return n_friends


def friend_names(n_friends: int):
    names = []
    for i in range(n_friends):
        name = input(f"Enter the name of the friend number {i+1}: ")
        names.append(name)
    return names


def bill_total():
    total = int(input("Enter the total bill value: "))
    return total


def main():
    n_friends = number_of_friends()
    if n_friends == 0:
        raise Exception("No one is joining for the party")
    names = friend_names(n_friends)
    total_bill = bill_total()
    splitted_bill = round(total_bill/len(names), 2)
    print({name: splitted_bill for name in names})


main()
