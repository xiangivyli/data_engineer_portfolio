# Data Engineer Portfolio
The subdivision about data engineering, it covers **airflow** with high-level features and involves popular tools, like **data transformation (dbt)**, **infrastructure as code (terraform)**, **data quality (soda)**, **data visualisation (streamlit, Power BI)**, **cloud-based data warehouse(BigQuery, Snowflake)**, etc. 

And also adds tiny projects for on-premises databases and Business Intelligence (BI) Tools.

The purpose of each project is to automate end-to-end data pipelines (from raw data to data reporting), equipped with containerisation and infrastructure as code.

Some projects are folders in this repository, some projects are independent repositories for easy execution, and some tiny projects are written as a blog on my website.

# Table of Contents
## Part A Cloud-based Data Warehouse

### Job Postings on Linkedin

Tools:
 - Python with Jupyter Notebook
 - Data Transformation: **dbt**
 - Data Loading: **Airflow** (Astro Cli)
 - Data Visualisation: **Power BI**
 - Data Quality Testing: **Soda**
 - Data Lake: **Google Cloud Storage**
 - Data Warehouse: **BigQuery**
 - Data Orchestration: **Airflow**

Objectives:
   - extract raw data from Kaggle, and process data for a read-to-use dataset
   - reduce file size and identify schema by using parquet files
   - achieve automation and monitorization with Airflow and dbt
   - visualize data for insights with Power BI

### [PM2.5-Monitoring](https://github.com/xiangivyli/pm25_monitoring)

Tools:
 - Data Extraction, Transformation, Validation: API, Python
 - Data Orchestration: **Airflow**
 - Database: **DuckDB**
 - Data Reporting： **Streamlit**
 - Containerization: **Docker** and **Docker Compose**

Objectives:
   - Ingest pm2.5 data into DuckDB daily
   - Transformation is triggered by data ingestion in Airflow
   - Streamlit container keeps running and monitors the pm2.5 data in real-time 

## Part B On-premises Database

### [Data Platform Design for Healthcare Research (Database)](https://xiangivyli.com/blog/data-platform-design-for-healthcare-research-mysql/)
 
Tool: **MySQL**
 
Objectives:
   - identify how diseases begin and progress
   - integration of genetics and healthcare data
   - research-ready, well-curated and well-documented data

### [Nomalisation (SQL Server)](https://xiangivyli.com/blog/normalisation-for-professors-in-organisations-with-sql-server/)

Tool: **SQL Server**

Objectives:
  - Split a table into a fact table and dimension tables
  - Set datatype, primary key, foreign key and referential integrity

## Part C Business Intelligence Tools (BI)

### [Revenue increase strategy analysis for Google merchandise store (Business Intelligence)](https://xiangivyli.com/blog/revenue-google-store/)

Tool: Google Analytics and **Looker**

Objectives:
  - map the persona of customers
  - identify the performance of products
  - identify the pattern of activity
  - the funnel diagram shows the buyer's journey

### [Education-Focused Analysis (Power BI and Python)](https://xiangivyli.com/blog/education-focused-analysis-assessment-types-final-results)

Tool: Python and Power BI

Objectives:
  - Prepare a cleansed dataset for analysis
  - A logical story to explain why the mix and weighting of assessment types changed the final result

### [A self-service platform for GDP, Life Satisfaction and Education Level](https://xiangivyli.com/blog/an-information-retrieval-platform-for-gdp-satisfaction-education/)

Tool: Tableau

Objectives:
  - Provide users a platform to retrieve information about **GDP**, **Life Satisfaction**, and **Education Level** for countries in different year
  - Give a general idea about this information for regions
  - Check the relationship between **education level** and **GDP per capita**
