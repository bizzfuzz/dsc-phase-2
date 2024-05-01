# KING COUNTY REALTY ANALYSIS

## Overview

The real estate sector encompasses a diverse range of activities involving the acquisition, development, management, and transaction of properties, including residential, commercial, and investment real estate. The urban real estate investment business model is undergoing a fundamental overhaul attributed to digitization and a growing market for smart and environmentally demanding buildings.


## Business Understanding

The client is King County Realty. A real estate company looking to understand the anatomy of a high priced home. Armed with a dataset of house sales in King County, the team of analysts look to define the most sought after characteristics in a home.

This analysis will focus on the following factors that majorly affect the real estate industry to achieve the client's request:<br>
i) Market Trends: This analysis will help the client make well-informed decisions about the purchase, sale, and investment strategies of real estate. The dataset provides insights into pricing dynamics, market trends, and property features.<br>
ii) Customer Preferences: Understanding of consumer preferences and market demand through analysis of bedroom and bathroom numbers, property condition, view ratings makes targeted markeing and property customization easier and more scalable so as to suit all their clients' expectations.<br>
iii) Investment Opportunities: By analyzing variables including property size, location, condition, and market trends, investors in real estate can find properties that are cheap, evaluate possible returns, and optimize their investment portfolios.<br>
iv) Competitive Analysis: Real estate agents can benchmark against rivals, spot market gaps, and more by comparing property prices, sizes, amenities, and location features and set themselves out from the competition to obtain a market advantage.

## Data Understatnding

This project uses the King County House Sales dataset, which can be found in  `kc_house_data.csv` in the data folder in this assignment's GitHub repository. The description of the column names can be found in `column_names.md` in the same folder.

### Challenges
Missing Values:
waterfront, view, and yr_renovated columns have missing values. This can be seen in the count row of the descriptive statistics section.

Potential Data Quality Issues:
The bedrooms column has a maximum value of 33, which seems unusually high and might be an error or outlier.
The bathrooms column has a maximum value of 8, which could also be considered high and should be examined for outliers.
The yr_renovated column has a maximum value of 2015, which seems unusual as it's the same as the maximum value of the yr_built column. This suggests that some values in the yr_renovated column might represent the year built instead of renovation years.

Inconsistent Data Types:
Some columns, such as waterfront, view, condition, and grade, appear to have categorical data but are represented as objects (strings) instead of categorical data types.
The date column is represented as an object (string) but should be converted to a datetime data type for easier manipulation and analysis.

## Findings
The biggest factor that increases a house's price was number floors. Adding $19,000 to the asking price for every additional floor. Other major contributing factors were number o bathrooms and the condition rating of the home. Houses with a view also demand a higher fee.