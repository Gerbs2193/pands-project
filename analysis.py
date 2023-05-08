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
import matplotlib.pyplot as plt

# Load the iris dataset
iris = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

# Group the data by class and get the mean of each feature
iris_mean = iris.groupby('class').mean()

# Create a bar chart of the mean feature values for each class
iris_mean.plot(kind='bar')
plt.title('Mean Feature Values for Each Iris Class')
plt.xlabel('Class')
plt.ylabel('Feature Value')

# Save the bar chart as a PNG file
plt.savefig('iris_bar_chart.png')

# Display the bar chart
plt.show()