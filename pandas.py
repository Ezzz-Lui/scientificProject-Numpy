#%% md
# # Jupyter Notebook + Python + Pandas
# 
# Ingresar y visualizar datos con Pandas
#%% md
# ## Import Pandas
# 1. pandas
#%%
import pandas as pd
#%% md
# ## Read data and import to DataFrame
# #### 1. read_csv
# #### 2. import csv file (into data folder)
# #### 3. "Skip-rows" uses for skip the first 5 lines in the csv file
# #### 4. "Delimiter" uses for separate the data in the file with ";"
# 
#%%
data = pd.read_csv('./data/VentasPorProveedor.csv', skiprows=5,delimiter=';')
#%% md
# ## Show data
#%%
data
#%% md
# ## Show dataframe dimensions (Shape[])
# 1. Shape[0] = Number of rows
# 2. Shape[1] = Number of columns
# 3. shape = (rows, columns)
#%%
data.shape
#%%
data.shape[0]
#%%
data.shape[1]
#%% md
# ## Show the first 5 rows (head[])
# 1. head() = Show the first 5 rows
# 2. By default, head() show the first 5 rows
#%%
data.head()
#%%
data.head(10)
#%% md
# ## Show the last 5 rows (tail[])
#%%
data.tail()
#%% md
# ## Show dataframe information (info())
# 1. info() = Show the dataframe information as the number of rows, columns, data types, and memory usage
#%%
data.info()
#%% md
# ## Show counts with value_counts()
# 1. value_counts() = Show the counts of the unique values in the column of the series
# 2. We can specify order the values with the parameter "ascending=True/False", by default ascending=True
#%%
data.Vendedor.value_counts()
#%%
data.Región.value_counts()
#%%
data.Artículo.value_counts()
#%%
data.Vendedor.value_counts(ascending=True)
#%% md
# # If exists null values (dropna=False)
# 1. dropna delete the null values or rows with null values and exclude from the count, by default dropna=True
#%%
data.Vendedor.value_counts(dropna=False)
#%% md
# ## Sort Values (sort_values())
# 1. object.sort_values(axis=0), axis=0 is the default value
# 2. na_position='first' or 'last' for the position of the null values
# 3. for multiple columns, we can use the parameter by=['column1', 'column2']
#%%
data.Vendedor.sort_values()
#%%
data.sort_values(by=['Vendedor', 'Ganancia'])
#%% md
# ## Boolean Indexing
# 1. We can find the rows that meet a condition for example search all rows where the column or serie 
# 'Articulo' is equal to 'Gorras'.
# 2. We can apply multiple conditions with the operators "&" for "and" and "|" for "or"
# 3. If we only write 'data.Articulo == 'Gorras' we can see the rows that meet the condition(True or False) and this is not useful
# 4. For multiple conditions, we need to use parentheses for each condition:
#     data[(data.Articulo == 'Gorras') & (data.Region == 'Norte')] or
#     object[(condition1) & (condition2)]
#%%
data[data.Artículo == 'Gorras']
#%%
data.Artículo == 'Gorras'
#%%
data[(data.Artículo == 'Gorras') & (data.Región == 'Norte')]
#%% md
# ## Strings (str attribute)
# 1. We can use the string methods with the str attribute
#%%
data.Vendedor.str.contains('Trevor') # Not is useful
#%%
data[data.Vendedor.str.contains('Trevor')] # Useful
#%%
