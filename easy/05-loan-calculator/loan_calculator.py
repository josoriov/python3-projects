import math
from src.functions import safe_cast


def ordinary_annuity(p: float, i: float, n: float) -> float:
    """
    Calculates the annuity payment given loan principal, interest rate and number of payments
    :param p: loan principal value
    :param i: monthly nominal interest rate
    :param n: number of payments
    :return: annuity payment
    """
    numerator = p * i * ((1 + i) ** n)
    denominator = ((1 + i)**n) - 1
    return numerator/denominator


def loan_principal(a: float, i: float, n: float) -> float:
    """
    Calculates the loan principal given annuity payment, interest rate and number of payments
    :param a: annuity payment
    :param i: monthly nominal interest rate
    :param n: number of payments
    :return: loan principal
    """
    numerator = a
    denominator = (i*(1+i)**n)/((1+i)**n - 1)
    return numerator/denominator


def number_of_payments(p: float, i: float, a: float) -> float:
    """
    Calculates the number of payments given loan principal, interest rate and annuity payment
    :param p: loan principal value
    :param i: monthly nominal interest rate
    :param a: annuity payment
    :return: number of payments
    """
    numerator = a
    denominator = a - (i*p)
    return math.log(numerator/denominator, i+1)


def nominal_interest(annual_interest: float):
    """
    Calculate the nominal interest rate given the annual interest rate
    :param annual_interest: annual interest rate (percentage)
    :return: nominal interest rate (fraction)
    """
    return annual_interest/(12*100)


def main():
    start_message = """What do you want to calculate?
    Type 'n' for number of monthly payments
    Type 'a' for annuity monthly payment amount
    Type 'p' for loan principal\n"""
    action = input(start_message)
    if action == "n":
        p = safe_cast(input("Enter the loan principal:\n"), float)
        a = safe_cast(input("Enter the monthly payment:\n"), float)
        i = safe_cast(input("Enter the loan interest:\n"), float)
        i = nominal_interest(i)
        response = number_of_payments(p, i, a)
        response = math.ceil(response)
        print(f"It will take {int(response//12)} years and {int(response%12)} months to pay the loan!")
    if action == "a":
        p = safe_cast(input("Enter the loan principal:\n"), float)
        n = safe_cast(input("Enter the number of periods:\n"), float)
        i = safe_cast(input("Enter the loan interest:\n"), float)
        i = nominal_interest(i)
        response = ordinary_annuity(p, i, n)
        print(f"Your monthly payment is {math.ceil(response)}!")
    if action == "p":
        a = safe_cast(input("Enter the monthly payment:\n"), float)
        n = safe_cast(input("Enter the number of periods:\n"), float)
        i = safe_cast(input("Enter the loan interest:\n"), float)
        i = nominal_interest(i)
        response = loan_principal(a, i, n)
        print(f"Your monthly payment is {math.floor(response)}!")
    else:
        print(f"The option {action} is not supported. Try again!")
    return


main()
# The first is the loan principal.
# The second is the monthly payment.
# The next is the number of monthly payments.
# The last is the loan interest.
