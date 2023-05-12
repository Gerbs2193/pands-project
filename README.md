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
### Sources used to achieve the histograms
- https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/. This showed me how to format the code for each variable, what the output should look like. What I wanted to do was change it to output to a single text file, rather than 4 separate ones. It was also excellent for reading up on the summary variable descriptions - which I used it for and the box plots - which I didn't understand how to get to work so I didn't care to include it.
- https://www.nickmccullum.com/python-visualization/histogram/ - I was mostly familair with how to create histograms from the plot.py tank but regardless, used this source to go over it again. 


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
### Sources used to achieve the scatter plot variable comparisons
- https://www.geeksforgeeks.org/plotting-graph-for-iris-dataset-using-seaborn-and-matplotlib/ - Great source that shows how to code single scatter plot for each variable - also shows advantages for certain libraries like seaborn over lesser ones. It didn't show me how to compare them though but eventually I found a way using nested loops: 
- https://stackoverflow.com/questions/62541229/how-to-nest-a-for-loop-to-subplot-a-scatter-on-iris-data used this for example of half similar implementation and used this for what nested loops are and how to do them: 
- https://www.geeksforgeeks.org/python-nested-loops/



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
### Sources needed to be able to achieve this:
- https://www.geeksforgeeks.org/violin-plot-for-data-analysis/ - I wouldn't have been able to achieve the violin's without seeing an implementation elsewhere. This example codes most of it and I liked the unique visualisations so I took heavy inspiration from it. I had never seen violin plots before seeing this source. 
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.violinplot.html - Looked through this to see why it would be nice to use a violin plot aka unique visualisation among different classes and the vars
- https://medium.com/@harimittapalli/exploratory-data-analysis-iris-dataset-9920ea439a3e - This showed me what the violin's output 'should' look like. Mine seems to be 90 percent right if so. 



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
### Sources needed to achieve the above
- https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/ - Showed me what each heading meant, what the number should be, how to code an implementation. Had to change code to output to a single file called variable_descriptions.


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
### Sources needed to complete the Correlation Coefficient
- https://medium.com/analytics-vidhya/first-step-to-statistics-with-iris-data-3d29c0820c5d - no code on display here, but good insight into what the diagrams of the CC should look and gave me the inspiration to look into the seaborn function heatmap for the correlation coefficient. Also great for violin plots, hists and summary statistics
- https://www.geeksforgeeks.org/exploring-correlation-in-python/ - Used to learn how to code it. Adapted it to the iris data set as couldn't find good enough source. 


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
### Sources needed to complete matrix
- https://stackoverflow.com/questions/45862223/use-different-colors-in-scatterplot-for-iris-dataset - Used to learn how to code it for my applications.
- https://vitalflux.com/what-when-how-scatterplot-matrix-pairplot-python/ - Got the guts of my code and inspiration from this resource. Showed me how to do most all of it. 

### Mean Bar Chart of Classes:
This was done to perform an additional fairly straight-forward exploratory of the relationship between the classes and the variables.

#### Iris-setosa:
For the setosa, on average - sepal length is approximately 5.0 cm, sepal width is approximately 3.4 cm, petal length is approximately 1.5 cm, and lastly, petal width is about 0.2 cm.

#### Iris-versicolour:
For the iris-versicolour, on average, sepal length is about 5.9 cm, sepal width is about 2.8 cm, petal length is about 4.3 cm while, lastly, petal width is about 1.3 cm.

#### Iris-virginica:
Laslty for the virginica, on average sepal length is around 6.6 cm, sepal width is 3.0 cm, petal length is 5.6 cm and petal width is 2.0 cm.

These average values give some idea of the sizes of the different variables in each class.
### Sources needed for mean bar chart
- https://pythonguides.com/matplotlib-plot-bar-chart/ - not too hard, just used to know how to generally plot a bar chart. 

### Predicting species with assumed sepal length using function and IF statement

For this, I wanted to try a very basic and limited sort of machine learning alternative code that predicts the iris class based on the sepal length of the flower. The code takes the sepal length as input and uses a prediction of the iris class.

Specifically, If sepal length is less than 5.84, the predicted iris class is "Iris-setosa". 5.84 was chosen because both the other two classes have, generally, overwhelmingly larger sepal lengths. Next, If the sepal length is between 5.84 and 6.62 then predicted iris class is Iris-versicolor as its sepal length usually falls in this range. Lastly, everything larger than this aka sepal lengths that are greater than or equal to 6.62 - then predicted iris class is "Iris-virginica". It's simple, easy to enough to code but very limited. 

