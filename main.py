'''
TO DO still:

techincal
> why is there a dip at 5 years?

account for
> taxes on net worth
> yearly expenses
> add rest of salary to net worth per year
> changing interest rates and salary changes
> changing inflation
> variable yearly contributions

Question to answer:
> how long can one live for without working in the middle of their life?
> how long retirement last with/without social security?

'''


# imports --------------------------------------------------------
import numpy as np
from matplotlib import pyplot as plt


### Defining Functions ----------------------------------------------

## Main Function 
def total_investment_value(rate, amount, time, contribution):
    for i in range(1, time):
        interest =  amount[i-1]*rate[i-1]
        amount[i] = amount[i-1] + interest + contribution[i-1] 
    return amount


## Global Values -------------------------------------------------------
net_years = 10
years_array = range(1,net_years+1)
initial_value = 2000 # current net value
current_age = 19


# 5th year masters --------------------------------------------------------
amount_masters = np.zeros(net_years)
amount_masters[0] = initial_value
contribution_masters = np.zeros(net_years) # preallocation
rate_masters = np.zeros(net_years) # pe
contribution_masters[0:3] = 500 # college years
contribution_masters[3] = 500 # masters year
contribution_masters[4:] = 46400 # take home each year = salary * .72 (tax) - 40,000 (living)
rate_masters[4:-1] = 0.04 # return on investments


# PhD program -------------------------------------------------------------------
amount_phd = np.zeros(net_years)
amount_phd[0] = initial_value
contribution_phd = np.zeros(net_years) # preallocation
contribution_phd[0:3] = 500 # college years
contribution_phd[3:9] = 5000 # phd years
contribution_phd[9:] = 68000 # take home each year = salary * .72 (tax) - 40,000 (living)
rate_phd = np.zeros(net_years) # pe
rate_phd[3:-1] = 0.04 # return on investments


# Function calls ---------------------------------------------------------------------
amount_masters = total_investment_value(rate_masters, amount_masters, net_years, contribution_masters)
amount_phd = total_investment_value(rate_phd, amount_phd, net_years, contribution_phd)

# printing data to screen, net worth at last time
print('Worth at', net_years+current_age, ' years with PhD:', '${:,.2f}'.format(amount_phd[-1]))
print('Worth at', net_years+current_age, ' years with Masters:', '${:,.2f}'.format(amount_masters[-1]))


# graphing data ----------------------------------------------------------------------------
plt.figure(1)
plt.plot(years_array, amount_masters)
plt.plot(years_array, amount_phd)
plt.xlabel('Time (years)')
plt.ylabel('Net Worth (Dollars)')
plt.title('Net Worth')
plt.legend(['Masters','Phd'])

plt.figure(2)
plt.plot(years_array, amount_masters - amount_phd)
plt.xlabel('Time (years)')
plt.ylabel('Difference in net worth')
plt.grid(True)
plt.title('Masters worth minus Ph.D worth')


# End of program
plt.show()
