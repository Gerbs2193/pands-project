# Data analysis of the Iris-data set 

## What is it?

The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis.[1] It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species.[2] Two of the three species were collected in the Gaspé Peninsula "all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus".[3]
The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other - www.kaggle.com. (n.d.). Iris Dataset. [online] Available at: https://www.kaggle.com/datasets/vikrishnan/iris-dataset. That is the definition from kaggle - however I will detail my understanding of it below.

The Iris flower dataset is a collection of measurements on three types of flowers: setosa, versicolor, and virginica. It was created to understand the differences between these flowers based on their physical characteristics.

The dataset contains 150 samples, with each flower type having 50 samples. Four variables were exist for each: sepal length, sepal width, petal length and, lastly, petal width.

The goal of the dataset is to classify the flowers into their respective types using the above variables. In this project, I use simple plots and calculations to explore the relationships between the measurements and gain insights about the flowers.

By examining histograms, scatter plots, bar charts, violin plots, and correlation coefficients - it becomes possbile to identify patterns and understand how the measurements relate to each other. This project focuses on analysing the dataset without advanced machine learning techniques, making it accessible to beginners.

Overall, the Iris dataset provides an opportunity to learn about data analysis and visualization by exploring the relationships between the flower measurements and their types.



## Introduction  

This Iris Dataset Analysis project attempts to explore and gain insights into the relationships between various attributes of Iris flowers. The dataset consists of measurements of sepal length, sepal width, petal length, and petal width for 150 Iris flowers. Along with the attribute measurements, each flower is classified into one of three species: setosa, versicolor, or virginica.

The primary objective of this project is to analyse the dataset using statistical and data visualization techniques, without relying on complex machine learning algorithms. By leveraging the power of Python programming language and popular libraries like Pandas, Matplotlib, and Seaborn - I aim to uncover patterns and insights within the dataset in a beginner-friendly manner.


## Target Audience

Who is this project aimed at? Well, this project is tailored for beginners like myself who are keen to understand the Iris dataset and learn how to perform mostly basic exploratory data analysis and visualizations using python. It provides a foundational understanding of statistical methods and data visualization techniques, which are essential skills in the data analysis of the Iris dataset.


## Research Context

Myriad other research projects on the Iris dataset have used advanced machine learning techniques for classification and prediction of the dataset. For example; https://github.com/jennifer-ryan/iris-data-set-project - this excellent and far superior project by Jennifer Ryan on Github details how to use the KNN algorithm for further training analysis. However, this project takes a different approach by focusing solely on exploratory data analysis techniques and visualizations. By using histograms, scatter plots, bar charts, correlation coefficients and summary statistics, we can discover meaningful relationships and patterns within the dataset whilst contributing to our understanding of the Iris flowers' characteristics.

## Importance

By performing exploratory data analysis and visualization techniques, this project highlights the importance of foundational statistical methods and visual exploration in understanding the dataset. Through this approach - valuable insights can be gained into the relationships between the attributes of Iris flowers and their species, without relying on advanced machine learning algorithms. This project showcases the power of descriptive statistics and data visualization in uncovering valuable information and patterns within a dataset.

## Scope of data analysis

To focus on exploratory data analysis techniques and visualizations rather than advanced machine learning algorithms. The emphasis is on understanding the structure, patterns and relationships within the Iris dataset. By analysing attribute distributions and relationships, I aim to answer questions about attribute differences between species, correlations among measurements, visual distinguishability and insights into Iris flowers' characteristics. To achieve this, the following will be utilized; 
- 6 complete scatter plots of all the variables comparisons aka; Sepal Width v Petal Width, Sepal Width v Petal Length, Sepal Length v Sepal Width, Sepal Length v Petal Width, Sepal Length v Petal Length and Petal Length v Petal Width. 
- 4 completed histograms of the variables
- 4 completed violin plots of the variables for each of the classes
- 1 completed scatter plot matrix showcasing the variables to the classes
- 1 variable descriptions txt file outlining the summary of the variables
- 1 iris class prediction based on its petal length
- 1 mean bar chart of classes
- 1 correlation coefficient of the variales++++



## Conclusion of introduction

 This Iris Dataset Analysis project offers a beginner-friendly approach to understanding the Iris dataset. By leveraging statistical analysis techniques and data visualizations - I aim to uncover patterns and insights within the dataset. The focus is on exploring the relationships between attributes and species which, in turn - provides valuable insights into the classification and characteristics of Iris flowers.