So, by using this code, I can determine the iris class based on the sepal length alone. It offers a straightforward approach for making predictions without the need for complex calculations or using machine learning - though at the cost of precision.
### Sources needed for predicting class based off of sepal length
This one was I guess unsurprisingly not that hard as its very silly and limited. Didn't need much sources, only ended up working as I was messing around with machine learning (and failing) and thought to try to use if statement and define function. 

## Conclusion

To conclude - throughout this analysis, my mission was to, essentially, not bite off more than I could chew. Simply, I wanted to satisfy the parameters for the brief whilst also looking to explore and understand as much of the Iris dataset as possible. I wanted to examone the variables, plot them in all manner of ways to get some insights and more importantly, see how the relationship compares between them and their classes. These variables called sepal length, sepal width, petal length, and petal width were compared with the three different types of iris classes - namely - Iris-setosa, Iris-versicolor and Iris-virginica.

To start - I began by visualizing the distribution of each variable using histograms which provided me with the range and frequency of values for all 4 variables shown across 4 histograms.

Following that, I began looking into the the relationships between each variable through 6 scatter plots. These plots allowed me to observe patterns and correlations between different parts of the variables - shedding somee light on their interdependencies or otherwise.

Next I needed to be more proactive regarding the actual classes so I utilized 4 separate violin plots, which showed the distribution and variation of each variable size within each class. These plots offered valuable insights into the unique features and differences among the three iris species.

The scatter plot matrix was generated the as it, again, allowed me to oversee more of the relationship between the variables and the classes by enabling me to clearly see patterns, separations and overlaps between each class. This visual representation, whilst a great resource - was more confusing that anything but it did show how the variables contribute to the classification of iris flowers.

A text file - which summarizing the descriptive statistics for each variable - was also generated. This single textfile summary provided a succinct, in-depth and quantitative overview of the dataset which showcased the numerical characteristics of the iris measurements in an easy to see way. 

Calculating the correlation coefficient was one of the final things to code and was useful as it showed the strength and direction of the relationships between pairs of variables.

I also visualized the mean feature values for each iris class using a bar chart - the only bar chart I used. This visual highlighted the average differences in variable values among the three classes which gave an insight into the characteristics of each iris species.

Lastly, I wrote a pretty basica code that predicted the iris class based on the sepal length. This predictive capability allowed me to assign a predicted species to a given sepal length - which offered a practical application of the analysis and a simple alternative to machine learning.

Many failed attempts at box plotting and KNN machine learning went by the way side and were, obviously, not included.

By undertaking these analyses and visualization techniques - I hope I have accomplished my mission of exploring and comprehending the Iris dataset by unraveling its relationships, patterns, and unique traits among the different types of iris flowers.


## How to

### Introduction:
The goal here is to provide instructions on how to replicate the analysis and visualizations I performed on the Iris dataset. By following these instructions, you can gain insights into the dataset and explore the relationships between variables and the classes.

### Data Preparation:
- Download the Iris dataset or import it from a specific source. I imported it and saved it as iris.data and used this when manipulating its data afterwards.
- Ensure that the required python libraries like Pandas, NumPy, Matplotlib, and Seaborn are installed. If not, install what libraries you may need depending on your project specifics. For me, the aforementioned were used. 
- Import the necessary modules and load the dataset into your Python environment.
-Histograms:
Use Matplotlib library to create the 4 hists variables.
Specify the number of bins to control the granularity distribution representation.
Customize the histograms with the labels you want for the x-axis, y-axis, and title.
- Scatter Plots:
Use the Matplotlib library to easily generate scatter plots.
Incorporate the iris class information by mapping it to colours or shapes in the scatter plots.
Adjust the appearance of the scatter plots by messing with the markers, marker size and adding a legend if needs be.
- Violin Plots:
Use the Seaborn library to create these.
Choose the variable and iris class combinations you want to visualize.
Customize the plots as required like by changing the colour, width etc.
- Scatter Plot Matrix:
Again, use the Seaborn library to generate this.
Display the relationships between all variables in the dataset.
Include the class info by colour-coding the data points.
Customize the scatter plot matrix as you see fit like with options like colour and size as I did.
- Variable Summary Descriptions:
Use pandas library for this.
Save the results to a single text file for reference.
Customize the file format to your needs. I needed it outputted to a single text file to fit the projects requirements.
- Correlation Coefficient:
Calculate the correlation coefficient between the pairs of variables using Pandas library.
Once you interpret the values as 1 meaning good positive relationship, 0 meaning a weak one and -1 meaning a good negative relationship - you will easily be able to discern insights from the data.
- Bar Chart:
Use the Matplotlib library to create this.
Display mean feature values for each class.
Customize the chart's appearance to your needs like colours, bar width etc. 
- Predicting Iris Species:
Utilize the provided code that predicts the iris species based on sepal length.
Input the sepal length value of less than 5.84 to be setosa, if not that but below 6.62 then it's versicolour. Use these parameters to predict the classes as I did.

