# Modules
from math import log
from math import ceil

print("""What do you want to calculate?
type \"n\" for number of monthly payments,
type \"a\" for annuity monthly payment amount,
type \"p\" for loan principal:""")
parameter = input()

if parameter == "n":
    print("Enter the loan principal:")
    principal = int(input())
    print("Enter the monthly payment:")
    monthly_payment = int(input())
    print("Enter the loan interest")
    loan_interest = float(input())

    i = loan_interest / (12 * 100)
    number_of_payments = log(float(monthly_payment) / (float(monthly_payment) - i * float(principal)), i + 1)

    counts = divmod(number_of_payments, 12)
    years = round(counts[0])
    months = ceil(counts[1])

    if months == 12:
        years += 1
        months = 0

    # years = number_of_payments / 12
    # months = round(number_of_payments - (years * 12))
    # years = round(years)

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
elif parameter == "a":
    print("Enter the loan principal:")
    loan_principal = int(input())
    print("Enter the number of periods:")
    number_of_periods = int(input())
    print("Enter the loan interest:")
    loan_interest = float(input())

    i = loan_interest / 12 / 100
    annuity_payment = loan_principal * ((i * pow(1 + i, number_of_periods)) / (pow(1 + i, number_of_periods) - 1))
    annuity_payment = ceil(annuity_payment)
    print(f"Your monthly payment = {annuity_payment}!")

elif parameter == "p":
    print("Enter the annuity payment:")
    annuity_payment = float(input())
    print("Enter the number of periods:")
    number_of_periods = int(input())
    print("Enter the loan interest:")
    loan_interest = float(input())

    i = loan_interest / 12 / 100
    loan_principal = annuity_payment / ((i * pow(1 + i, number_of_periods)) / (pow(1 + i, number_of_periods) - 1))

    print(f"Your loan principal = {loan_principal}!")
