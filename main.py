import math

### Defining Functions

## Main Function 
def total_investment_value(rate=0.04, principle=10000, time=10, contribution=1000):
    for i in range(time):
        interest =  principle*rate
        principle += interest + contribution 
    return principle

## Global Values
rate = 0.04 # yearly return rate
initial_value = 2000



### Considering Different Career Paths

## Suppose that I get my PhD before industry
amount = initial_value

# From now until Graduation
time = 3 # Counting this year
contribution = 500
amount = total_investment_value(0, amount, time, contribution)

# Fifth year Masters Program
time = 1
contribution = 500
amount = total_investment_value(0, amount, time, contribution)

# During Grad School
time = 5
contribution = 5000
amount = total_investment_value(rate, amount, time, contribution)

# From Grad School to age 30
time = 2 
contribution = 68000 # take home each year = salary * .72 (tax) - 40,000 (living)
amount = total_investment_value(rate, amount, time, contribution)
print('Worth at 30 with PhD:', '${:,.2f}'.format(amount))


## Now Suppose that I only get a Masters with NUs 5year program
amount = initial_value

# From now until Graduation
time = 3 # Counting this year
contribution = 500
amount = total_investment_value(0, amount, time, contribution)

# Fifth year Masters Program
time = 1
contribution = 500
amount = total_investment_value(0, amount, time, contribution)

# From Masters to age 30
time = 7
contribution = 46400 # take home each year = salary * .72 (tax) - 40,000 (living)
amount = total_investment_value(rate, amount, time, contribution)
print('Worth at 30 with Masters:', '${:,.2f}'.format(amount))
