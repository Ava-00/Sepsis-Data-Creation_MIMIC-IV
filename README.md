# Comprehensive Time-Series Database for Sepsis Patients using MIMIC-IV

## Overview

This project focuses on **creating a comprehensive time-series database for Sepsis patients** derived from the **MIMIC-IV** dataset, a widely-used and publicly available critical care database. The goal is to build an efficient system that enables the analysis and modeling of Sepsis in critically ill patients by organizing and processing time-series data, such as vital signs, lab results, medications, and clinical interventions, over time. 

By utilizing the rich, multi-dimensional nature of the MIMIC-IV dataset, this project aims to facilitate further research and development of predictive models, clinical decision support systems, and analytics tools to improve the detection, treatment, and outcomes of Sepsis in ICU patients.

### Key Objectives:
- **Data Extraction and Processing**: Efficiently extract, preprocess, and clean the raw data from the MIMIC-IV database, ensuring it is suitable for time-series analysis.
- **Time-Series Database Construction**: Create a structured, scalable time-series database that organizes patient data across multiple time points, capturing vital signs, lab results, medication usage, and clinical interventions.
- **Sepsis Detection**: Utilize the created database to facilitate the identification and prediction of Sepsis in ICU patients based on their physiological and clinical data over time.
- **Query Optimization**: Design efficient queries and data retrieval methods to handle large-scale time-series data, enabling researchers and clinicians to perform analyses and modeling tasks efficiently.
  
This project leverages state-of-the-art tools like **Python**, **SQL**, and **Apache Spark** for data processing and analysis. The database structure supports the needs of both real-time clinical applications and retrospective research projects, helping to bridge the gap between clinical decision-making and research advancements.

### Key Features:
- **Time-Series Data Organization**: Organizes complex patient data (vital signs, lab tests, medications, etc.) into a time-series format that can be easily queried and analyzed for Sepsis detection.
- **Scalable Database Architecture**: Uses Apache Spark for distributed processing, allowing efficient handling of large-scale datasets such as MIMIC-IV.
- **SQL Integration**: Leverages SQL for structured querying and extraction of specific data points from the MIMIC-IV database.
- **Sepsis Prediction and Analytics**: Prepares data for time-series analysis and machine learning models that aim to predict Sepsis onset and progression.
- **Data Preprocessing and Cleansing**: Applies a series of preprocessing steps to handle missing values, normalize data, and ensure that the time-series data is suitable for downstream analysis.

## Technologies Used:
- **Programming Languages**: Python, SQL
- **Libraries/Frameworks**: Pandas, NumPy, Apache Spark, SQLAlchemy, Matplotlib, Scikit-learn
- **Database**: MIMIC-IV (available through PhysioNet)
- **Data Processing**: Apache Spark for distributed computing, Python for data cleaning and manipulation
- **Tools**: Jupyter Notebooks for prototyping and analysis
