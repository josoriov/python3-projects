from src.functions import safe_cast


def introduction():
    botname = "Talko"
    bith_year = 2021
    print(f"Hello! My name is {botname}")
    print(f"I Was created in {bith_year}")


def presentation():
    print("Please, remind me your name")
    name = input()
    print(f"What a great name you have, {name}!")


def age_guess():
    print("Let me guess your age.")
    remainder_3 = int(input("Enter the remainder of dividing you age by 3: "))
    remainder_5 = int(input("Enter the remainder of dividing you age by 5: "))
    remainder_7 = int(input("Enter the remainder of dividing you age by 7: "))
    age = (remainder_3*70 + remainder_5*21 + remainder_7*15) % 105
    print(f"Your age is {age}; that's a good time to start programming!")


def counting():
    print("Now I will prove to you that I can count to any number you want.")
    number = int(input("Enter the number you want me to count to: "))
    for i in range(number):
        print(i, end=" - ")
    print(number)


def quiz():
    question = """
    Let's test your programming knowledge!
    What type of language Python is?
    1) Interpreted and statically typed
    2) Interpreted and dynamically typed
    3) Compiled and statically typed
    4) Compilled and dynamically typed"""
    print(question)
    correct = False
    while not correct:
        ans = input("Enter your anwser: ")
        ans = safe_cast(ans, int, 0)
        if ans == 2:
            print("That's correct! Python is both interpreted and dynamically typed")
            correct = True
        else:
            print("Please, try again.")


def exit_message():
    print("Congratulations, have a nice day!")


def main():
    introduction()
    presentation()
    age_guess()
    counting()
    quiz()
    exit_message()


main()
