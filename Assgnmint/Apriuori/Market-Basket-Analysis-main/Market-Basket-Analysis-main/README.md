# Market-Basket-Analysis
This repository contains files for Market Basket Analysis project using the Apriori Algorithm. The data used for this analysis is an open source Bakery dataset found on Kaggle. Association rule-mining in Market Basket Analysis helps to uncover relationships between items that are frequently purchased together. This can be valuable for targeted marketing or inventory management strategies.

# Objective

The main objective of this study was to discover items that are frequently purchased together, based on the time of the day.

# Key Processes

* **Data Preprocessing:** Cleaning the data, grouping together observations with same transaction number and date_time, transforming the data into a set of transactions.
* **Exploratory Data Analysis:** Generating summary statistics, Finding and Inspecting Frequent Itemsets, Visualizating Association Rules to uncover patters in purchasing behaviour.
* **Modeling:** Mining Association Rules using Apriori Algorithm, and Inspecting the Rules based on measures like Support, Confidence, Lift, Phi and Gini.

# Results

* There's 87% certainty that coffee is more likely to be purchased together with extra salami or feta and salad.
* There's 86% certainty that coffee is more likely to be purchased together with pastry and toast.
* There's also 85% certainty that coffee is more likely to be purchased together with Hearty & Seasonal and Sandwich.
* There's 83% certainty that coffee is more likely to be purchased together with cake and vegan mince pie.
* There's also 83% certainty that coffee is more likely to be purchased together with salad and sandwich.
* Those who like to "keep it local" were also more likely to buy coffee.
* There's 100% likelihood that T-shirts are purchased in the evening.
* There's also 100% likelihood that tea and pastry are purchased on weekdays.
* There's also 100% likelihood that sandwich and coke are purchased in the afternoon.
* There's 90.9% likelihood that coffee and soup are purchased on weekdays.
* There's 83.3% likelihood that coffee and sandwich are purchased in the afternoon.
* There's 91.6% likelihood that coffee and sandwich are purchased on weekdays.

More association rules are contained in the Knitted html file. Please download the file to see the rules.

## Tools and Libraries

RStudio Software (tidyverse, janitor, plyr, arules, arulesViz, RColorBrewer).

## Contributions

Contributions are welcome. Please fork the repository, make your changes, and submit a pull request.
