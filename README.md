# AWS-Market-Analysis
This project aims to generate a complete ETL and EDA pipeline and analysis of the current job market for data analysts, with the aim of evaluating which skills are the most sought after, the cities and companies that are hiring the most data analysts, and also investigate the salary outcome of remote vs non-remote work. The project is built using Amazon PostgresSQL, sqlalchemy, sklearn, and Python’s libraries such as pandas and seaborn. 

## Methodology
To start I used sqlalchemy to extract the data from the database and created three pandas DataFrames. In addition, I joined the tables on their primary key, then saved the joined data into a CSV file in the data folder. 

After data extraction, next, I transform the data by first dropping all the null values from the description_tokens and the salary_standardized columns. Then filled in the missing values in the work_from_home column to be false. After cleaning this data I saved it into a CSV file and into the data folder. Furthermore, I created a new column for each possible skill in the description_tokens column using a multi-label binarizer. I first converted the description_tokens column into a column of lists then encoded each skill as a unique column, then saved it as csv file into the data folder.

 Lastly, after cleaning and preparing all the data, I did some EDA to answer the questions above. I created some visualization of the distribution of standard salaries and then explored the salaries of working from home vs office. Also salaries of jobs that require skills such as Python, tableau, or SQL versus jobs that do not require these skills. I also looked at top-ranked skills, companies, and cities for data analyst positions. To get more insight I did statistical analysis by performing a t-test and a Kolmogorov Smirnov test. 

## Visuals & Results

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
