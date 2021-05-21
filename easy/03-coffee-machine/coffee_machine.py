from src.functions import safe_cast


class CoffeeMachine:
    def __init__(self, water: int, milk: int, coffee: int, cups: int, money: float, password: str):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money
        # Private attribute
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

    def add_money(self, money: float, password: str):
        if self.__pasword == password:
            self.money += money
            # !TODO complete this message
            return
        else:
            # !TODO complete this message
            return

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
        self.money += total_price
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
        self.money += total_price
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
        self.money += total_price
        return f"Successfully made {to_make} cappuccino(s). Enjoy them!"


def main():
    machine = CoffeeMachine(100, 100, 25, 20, 100)

    print(machine)


main()

# !TODO fill - add new resources to the machine
# !TODO take - enter password to take out the money earned
# !TODO remaining - print how many resources are left - can use the str dunder method
# !TODO exit - exit the program loop
