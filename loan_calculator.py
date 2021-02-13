import math
import argparse

parser = argparse.ArgumentParser(description="Calculation of differentiated payments, Loan Principals, Monthly Payments and Periods \
To do this, the user can run the program specifying interest, number of monthly payments, and loan principal.")

parser.add_argument("--type", choices=["diff", "annuity"], help="You need to choose only one type from the list.")
parser.add_argument("--principal")
parser.add_argument("--payment")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()

select = ""

while True:
    if args.type is None:
        print("Incorrect parameters")
        break

    elif args.type == "diff" and args.principal is not None and args.periods is not None and args.interest is not None:
        select = "d"
        break

    elif args.type == "annuity" and (
            args.principal is not None and args.periods is not None and args.interest is not None):
        select = "a"
        break

    elif args.type == "annuity" and (
            args.payment is not None and args.periods is not None and args.interest is not None):
        select = "p"
        break

    elif args.type == "annuity" and (
            args.payment is not None and args.principal is not None and args.interest is not None):
        select = "n"
        break

    else:
        print("Incorrect parameters")
        break

sum = 0

if select == "n":
    # print("Enter the loan principal:")
    loan_principal = int(args.principal)
    # print("Enter the monthly payment:")
    monthly_payment = float(args.payment)
    # print("Enter the loan interest:")
    loan_interest = float(args.interest)

    i = loan_interest / (12 * 100)

    temp_log = monthly_payment / (monthly_payment - i * loan_principal)

    n_months = math.ceil(math.log(temp_log, 1 + i))

    sum = monthly_payment * n_months

    over_payment = int(sum - loan_principal)

    if n_months % 12 == 0:
        years = n_months // 12
        print(f"It will take {years} years to repay this loan!")
    elif n_months % 12 != 0:
        years = n_months // 12
        month = n_months % 12
        if years == 0:
            print(f"It will take {month} months to repay this loan!")
        else:
            print(f"It will take {years} years and {month} months to repay this loan!")

    print(f"Overpayment = {over_payment}")

elif select == "a":
    # print("Enter the loan principal:")
    loan_principal = int(args.principal)
    # print("Enter the number of periods:")
    num_months = int(args.periods)
    # print("Enter the loan interest:")
    loan_interest = float(args.interest)

    i = loan_interest / (12 * 100)
    z = 1 + i
    cus_pow = math.pow(z, num_months)

    monthly_pay = math.ceil(loan_principal * abs((i * cus_pow) / (cus_pow - 1)))

    sum = num_months * monthly_pay

    over_payment = int(sum - loan_principal)

    print(f"Your annuity payment = {monthly_pay}!")

    print(f"Overpayment = {over_payment}")


elif select == "p":
    # print("Enter the annuity payment:")
    montly_payment = float(args.payment)
    # print("Enter the number of periods:")
    num_months = int(args.periods)
    # print("Enter the loan interest:")
    loan_interest = float(args.interest)

    i = loan_interest / (12 * 100)

    z = 1 + i

    cus_pow = math.pow(z, num_months)

    loan_principal = int(montly_payment // (abs((i * cus_pow) / (cus_pow - 1))))

    sum = num_months * montly_payment

    over_payment = int(sum - loan_principal)

    print(f"Your loan principal = {loan_principal}!")

    print(f"Overpayment = {over_payment}")

elif select == "d":
    # print("Enter the loan principal:")
    loan_principal = int(args.principal)
    # print("Enter the number of periods:")
    num_months = int(args.periods)
    # print("Enter the loan interest:")
    loan_interest = float(args.interest)

    p = loan_principal

    n = num_months

    m = n

    i = loan_interest / (12 * 100)

    for m in range(1, num_months + 1):
        d = int(math.ceil((p / n + i * (p - ((p * (m - 1)) / n)))))
        sum = sum + d
        print(f"Month {m}: payment is {d}")

    over_payment = int(sum - p)

    print(f"Overpayment = {over_payment}")
