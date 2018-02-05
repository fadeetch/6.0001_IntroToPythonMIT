

def months_for_downpayment(annual_salary,portion_salary_saved,total_cost):
    """function retrieves the number of months needed to cover downpayment for a house"""
    annual_return = 0.04
    portion_down_payment = 0.25
    current_savings = 0
    months = 0
    abs_down_payment = total_cost * portion_down_payment

    while current_savings <= abs_down_payment:
        monthly_increase = annual_salary/12 * portion_salary_saved
        current_savings += current_savings * annual_return / 12 + monthly_increase
        #print(current_savings)
        months += 1
    return months

print("Number of months: %d" % months_for_downpayment(120000, 0.10, 1000000))
print("Number of months: %d" % months_for_downpayment(80000,  0.15, 500000))