## Dependencies

- Python
- Pandas
- Matplotlib
- Numpy 
- Seaborn

## (Mostly) Consolidated final code blocks and more detailed comments

```import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset into a pandas dataframe
iris = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

# Calculate the mean feature values for each class of Iris flower
iris_mean = iris.groupby('class').mean()

# Create a bar chart to visualize the mean feature values for each Iris class
iris_mean.plot(kind='bar')

# Set the title and labels for the bar chart
plt.title('Mean Feature Values for Each Iris Class')
plt.xlabel('Class')
plt.ylabel('Feature Value')

# Save the bar chart as a PNG image file
plt.savefig('iris_bar_chart.png')

# Display the bar chart
plt.show()

# Define a function to predict the species of Iris flowers based on their sepal length
def predict_species(sepal_length):
    if sepal_length < 5.84:
        return 'Iris-setosa'
    elif sepal_length < 6.62:
        return 'Iris-versicolour'
    else:
        return 'Iris-virginica'

# Apply the predict_species function to the sepal length column
iris['predicted_species'] = iris['sepal_length'].apply(predict_species)

# Save the dataframe with the predicted species to a CSV file
iris.to_csv('iris_predicted_species.csv', index=False)

# Create a scatter plot matrix to visualize the relationships between different variables
sns.pairplot(iris, hue='class')

# Save the scatter plot matrix as a PNG image file
plt.savefig('scatter_plot_matrix.png')

# Close the scatter plot matrix figure
plt.close()

# Create violin plots to visualize the distribution of each variable by class
variables = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
for variable in variables:
    # Set the figure size for the violin plot
    plt.figure(figsize=(8, 6))
    
    # Create the violin plot
    sns.violinplot(x='class', y=variable, data=iris)
    
    # Set the labels and title for the violin plot
    plt.xlabel('Class')
    plt.ylabel(variable)
    plt.title(f'Violin Plot: {variable} by Class')
    
    # Save the violin plot as a PNG image file
    plt.savefig(f'violin_plot_{variable}.png')
    
    # Close the violin plot figure
    plt.close()


    # Import the required libraries for data analysis and visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset into a pandas dataframe
iris = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

# Create scatter plots to visualize the relationships between different variables
variables = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
for i in range(len(variables)):
    for j in range(i + 1, len(variables)):
        var1 = variables[i]
        var2 = variables[j]
        
        # Create a scatter plot using the selected variables
        plt.scatter(iris[var1], iris[var2])
        
        # Set the labels and title for the scatter plot
        plt.xlabel(var1)
        plt.ylabel(var2)
        plt.title(f'Scatter Plot: {var1} vs {var2}')
        
        # Save the scatter plot as a PNG image file
        plt.savefig(f'{var1}_vs_{var2}.png')
        
        # Close the scatter plot figure
        plt.close()

# Load the Iris dataset into a pandas dataframe
iris = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

# Create histograms to visualize the distribution of each variable
variables = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
iris.hist(column=variables, grid=False)

# Set the title and layout for the histograms
plt.suptitle('Histograms of Iris Variables')
plt.tight_layout()

# Save the histograms as a single PNG image file
plt.savefig('histograms.png')

# Display the histograms
plt.show()

# Load the Iris dataset into a pandas dataframe
iris = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

# Get the statistical descriptions of the variables
var_descriptions = iris.describe()

# Write the variable descriptions to a text file
with open('variable_descriptions.txt', 'w') as f:
    f.write(str(var_descriptions))

# Load the Iris dataset into a pandas dataframe
iris = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

# Calculate the correlation between variables
correlation = iris.iloc[:, :-1].corr()

# Create a correlation heatmap using seaborn
sns.heatmap(correlation, cmap='coolwarm', annot=True, fmt=".2f", cbar=False)

# Save the plot as a PNG image
plt.savefig('correlation_coefficients.png', dpi=300)
      
```

## Licensing

Free to use


## Reference List

