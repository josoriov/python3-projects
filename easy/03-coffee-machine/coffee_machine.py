from src.functions import safe_cast


class CoffeeMachine:
    def __init__(self, water: int, milk: int, coffee: int, cups: int, money: float, password: str):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        # Private attribute
        self.__money = money
        self.__pasword = password

    def __str__(self):
        description = f"""The machine currently have:
        {self.water}ml of water
        {self.milk}ml of milk
        {self.coffee}g of coffee beans
        {self.cups} disposable cups"""
        return description

    def add_resources(self, water: int, milk: int, coffee: int, cups: int):
        self.water += water
        self.milk += milk
        self.coffee += coffee
        self.cups += cups
        return "Successfully added the resources"

    def add_money(self, money: float, password: str):
        if self.__pasword == password:
            self.__money += money
            return f"Successfully added {money} dollars. Current balance {self.__money}"
        else:
            return f"Wrong password. Please, try again!"

    def take_money(self, password: str):
        if self.__pasword == password:
            retrieved = self.__money
            self.__money = 0.0
            return f"You retreived {retrieved} dollars. Current balance {self.__money}"
        else:
            return f"Wrong password. Please, try again!"

    def make_espresso(self, to_make: int):
        needed = {
            "water": 250*to_make,
            "coffee": 16*to_make,
            "cups": to_make
        }
        total_price = 4 * to_make
        if needed["water"] > self.water:
            return f"Sorry, not enough water to make {to_make} espresso(s)"
        if needed["coffee"] > self.coffee:
            return f"Sorry, not enough coffee to make {to_make} espresso(s)"
        if needed["cups"] > self.cups:
            return f"Sorry, not enough cups to make {to_make} espresso(s)"
        self.water -= needed["water"]
        self.coffee -= needed["coffee"]
        self.cups -= needed["cups"]
        self.__money += total_price
        return f"Successfully made {to_make} espresso(s). Enjoy them!"

    def make_latte(self, to_make: int):
        needed = {
            "water": 350 * to_make,
            "milk": 75 * to_make,
            "coffee": 20 * to_make,
            "cups": to_make
        }
        total_price = 7 * to_make
        if needed["water"] > self.water:
            return f"Sorry, not enough water to make {to_make} latte(s)"
        if needed["milk"] > self.milk:
            return f"Sorry, not enough milk to make {to_make} latte(s)"
        if needed["coffee"] > self.coffee:
            return f"Sorry, not enough coffee to make {to_make} latte(s)"
        if needed["cups"] > self.cups:
            return f"Sorry, not enough cups to make {to_make} latte(s)"
        self.water -= needed["water"]
        self.milk -= needed["milk"]
        self.coffee -= needed["coffee"]
        self.cups -= needed["cups"]
        self.__money += total_price
        return f"Successfully made {to_make} latte(s). Enjoy them!"

    def make_cappuccino(self, to_make):
        needed = {
            "water": 200 * to_make,
            "milk": 100 * to_make,
            "coffee": 12 * to_make,
            "cups": to_make
        }
        total_price = 6 * to_make
        if needed["cups"] > self.cups:
            return f"Sorry, not enough cups to make {to_make} cappuccino(s)"
        if needed["coffee"] > self.coffee:
            return f"Sorry, not enough coffee to make {to_make} cappuccino(s)"
        if needed["water"] > self.water:
            return f"Sorry, not enough water to make {to_make} cappuccino(s)"
        if needed["milk"] > self.milk:
            return f"Sorry, not enough milk to make {to_make} cappuccino(s)"
        self.water -= needed["water"]
        self.milk -= needed["milk"]
        self.coffee -= needed["coffee"]
        self.cups -= needed["cups"]
        self.__money += total_price
        return f"Successfully made {to_make} cappuccino(s). Enjoy them!"


def initialize_machine() -> CoffeeMachine:
    water = safe_cast(input("Put on some water (ml): "), int)
    milk = safe_cast(input("Put on some milk (ml): "), int)
    coffee = safe_cast(input("Put on some coffee (g): "), int)
    cups = safe_cast(input("Put on some disposable cups: "), int)
    money = safe_cast(input("Amount of money to start: "), float)
    password = safe_cast(input("Insert the machine password (5 characters): "), str)[:5]

    return CoffeeMachine(water, milk, coffee, cups, money, password)


def buy(machine: CoffeeMachine) -> str:
    wanted = input("What do you want to buy? 1) Espresso 2) Latte 3) Cappuccino 4) Back to main menu \n")
    if wanted == "1":
        return machine.make_espresso(1)
    elif wanted == "2":
        return machine.make_latte(1)
    elif wanted == "3":
        return machine.make_cappuccino(1)
    elif wanted == "4":
        pass
    return "Not a valid input. Sale cancelled."


def fill(machine: CoffeeMachine) -> str:
    resources = input("What do you want to add? 1) Resources 2) Money (requires password) 3) Back to main menu\n")
    if resources == "1":
        water = safe_cast(input("How much water (ml) will you add: "), int)
        milk = safe_cast(input("How much milk (ml) will you add: "), int)
        coffee = safe_cast(input("How much coffee (g) will you add: "), int)
        cups = safe_cast(input("How many disposable cups will you add: "), int)
        return machine.add_resources(water, milk, coffee, cups)
    elif resources == "2":
        money = safe_cast(input("Money to add: "), float)
        password = input("Enter the machine password: ")
        return machine.add_money(money, password)
    elif resources == "3":
        pass
    return "Not a valid input. Operation cancelled."


def take(machine: CoffeeMachine) -> str:
    password = input("Enter the machine password: ")
    return machine.take_money(password)


def main():
    exit_program = False
    # machine = initialize_machine()
    machine = CoffeeMachine(1000, 1000, 300, 30, 30.0, 'abcde')
    while not exit_program:
        action = input("Write action (buy, fill, take, remaining, exit): ")
        if action == "exit":
            exit_program = True
        elif action == "buy":
            response = buy(machine)
            print(response)
        elif action == "fill":
            response = fill(machine)
            print(response)
        elif action == "take":
            response = take(machine)
            print(response)
        elif action == "remaining":
            print(machine)

    # machine = initialize_machine()


main()

# !TODO include a better validation
# !TODO all the fill options should require password
# !TODO create a getter for the amount of money
# !TODO all the remaining options should require validation
#
