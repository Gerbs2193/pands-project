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

'''import pandas as pd

# Load the iris dataset
iris = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
# Define the function to predict the species based on sepal length
def predict_species(sepal_length):
    if sepal_length < 5.84:
        return 'Iris-setosa'
    elif sepal_length < 6.62:
        return 'Iris-versicolor'
    else:
        return 'Iris-virginica'

# Apply the function to the sepal length column and store the predicted species in a new column
iris['predicted_species'] = iris['sepal_length'].apply(predict_species)

# Save the dataframe to a CSV file
iris.to_csv('iris_predicted_species.csv', index=False)'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
iris = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

# Create a scatter plot matrix
sns.pairplot(iris, hue='class')

# Save the plot to a PNG file
plt.savefig('scatter_plot_matrix.png')