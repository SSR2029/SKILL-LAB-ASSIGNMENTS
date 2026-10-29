
import numpy as np
import pandas as pd


# 1. DataFrame Product

df = pd.DataFrame(
    np.random.randint(1, 10, (5, 3)),
    columns=['A', 'B', 'C']
)

df['Product'] = df['A'] * df['B']

print("1.")
print(df)


# 2. Row-wise and Column-wise Sum

df = pd.DataFrame(
    np.random.randint(1, 10, (4, 3)),
    columns=['A', 'B', 'C']
)

print("2.")
print("Row sum:")
print(df.sum(axis=1))
print("Column sum:")
print(df.sum(axis=0))


# 3. Fill NaN with Column Mean

df = pd.DataFrame(
    np.random.randint(1, 10, (5, 3)),
    columns=['A', 'B', 'C']
)

df.iloc[1, 0] = np.nan
df.iloc[3, 1] = np.nan

df = df.fillna(df.mean())

print("3.")
print(df)


# 4. Drop Rows with NaN

df = pd.DataFrame(
    np.random.randint(1, 10, (6, 4)),
    columns=['A', 'B', 'C', 'D']
)

df.iloc[1, 0] = np.nan
df.iloc[4, 2] = np.nan

df = df.dropna()

print("4.")
print(df)


# 5. Data Aggregation

df = pd.DataFrame({
    'Category': np.random.choice(['A', 'B', 'C'], 10),
    'Value': np.random.randint(1, 50, 10)
})

result = df.groupby('Category')['Value'].agg(['sum', 'mean'])

print("5.")
print(result)


# 6. Total Sales by Category

df = pd.DataFrame({
    'Product': ['Pen', 'Book', 'Bag', 'Pencil', 'Bottle'],
    'Category': ['A', 'B', 'A', 'B', 'A'],
    'Sales': np.random.randint(100, 500, 5)
})

result = df.groupby('Category')['Sales'].sum()

print("6.")
print(result)


# 7. Merging DataFrames

df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Tom', 'Andy', 'Lucas']
})

df2 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Marks': [80, 90, 85]
})

result = pd.merge(df1, df2, on='ID')

print("7.")
print(result)


# 8. MultiIndex DataFrame and Indexing

df = pd.DataFrame(
    {'Value': [10, 20, 30, 40]},
    index=pd.MultiIndex.from_tuples(
        [('A', 1), ('A', 2), ('B', 1), ('B', 2)],
        names=['Category', 'Number']
    )
)

print("8.")
print(df)
print("Category A:")
print(df.loc['A'])
print("Category B:")
print(df.loc['B'])


# 9. MultiIndex Category and SubCategory

df = pd.DataFrame({
    'Category': ['A', 'A', 'B', 'B'],
    'SubCategory': ['X', 'Y', 'X', 'Y'],
    'Value': [10, 20, 30, 40]
})

df = df.set_index(['Category', 'SubCategory'])

print("9.")
print(df)
print(df.groupby(level=['Category', 'SubCategory'])['Value'].sum())


# 10. Double Values

df = pd.DataFrame(
    np.random.randint(1, 10, (5, 3)),
    columns=['A', 'B', 'C']
)

result = df.apply(lambda x: x * 2)

print("10.")
print(result)


# 11. Lambda Sum Column

df = pd.DataFrame(
    np.random.randint(1, 10, (6, 3)),
    columns=['A', 'B', 'C']
)

df['Sum'] = df.apply(
    lambda x: x['A'] + x['B'] + x['C'],
    axis=1
)

print("11.")
print(df)


# 12. Convert Text to Uppercase

series = pd.Series([
    'hello', 'python', 'pandas', 'numpy', 'world'
])

series = series.str.upper()

print("12.")
print(series)


# 13. First Three Characters

series = pd.Series([
    'hello', 'python', 'pandas', 'numpy', 'world'
])

result = series.str[:3]

print("13.")
print(result)
