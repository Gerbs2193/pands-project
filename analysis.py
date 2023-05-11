""" what to do/check list

Load the Iris dataset into a pandas dataframe and display the first few rows/then all
Output a summary of each variable to the console
Save a histogram of each variable to a png file
Output a summary of each variable to a text file
Create a scatter plot of sepal length vs sepal width and save it to a png file
Create scatter plots the var comparisona - sepal length vs petal length, sepal length vs petal width, sepal width vs petal length, and sepal width vs petal width, and save each to a png file
Add labels and titles to the scatter plots
Color the scatter plots by class
Create function to generate scatter plots for any two variables and save them to png files """

#Import the required libraries for data analysis and visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load the Iris dataset into a pandas dataframe, iris.data in same directory as PANDS-PROJECT
#Read the Iris dataset from a CSV file
iris = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
#Calculate ghe mean feature values for each class of Iris flower
#Group the data by Iris class and calculate the mean of each feature
iris_mean = iris.groupby('class').mean()
#Create a bar chart to visualize the mean feature values for each Iris class
iris_mean.plot(kind='bar')
#Plot the mean feature values as a bar chart
#Set the title and labels for the bar chart
plt.title('Mean Feature Values for Each Iris Class')
plt.xlabel('Class')
plt.ylabel('Feature Value')

#Save the bar chart as a PNG image file
plt.savefig('iris_bar_chart.png')
#Display the bar chart
plt.show()
#Now I predict the species of Iris flowers based on its sepal length
#Define a function to predict the species based on its sepal length
def predict_species(sepal_length):
    if sepal_length < 5.84:
        return 'Iris-setosa'
    elif sepal_length < 6.62:
        return 'Iris-versicolor'
    else:
        return 'Iris-virginica'

#Apply the predict_species function to the sepal length column 
iris['predicted_species'] = iris['sepal_length'].apply(predict_species)
#Save the dataframe with the predicted species to a CSV file
iris.to_csv('iris_predicted_species.csv', index=False)
#Create a scatter plot matrix to visualize the relationships between different variables
sns.pairplot(iris, hue='class')
#Use the seaborn library to create a scatter plot matrix
#Save the scatter plot matrix as a PNG image file
plt.savefig('scatter_plot_matrix.png')
#Close the scatter plot matrix figure
plt.close()

#Import the required libraries for data analysis and visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset into a pandas dataframe
iris = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

#Create violin plots to visualize the distribution of each variable by class
variables = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
for variable in variables:
    plt.figure(figsize=(8, 6))
    sns.violinplot(x='class', y=variable, data=iris)
    #Set the labels and title for the violin plot
    plt.xlabel('Class')
    plt.ylabel(variable)
    plt.title(f'Violin Plot: {variable} by Class')
    
    #Save the violin plot as a PNG image file
    plt.savefig(f'violin_plot_{variable}.png')
    
    #Close the violin plot figure
    plt.close()

# Create scatter plots to visualize the relationships between different variables
variables = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
for i in range(len(variables)):
    for j in range(i + 1, len(variables)):
        var1 = variables[i]
        var2 = variables[j]
        plt.scatter(iris[var1], iris[var2])
        
        #Set the labels and title for the scatter plot
        plt.xlabel(var1)
        plt.ylabel(var2)
        plt.title(f'Scatter Plot: {var1} vs {var2}')
        
        #Save the scatter plot as a PNG image file
        plt.savefig(f'{var1}_vs_{var2}.png')
        
        #Close the scatter plot figure
        plt.close()

# Import the required libraries for data analysis and visualization
import pandas as pd
import matplotlib.pyplot as plt

#Load the Iris dataset into a pandas dataframe
iris = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

#Create histograms to visualize the distribution of each variable
variables = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
iris.hist(column=variables, grid=False)
#Set title and layout for th hists
plt.suptitle('Histograms of Iris Variables')
plt.tight_layout()
#Save the hists as a (single)PNG image file
plt.savefig('histograms.png')
#Display the hists
plt.show()

#Load the Iris dataset into a pandas dataframe
iris = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
#Get the statistical descriptions of the variables
var_descriptions = iris.describe()
#Write he variable descriptions to a text file
with open('variable_descriptions.txt', 'w') as f:
    f.write(str(var_descriptions))

#Load the Iris dataset into a pandas dataframe
iris = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
#Calculate the correlation coefficients
correlation = iris.iloc[:, :-1].corr()
#Write the correlation coefficients to a text file
correlation.to_csv('correlation_coefficients.txt', sep='\t')