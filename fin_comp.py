# fin_comp is short for financial computations
# Contatins functions that do common financial calulations
# as well as test data generation

# imports 
import numpy as np


## Calculates total investment worth over time
def total_investment_value(rate, amount, time, contribution, over_time=True):
    # RATE is the return on investment for every year.
    # AMOUNT is the net worth of the investment account.
    #   This should be a scalar value which is the initial amount put into the account.
    #   AMOUNT can be returned as a scaler or vector depending on OVER_TIME
    # TIME is the total years the investment account is held for
    # CONTRIBUTION is the amount contributed to the account every year
    #   in addition to the return earned.
    # OVER_TIME is the parameter that determines if the AMOUNT for every year is returned,
    #   or just the final value of the account. If True, then the array, AMOUNT, is returned
    #   If False, then the final value of amount if returned.


    # Creates the returned array by making the first item the value AMOUNT 
    amount = np.insert(np.zeros(len(contribution)-1),0,amount)

    # calulates the net worth of the investment account for each year and stores it in amount
    for i in range(1, time):
        interest =  amount[i-1]*rate[i-1]
        amount[i] = amount[i-1] + interest + contribution[i-1]

    # returns either the whole amount array or the final value depeding on OVER_TIME
    if over_time:
        return amount
    else:
        return amount[-1]


# Generates investment contribution data
def contribution_over_time(contribution_levels, years_spent):
    # CONTRIBUTION_LEVELS is a numpy array of the dollar amounts contributed
    #   to an account for every era in ones life. 
    # YEARS_SPENT is a numpy array of the years spent at each point in ones life
    # Ex: YEAR_SPENT = np.array([4, 5, 10]) 4 years in college, 5 years in PhD., and 10 years working
    #   the corresponding CONTRIBUTION_LEVELS would be np.array([100, 500, 20000])
    #   meaning 100 dollars contributed while in college, 500 dollars contribtued while in PhD.
    
    # creates the returned array that is the contribution amount for every year 
    contribution = np.zeros(sum(years_spent))
    
    # adds a zero to the beginning of program_years for ease of for loop
    years_spent = np.insert(years_spent,0,0)

    # assigns contribution values to their correstponding years
    for i in range(len(contribution_levels)):
        contribution[sum(years_spent[:i+1]):sum(years_spent[:i+2])] = contribution_levels[i]
                
    return contribution

def federal_income_tax(salary):
    '''
    Uses data from
    https://www.irs.gov/pub/irs-drop/rp-16-55.pdf
    level of taxation per level of income
    to calculate the amount of tax paid     
    '''
    # uses a series of if statements to determine the corret tax bracket,
    # then determines how much tax must be paid based on that rate
    pass # temporary place holder

    
    
        
    

    

















    

