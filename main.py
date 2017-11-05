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
> For any point in the middle of my life, how long could I go without
    employment before I had to continue working again, without sacrificing
    the ability of myself and my family to retire withand meet our long-term financial goals?
> how long retirement last with/without social security?

'''


# imports --------------------------------------------------------
import numpy as np
from matplotlib import pyplot as plt

# custom files
import fin_comp as fc


### Defining Functions ----------------------------------------------


## Global Values -------------------------------------------------------
current_age = 19
net_years = 20
years_array = np.arange(current_age+1, current_age+net_years+1)
initial_value = 2000 # current net value


# 5th year masters --------------------------------------------------------
contribution_levels_m = np.array([500, 500, 46400]) # take home each year = salary * .72 (tax) - 40,000 (living)
eras_masters = np.array([3, 1, net_years-4])
contribution_masters = fc.contribution_over_time(contribution_levels_m, eras_masters) # generates the contribution levels
print(contribution_masters)
rate_masters = np.zeros(net_years) # preallocation
rate_masters[4:] = 0.04 # return on investments

#6 year masters ???


# PhD program -------------------------------------------------------------------
contribution_levels_phd = np.array([500, 5000, 68000])# take home each year = salary * .72 (tax) - 40,000 (living)
eras_phd = np.array([3, 5, net_years-8])
contribution_phd = fc.contribution_over_time(contribution_levels_phd, eras_phd)
print(contribution_phd)
rate_phd = np.zeros(net_years) # preallocation
rate_phd[3:] = 0.04 # return on investments


# Function calls ---------------------------------------------------------------------
amount_masters = fc.total_investment_value(rate_masters, initial_value, net_years, contribution_masters)
amount_phd = fc.total_investment_value(rate_phd, initial_value, net_years, contribution_phd)

# printing data to screen, net worth at last time
print('Worth at', net_years+current_age, ' years with PhD:', '${:,.2f}'.format(amount_phd[-1]))
print('Worth at', net_years+current_age, ' years with Masters:', '${:,.2f}'.format(amount_masters[-1]))


# graphing data ----------------------------------------------------------------------------
plt.figure(1)
plt.plot(years_array, amount_masters)
plt.plot(years_array, amount_phd)
plt.xlabel('Years of Work')
plt.ylabel('Net Worth (Dollars)')
plt.title('Net Worth')
plt.legend(['Masters','Phd'])

plt.figure(2)
plt.plot(years_array, amount_masters - amount_phd)
plt.xlabel('Years of Work')
plt.ylabel('Difference in net worth')
plt.grid(True)
plt.title('Masters worth minus Ph.D worth')


# End of program
plt.show()
