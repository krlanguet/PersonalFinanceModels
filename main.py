# main function
def total_investment_value(rate, principle, time, salary):
    interest = 0
    for i in range(time):
        interest =  principle*rate
        principle += interest + salary
    return principle


rate = 0.04 # yearly return rate
salary = 68000 # what one makes each year
principle = 68000 # initial investment
time = 13 # years

new_amount = total_investment_value(rate, principle, time, salary)
print(new_amount)