## Results

### Histograms of the Variables:

The histograms I generated provide an easy visualisation of the distribution of the variables. Here, it shows how often certain sizes appear in the dataset. By looking at the shape of the histograms it becomes possible to see the patterns and characteristics. Looking at the bell-shaped distribution for sepal length and width, for example - seems to show that most of the flowers have similar sizes in these dimensions. On the other hand though, the two peaks in the histograms of petal length and width shows the existence of distinct groups or clusters within the dataset. This - to me - means that some flowers have shorter and narrower petals, while others have longer and wider ones. Also, just by looking closely at the hists you can gain some valuable insights into the range and variation of sizes in different attributes of the Iris flowers. For example; Size range, shape and distribution, outliers to name but three. For the range of sizes - sepal length ranges from about 4.3 to 7.9 centimeters whereas petal width ranges from around 0.1 to 2.5 centimeters. Just by understanding and noting these ranges, it becomes possible us more easily grasp the diversity and variability of the Iris flowers' attributes.

### Scatter Plots of Variable Comparisons:

The 6 variable comparison scatter plots are good for visualisations of the iris dataset as they can show how the sizes of different parts of the Iris flowers are related to each other. Specifically, the results for each comparison is below:

#### Sepal Width vs. Petal Width:
Comparing the width of the sepal (the leaf-like part) to the width of the petal (the colourful part), you can see that as the sepal gets wider, the petal tends to get wider too. This suggests that there is a connection between the width of these two parts as when one increases in width - so does the other. 

#### Sepal Width vs. Petal Length:
Comparing the width of the sepal to the length of the petal, you can see something different than above. It appears that as the sepal gets wider, the petal tends to get longer. This comparison shows that while a relationship exists between the two, it differs strongly to the first comparison - as you'd expect.

#### Sepal Length vs. Sepal Width:
Comparing the length of the sepal and its width it doesn't appear to show any pattern or relationship between them. They seem to be independent of each other as knowing the sepal's length doesn't mean you can discern well its width. From a data analysis point of view, this comparison doesn't really show anything valuable. 

#### Sepal Length vs. Petal Width:
Comparing the length of the sepal to the width of the petal there is a connection. As the sepal gets longer the petal wider. Unlike the above comparison, this to me suggests that there is a connection between the length of the sepal and the width of the petal. Knowing one can mean making accurate assumptions of the other.

#### Sepal Length vs. Petal Length:
Comparing the length of the sepal and the length of the petal, there is a connection between the two. As the sepal gets longer - the petal also gets longer. Again, knowing this relationship means you can at least guess the behaviour of one variable, when knowing the other. 

#### Petal Length vs. Petal Width:
Lastly, comparing petal length to its width, there appears to be a connaction also. Looking at the petal -  as it gets longer the width tends to increase too. This shows us that there is a relationship between the length and width of the petal.


### Violin Plots:

The 4 violin plots  were generated as I wanted another way to showcase the relationship between the variables and the classes. I chose violin plot as I couldn't get box plots to work properly and violin plots seemed to work better regardless. 

#### Iris-setosa:
##### Sepal Length: 
The sepal length of the iris class of setosa semes to mostly fall between 4.8 - 5.4. It does range, however, from about 4 - 6.2 approximately its just predominately between 4.8-5.4 as mentioned. The absolute data peak is approximately 5 - this indicates where the absolute highest density of data points reside. Overall, not too much variation.

##### Sepal Width: 
For the sepal width  of the iris setosa, the violin plot shows the flowers mostly between 3.3 - 3.6. The range is from approximately 2-5. The absolute peak seems to be 3.3. Little bit more variation than sepal length. 

##### Petal Length: 
Regarding the petal length of setosa, it shows mostly between 1.4-1.6 with an overall range of 1-2.2 or so. The absolute data peak is 1.5. More size variation again. 

##### Petal Width: 
The petal width of the setosa shows a predominance between 0.2-0.3. The range is approximately 0-0.75. The absolute peak is approximately 0.45. This variable shows the smallest variation of the setosa and variable comparisons. However, it is also the only variable that has its absolute peak not fall within the the most common data points of 0.2-0.3. The variable has the smallest variation but shows the erratic violin plot.  


#### Iris-versicolour:
##### Sepal Length: 
The data here falls mostly between 5.5 to 6.7 for the sepal length of the versicolour. There is a peak around 6.0, indicating a common size among the flowers. The range is approximately 4.5-7.5.

