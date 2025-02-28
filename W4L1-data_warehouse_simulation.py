# Program 1: Data Warehousing Simulation
import pandas as pd
import numpy as np

# Simulating a Data Warehouse with multiple datasets
sales_data = pd.DataFrame({
'Transaction_ID': np.arange(1, 1001),
'Customer_ID': np.random.randint(1, 500, 1000),
'Product_ID': np.random.randint (1000, 1100, 1000),
'Amount': np.random.uniform (10, 500, 1000),
'Date': pd.date_range(start='1/1/2023', periods=1000, freq='D')
})

customer_data = pd.DataFrame({
    'Customer_ID': np.arange(1, 500),
    'Name': [f'Customer {i}' for i in range(1, 500)],
    'Location': np.random.choice (['New York', 'London', 'Tokyo', 'Paris'],499)
})

# Merging datasets into a Data Warehouse
data_warehouse = sales_data.merge (customer_data, on='Customer_ID', how='left')
print("Data Warehouse Sample:")
print(data_warehouse.head())

# Program 2: Data Mart Simulation
# Creating a Finance Data Mart from Data Warehouse
finance_data_mart = data_warehouse[['Transaction_ID', 'Amount', 'Date', 'Location']]
print("Finance Data Mart Sample:")
print (finance_data_mart.head())

# Creating a Sales Data Mart
sales_data_mart = data_warehouse.groupby(['Location', 'Amount']).sum().reset_index()
print("Sales Data Mart Sample:")
print(sales_data_mart.head())