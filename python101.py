import pandas as pd
import numpy as np
import re

# Test 
print(pd.__version__)
print(np.__version__)

# file path p
file_path = "C:/Users/kknya/Documents/z_data/NB Data/InceptedNew.csv"

# Import the file
df = pd.read_csv(file_path,sep=",",encoding="Windows-1252")

# Clean the headers
df.columns = [re.sub(r'_+','_',re.sub(r'[^a-zA-Z0-9]','_',x)).lower() for x in df.columns]
print(df.head())
print(df.columns)

# Check date data types 
df['inception_month'] = pd.to_datetime(df['inception_month'])
print(df.loc[1:5,['policy_no','inception_month']].head())
df['yyyymm'] =[x.year*100+x.month for x in df['inception_month'] ]

# Update data columns
df['payment_date'] = pd.to_datetime(df['payment_date'])
df['transaction_date'] = pd.to_datetime(df['transaction_date'])


# Remove columns
df.drop(['inflation','acceptance_date','payment_date','transaction_date'],inplace=True,axis = 1)

# Check Data types
print(df.dtypes)

# Import excel files
product = (pd.read_excel(r"C:\Users\kknya\Documents\z_data\data_prep\dim_files\product_details.xlsx")
           .drop(['sdr_group','never_lapsed'],axis = 1)
           )

print(product.head())

# Merge 
df1 = pd.merge(
    df.drop(['product_name'],axis=1),
    product,how='left',
    left_on='product',
    right_on='product_code')


