'''
TO DO still:

techincal:


account for:
> taxes on net worth
> possible debt from masters program
> yearly expenses
> add rest of salary to net worth per year
> changing interest rates and salary changes
> changing inflation
> variable yearly contributions

Tests to run:
> Model what would happen during different macroeconomic environments

Question to answer:
> For any point in the middle of my life, how long could I go without
    employment before I had to continue working again, without sacrificing
    the ability of myself and my family to retire withand meet our long-term financial goals?
> how long retirement last with/without social security?

'''


# imports --------------------------------------------------------
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style
style.use('bmh')

# custom files
import fin_comp as fc


## Global Values -------------------------------------------------------
current_age = 19
net_years = 20
years_array = np.arange(current_age+1, current_age+net_years+1)
initial_value = 2000 # current net value
return_rate = 0.04 # return on investments

''' Salary Sources
Salary data from BLS for 2016 https://www.bls.gov/ooh/computer-and-information-technology/home.htm
B.S. -> $95,000 for relevant careers
M.S. -> $110,000 for relecant careers
Salary data from NSF https://www.nsf.gov/statistics/2017/nsf17306/static/report/nsf17306.pdf
for 2015
PhD. -> $120,000
This is will underestimate salary data
'''

# B.S. in Comp Sci -----------------------------------------------------------
salaries_b = np.array([500, 95000])
living_expenses_b = np.array([0, 40000])
additional_expenses_b = np.array([0, 0])
eras_b = np.array([3, net_years-3])

contribution_b = fc.contribution_over_time(salaries_b, living_expenses_b, additional_expenses_b, eras_b) # generates the contribution levels
rate_b = np.zeros(net_years) # preallocation
rate_b[4:] = return_rate # return on investments

# 5th year masters --------------------------------------------------------
salaries_m = np.array([500, 500, 110000])
living_expenses_m = np.array([0, 0, 40000])
additional_expenses_m = np.array([0, 0, 0])
eras_m = np.array([3, 1, net_years-4])

contribution_m = fc.contribution_over_time(salaries_m, living_expenses_m, additional_expenses_m, eras_m)
rate_m = np.zeros(net_years)
rate_m[4:] = return_rate

#6 year masters ???


# PhD program -------------------------------------------------------------------
salaries_phd = np.array([500, 5000, 120000]) 
living_expenses_phd = np.array([0, 0, 40000])
additional_expenses_phd = np.array([0, 0, 0])
eras_phd = np.array([3, 5, net_years-8])

contribution_phd = fc.contribution_over_time(salaries_phd, living_expenses_phd, additional_expenses_phd, eras_phd)
rate_phd = np.zeros(net_years) # preallocation
rate_phd[3:] = return_rate # return on investments


# Function calls ---------------------------------------------------------------------
amount_bachelors = fc.total_investment_value(rate_b, initial_value, net_years, contribution_b)
amount_masters = fc.total_investment_value(rate_m, initial_value, net_years, contribution_m)
amount_phd = fc.total_investment_value(rate_phd, initial_value, net_years, contribution_phd)

# printing data to screen, net worth at last time
print('Worth at', net_years+current_age, ' years with Bachelors:', '${:,.2f}'.format(amount_bachelors[-1]))
print('Worth at', net_years+current_age, ' years with PhD:', '${:,.2f}'.format(amount_phd[-1]))
print('Worth at', net_years+current_age, ' years with Masters:', '${:,.2f}'.format(amount_masters[-1]))


# graphing data ----------------------------------------------------------------------------
plt.figure(1)
plt.plot(years_array, amount_bachelors,color='g')
plt.plot(years_array, amount_masters, color='k')
plt.plot(years_array, amount_phd,color='r')
plt.xlabel('Age')
plt.ylabel('Net Worth (Dollars)')
plt.title('Net Worth')
plt.legend(['Bachelors','Masters','Phd'])

# End of program
plt.show()
