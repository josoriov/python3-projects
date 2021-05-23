import requests

from src.functions import safe_cast
cache = {}


def request_currency_exchange(search_currency: str) -> dict:
    global cache

    # Find results in cache dict else make the request
    is_cached = cache.get(search_currency, 0)

    if is_cached == 0:
        url = f"https://www.floatrates.com/daily/{search_currency}.json"
        try:
            r = requests.get(url)
            cache[search_currency] = r.json()
            return r.json()
        except ValueError:
            return {}
    return cache[search_currency]


def convert_currency() -> str:
    money = safe_cast(input("Amount of money you want to convert:\n"), float, 0.0)
    money = round(money, 2)
    str_currency = "Enter currency of origin and destiny separated by a hyphen e.g. USD-EUR:\n"
    origin_currency, output_currency = input(str_currency).lower().strip().split("-")
    exchange_rate = request_currency_exchange(origin_currency)
    converted = round(money*exchange_rate[output_currency]['rate'], 2)
    return f"{origin_currency.upper()}${money} are equivalent to {output_currency.upper()}${converted}"


def main():
    exit_program = False
    while not exit_program:
        action = input("Choose the action: 1) Convert currency 2) Exit program\n")
        if action == "2":
            exit_program = True
        elif action == "1":
            response = convert_currency()
            print(response)
        else:
            print("Not a valid input. Please, try again!")


main()

# !TODO create a search option case you don't know the currency code
# !TODO search by country, name of currency
