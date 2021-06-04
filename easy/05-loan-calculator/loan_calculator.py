import math
import argparse


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


def nominal_interest(annual_interest: float) -> float:
    """
    Calculate the nominal interest rate given the annual interest rate
    :param annual_interest: annual interest rate (percentage)
    :return: nominal interest rate (fraction)
    """
    return annual_interest/(12*100)


def differentiated_payment(p: float, n: float, i: float, m: int) -> float:
    """
    Calculate the differentiated payment for the m-th period
    :param p: loan principal value
    :param n: number of payments
    :param i: monthly nominal interest rate
    :param m: current repayment period
    :return: amount of the m-th differentiated payment
    """
    term_1 = p/n
    term_2 = i * (p - (p * (m-1) / n))
    return term_1 + term_2


# Creating parser to recieve the arguments
parser = argparse.ArgumentParser(description="Loan calculator")
# type
parser.add_argument(
    "--type", choices=["annuity", "diff"], default=False, dest="type_loan",
    help="Choose the type of loan annuity of differentiated payment"
)
# payment
parser.add_argument("--payment", default=0, help="Monthly payment amount")
# principal
parser.add_argument("--principal", default=0, help="Loan principal")
# periods
parser.add_argument("--periods", default=0, help="Number of months to pay the loan")
# interest
parser.add_argument("--interest", default=0, help="Annual interest rate in percentage (required).")

# Retrieving the arguments
args = parser.parse_args()
type_loan = str(args.type_loan)
payment = float(args.payment)
principal = float(args.principal)
periods = int(args.periods)
interest = float(args.interest)


def main():
    if interest == 0:
        return "The interest value is required. Use --help to learn more."
    elif (payment < 0) or (principal < 0) or (periods < 0) or (interest < 0):
        return "Negative values are not accepted"
    elif (type_loan == "diff") and (principal != 0) and (periods != 0):
        # !TODO calculate the number of payments and the overpayment
        ans = "\n"
        overpayment = -1 * principal
        for m in range(1, periods+1):
            m_payment = differentiated_payment(principal, periods, nominal_interest(interest), m)
            m_payment = math.ceil(m_payment)
            overpayment += m_payment
            ans += f"Month {m} payment is {m_payment}\n"
        ans += f"\nOverpayment = {int(overpayment)}"
        return ans
    elif (type_loan == "annuity") and (principal != 0) and (periods != 0):
        ann_payment = ordinary_annuity(principal, nominal_interest(interest), periods)
        ann_payment = math.ceil(ann_payment)
        overpayment = ann_payment*periods - principal
        ans = ""
        ans += f"Your annuity payment = {int(ann_payment)}\n"
        ans += f"Overpayment = {int(overpayment)}\n"
        return ans
    elif (type_loan == "annuity") and (payment != 0) and (periods != 0):
        ann_principal = loan_principal(payment, nominal_interest(interest), periods)
        ann_principal = math.ceil(ann_principal)
        overpayment = payment*periods - ann_principal
        ans = ""
        ans += f"Your loan principal = {int(ann_principal)}\n"
        ans += f"Overpayment = {int(overpayment)}"
        return ans
    elif (type_loan == "annuity") and (principal != 0) and (payment != 0):
        n_payments = number_of_payments(principal, nominal_interest(interest), payment)
        n_payments = math.ceil(n_payments)
        years = int(n_payments // 12)
        months = int(n_payments)
        if n_payments < 12:
            msg = f"{months} months"
        elif n_payments % 12 == 0:
            msg = f"{years} years"
        else:
            msg = f"{years} years and {months} months"
        overpayment = n_payments*payment - principal
        ans = f"It will take {msg} to repay the loan!\n"
        ans += f"Overpayment = {int(overpayment)}"
        return ans

    return "Incorrect parameters submitted. Use --help to learn more."


if __name__ == "__main__":
    response = main()
    print(response)

# !TODO Create a function to handle annuity cases and another to handle diff cases

# Test cases
# example 1: python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10
# output 1: Month 1: payment is 108334 ... Month 2: payment is 107500

# example 2: python creditcalc.py --type=annuity --principal=1000000 --periods=60 --interest=10
# output 2: Your annuity payment = 21248! ... Overpayment = 274880

# example 3: python creditcalc.py --type=diff --principal=1000000 --payment=104000
# output 3: Incorrect parameters

# example 4: python creditcalc.py --type=diff --principal=500000 --periods=8 --interest=7.8
# output 4: Month 1: payment is 65750 ... Overpayment = 14628

# example 5: python creditcalc.py --type=annuity --payment=8722 --periods=120 --interest=5.6
# output 5: Your loan principal = 800018! ... Overpayment = 246622

# example 6: python creditcalc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
# It will take 2 years to repay this loan! ... Overpayment = 52000
