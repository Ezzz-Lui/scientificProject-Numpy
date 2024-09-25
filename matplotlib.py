#%% md
# 
#%% md
# # Matplotlib: Graphs, Plots, and Visualizations with Python
# plot() => Without any arguments, it will plot an empty graph or lineal graph, we can specify graph type with the help of 'kind' argument.
# 
# For example: 
# 1. object.plot(kind='bar')
# 2. object.plot(kind='pie')
# 3. object.plot(kind='barh')
# 4. object.plot(kind='scatter')
# 5. object.plot(kind='line')
#%% md
# # MATPLOTLIB WITH PANDAS 
# - How to integrate Matplotlib with Pandas in Python
# - Install or import pandas 
# - Install or import matplotlib
# - In this case we will use the same dataset as in the previous example (data folder)
#%%
import pandas as pd
#%%
data = pd.read_csv('./data/VentasPorProveedor.csv', skiprows=5, delimiter=';',decimal=',')
#%%
data.info() # verify the data has been loaded correctly
#%%
data.head(10) # the first 10 rows
#%% md
# # Matplotlib
#%%
import matplotlib.pyplot as plt
%matplotlib inline
#%%
products = data[data.Categoría == 'Vestimenta']
products.head(5)
#%%
products.Artículo.value_counts() # With value counts
#%%
products.Artículo.value_counts().plot(kind='line');
#%%
products.Artículo.value_counts().plot(kind='bar');
#%%
products.Artículo.value_counts().plot(kind='barh'); # 'h' means horizontal to differentiate from the vertical bar
#%%
products.Artículo.value_counts().plot(kind='pie'); # circular graph or pie chart
#%%
filterData = data.plot(kind='scatter', x='Unidades',y='Ganancia', color='green'); # scatter plot or dispersion graph
#%%
