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
Refactor the code to make it more modular and reusable

import pandas as pd

# Load the iris dataset into a pandas dataframe
iris = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

# Display the first few rows of the dataframe
print(iris.head())

import pandas as pd
iris = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
print(iris)
import pandas as pd 
'''
'''import pandas as pd
# Load the iris dataset into a pandas dataframe
iris = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
# Output a summary of each variable to the console
print(iris.describe())'''

import pandas as pd

'''# Load the iris dataset into a pandas dataframe
iris = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

# Get the variable descriptions
var_descriptions = iris.describe()

# Write the variable descriptions to a text file
with open('variable_descriptions.txt', 'w') as f:
    f.write(str(var_descriptions))
'''
'''import pandas as pd
import matplotlib.pyplot as plt

# Load the iris dataset into a pandas dataframe
iris = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

# Generate the histogram
plt.hist(iris['sepal_length'], bins=20)
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.title('Histogram of Sepal Length')
plt.savefig('sepal_length_histogram.png')
plt.show()'''

'''import pandas as pd
import matplotlib.pyplot as plt

# Load the iris dataset into a pandas dataframe
iris = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

# Generate the histogram
plt.hist(iris['sepal_width'], bins=20)
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.title('Histogram of Sepal Width')
plt.savefig('sepal_width_histogram.png')
plt.show()'''

'''import pandas as pd
import matplotlib.pyplot as plt

# Load the iris dataset into a pandas dataframe
iris = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

# Generate the histogram
plt.hist(iris['petal_length'], bins=20)
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.title('Histogram of Petal Length')
plt.savefig('petal_length_histogram.png')
plt.show()'''

import pandas as pd
import matplotlib.pyplot as plt

# Load the iris dataset into a pandas dataframe
iris = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

# Generate the histogram
plt.hist(iris['petal_width'], bins=20)
plt.xlabel('Petal Width (cm)')
plt.ylabel('Frequency')
plt.title('Histogram of Petal Width')
plt.savefig('petal_width_histogram.png')
plt.show()

