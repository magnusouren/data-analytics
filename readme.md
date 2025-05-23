# Data Analytics - What Makes a Country Happy?

## Overview
This repository is the codebase of the project conducted in the course Data Analytics (BMEGT20MN49) at BME in the spring semester of 2025.

## Task
The objective of this task is to examine the relationship between the Happiness Index Score
and other variables describing the country, such as identifying which characteristics
contribute most to a country's happiness. 

## Dataset
Dataset: [https://www.kaggle.com/datasets/sougatapramanick/happiness-index-2018-2019](https://www.kaggle.com/datasets/sougatapramanick/happiness-index-2018-2019)

## Preprocessing

The dataset contains data from two different years, 2018 and 2019. The data is collected into one dataset, and the column year is added.

The dataset contains the following columns:
- Overall rank
    - The rank of the country in the Happiness Index Score, not used in the analysis
- Country or region
    - The name of the country or region
- Year
    - The year of the data collection
- Score
    - The Happiness Index Score, a measure of the overall happiness of the country from 0 to 10, where 0 is the lowest and 10 is the highest
- GDP per capita
    - The GDP per capita of the country, a measure of the economic strength of the country
- Social support
    - The social support of the country, a measure of the interpersonal networks and social connections of the country
- Healthy life expectancy
    - The healthy life expectancy of the country, a measure of the health and well-being of the country
- Freedom to make life choices
    - The freedom to make life choices of the country, a measure of the personal freedom and autonomy of the country
- Generosity
    - The generosity of the country, a measure of the charitable behavior and altruism of the country
- Perceptions of corruption
    - Note: The variable reflects the absence of corruption, meaning higher values indicate less perceived corruption.

It contains 312 rows

### Standardization

The dataset contains some columns that are not in the same range. For example, the GDP per capita is in the range of 0 to 100, while the score is in the range of 0 to 10. To standardize the data, we can used Z-score normalization. This method transforms the data into a standard normal distribution with a mean of 0 and a standard deviation of 1.
