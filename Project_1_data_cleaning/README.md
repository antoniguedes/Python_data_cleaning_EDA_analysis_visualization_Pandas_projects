# Data Cleaning of Customer Calls Data

## Overview

This Jupyter Notebook demonstrates a step-by-step process for data cleaning using Python and pandas. The goal is to prepare raw call logs for analysis by addressing common data quality issues such as missing values, inconsistent formats, and duplicates.

## Features

- Loading raw 'Customer Call List.xlsx' Excel file
- Removing duplicates
- Standardizing date and phone numbers
- Identifying, normalizing and handling missing data
- Exporting cleaned data for further analysis

<img width="933" height="675" alt="image" src="https://github.com/user-attachments/assets/4d1c3870-6f90-4aab-bbcc-69a0b88686d8" />


## Examples of Data Cleaning operations
**Removing Duplicate rows**
```python
# Remove duplicate rows from the dataframe to ensure data integrity with drop_duplicates() method
df1=df.drop_duplicates()
```

**Cleaning & Standardizing Phone Numbers**
```python
# Let's clean the phone numbers column: clean phone numbers by removing special characters (-, /, |)
df2["Phone_Number"]=df2["Phone_Number"].str.replace(r'[^a-zA-Z0-9]','',regex=True)
#Else to remove all non-digit characters from phone numbers you can use 
#df['phone'] = df['phone'].str.replace(r'[-/|]', '', regex=True)
df2["Phone_Number"]=df2["Phone_Number"].apply( lambda x: str(x))
df2["Phone_Number"]=df2["Phone_Number"].apply( lambda x: x[0:3]+'-'+ x[3:6]+'-'+x[6:10])
```

**Splitting columns**
```python
#Split the Address column into 3 columns for each type of information
df2[['Street_Address','State','Zip_Code']]=df2['Address'].str.split(',', n=2, expand=True)
```

**Replacing Missing or NULL values** 
```python
# Replace 'N/a' values with empty strings
# For NaN you need to use another method because it is not a string, it's a NULL value. Fill all NaN/null values with method fillna('') 
df2=df2.replace('N/a','')
df2=df2.fillna('')
```
**Dropping Not Useful Records with For Loop**
```python
df2_copy=df2.copy()
df2.dropna(subset='Phone_Number', inplace=True)
for x in df.index:
    if df2.loc[x,'Do_Not_Contact']=='Y':
       df2.drop(x, inplace=True)
```

## Output

At the end of the notebook, you can export (by uncomenting the below code lines) a cleaned version of the customer calls data saved as **Customer_Call_List_cleaned.csv**, ready for analysis or visualization.
```python
#If needed you can export the cleaned data after all cleaning operations to a csv using to_csv method
#df2_filtered.to_csv("Customer_Call_List_cleaned.csv", index=True, sep=";", encoding="utf-8")
```

---
## How to Use

1. Upload your **Customer_Calls_List.xlsx** dataset to the same directory as the notebook.
2. Open the notebook and run each cell sequentially.
3. Follow the comments and instructions for customizing the cleaning steps to your dataset.
4. Requirements:

- Python 3.x
- pandas package to import (_import pandas as pd_)
- Jupyter Notebook (**with Anaconda distribution Navigator is best**)

Install dependencies with (**not needed if you reading the file with Anaconda distribution interpreter**):
```bash
pip install pandas numpy jupyter
```



Le
t me know if you want this customized with more details or want the markdown file generated!
