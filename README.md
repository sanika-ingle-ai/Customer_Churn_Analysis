# Customer Churn Analysis

An end-to-end data analytics project that explores customer churn in a
telecommunications dataset using **Excel, SQL Server, Python, and Power
BI**.

The project focuses on data cleaning, validation, exploratory data
analysis, and interactive business reporting. It identifies customer
segments and service/account patterns associated with churn.

------------------------------------------------------------------------

## Table of Contents

-   [Project Overview](#project-overview)
-   [Business Problem](#business-problem)
-   [Objectives](#objectives)
-   [Dataset](#dataset)
-   [Technology Stack](#technology-stack)
-   [Project Workflow](#project-workflow)
-   [Key Findings](#key-findings)
-   [Power BI Dashboard](#power-bi-dashboard)
-   [Project Structure](#project-structure)
-   [How to Use This Project](#how-to-use-this-project)
-   [Business Recommendations](#business-recommendations)
-   [Limitations](#limitations)

## Project Overview

Customer churn occurs when customers stop using a company's products or
services. Understanding churn patterns helps businesses investigate
customer experience and identify opportunities to improve retention.

This project analyzes the IBM Telco Customer Churn sample dataset. The
workflow includes:

1.  Cleaning and preparing the dataset in Microsoft Excel.
2.  Validating records and performing business analysis in SQL Server.
3.  Exploring churn patterns and creating visualizations in Python.
4.  Building an interactive Power BI dashboard with KPI cards, charts,
    and slicers.

## Business Problem

A telecommunications company wants to understand how customer tenure,
contract type, payment method, internet service, and customer
characteristics relate to customer churn.

The analysis provides descriptive insights that can help the business
decide which customer groups or service experiences require further
investigation.

## Objectives

-   Inspect and clean the customer dataset.
-   Validate row counts, unique customer IDs, duplicates, and important
    fields.
-   Calculate overall churn and compare churn across customer
    categories.
-   Perform exploratory data analysis using Python.
-   Build an interactive Power BI dashboard.
-   Communicate findings through business insights and recommendations.

## Dataset

**Dataset:** IBM Telco Customer Churn sample\
**Common source filename:** `WA_Fn-UseC_-Telco-Customer-Churn.csv`

  Dataset detail         Value
  -------------------- -------
  Customer records       7,043
  Columns                   21
  Churned customers      1,869
  Retained customers     5,174

The dataset includes customer profile, tenure, services, contract,
payment method, monthly charges, total charges, and churn status.

## Technology Stack

  -----------------------------------------------------------------------
  Technology                          Purpose
  ----------------------------------- -----------------------------------
  Microsoft Excel                     Initial data inspection and
                                      cleaning

  SQL Server / SSMS                   Data validation, aggregation, and
                                      business queries

  Python                              Exploratory data analysis

  Pandas, NumPy                       Data manipulation and analysis

  Matplotlib, Seaborn                 Data visualization

  Power BI Desktop                    Interactive dashboard

  DAX                                 KPI calculations and calculated
                                      columns

  Git and GitHub                      Version control and project
                                      portfolio
  -----------------------------------------------------------------------

## Project Workflow

### 1. Excel -- Data Cleaning

-   Inspected the dataset and checked row and column counts.
-   Checked duplicate rows and duplicate customer IDs.
-   Investigated blank values.
-   Found 11 whitespace-only values in `TotalCharges`, associated with
    customers whose tenure was zero.
-   Converted those values to numeric zero and saved a separate cleaned
    CSV.

Example formula used:

``` excel
=IF(LEN(TRIM(T2))=0,0,VALUE(T2))
```

### 2. SQL Server -- Data Validation and Analysis

The cleaned CSV was imported into SQL Server database `CustomerChurnDB`,
using the main table `dbo.TelcoCustomerChurn`.

Validation results recorded during the project:

-   7,043 total records.
-   7,043 distinct customer IDs.
-   Zero duplicate customer IDs.
-   Zero missing values in the checked key fields: `customerID`,
    `TotalCharges`, and `Churn`.
-   11 records with `TotalCharges = 0`.

SQL analysis covered:

-   Overall churn and retention.
-   Churn by contract type.
-   Churn by payment method.
-   Churn by internet service.
-   Churn by tenure group.
-   Average monthly charges by churn status.

Example SQL query:

``` sql
SELECT
    Contract,
    COUNT(*) AS TotalCustomers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS ChurnedCustomers,
    100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*) AS ChurnRatePercent
FROM dbo.TelcoCustomerChurn
GROUP BY Contract
ORDER BY ChurnRatePercent DESC;
```

### 3. Python -- Exploratory Data Analysis

EDA was completed in `Customer_Churn_EDA.ipynb`.

Libraries used:

-   Pandas
-   NumPy
-   Matplotlib
-   Seaborn

Analysis included dataset inspection, missing-value and duplicate
checks, churn distributions, category comparisons, tenure grouping, a
contract crosstab, and business-insight summaries.

Visualizations saved during the project:

-   `churn_distribution.png`
-   `churn_by_contract.png`
-   `churn_by_tenure.png`
-   `correlation_heatmap.png`
-   `churn_by_payment_method.png`
-   `churn_by_internet_service.png`
-   `churn_by_senior_citizen.png`

### 4. Power BI -- Interactive Dashboard

The Power BI report uses the SQL Server customer table and includes four
KPI cards:

-   Total Customers
-   Churned Customers
-   Retained Customers
-   Overall Churn Rate

It includes seven charts:

1.  Customer Churn by Contract
2.  Customer Churn by Payment Method
3.  Customer Churn by Internet Service
4.  Customer Churn by Gender
5.  Customer Churn by Tenure
6.  Customer Churn by Senior Citizen
7.  Customer Churn by Customer Segment

Three dropdown slicers provide interactive filtering:

-   Contract
-   Internet Service
-   Gender

The report uses green for retained customers (`Churn = No`) and red for
churned customers (`Churn = Yes`). Slicer functionality was tested
during the project.

## Key Findings

### Overall Churn

  Metric                 Result
  -------------------- --------
  Total customers         7,043
  Churned customers       1,869
  Retained customers      5,174
  Overall churn rate     26.54%

### Churn by Contract

  Contract           Churn rate
  ---------------- ------------
  Month-to-month         42.71%
  One year               11.27%
  Two year                2.83%

Month-to-month customers had the highest recorded churn rate among the
contract groups.

### Churn by Payment Method

  Payment method                Churn rate
  --------------------------- ------------
  Electronic check                  45.29%
  Mailed check                      19.11%
  Bank transfer (automatic)         16.71%
  Credit card (automatic)           15.24%

Electronic-check users had the highest recorded churn rate among the
listed payment methods.

### Churn by Internet Service

  Internet service        Churn rate
  --------------------- ------------
  Fiber optic                 41.89%
  DSL                         18.96%
  No internet service          7.40%

Fiber-optic customers had a higher recorded churn rate than the other
internet-service groups.

### Churn by Tenure

  Tenure group      Churn rate
  --------------- ------------
  0--12 months          47.44%
  13--24 months         28.71%
  25--48 months         20.39%
  49+ months             9.51%

The 0--12 month group had the highest recorded churn rate.

### Other Findings

  Comparison                                          Result
  ------------------------------------------------ ---------
  Senior citizen churn rate                           41.68%
  Non-senior citizen churn rate                       23.61%
  Average monthly charges for churned customers      \$74.44
  Average monthly charges for retained customers     \$61.27

### Customer Segments

  Segment             Tenure definition     Recorded churn rate
  ------------------- ------------------- ---------------------
  New Customers       0--12 months                       47.44%
  Growing Customers   13--48 months                      23.64%
  Loyal Customers     49+ months                          9.51%

## Power BI Dashboard

The report and screenshot are stored in `04_PowerBI/`.

-   Power BI file: `Customer_Churn_Dashboard.pbix`
-   Dashboard screenshot: `Dashboard_Screenshots/Overview_Dashboard.png`

Open the PBIX file using Power BI Desktop to interact with the report
and its slicers.

## Project Structure

``` text
Customer_Churn_Analysis/
├── 01_Dataset/
│   ├── Raw_Data/
│   │   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│   └── Cleaned_Data/
│       └── Telco_Customer_Churn_Cleaned.csv
├── 02_SQL/
│   ├── SQL_Queries.sql
│   └── SQL_Analysis_Results/
├── 03_Python_EDA/
│   ├── Customer_Churn_EDA.ipynb
│   ├── EDA_Results/
│   └── Visualizations/
├── 04_PowerBI/
│   ├── Customer_Churn_Dashboard.pbix
│   ├── Dashboard_Screenshots/
│   │   └── Overview_Dashboard.png
│   └── DAX_Measures.txt
├── 05_Documentation/
│   ├── Project_Report.pdf
│   └── Business_Insights.md
└── README.md
```

## How to Use This Project

1.  Clone or download this repository.
2.  Open the cleaned dataset from `01_Dataset/Cleaned_Data/`.
3.  Review and run the SQL script in `02_SQL/SQL_Queries.sql` after
    configuring the SQL Server database and table.
4.  Open `03_Python_EDA/Customer_Churn_EDA.ipynb` in Jupyter Notebook or
    JupyterLab and update the CSV path if needed.
5.  Open `04_PowerBI/Customer_Churn_Dashboard.pbix` in Power BI Desktop.
    Update the SQL Server connection to match your environment if
    prompted.
6.  Read `05_Documentation/Project_Report.pdf` and
    `05_Documentation/Business_Insights.md` for the project explanation
    and findings.

## Business Recommendations

Based on the observed patterns, areas for further investigation include:

1.  Review the customer journey for month-to-month contract customers
    and assess whether relevant longer-term plan options improve
    retention.
2.  Strengthen onboarding and support during the first 12 months.
3.  Investigate billing experience and payment friction for
    electronic-check users.
4.  Review fiber-optic service reliability, pricing, customer
    expectations, and support issues.
5.  Study customer charges alongside service usage, complaints, and
    customer value before proposing retention offers.

## Limitations

-   The findings are descriptive associations from the analyzed dataset;
    they do not establish causation.
-   The analysis does not include a predictive churn model.
-   Further investigation using cancellation reasons, service
    complaints, outage data, and customer feedback would be needed to
    test possible explanations.
-   Update local database names and file paths before running the
    scripts in a different environment.

------------------------------------------------------------------------

**Project:** Customer Churn Analysis\
**Domain:** Telecommunications\
**Tools:** Excel \| SQL Server \| Python \| Power BI
