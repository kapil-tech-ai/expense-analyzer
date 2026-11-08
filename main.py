import pandas as pd
import numpy as np
df = pd.read_csv("expense-analyzer.csv")
print(df)
total_expense = df['Amount'].sum()
print("Total Expense:",
      total_expense)
avg_expense = df['Amount'].mean()
print("Average Expense:",
      avg_expense)
max_expense = df['Amount'].max()
print("Maximum Expense:", max_expense)
min_expense = df['Amount'].min()
print("Minimum Expense:", min_expense)
category_expense = df.groupby('Category')['Amount'].sum()
print("\n Expense by Category:")
print(category_expense)
