# Data analysis of the Iris-data set 

## What is it?

The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis.[1] It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species.[2] Two of the three species were collected in the Gaspé Peninsula "all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus".[3]
The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other - www.kaggle.com. (n.d.). Iris Dataset. [online] Available at: https://www.kaggle.com/datasets/vikrishnan/iris-dataset. That is the definition from kaggle - however I will detail my understanding of it below.

The Iris flower dataset is a collection of measurements on three types of flowers: setosa, versicolor, and virginica. It was created to understand the differences between these flowers based on their physical characteristics.

The dataset contains 150 samples, with each flower type having 50 samples. Four variables were exist for each: sepal length, sepal width, petal length and, lastly, petal width.

The goal of the dataset is to classify the flowers into their respective types using the above variables. In this project, I use simple plots and calculations to explore the relationships between the measurements and gain insights about the flowers.

By examining histograms, scatter plots, bar charts, violin plots and correlation coefficients - it becomes possible to identify patterns and understand how the measurements relate to each other. This project focuses on analysing the dataset without advanced machine learning techniques which - I found - makes it more accessible to beginners.

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

So, to summarise the above violin plots; The plots allowed me to visualise and greater understand how the variables of the Iris flowers vary across the iris classes - setosa, versicolour and virginica. I could observe the ranges, common sizes, the absolute max data points and the degree of variation in sizes for each class. To add to this, the violin plots give me a clearer illustration of the range of sizes for all the variables of the Iris flowers within each of the classes. Also, having access to these plots - it's easy to compare the shapes and spreads of the plots to understand the differences. For example - the Iris-setosa seems to have smaller petals and sepals compared to both Iris-versicolor and Iris-virginica whereas Iris-virginica tends to have longer sepals compared to the other two classes. Simple insight that wasn't possible until seeing the data as it was presented to me in the plots. 


### Summary Description of Variables:

The variable summary description shows some useful numbers and data about the sizes of the 4 variables. They show the count, mean, standard deviation, min, 25%, 50%, 75% and max data point. By coding this, it makes it easy to see - for example - average sizes and how much they may vary. An example being that, on average, sepal length is around 5.84 cm, the sepal width is approximately 3.05 cm, the petal length is around 3.76cm whereas petal width is around 1.20 cm. This fairly simple data give us a general idea of the typical sizes of the different parts.

#### The full results;

sepal_length  sepal_width  petal_length  petal_width
count    150.000000   150.000000    150.000000   150.000000
mean       5.843333     3.054000      3.758667     1.198667
std        0.828066     0.433594      1.764420     0.763161
min        4.300000     2.000000      1.000000     0.100000
25%        5.100000     2.800000      1.600000     0.300000
50%        5.800000     3.000000      4.350000     1.300000
75%        6.400000     3.300000      5.100000     1.800000
max        7.900000     4.400000      6.900000     2.500000

### Correlation Coefficient:

The correlation coefficient below shows how closely or not two variables are related to each other. It also measures the strength and direction of the relationship. Below are the completed results:

Sepal Length vs. Sepal Width: 0.682
Sepal Length vs. Petal Length: 0.864
Sepal Length vs. Petal Width: 0.837
Sepal Width vs. Petal Length: -0.366
Sepal Width vs. Petal Width: -0.249
Petal Length vs. Petal Width: 0.960

Overall then, the correlation coefficient seems to range from -0.366 to .960. When the coefficient is close to 1, it means there is a strong positive relationship between the variables. When it's close to -1, it means there is a strong negative relationship. If the coefficient is close to 0, it means there is little to no relationship between the variables. Source for understanding and code implementation - https://www.statisticshowto.com/probability-and-statistics/correlation-coefficient-formula/ and https://realpython.com/numpy-scipy-pandas-correlation-python/, https://seaborn.pydata.org/generated/seaborn.heatmap.html - specifically on how to use seaborn's heatmap function to get the heatmap as I don't know how to code it myself. 

From the correlation coefficients the following highlights can be seen given, again, that 1 indicates a strong positive relationship, 0 indicates there is little relationship between the vars and -1 indicates a strong negative relationship:

