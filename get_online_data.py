# gets financial and economic data from online sources
# Sources are:
'''

'''

# imports
import pandas as pd

## Inflation over time -----------------------------------------------------
# use pandas to read data from
inflation = pd.read_html('http://www.inflation.eu/inflation-rates/united-states/historic-inflation/cpi-inflation-united-states.aspx',match='CPI United States',header=0)
inflation = inflation[2]
df1 = inflation[['annual inflation (dec vs. dec)','inflation']]
df2 = inflation[['annual inflation (dec vs. dec).1','inflation.1']]
df2.columns = ['annual inflation (dec vs. dec)','inflation']

inflation = pd.concat([df1,df2])
inflation = inflation['inflation']
#inflation = inflation[-1:-1:1]
print(inflation)
