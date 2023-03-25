# ASW-Market-Analysis
This project aim to generate a complete ETL and EDA pipeline and analysis of the current job market for data analysts, with the aim of evaluating which skills are the most sought after, the cities and companies that are hiring the most data analysts and also investigate the salary outcome of remote vs non-remote work. The project is built using Amazon PostgresSQL, sqlalchemy, sklearn and python’s libraries such as pandas and seaborn. 

## Methodology
To start I used sqlalchemy to extract the data from the database, and created three pandas dataframes. In addition I joined the tables on their primary key, then saved the joined data into a csv file in the data folder. In the next phase of transforming the data, I first read the joined csv file and dropped all the null values from the description_tokens and the salary_standardized columns. Then filled in the missing values in the work_from_home column to be false. After cleaning this data I saved into csv file and into the data folder. Furthermore, I created a new column for each possible skill in the description_tokens column using a multi label binarizer. I first converted the description_tokens column into a column of lists then encoded each skill as a unique column, then save it as csv file into the data folder. Lastly, after cleaning and preparing all the data, I did some eda in order to answer the questions above. I created some visualisation of the distribution of standard_salaries and then exploring the salaries of working from home vs office. Also salaries of having skills such as python or tableau or sql versus not possessing these skills. I also looked at top ranked skills, companies and cities for data analysts positions. To get more insight I did statistical analysis by performing a t-test and a Kolmogorov Smirnov test. 

## Results
image.png
Observing the visualisations we can notice that people who work from home have less of a salary compared to those who work from the office. 
Despite both remote and non-remote having a p-value greater than 0.05, if we drop the outliers the p-values could change. 

image.png
In addition, we also observe that the top ranked skills for data analyst are SQL, excel, tableau, python, power-bi, and R. 
image.png 
image.png
image.png
Also people with SQL, python, and tableau skill have a higher salary compared to those who do not. 

image.png
image.png
Moreover, some of the top cities for data analyst apart from LA, NY and Atlanta, are cities such as Wichita, Maize, Tulsa.  For the top companies, there is a mix of companies and external contracts therefore some of the top companies for data analyst base on this visual are Citi, Edward Jones and Apex systems.  

## Next Actions
Further action that can be taking to better this project is to remove outlier in some of the data and see what effect it has, and also for top ranked cities have better data because the top two are anywhere and united states therefore a better data to make things clear.