# gets financial and economic data from online sources

# imports
import pickle
import quandl

### created a fake account. PLEASE USE YOUR OWN TOKEN
api_token = 'eo4yQnjdYrzPr57LeQFi'

## Inflation over time -----------------------------------------------------
'''
INFLATION_DATA gets CPI inflation data from Quandl. The data is
stored in a pickle in the "stored_data" folder. If detail is set to 'annualy',
the data is formated from datetime datatype to int in (year, percent) pairs.

> should put in a check to make sure pickle data matches the desired dates and detail
'''
def inflation_data(data_set='FRED/FPCPITOTLZGUSA', start_date='1992-1-1',
                   end_date='2005-1-1', return_type='numpy',
                   detail='annualy', from_pickle=True, authtoken = api_token):

    # loads the pickled inflation data into variable called inflation
    if from_pickle:
        pickle_in = open('stored_data//inflation_data_q.pickle','rb')
        inflation = pickle.load(pickle_in)
        pickle_in.close()

    # Loads data from Quandl web service and writes it to pickle
    else:
        # Uses the Federal Reserve database on Quandl to return CPI data   
        inflation = quandl.get(data_set, start_date=start_date,
                               end_date=end_date, returns=return_type,
                               collapse=detail, authtoken=authtoken)
        
        # formatting data from datatime to numerical values
        if detail == 'annualy':
            for i in range(len(inflation)):
                inflation[i][1] = inflation[i][1]/100 
                inflation[i][0] = inflation[i][0].year 

        # storing data into pickle file in the stored data folder
        with open('stored_data//inflation_data_q.pickle','wb') as f:
                pickle.dump(inflation,f)
                f.close()    
    
    # end of function
    return inflation   
    

    
