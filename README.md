# AWS-Market-Analysis

## Table of Contents 

- [Project Overview](#project-overview)
- [Data Sources ](#data-sources)
- [Tools](#tools)
- [Methodology](#methodology)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Data Analysis](#data-analysis) 
- [Results Findings](#results-findings)
- [Recommendations](#recommendations)
- [Next Actions](#next-actions)

##  Project Overview 

This project aims to develop a comprehensive ETL (Extract, Transform, Load) and EDA (Exploratory Data Analysis) pipeline to analyze the current job market for data analysts. The key objectives include:

- Evaluating which technical and soft skills are most sought after by employers in the data analysis field.
- Identifying the cities and companies that are actively hiring the most data analysts, providing insight into regional demand.
- Investigating salary outcomes to compare compensation for remote vs. non-remote positions, offering a clear picture of market trends.

The outcome of this project will provide valuable insights for aspiring data analysts and professionals looking to understand current market demands and optimize their career strategies.

## Data Sources 

Data: The primary dataset used for this analysis is the CSV files in the data folder. This data was retrieved from an AWS site.

## Tools 

PostgreSQL: For database management and data storage.

SQLAlchemy: For SQL toolkit and Object-Relational Mapping (ORM) in Python.

sklearn: For implementing machine learning algorithms and models.

Python Libraries:

  - Pandas: For data manipulation and analysis.
  - Seaborn: For data visualization and statistical plotting.
    
## Methodology
In the data analysis phase, the following tasks were performed:

1. Data extraction from the PostgreSQL database using SQLalchemy.
2. Data inspection, cleaning, and manipulation. (Dropped null values, filled missing values, created new columns)
3. Created a new column for each possible skill in the description_tokens column using MultiLabelBinarizer:
  - Converted description_tokens into a list of skills.
  - Encoded each skill as a unique column and saved it as a CSV file in the data folder.
4. Created three pandas DataFrames from the extracted data.
5. Joined tables on their primary key and saved the merged data into a CSV file in the data folder.
6. Conducted visualizations to examine the distribution of standard salaries.
7. Compared salaries for remote versus non-remote based positions.
8. Analyzed salaries for jobs requiring skills like Python, Tableau, or SQL versus those that do not.
9. Identified top-ranked skills, companies, and cities for data analyst positions.
10. Performed statistical analysis using a t-test and Kolmogorov-Smirnov test to gain deeper insights into the data.

## Exploratory Data Analysis
EDA involved exploring the sales data to answer key questions such as:

- What is the salary standard for data analysts? 
- What is the salary standardized for remote v non-remote workers?
- What are the most sought-after skills by employers in the data analysis field?
- Which cities and companies are actively hiring data analysts?

## Data Analysis

Here are some examples of the visuals from the analyses

![](images/sal_stand_boxplot.jpg) 

This histogram indicates that the median salary for data analysts is approximately $100,000. The distribution is right-skewed, which suggests that the mean salary is higher than the median. The presence of a significant number of outliers contributes to this skewness. By removing these outliers, we could achieve a distribution that is closer to normality.
![](images/work_from_home_boxplot.jpg)

This box plot compares the salaries of remote workers versus non-remote workers. The observation shows that the median salary for those who work from home is lower than that of those who work from the office. Both box plots exhibit a significant number of outliers. Additionally, both the T-test and KS-test yield p-values of less than 0.05, indicating a statistically significant difference between the salaries of remote and non-remote workers. 

- KstestResult(statistic=0.18113066066731165, pvalue=3.184538697598516e-26)

- Ttest_indResult(statistic=-3.9416042344144477, pvalue=8.34357154515801e-05)

![](images/ranked_skills.jpg)

This bar graph highlights the top-ranked skills for data analysts. The most frequently cited skills are SQL, Excel, Tableau, Python, Power BI, and R. This is consistent with industry expectations, as these are the tools and technologies commonly used by data analysts in their day-to-day tasks.
These boxplots illustrate jobs that require SQL, python, or Tableau versus jobs that do not need these skills.

#### These boxplots below compare jobs that require SQL, Python, or Tableau with those that do not

![](images/sql_salaries_boxplot.jpg)

- KstestResult(statistic=0.14859694970660242, pvalue=2.428624055011539e-22) 

- Ttest_indResult(statistic=5.010842822466604, pvalue=5.845959349504406e-07)

![](images/python_salaries_boxplot.jpg)

- KstestResult(statistic=0.10816134598371768, pvalue=5.1004787412886686e-05)

- Ttest_indResult(statistic=4.752007752153935, pvalue=2.1425679458331286e-06)

![](images/tableau_salaries_boxplot.jpg)

- KstestResult(statistic=0.22652993258106247, pvalue=1.9059409500066205e-33)

- Ttest_indResult(statistic=2.60192320578311, pvalue=0.009331719250939272)

These boxplots demonstrate that jobs requiring skills such as SQL, Python, and Tableau offer higher salaries compared to those that do not. The p-values from both the KS-test and T-test are less than 0.05, indicating a statistically significant difference in salaries between jobs that require these skills and those that don't. This underscores the importance of possessing SQL, Python, and Tableau for anyone seeking a data analyst position with a competitive salary.


![](images/ranked_cities.jpg)

![](images/company_salaries_boxplot.jpg)

These visualizations suggest that apart from major hubs like Los Angeles, New York, and Atlanta, cities such as Wichita, Maize, and Tulsa also rank highly for data analyst opportunities, following 'United States' and 'Anywhere' as general categories. However, the representation is unclear and may not accurately reflect the true distribution.

For top employers, the data shows a mix of companies and external contracts. Some of the leading companies hiring data analysts, based on this visualization, include Citi, Edward Jones, and Apex Systems

## Results Findings

The analysis results are summarized as follows:

- The median salary for data analysts is approximately $100,000. The salary distribution is right-skewed, with the mean salary higher than the median.
A significant number of outliers are present, and removing them could normalize the distribution.
- Both the T-test and KS-test indicate p-values of less than 0.05, suggesting a statistically significant difference between the salaries of remote and non-remote workers.
- The most in-demand skills include SQL, Excel, Tableau, Python, Power BI, and R. These skills are integral to the daily tasks of data analysts, making them essential for success in the field.
- Jobs requiring SQL, Python, and Tableau tend to offer higher salaries than those that do not. The p-values from the KS-test and T-test (both < 0.05) confirm a statistically significant difference in salaries, emphasizing the importance of these skills for securing better-paying positions.
- Major cities like Los Angeles, New York, and Atlanta are top locations for data analysts. Other notable cities include Wichita, Maize, and Tulsa, though some representations in the data may be unclear.
- Leading companies hiring data analysts include Citi, Edward Jones, and Apex Systems, with a mix of companies and external contracts featured. 

## Recommendations

Based on the analysis, the following is recommended:

- Focus on SQL, Python, Excel, and Tableau, given their impact on salary. Aspiring and current data analysts should prioritize mastering these skills to enhance their employability and earning potential.
- Data analysts should consider relocating to or seeking opportunities in major cities like Los Angeles, New York, and Atlanta, which are top locations for data analyst roles.
- Given that on-site positions tend to offer higher salaries, data analysts who prioritize income might consider office-based roles. However, personal preferences for work-life balance and flexibility should also be weighed.
- Use insights from the analysis to negotiate higher salaries by highlighting expertise in high-demand skills like SQL, Python, and Tableau, especially when applying for roles in higher-paying cities or companies.

## Next Actions

Further action to enhance this project could include: 
-  Removing outliers from the data and reassessing the distribution and statistical significance of the results. This will help in understanding how these outliers affect the overall analysis and potentially lead to more accurate insights.
-  Acquiring more precise data to address the issue of generic categories like 'Anywhere' and 'United States' being listed as top cities. This will provide a clearer and more accurate representation of the cities with the highest demand for data analysts.
-  Ensuring that the data used for identifying top companies hiring data analysts excludes external contracts. This will help in focusing solely on established companies, providing a more accurate reflection of the job market. 

