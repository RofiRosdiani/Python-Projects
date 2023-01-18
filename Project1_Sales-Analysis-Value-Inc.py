#import library
import pandas as pd

#import csv file with pandas
data = pd.read_csv('transaction.csv', sep=';')

#summary of the data
data.info()

#check data type
# month = object , time = object, 

data['Year'] = data['Year'].astype(str)
data['Month'] = data['Month'].astype(str)
data['Day'] = data['Day'].astype(str)
data.info()

#concate date
data['date'] = data['Day'] + " " + data['Month'] + " " + data['Year']


#change date type: str into datetime
from datetime import datetime
data['date'] = pd.to_datetime(data['date'], format='%d %b %Y').dt.date
data['date'] = data['date'].astype('datetime64[ns]')

#calculation
CostPerItem = data['CostPerItem']
SellingPricePerItem = data['SellingPricePerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']

#mathematical on Tableau

#calculating Profit has 2 ways
#1
#Profit per Item = Sales - Cost
#Profit per Transaction = Profit per Item * Number item purchased
ProfitPerItem = SellingPricePerItem - CostPerItem
ProfitPerTransaction = ProfitPerItem * NumberOfItemsPurchased

#2
#calculating CostPerTransaction
CostPerTransaction = CostPerItem * NumberOfItemsPurchased
#calculating SalesPerTransaction
SalesPerTransaction = SellingPricePerItem * NumberOfItemsPurchased
#calculating Profit per Transaction
#ProfitPerTransaction = SalesPerTransaction - CostPerTransaction

#calculating Mark Up = Sales - Cost / Cost 
MarkUp_Item = (SellingPricePerItem - CostPerItem) / CostPerItem
#or
#MarkUp_Transaction = (SalesPerTransaction - CostPerTransaction) / CostPerTransaction

#adding a new column to dataframe
data['CostPerTransaction'] = CostPerTransaction
data['SalesPerTransaction'] = SalesPerTransaction
data['ProfitPerTransaction'] = ProfitPerTransaction
data['MarkUp'] = MarkUp_Item

#rounding markup into 2 decimals only
roundmarkup = round(data['MarkUp'], 2)
data['MarkUp'] = round(data['MarkUp'], 2)

#split value into column
split_col = data['ClientKeywords'].str.split(',' , expand=True)

#add column
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

#replace values bracket [] and mark ''
data['ClientAge'] = data['ClientAge'].str.replace('[', '')
data['ClientAge'] = data['ClientAge'].str.replace("'", '')
data['ClientType'] = data['ClientType'].str.replace("'", "")
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']', '')
data['LengthOfContract'] = data['LengthOfContract'].str.replace("'", "")

#lower case
data['ItemDescription'] = data['ItemDescription'].str.lower()

#import other dataset
seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#merge
data_merge = pd.merge(data, seasons, on='Month')

#dropping column
data_merge = data_merge.drop('ClientKeywords', axis=1)
# data_merge = data_merge.drop(['Year', 'Month', 'Day'], axis=1)

#export to csv
data_merge.to_csv('Project1_Sales-Analysis-Value-Inc.csv', index=False)











