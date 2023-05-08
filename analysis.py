#what to do/check list
'''
Load the Iris dataset into a pandas dataframe and display the first few rows/then all
Output a summary of each variable to the console
Save a histogram of each variable to a png file
Output a summary of each variable to a text file
Create a scatter plot of sepal length vs sepal width and save it to a png file
Create scatter plots of sepal length vs petal length, sepal length vs petal width, sepal width vs petal length, and sepal width vs petal width, and save each to a png file
Add labels and titles to the scatter plots
Color the scatter plots by class
Create a function to generate scatter plots for any two variables and save them to png files
Refactor the code to make it more modular and reusable'''



import pandas as pd

# Load the iris dataset into a pandas dataframe
iris = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

# Calculate summary statistics for each variable
summary_stats = iris.describe()

#Write the summary statistics to a text file
with open('iris_summary.txt', 'w') as f:
    f.write(summary_stats.to_string())