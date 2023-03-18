from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import pandas as pd
from config import key 
# connect to the database
engine = create_engine(key)
Base = automap_base()
Base.prepare(engine, reflect=True)

# save classes as variables, prepare classes
jobs = Base.classes.jobs
salaries = Base.classes.salaries
skills = Base.classes.skills
# query our database (pull data and save into objects)
session = Session(engine)

#Extract all 3 tables from Amazon RDS postgres database
jobs_table = session.query(jobs)
print(jobs_table)
salaries_table = session.query(salaries)
print(salaries_table)
skills_table = session.query(skills)
print(skills_table)

# using the tables to create new pandas dataframe
jobs_df = pd.read_sql(jobs_table.statement, engine.connect())
print(jobs_df)
salaries_df = pd.read_sql(salaries_table.statement, engine.connect())
print(salaries_df)
skills_df = pd.read_sql(skills_table.statement, engine.connect())
print(skills_df)

#joining all three tables on their primary key
merge_1 = pd.merge(salaries_df, jobs_df, how="inner", on=["id"])
total_merge = pd.merge(merge_1, skills_df, how="inner", on=["id"])
print(total_merge)

total_merge.to_csv('data/joined_data.csv', encoding= 'utf-8', index = False, line_terminator= '\n' )  

