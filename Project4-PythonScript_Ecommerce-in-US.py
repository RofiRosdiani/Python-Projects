# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 20:54:02 2023

@author: admin
"""

#import library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import main data
main_data = pd.read_csv('Order on Ecommerce in US.csv', sep=',')
main_data.head(5)

#check data
main_data.info()

#drop unnecessary columns
main_data = main_data.drop(main_data.columns[[6,7,8,9,10,12,13,14,15,18,19,20,21]], axis=1)
main_data.info()
main_data.head(10)

# #Check Misssing value
# missing_data = main_data1.isnull()
# missing_data.head(15)

# #Count missing values in each column
# for column in missing_data.columns.values.tolist():
#     print(column)
#     print (missing_data[column].value_counts())
#     print("")
    
# #check data type
# main_data1.dtypes

#split value into column
split_col = main_data['order_date'].str.split('/' , expand=True)

#add column
main_data['year'] = split_col[2]

#change column order_date into date data type
# from datetime import datetime
# main_data['year'] = pd.to_datetime(main_data['year'], format='%Y').dt.date
# main_data.info()

##merge main data with Order delivery in the US.csv
#import other dataset
delivery_status = pd.read_csv('Order delivery in the US.csv', sep=',')
delivery_status = delivery_status[['order_id', 'delivery_status']]

#merge
main_data_merge1 = pd.merge(main_data, delivery_status, on='order_id')


#filter by delivery_status = delivered
main_data_merge1 = main_data_merge1[main_data_merge1['delivery_status'] == 'DELIVERED']


#filter by payment_status = paid
main_data_merge1 = main_data_merge1[main_data_merge1['payment_status'] == 'PAID']

#define list of year that we want to filters
year = ['2018', '2019', '2020', '2021', '2022']

#return only rows where year is in the list of values
main_data_merge1 = main_data_merge1[main_data_merge1.year.isin(year)]

main_data_merge1.info()

##calculation
#total sales = sum(quantity)
#payment = quantity * price
#revenue = sum(payment)

#2019
filter_2019 = main_data_merge1['year'] == '2019'
df_2019 = main_data_merge1[filter_2019]
TotalSales_2019 = df_2019['quantity'].sum()
Revenue_2019 = df_2019['payment_amount'].sum().round(2)
print(f'Total sales 2019 = {TotalSales_2019} qty and Revenue 2019 = ${Revenue_2019}')

#2020
filter_2020 = main_data_merge1['year'] == '2020'
df_2020 = main_data_merge1[filter_2020]
TotalSales_2020 = df_2020['quantity'].sum()
Revenue_2020 = df_2020['payment_amount'].sum().round(2)
print(f'Total sales 2020 = {TotalSales_2020} qty and Revenue 2019 = ${Revenue_2020}')

#2021
filter_2021 = main_data_merge1['year'] == '2021'
df_2021 = main_data_merge1[filter_2021]
TotalSales_2021 = df_2021['quantity'].sum()
Revenue_2021 = df_2021['payment_amount'].sum().round(2)
print(f'Total sales 2021 = {TotalSales_2021} qty and Revenue 2021 = ${Revenue_2021}')


#2022
filter_2022 = main_data_merge1['year'] == '2022'
df_2022 = main_data_merge1[filter_2022]
TotalSales_2022 = df_2022['quantity'].sum()
Revenue_2022 = df_2022['payment_amount'].sum().round(2)
print(f'Total sales 2022 = {TotalSales_2022} qty and Revenue 2022 = ${Revenue_2022}')


# # initialize data of lists.
# table_sales_revenue = {'Total Sales (qty)': [217, 361, 10937, 1653],
#         'Revenue ($)': ['53558.84', '93663.55', '2777341.63', '415177.62']}
  
# # Creates pandas DataFrame.
# table_sales_revenue = pd.DataFrame(table_sales_revenue, index=['2019',
#                                               '2020',
#                                               '2021',
#                                               '2022'])

# %Growth Sales = (Sales Present - Sales Last Year) / Sales Last Year 
growth_sales_2020 = round((TotalSales_2020 - TotalSales_2019) / TotalSales_2019 * 100, 2)
growth_sales_2021 = round((TotalSales_2021 - TotalSales_2020) / TotalSales_2020 * 100, 2)
growth_sales_2022 = round((TotalSales_2022 - TotalSales_2021) / TotalSales_2021 * 100, 2)


# %Growth Revenue = (Revenue Present - Revenue Last Year) / Revenue Last Year 
growth_revenue_2020 = round((Revenue_2020 - Revenue_2019) / Revenue_2019 * 100, 2)
growth_revenue_2021 = round((Revenue_2021 - Revenue_2020) / Revenue_2020 * 100, 2)
growth_revenue_2022 = round((Revenue_2022 - Revenue_2021) / Revenue_2021 * 100, 2)

# initialize data of lists.
table_sales_revenue1 = {'2019': ['217 qty', '0%', '$ 53558.84', '0%'],
                        '2020': ['361 qty', '66.36%', '$ 93663.55', '74.88%'],
                        '2021': ['10937 qty', '2929.64%', '$ 2777341.63', '2865.23%'],
                        '2022': ['1653 qty', '-84.89%', '$ 415177.62', '-85.05%'],
                        }
  
# Creates pandas DataFrame.
table_sales_revenue1 = pd.DataFrame(table_sales_revenue1, index=['Total Sales',
                                              '%Growth Sales',
                                              'Revenue',
                                              '%Growth Revenue'])


## 2. total orders by e-commerce company
category_seller = main_data_merge1.groupby(['online_retail_seller']).size().sort_values(ascending=False)
category_seller.plot.barh(color='yellow', width = 0.3)
plt.title('eCommerce Company')
plt.xlabel('Total Orders')
plt.ylabel(None)
plt.show()

## 3. top selling products

#import data products
product = pd.read_csv('Product details on Ecommerce 2.csv', sep=',')
product.info()

#first row is null then i have to change first row to be column name
product = product.rename(columns=product.iloc[0]).drop(product.index[0])
product.info()

#only use product_name and number_of_reviews column
product1 = product[['product_id','product_name', 'number_of_reviews']]

#drop missing values
product1 = product1[product['product_name'].notnull()]

#import primary key from order details on ecommerce
primary_key = pd.read_csv('Order Details on Ecommerce in US.csv', sep=',')
primary_key.info()

primary_key = primary_key[['order_id', 'product_id']]

#merge main_data_merge1 with primary key
main_data_merge2 = pd.merge(main_data_merge1, primary_key, on='order_id')

#merge main_data_merge2 with product
main_data_merge2 = pd.merge(main_data_merge2, product1, on='product_id')

#group by product_name to get the top selling
category_product1 = main_data_merge2.groupby('product_name')['quantity', 'payment_amount'].sum().nlargest(5,'payment_amount')
category_product_sorted1 = category_product1.sort_values('payment_amount', ascending=True)
category_product_sorted1.plot.barh(color='yellow', width = 0.3, legend=None)
plt.title('Top Selling Products')
plt.xlabel('Total Revenue')
plt.ylabel(None)
plt.show()

#group by product_name to get the least selling
category_product2 = main_data_merge2.groupby('product_name')['quantity', 'payment_amount'].sum().nsmallest(5,'payment_amount')
category_product_sorted2 = category_product2.sort_values('payment_amount', ascending=True)
category_product_sorted2.plot.barh(color='yellow', width = 0.3, legend=None)
plt.title('Least Selling Products')
plt.xlabel('Total Revenue')
plt.ylabel(None)
plt.show()

#group by number_of_reviews
main_data_merge2['number_of_reviews'] = main_data_merge2['number_of_reviews'].astype(float)
count_number_of_reviews = main_data_merge2.groupby('product_name')['number_of_reviews'].mean()

##4. The most payment method used by customer 
most_payment_method = main_data_merge1.groupby(['payment_method']).size().sort_values(ascending=True)
most_payment_method.plot.barh(color='yellow', width = 0.3)
plt.title('The Most Payment Method')
plt.ylabel(None)
plt.show()

##Calculate numbers of male and female customers by age category

#import data_customer
data_customer = pd.read_csv('Customer dataset on Ecommerce.csv', sep=',', encoding='ANSI')
data_customer.head(5)

#check data
data_customer.info()
data_customer = data_customer[['customer_id', 'gender', 'age']]
data_customer['age'].unique()

#make a category of age

length = len(data_customer)
cat_age = []
for x in range(0, length):
    category = data_customer['age'][x]
    if category < 20:
        cat = '18-20'
    elif category >= 20 and category <= 29:
        cat = '20-29'
    elif category >= 30 and category <= 39:
        cat = '30-39'
    elif category >= 40 and category <= 49:
        cat = '40-49'
    elif category >= 50 and category <= 59:
        cat = '50-59'
    else:
        cat = '60-70'
    cat_age.append(cat)
    
#change datatype list to series using pandas series    
cat_age = pd.Series(cat_age)

#adding series to data_customer
data_customer['category_age'] = cat_age


#merge with main_data_merge2
main_data_merge3 = pd.merge(main_data_merge2, data_customer, on='customer_id')
groupby_category_age = main_data_merge3[['customer_id', 'payment_amount', 'gender', 
                                         'category_age']].sort_values('category_age')

#filter by gender
female = groupby_category_age[groupby_category_age['gender'] == 'Female']
male = groupby_category_age[groupby_category_age['gender'] == 'Male']

#group by gender
group_female = female.groupby(['gender', 'category_age'])['payment_amount'].sum()
group_male = male.groupby(['gender', 'category_age'])['payment_amount'].sum()


#graph by female
plt.ion()

group_female.plot.barh(color='pink', width = 0.3, legend=None)
plt.title('Numbers of Customer by Female')
plt.xlabel('Total Revenue')
plt.ylabel(None)
plt.show()

#graph by male
group_male.plot.barh(color='blue', width = 0.3, legend=None)
plt.title('Numbers of Customer by Male')
plt.xlabel('Total Revenue')
plt.ylabel(None)
plt.show()

#group by all gender
groupby_category_age1 = groupby_category_age.groupby(
    ['gender', 'category_age'])['payment_amount'].sum().sort_values()
groupby_category_age1.plot.barh(color=['blue', 'pink',
                                       'pink', 'blue', 
                                       'pink', 'blue',
                                       'pink', 'blue',
                                       'blue', 'pink',
                                       'blue', 'pink'], width = 0.3, legend=None)
plt.title('Numbers of Customer by Category Age')
plt.xlabel('Total Revenue')
plt.ylabel(None)
plt.show()


#group by all gender other preference
groupby_category_age2 = groupby_category_age.groupby(
    ['gender', 'category_age'])['payment_amount'].sum()
groupby_category_age2.plot.barh(color=['pink', 'pink',
                                       'pink', 'pink', 
                                       'pink', 'pink',
                                       'blue', 'blue',
                                       'blue', 'blue',
                                       'blue', 'blue'], width = 0.3, legend=None)
plt.title('Numbers of Customer by Gender')
plt.xlabel('Total Revenue')
plt.ylabel(None)
plt.show()




















