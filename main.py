import math

# Main file to run all personal finance functions
def total_investment_value(rate=0.04, principle=10000, time=10, contribution=1000):
    for i in range(time):
        interest =  principle*rate
        principle += interest + contribution
    return principle

# input parameters for functions
rate = 0.04 # yearly return rate
contribution = 68000 # what one makes each year
principle = 68000 # initial investment
time = 13 # years

new_amount = total_investment_value(rate, principle, time, contribution)
print('Amount of money returned is', '{:.2f}'.format(new_amount))