##### Sepal Width: 
The sizes of the sepal width for Iris-versicolor are most concentrated around 2.7 to 3.1. The overall 0.8-3.75 with the absolute peak being around 3. The range shows a slightly wider shape - which suggests some variation in sizes.

##### Petal Length: 
The sizes of the petal length for Iris-versicolor are mostly distributed between 3.7 and 4.7. The range is around 2.8-5.7 with an absolute peak of 4.7. This plot, like sepal width before it, shows a fairly wide shape, indicating more noticeable variation in sizes.

##### Petal Width:
The petal width of the versicolour are mostly around the 1.0 to 1.3 datapoints. The overall range ranges from .8-2 with the max peak being 1.4. Like the petal width of the setosa also, the petal width of the versicolour shows a narrow shape which suggests less variation in sizes.

#### Iris-virginica:
##### Sepal Length: 
The data here concentrates mostly between 6.0 to 7.9. The range is 4.5-8.5 and the absolute peak is 6.5. 

#### Sepal Width: 
Data concentates between 2.8 to 3.2. The range is approximately 2-4 and the absolute peal data point is around 3. The plot here shows a wider shape which suggests there are some solid size variations happening.

#### Petal Length: 
Petal length is predominantly around the data points of 4.5 and 6.9. The range is between 4 and 7.2, roughly. The peak data point is 5.5. This plot also shows a wider shape, indicating some noticeable variation in sizes.

#### Petal Width: 
This is a small data point with about 1.6 to 2.0 representing the most common values. The range is 1.25-2.75 and the maximum value point is 1.9. The plot shows a much more narrow shape, just like the petal width of the other two classes setosa and versicolour which, again, suggests less variation in sizes.

These violin plots give us an understanding of how the sizes of the different parts of the Iris flowers vary across the iris classes. We can observe the ranges, common sizes, and the degree of variation in sizes for each class.

The violin plots give us a clearer picture of the range of sizes for the different parts of the Iris flowers within each flower class. We can compare the shapes and spreads of the plots to understand the differences. For instance, Iris-setosa generally has smaller petals and sepals compared to Iris-versicolor and Iris-virginica. Iris-virginica, on the other hand, tends to have longer sepals compared to the other two classes.

Summary Description of Variables:

The summary description provides us with some key numbers about the sizes of the petals and sepals. We can look at the average sizes and see how much they vary. On average, the sepal length is around 5.84 cm, the sepal width is approximately 3.05 cm, the petal length is about 3.76 cm, and the petal width is roughly 1.20 cm. These numbers give us a general idea of the typical sizes of the different parts.

Correlation Coefficient:

The correlation coefficient tells us how closely related the length and width of the petals are. It helps us understand if there is a strong or weak relationship between these two variables. We find that the petal length and width have a strong positive correlation of approximately 0.96, indicating that they tend to change together. As the petal length increases, the petal width also increases.

Scatter Plot Matrix:

The scatter plot matrix allows us to see all possible combinations of the variables in one place. We can visually explore the relationships between the sizes of the different parts of the Iris flowers. This helps us identify any trends or clusters within the data.

Iris Class Prediction based on Petal Length:

We can make a prediction about the type of Iris flower by looking at the length of its petals. If the petal length is less than 2.5 cm, it is likely to be Iris-setosa. If the petal length falls between 2.5 cm and 4.9 cm, it is probably Iris-versicolor. And if the petal length exceeds 4.9 cm, it is likely to be Iris-virginica. This simple rule helps us classify Iris flowers based on a single attribute.

Mean Bar Chart of Classes:

The bar chart shows the average sizes of the petals and sepals for each type of Iris flower. We can compare the sizes of the different parts across the flower classes. Iris-setosa generally has the smallest average sizes, Iris-virginica has the largest, and Iris-versicolor falls in between. This information helps us understand the typical characteristics of each flower class.

By examining the different visualizations and summary measures, we gain insights into the sizes, relationships, and classification of the Iris flowers.
##
Conclusion

##
How to

##
Dependencies

##
Reference List

https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html
https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/04_plotting.html#min-tut-04-plotting
https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_hist.html
https://seaborn.pydata.org/examples/scatterplot_matrix.html
https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html
https://www.kaggle.com/datasets/vikrishnan/iris-dataset
===                         


