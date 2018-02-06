
def pay_off_in_year(balance, annual_interest_rate,monthly_payment_rate):
    """Check balance after 12 months"""
    months = 0
    while months < 12:

        min_monthly_payment = monthly_payment_rate * balance
        monthly_unpaid_balance = balance - min_monthly_payment
        balance = round(monthly_unpaid_balance + (annual_interest_rate/12)*monthly_unpaid_balance,2)

        #balance -= 1
        months += 1
        #print(months, balance)
    print("Remaining balance:  %s" % balance)
    return True

pay_off_in_year(42,0.2,0.04)
pay_off_in_year(484,0.2,0.04)
pay_off_in_year(498,0.12,0.08)

