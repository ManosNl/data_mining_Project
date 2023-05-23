import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

#importing the data set
df = pd.read_csv("data.csv")

# Selecting the columns that I want to include in the matrix: 
cols = ['Population', 'Daily tests', 'Cases', 'Deaths','Medical doctors per 1000 people','GDP/Capita',"Median age"]

# Creating a data frame with the upper (selected) columns using Pandas Library 
df_selected = df.loc[:, cols]

# Compute the correlation matrix
corr_matrix = df_selected.corr() 

# Ploting the cor.matrix as a heatmap -- Correlation Coefficients between -1 .. 1 
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title('Correlation Matrix for Covid-19 Data')
plt.show()