1 - scikit-learn. (n.d.). The Iris Dataset. [online] Available at: https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html
2 - pandas.pydata.org. (n.d.). How do I create plots in pandas? — pandas 2.0.1 documentation. [online] Available at: https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/04_plotting.html#min-tut-04-plotting [Accessed 12 May 2023]
3 - matplotlib.org. (n.d.). Scatter plot with histograms — Matplotlib 3.7.1 documentation. [online] Available at: https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_hist.html [Accessed 12 May 2023]
4 - seaborn.pydata.org. (n.d.). Scatterplot Matrix — seaborn 0.11.2 documentation. [online] Available at: https://seaborn.pydata.org/examples/scatterplot_matrix.html
5 - GeeksforGeeks. (2020). Python - Basics of Pandas using Iris Dataset. [online] Available at: https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/.
6 - scikit-learn.org. (n.d.). sklearn.datasets.load_iris — scikit-learn 0.24.1 documentation. [online] Available at: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html.
7 - www.kaggle.com. (n.d.). Iris Dataset. [online] Available at: https://www.kaggle.com/datasets/vikrishnan/iris-dataset.
8 - Glen, S. (2022). Correlation coefficient: simple definition, formula, easy steps. [online] Statistics How To. Available at: https://www.statisticshowto.com/probability-and-statistics/correlation-coefficient-formula/.
9 - Python, R. (n.d.). NumPy, SciPy, and Pandas: Correlation With Python – Real Python. [online] realpython.com. Available at: https://realpython.com/numpy-scipy-pandas-correlation-python/.
10 - GeeksforGeeks. (2019). Box plot and Histogram exploration on Iris data. [online] Available at: https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/.
11 - GeeksforGeeks. (2020). Plotting graph For IRIS Dataset Using Seaborn And Matplotlib. [online] Available at: https://www.geeksforgeeks.org/plotting-graph-for-iris-dataset-using-seaborn-and-matplotlib/ [Accessed 12 May 2023].
12 - www.nickmccullum.com. (n.d.). How To Create Histograms in Python Using Matplotlib. [online] Available at: https://www.nickmccullum.com/python-visualization/histogram/ [Accessed 12 May 2023].
13 - Stack Overflow. (n.d.). python - how to nest a for loop to subplot a scatter on iris data? [online] Available at: https://stackoverflow.com/questions/62541229/how-to-nest-a-for-loop-to-subplot-a-scatter-on-iris-data [Accessed 12 May 2023].
14 - GeeksforGeeks. (2022). Python Nested Loops. [online] Available at: https://www.geeksforgeeks.org/python-nested-loops/.
15 - GeeksforGeeks. (2019). Violin Plot for Data Analysis. [online] Available at: https://www.geeksforgeeks.org/violin-plot-for-data-analysis/ [Accessed 12 May 2023].
16 - matplotlib.org. (n.d.). matplotlib.pyplot.violinplot — Matplotlib 3.7.1 documentation. [online] Available at: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.violinplot.html [Accessed 12 May 2023].
17 - Mittapalli, H. (2018). Exploratory Data Analysis : Iris DataSet. [online] Medium. Available at: https://medium.com/@harimittapalli/exploratory-data-analysis-iris-dataset-9920ea439a3e [Accessed 12 May 2023].
18 - GeeksforGeeks. (2021). Exploratory Data Analysis on Iris Dataset. [online] Available at: https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/.
19 - Python, R. (n.d.). NumPy, SciPy, and Pandas: Correlation With Python – Real Python. [online] realpython.com. Available at: https://realpython.com/numpy-scipy-pandas-correlation-python/.
20 - Mukherjee, N. (2020). First step to Statistics (with Iris data). [online] Analytics Vidhya. Available at: https://medium.com/analytics-vidhya/first-step-to-statistics-with-iris-data-3d29c0820c5d.
21 - GeeksforGeeks. (2019). Exploring Correlation in Python. [online] Available at: https://www.geeksforgeeks.org/exploring-correlation-in-python/.
22 - Stack Overflow. (n.d.). python - Use different colors in scatterplot for Iris dataset. [online] Available at: https://stackoverflow.com/questions/45862223/use-different-colors-in-scatterplot-for-iris-dataset [Accessed 12 May 2023].
23 - Kumar, A. (2020). What, When & How of Scatterplot Matrix in Python. [online] Data Analytics. Available at: https://vitalflux.com/what-when-how-scatterplot-matrix-pairplot-python/ [Accessed 12 May 2023].
24 - Kumar, B. (2021). Matplotlib Plot Bar Chart - Python Guides. [online] Available at: https://pythonguides.com/matplotlib-plot-bar-chart/.

===                         


