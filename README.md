#
Iris-data set

##
What is it?

The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis.[1] It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species.[2] Two of the three species were collected in the Gaspé Peninsula "all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus".[3]
The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other - www.kaggle.com. (n.d.). Iris Dataset. [online] Available at: https://www.kaggle.com/datasets/vikrishnan/iris-dataset. That is the definition from kaggle - however I will detail my understanding of it below.

The iris dataset is a collection of information on three different types of flowers: setosa, versicolor, and virginica. Each of these flowers has measurements taken of its sepals (green leaf-likes at the base of the flower) and petals (colourful structures that make up the flower itself).I refer to these three flowers a sclasses. 

For each of the above different classes, there are 4 variables. These are; sepal length, sepal width, petal length, and petal width. These measurements are all given in centimeters. These variables describe different physical characteristics of iris flowers. Sepals are the green leaf-like structures that protect the flower bud and petals are the colourful structures that surround the reproductive parts of the flower. So, the dataset contains measurements of these different parts of the flower for different iris species.

The dataset contains a grand total of 150 different flowers, with 50 of each type. This dataset is often used as an example in machine learning because it is small, 'easy' to understand and has a clear classification problem. For this project, however, machine learning will not be used as it is beyind the scope of my capabilities. Ratrher, the project attempts to show how different attributes of the flowers are related to each other and how these attributes can be used to distinguish between the three different species mentioned above. By creating histograms, scatter plots, bar charts, violin plots, summary descriptions of the variables, a scatter plot matrix and a correlation coefficient - I hope to visualize these relationships and gain a better understanding of the dataset. Overall, the project attempts to demonstrate how data analysis and visualization techniques can be used to gain insights into complex datasets, without relying on advanced machine learning algorithms to do so. There will be references throughout of alternative and often more complex and informative ways to achieve tios understanding completed by other sources. This will help educate the reader on the possibilites of the data analytics -8of the Iris data 

sources so far; https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html
https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/04_plotting.html#min-tut-04-plotting
https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_hist.html
https://seaborn.pydata.org/examples/scatterplot_matrix.html
https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html
https://www.kaggle.com/datasets/vikrishnan/iris-dataset

##
Introduction                                                    

This Iris dataset analysis project aims to explore and gain insights into the relationships between various attributes of Iris flowers. The dataset consists of measurements of sepal length, sepal width, petal length and petal width for 150 Iris flowers. Along with the attribute measurements, each flower is classified into one of three species: setosa, versicolor, or virginic or classes as I refer to them. 

The main objective of this project is to analyze the dataset using statistical and data visualization techniques, without relying on complex machine learning algorithms. By leveraging the power of Python programming language and popular libraries like Pandas, Matplotlib, and Seaborn, I aim to uncover patterns and insights within the dataset that most could do with a basic python programming understanding. 

By examining the relationships between the attributes and the flower species, this project seeks to answer questions such as:

How do the attribute values differ between the different species of Iris flowers?
Are there any strong correlations or dependencies among the attribute measurements?
Can I visually distinguish one species from another based on the attribute values?
What can I lean about the Iris flowers by analzing their attribute distributions and relationships?
By focusing on exploratory data analysis techniques and visualizations, dhis project offers a beginner-friendly approach to understanding the Iris dataset. It provides insights into the dataset's structure, patterns and relationships, helping us appreciate the power of descriptive statistics and data visualization in uncovering valuable information from a dataset.
What do other research projects projects on this matter tell us that this project doesnt? What can we learn from these?

The absence of advanced machine learning techniques in this project allowed me to emphasize the importance of foundational statistical methods and visual exploratory analysis. By using histograms, scatter plots, bar charts, and summary statistics, I can see meaningful relationships and patterns within the dataset, contributing to our understanding of the Iris flowers' characteristics.

Overall, this project demonstrates how a combination of basic statistical analysis, data visualization and programming skills can lead to valuable insights and a deeper understanding of a dataset, setting the stage for further research and exploration in the field of data science. The primary goal of the project is to analyze the relationships between the attributes - aka the 4 variables - of the Iris flowers and their species using statistical and data visualization techniques, without employing advanced machine learning algorithms as it is beyond the scope of beginners, or at least this particular beginner. 

##
Data Analysis

##
Results

Mean Feature Values for Each Iris Class:

The bar chart shows how the different types of Iris flowers have different average sizes for their petals and sepals.
Iris-setosa is the smallest overall, Iris-virginica is the largest, and Iris-versicolor falls in between.
This tells us that we can look at the size of the petals and sepals to figure out which type of Iris flower we have.
Predicted Species of Iris Flowers:

We can guess the type of Iris flower by just looking at the length of its sepal.
If the sepal is less than 5.84, it's probably Iris-setosa.
If the sepal is between 5.84 and 6.62, it's likely Iris-versicolor.
If the sepal is bigger than 6.62, it's probably Iris-virginica.
Scatter Plot Matrix:

The scatter plot matrix would have shown us how the size of the petals and sepals are related to each other.
We could see if there's a pattern or a connection between them.
This helps us understand how the different parts of the Iris flower are related.
Violin Plots:

The violin plots give us a picture of how the sizes of the petals and sepals are spread out for each type of Iris flower.
We can see if there are any differences in the shapes and ranges of the plots.
This helps us compare the sizes of the petals and sepals between the different types of Iris flowers.
Histograms:

The histograms show us how often different sizes of petals and sepals appear in the Iris dataset.
We can see which sizes are more common and which are less common.
This gives us an idea of how the sizes are distributed and helps us understand the overall patterns.
Variable Descriptions and Correlation Coefficients:

The variable descriptions tell us some basic numbers about the sizes of the petals and sepals.
We can see the average size, the range of sizes, and how the sizes vary.
The correlation coefficients show us if there's any relationship between the sizes of the petals and sepals.
We can see if they tend to change together or if they're independent of each other.
In summary, by analyzing the Iris dataset, we can find out how the sizes of the petals and sepals can help us identify the different types of Iris flowers. We can look at their average sizes, compare their distributions, and see if there's a relationship between the sizes.

##
Conclusion

##
How to

##
Dependencies

##
Reference List

===                         


