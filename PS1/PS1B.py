

def months_for_downpayment_with_raise(annual_salary,portion_salary_saved,
                           total_cost, semi_annual_raise):
    """function retrieves the number of months needed to cover downpayment for a house
    with a semi annual raise occurring every 6 months"""
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

        """Interestingly, if I put months before counter, it wont work"""
        if months % 6 == 0:
            annual_salary = annual_salary * (1 + semi_annual_raise)
        else:
            annual_salary = annual_salary

    return months

print("Number of months: %d" % months_for_downpayment_with_raise(120000, 0.05, 500000,0.03))
print("Number of months: %d" % months_for_downpayment_with_raise(80000, 0.1, 800000,0.03))
print("Number of months: %d" % months_for_downpayment_with_raise(75000, 0.05, 1500000,0.05))