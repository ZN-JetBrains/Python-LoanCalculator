# Modules
import argparse
from math import ceil
from math import floor
from math import log


def is_none(param):
    if param is None:
        return True
    return False


def is_negative(param):
    if float(param) < 0:
        return True
    return False


def calculate_annuity(principal, periods, interest):
    if is_none(principal) or is_none(periods) or is_none(interest)\
            or is_negative(principal) or is_negative(periods) or is_negative(interest):
        print("Incorrect parameters")
        return

    p = float(principal)
    n = int(periods)
    i = float(interest) / (12 * 100)

    annuity_payment = p * ((i * pow(1 + i, n)) / (pow(1 + i, n) - 1))
    annuity_payment = ceil(annuity_payment)
    overpayment = (n * annuity_payment) - p

    print(f"Your annuity payment = {annuity_payment}!")
    print(f"Overpayment = {round(overpayment)}")


def calculate_annuity_periods(principal, payment, interest):
    if is_none(principal) or is_none(payment) or is_none(interest) \
            or is_negative(principal) or is_negative(payment) or is_negative(interest):
        print("Incorrect parameters")
        return

    p = float(principal)
    i = float(interest) / (12 * 100)
    pay = float(payment)

    n = log(pay / (pay - i * p), i + 1)
    n = ceil(n)
    overpayment = (n * pay) - p

    counts = divmod(n, 12)
    years = round(counts[0])
    months = ceil(counts[1])

    if months == 12:
        years += 1
        months = 0

    if years == 0:
        if months == 1:
            print(f"It will take {months} month to repay this loan!")
        else:
            print(f"It will take {months} months to repay this loan!")
    elif months == 0:
        if years == 1:
            print(f"It will take {years} year to repay this loan!")
        else:
            print(f"It will take {years} years to repay this loan!")
    else:
        print(f"It will take {years} ", end="")
        print("year" if years == 1 else "years", end="")
        print(f" and {months} ", end="")
        print("month" if months == 1 else "months", end="")
        print(" to repay this loan!")

    print(f"Overpayment = {round(overpayment)}")


def calculate_annuity_principal(periods, payment, interest):
    if is_none(periods) or is_none(payment) or is_none(interest) \
            or is_negative(periods) or is_negative(payment) or is_negative(interest):
        print("Incorrect parameters")
        return

    n = int(periods)
    i = float(interest) / (12 * 100)
    pay = float(payment)
    principal = pay / ((i * pow(1 + i, n)) / (pow(1 + i, n) - 1))
    principal = floor(principal)
    overpayment = (n * pay) - principal

    print(f"Your loan principal = {principal}!")
    print(f"Overpayment = {round(overpayment)}")


def calculate_diff(principal, periods, interest):
    if is_none(principal) or is_none(periods) or is_none(interest)\
            or is_negative(principal) or is_negative(periods) or is_negative(interest):
        print("Incorrect parameters")
        return

    p = float(principal)
    n = int(periods)
    i = float(interest) / (12 * 100)

    overpayment = p
    month = 1
    for _ in range(n):
        d = (p / n) + i * (p - ((p * (month - 1)) / n))
        d = ceil(d)
        print(f"Month {month + 1}: payment is {d}")
        month += 1
        overpayment -= d
    overpayment = -1 * overpayment
    print(f"\nOverpayment = {overpayment}")


parser = argparse.ArgumentParser()
parser.add_argument("--type", help="type of loan")
parser.add_argument("--principal", help="the initial loan amount")
parser.add_argument("--periods",  help="amount of months to make a payment")
parser.add_argument("--payment", help="payment amount per period")
parser.add_argument("--interest", help="the interest rate on the loan")

# Store input
args = parser.parse_args()

# Check: Type
if args.type == "annuity":
    if args.payment is None:
        calculate_annuity(principal=args.principal, periods=args.periods, interest=args.interest)
    elif args.principal is None:
        calculate_annuity_principal(periods=args.periods, payment=args.payment, interest=args.interest)
    elif args.periods is None:
        calculate_annuity_periods(principal=args.principal, payment=args.payment, interest=args.interest)
elif args.type == "diff":
    if args.payment is not None:
        print("Incorrect parameters")
    else:
        calculate_diff(principal=args.principal, periods=args.periods, interest=args.interest)
else:
    print("Incorrect parameters")
