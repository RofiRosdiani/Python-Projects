import json
import pandas as pd

#method 1 to import json file
json_file = open('loan_data_json.json')
data = json.load(json_file)

#method 2 to import json file
# with open('loan_data_json.json') as json_file1:
#     data1 = json.load(json_file1)

#transform list to table using pandas dataframe
data_loan = pd.DataFrame(data)

#finding unique values of spesific column (purpose column)
data_loan['purpose'].unique()

#describe the data
data_loan.describe()

#describe spesific column
data_loan['int.rate'].describe()

#import library numpy
import numpy as np

#using EXP() of numpy to get real income from log.annual.inc column
income = np.exp(data_loan['log.annual.inc'])

#adding income to column in data_loan
data_loan['annual_income'] = income

#using for loops and if conditional to get fico category from fico (credit score) column
length = len(data_loan)
ficocat = []
for x in range(0, length):
    category = data_loan['fico'][x]
    if category >= 300 and category < 400:
        cat = 'Very Poor'
    elif category >= 400 and category <= 600:
        cat = 'Poor'
    elif category >= 601 and category < 660:
        cat = 'Fair'
    elif category >= 660 and category < 780:
        cat = 'Good'
    else:
        cat = 'Excellent'
    ficocat.append(cat)
    
#testing error
# length = len(data_loan)
# ficocat = []
# for x in range(0, length):
#     category = data_loan['fico'][x]
    
#     try:
#         if category >= 300 and category < 400:
#             cat = 'Very Poor'
#         elif category >= 400 and category <= 600:
#             cat = 'Poor'
#         elif category >= 601 and category < 660:
#             cat = 'Fair'
#         elif category >= 660 and category < 780:
#             cat = 'Good'
#         else:
#             cat = 'Excellent'
#     except:
#         cat = 'Error - Unknown'        
        
#     ficocat.append(cat)
    
#fico series
fico = data_loan['fico']

#change datatype list to series using pandas series
ficocat = pd.Series(ficocat)

#adding series to data_loan
data_loan['fico_category'] = ficocat

##df.loc to conditional statement
#df.loc[df[columnname] condition, newcolumnname] = 'value is condition met'

#for interest rates, a new column is wanted, rate >= 0.12 then high, else low
data_loan.loc[data_loan['int.rate'] >= 0.12, 'int.rate.type'] = 'High'
data_loan.loc[data_loan['int.rate'] < 0.12, 'int.rate.type'] = 'Low'

##import matplotlib
import matplotlib.pyplot as plt

#number of loans/rows by fico_category
category_plot = data_loan.groupby(['fico_category']).size()
category_plot.plot.bar(color='green', width = 0.3)
plt.show()

#number of loans/rows by purpose
purpose_category = data_loan.groupby(['purpose']).size()
purpose_category.plot.bar(color='purple', width = 0.5)
plt.show()

#number of loans/rows by int.rate.type
IntRateType_category = data_loan.groupby(['int.rate.type']).size()
IntRateType_category.plot.bar(color='orange', width = 0.7)
plt.show()

##scatter plot
xpoint = data_loan['dti']
ypoint = data_loan['annual_income'] 
plt.scatter(xpoint, ypoint, color = 'green')
plt.show()

#to csv
data_loan.to_csv('Project2_Blue-Bank-Loan-Analysis.csv', index=True)