- Sepal Length looks to have a strong positive relationship with Petal Length (0.864) and Petal Width (0.837). From this, I can safely say that as Sepal Length increases, the other two variables should also increase.

- Sepal Width conversely, looks to have a weak negative relationship with Petal Length (-0.366) and Petal Width (-0.249). This means that as Sepal Width increases, the other two variables will also.

- Petal Length and Petal Width have a very strong positive relationship of 0.960 - by far the highest of any var relationship. This, then, means that as Petal Length increases Petal Width will also increase. 

These correlation coefficients give good insights into how the variables are related to each other in the dataset. The full heatmap is available in the correlation_coefficient.png. 


### Scatter Plot Matrix:

Next I performed a scatter plot matrix. This was chosen as an additional way to do some exploratory analysis between the relationship between the variables and the three classes. It shows several scatter plots that compare pairs of variables, though I'm not sure it's very well laid out. 

#### Sepal Length vs. Sepal Width:
This plot compares the length and width of the leaf-like part of the flower. It doesn't seem to show a clear pattern or relationship between them that I could discern.

#### Sepal Length vs. Petal Length:
For sepal length v petal length, it can be seen that as the sepal gets longer, the petal does likewise - clearly showcasing a strong relationship.

#### Sepal Length vs. Petal Width:
Next, in this plot, I noted that as sepal gets lengthier, the petal width follows suit. This, again, showcases a strong relationship between both variables.

#### Sepal Width vs. Petal Length:
For sepal width v petal length - there doesn't appear to be a clear pattern or relationship between the two.

#### Sepal Width vs. Petal Width:
Next, here, I note that as the sepal gets wider, the petal width variable follows suit which, you guessed it - indicates a strong relationship. 

#### Petal Length vs. Petal Width:
Finally, this plot compares petal length with the petal width. It shows that as the length of the petal increases, its width also tends to increase - highlighting it's strong relationship.

Also, my scatter plot matrix includes the 3 classes. The inclusion of the classes helps to visualize how the variables relate to the classes and if there are any interesting patterns between the classes based on the variables. For example - based on the scatter plot matrix generated, there are some patterns and differences visible between the 3 classes. As each of the classes has its own group of dots on the plots - It means that its easy and somewhat intuitive to see how the variables can show the different types of iris classes apart.

For instance - In the scatter plot matrix, its visible that some dots for one type of iris flower are far away from the dots of other types. For example - sepal length - the dots for its Iris-setosa flowers are, for the most part, at the bottom whereas the dots for the other types are much higher up. This can be useful as sepal length can help us tell Iris-setosa flowers apart from the others, merely by looking at the matrix. 

To add more results, there are plot points where the dots for two types of classes overlap somewhat, but the differences are still visible. Specifically, petal width shows that although the dots for Iris-versicolor and Iris-virginica are mixed together - Iris-versicolor for the most part, has smaller petal widths compared to Iris-virginica. This can be a helpful nudge to distinguish between these two.

So, the scatter plot matrix gives a visual way to understand how the different measurements relate to each other and how they can be useful in recognizing the different types of iris classes, as noted above. 


### Mean Bar Chart of Classes:
This was done to perform an additional fairly straight-forward exploratory of the relationship between the classes and the variables.

#### Iris-setosa:
For the setosa, on average - sepal length is approximately 5.0 cm, sepal width is approximately 3.4 cm, petal length is approximately 1.5 cm, and lastly, petal width is about 0.2 cm.

#### Iris-versicolour:
For the iris-versicolour, on average, sepal length is about 5.9 cm, sepal width is about 2.8 cm, petal length is about 4.3 cm while, lastly, petal width is about 1.3 cm.

#### Iris-virginica:
Laslty for the virginica, on average sepal length is around 6.6 cm, sepal width is 3.0 cm, petal length is 5.6 cm and petal width is 2.0 cm.

These average values give us an idea of the typical sizes of the different variables in each class.


## Conclusion

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
https://www.statisticshowto.com/probability-and-statistics/correlation-coefficient-formula/
https://realpython.com/numpy-scipy-pandas-correlation-python/
===                         


