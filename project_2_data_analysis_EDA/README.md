# Data Analysis & EDA with Python Pandas, Matplotlib, Seaborn

## 📊 Overview

This project presents an Exploratory Data Analysis (EDA) on the **world_population.csv** dataset. The goal is to show how you can quickly grasp a dataset to start understanding your data and visualizing it using Python and Pandas.
It will show trends and insights in global population statistics over the last 50 years.

## 🌍 Dataset
- **File:** `world_population.csv`
- **Source:** [Kaggle World Population Data upto 2022](https://www.kaggle.com/datasets/iamsouravbanerjee/world-population-dataset)]
- **Description:** Contains population data for countries worldwide, including metrics such as total population, density, growth rates, and more.

## 🚀 Objectives
- Visualize global population distribution and trends
- Identify top and bottom countries by population
- Explore correlations between population and other variables
- Highlight key findings and insights

<img width="1108" height="803" alt="image" src="https://github.com/user-attachments/assets/f2ba3552-13ca-4d5b-a63a-bb8c65874281" />

## 📑 Project Structure

👀 First Look at Data  
ℹ️ Info()  
📊 Describe()  
🚫 Counting all Null Values & Unique Values
```python
df.null().sum()
df.nunique()
# looking for unique values in each countries, non unique values are null values for most
``` 
📑 Sorting on Values  
🔗 Correlation between Columns  
```python
# Let's change the pandas display format to see 2 decimals at least for correlations
pd.options.display.float_format = '{:,.2f}'.format
# First, we need to select only the numeric columns for correlation
# Filter out non-numeric columns before calculating correlation
numeric_df = df.select_dtypes(include=['float64', 'int64'])
numeric_df.corr()
```
🌡️ Heatmap using Seaborn  
👥 Grouping Data by Continent  
 ```python
# Let's look at the world population by Continent then sort the Continents by their 2022 Population 
# Specify only numeric columns when calculating mean with numeric_only=True
dfc=df.groupby('Continent').mean(numeric_only=True).sort_values(by='2022 Population', ascending=False)
dfc.plot()
...
# Reverse the order of columns in the DataFrame. This creates a new DataFrame with columns in reverse order without modifying the original
dfc.columns[::-1]
...
# Transpose the DataFrame 'dfc' to convert rows to columns and columns to rows
# This is useful for changing the orientation of the data for different analysis perspectives
dfc3=dfc2.transpose()
 ```
📈 Visualizing Grouped Data  
📦 Boxplots for Outliers  
```python
# Create a boxplot visualization of all numeric columns in the dataframe
# It is useful to spot the outliers (isolated dots at the top) from a data distribution as well as the mean (below box) and the median 
df.boxplot(figsize=(20,10))
```
🏷️ Data Types of Columns  

## 📈 Key Visualizations

- Top 10 most populous countries
- Population distribution by continent
- Trends over time (if available)
- Density and growth rate comparisons
<img width="1106" height="683" alt="image" src="https://github.com/user-attachments/assets/aac62168-89d2-4e6a-beac-45f3cfdac0e8" />


## ✨ Some Trends

- [Asia population rise happened in the years 2000 where they took off, India's still rising]
- [China and India represent each 18% of the world population, therefore 36% combined]
- [There is a 0.5 correlation between population and country size area]
- [The smallest country is the Vatican with 510 inhabitants]

  <img width="881" height="519" alt="image" src="https://github.com/user-attachments/assets/e2b28b6d-0cae-4d3a-8c55-a3b36791cfb2" />

## 🛠️ Technologies Used & Requirements
- Python 3.x
- Jupyter Notebook (best installed with Anaconda distribution Navigator)
- Pandas
- Matplotlib / Seaborn

