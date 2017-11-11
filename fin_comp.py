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


# Calculates the income tax level for a given salary or an array of salaries
def federal_income_tax(salary):
    '''
    Uses data from
    https://www.irs.gov/pub/irs-drop/rp-16-55.pdf
    level of taxation per level of income
    to calculate the amount of tax paid     
    '''
    # uses a series of if statements to determine the corret tax bracket,
    # then determines how much tax must be paid based on that rate

    # determines if salary is a scaler or a vector
    if type(salary) == "numpy.ndarra":

        # creates an array of the tax for every salary passed
        tax = np.zeros(len(salary))

        # determines the federal tax for level of salary
        for i in range(len(salary)):
            if salary[i] < 18650:
                tax[i] = salary[i]*0.1
            elif salary[i] >= 18650 and salary[i] < 75900:
                tax[i] = 1865 + 0.15*(salary[i]-18650)
            elif salary[i] >= 75900 and salary[i] < 153100:
                tax[i] = 10452.5 + 0.25*(salary[i]-75900)
            elif salary[i] >= 153100 and salary[i] < 233350:
                tax[i]= 29752.5 + 0.28*(salary[i]-153100)
            elif salary[i] >= 233350 and salary[i] < 416700:
                tax[i] = 52222.5 + 0.3*(salary[i]-233350)
            elif salary[i] >= 416700 and salary[i] < 470700:
                tax[i] = 112728 + 0.35*(salary[i]-416700)
            elif salary[i] >= 470700:
                tax[i] = 131628 + 0.396*(salary[i]-470700)
        return tax
    
    else: # Scalar version of salary
        if salary < 18650:
            return salary*0.1
        elif salary >= 18650 and salary < 75900:
            return 1865 + 0.15*(salary-18650)
        elif salary >= 75900 and salary < 153100:
            return 10452.5 + 0.25*(salary-75900)
        elif salary >= 153100 and salary < 233350:
            return 29752.5 + 0.28*(salary-153100)
        elif salary >= 233350 and salary < 416700:
            return 52222.5 + 0.3*(salary-233350)
        elif salary >= 416700 and salary < 470700:
            return 112728 + 0.35*(salary-416700)
        elif salary >= 470700:
            return 131628 + 0.396*(salary-470700)
        

# Generates investment contribution data
def contribution_over_time(salary_levels, living_expense_levels, additional_expense_levels, years_spent):
    # SALARY_LEVELS is a numpy array of the salaries estimated for each era of life, in dollars.
    # LIVING_EXPENSE_LEVELS is a numpy array of estimated living expenses for each era.
    # ADDITIONAL_EXPENSE_LEVELS is a numpy array of estimated additional expenses for each era.
    # YEARS_SPENT is a numpy array of the years spent at each point in ones life
    # Ex: YEAR_SPENT = np.array([4, 5, 10]) 4 years in college, 5 years in PhD., and 10 years working
    #   the corresponding CONTRIBUTION_LEVELS would be np.array([100, 500, 20000])
    #   meaning 100 dollars contributed while in college, 500 dollars contribtued while in PhD.
    
    # Ensures consistent number of eras
    n_eras = years_spent.size
    if (salary_levels.size != n_eras) or (living_expense_levels.size != n_eras) or (additional_expense_levels.size != n_eras):
       print("Number of eras is inconsistent. Please enter arrays of the same size")
       return

    # creates the returned array that is the contribution amount for every year 
    contribution = np.zeros(sum(years_spent))
    
    # adds a zero to the beginning of program_years for ease of for loop
    years_spent = np.insert(years_spent,0,0)

    # assigns contribution values to their correstponding years
    for i in range(n_eras):
        amount = salary_levels[i]               # Salary
        amount -= federal_income_tax(amount)    # After taxes
        amount -= living_expense_levels[i]      # Factor for living expenses
        amount -= additional_expense_levels[i]  # Factor for other expenses
        contribution[sum(years_spent[:i+1]):sum(years_spent[:i+2])] = amount
                
    return contribution














    

