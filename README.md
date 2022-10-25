# Prediction-of-opening-price-of-Tesla-shares-using-a-machine-learning-algorithm.

# Problem Description

The Global market has assumed a change with the emergence of various technologies as a result of the fourth industrial revolution. There is now a fusion of technologies between the physical, biological and digital world. Some of these technologies include autonomous vehicles in which Tesla is a key player in this domain. Tesla reached a market capitalization of $86billion on January 10,2020 and this made the company surpass BMW, Daimler and Volkswagen combined(E-Autohersteller,2020). It was also found out that the company reached a valuation of $206billion which made the company surpass Toyota`s $202billion to become the world`s most valuablel automaker by market capitalization(Stevens Pippa,2020). The Global market is highly volatiile and there has been series of rises and falls over the years and this project seeks to predict the opening price of Tesla stocks by deploying a machine learning algoritm (Random Forest). 


# Data

Data used in this repository were gotten from Yahoo Finannce and saved as a csv folder and this can be gotten from the data folder in the repository. Name of the file is 'TSLA.csv'

# Approach to analysis

For the analysis done, I had to first install libraries that would be needed and they are are 
Pandas- Pandas is a library that is applicable for data manipulation and analysis in python

Numpy- its aplicable lfor adding support for large, multi-dimensional array and matrices and it can be used for a high-level mathematical operations. 

Matplotlib-Matplotlib is applicable for plotting in python

Scikit-learn- Its a free software machine learning library applicable for python programming language


# Exploratory data analysis

After the data were loaded into the IDE using the pandas library, missing values were checked to ascertain if my data is clean or I need to clen the data. It was found out that there are no missing values in the dataset which makes the analysis easy and straight forward. I also checked the head and tail to have a quick glance at the dataset by checking the first five values from the head and the first five values from the tail. Date was a column in the dataset and I had to convert date to year in order to create continous variables needed for my analysis and this was done using the DatetimeIndex function in python. The first five summary was done and other exploratory analysis were done too. 
The data was also visualized using a histogram. 

# Modelling
I used the following as features and Open as the response: 

High

Low

Close

Adj Close

Volume

Year


RandomForest was fitted into the Algorithm on the train dataset and predictions were made using the test data set. The RMSE was 2.2076 while for the feature importance, it was found out that Close, Adj Close, High and Low were good predictors.

# Conclusion
from the visualization in te feature importance, it can be seen that close, Adj Close, High, Low are good predictors in the model and they have influence on it.

# References

E-Autohersteller: Tesla ist wertvoller als BMW, Daimler und VW zusammen". Handelsblatt (in German). Retrieved November 25, 2020.
 
 Stevens, Pippa (July 1, 2020). "Tesla tops Toyota to become largest automaker by market value". CNBC. Retrieved July 1, 2020.
