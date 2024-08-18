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

This visualization displays that the median salary of a data analyst is close to 100000 and this histogram is right skewed therefore the mean is greater than the median. Also, there are a lot of outliers, therefore if we remove the outlier we can get close to normality. 

![](images/work_from_home_boxplot.jpg)

This box plot compares remote workers versus non-remote workers and based on this observation we notice that the median salary for people who work from home is less compared to those who work from the office. And both of these boxplots have a lot of outliers. The T-test and KS-test both indicate a p-value of less than 0.05 therefore this tells us that there is a statistically significant difference between working from home and not working from home, as the salaries indicate as well.  

KstestResult(statistic=0.18113066066731165, pvalue=3.184538697598516e-26)

Ttest_indResult(statistic=-3.9416042344144477, pvalue=8.34357154515801e-05)

![](images/ranked_skills.jpg)

This bar graph displays the top-ranked skills and we can observe that the top-ranked skills for data analysts are SQL, excel, tableau, python, power-bi, and R. This is reasonable since these are skills that most data analysts use in their day-to-day tasks. 

These boxplots illustrate jobs that require SQL, python, or Tableau versus jobs that do not need these skills

![](images/sql_salaries_boxplot.jpg)

KstestResult(statistic=0.14859694970660242, pvalue=2.428624055011539e-22) 

Ttest_indResult(statistic=5.010842822466604, pvalue=5.845959349504406e-07)

![](images/python_salaries_boxplot.jpg)

KstestResult(statistic=0.10816134598371768, pvalue=5.1004787412886686e-05)

Ttest_indResult(statistic=4.752007752153935, pvalue=2.1425679458331286e-06)

![](images/tableau_salaries_boxplot.jpg)

KstestResult(statistic=0.22652993258106247, pvalue=1.9059409500066205e-33)

Ttest_indResult(statistic=2.60192320578311, pvalue=0.009331719250939272)

These boxplots indicate that jobs requiring skills such as SQL, Python, and Tableau have a higher salary than jobs that do not require SQL, python, and Tableau. In addition, the p-values of less than 0.05 from the KS-test and T-tes tell us that there is a statistically significant difference between the salaries for jobs that require SQL, python, and Tableau and those that do not, therefore making it important for anyone seeking data analyst job to posses these skills for a better salary.

![](images/ranked_cities.jpg)

![](images/company_salaries_boxplot.jpg)

From these visualizations, some of the top cities for data analysts apart from LA, NY, and Atlanta, are cities such as Wichita, Maize, and Tulsa, after the United States and Anywhere being the top, however, this is not a good representation as it is not clear. For the top companies, there is a mix of companies and external contracts therefore some of the top companies for data analyst base on this visualisation are Citi, Edward Jones, and Apex Systems.  

## Next Actions
A further action that can be taken to better this project is to remove outliers in some of the data and see what effect it has, and also for top-ranked cities have better data because the top two are 'anywhere' and the united states, therefore, a better data to make things clear. Similarly, have better data so we do not include contract work included in companies that are hiring. 
