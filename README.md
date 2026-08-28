# 🚗 Zoom Car Data Processing Pipeline

A **PySpark-based ETL data processing pipeline** built using **Databricks and Delta Lake** to ingest, clean, transform, and manage ZoomCar customer and booking data.

The pipeline processes raw JSON data through **staging and target layers**, performs data quality validation and transformations, and uses **Delta Lake MERGE operations** to efficiently update existing records and insert new records.

### 🔑 Key Features

* Ingests customer and booking data from JSON files
* Performs data cleaning and validation using PySpark
* Transforms booking timestamps, dates, and trip duration
* Validates customer records and email formats
* Creates staging tables using Delta Lake
* Implements MERGE logic for incremental data processing
* Handles cancelled bookings by removing them from the target dataset
* Updates existing customer and booking records
* Inserts new records into target Delta tables
* Uses Databricks Workflows to orchestrate the end-to-end pipeline

### 🛠️ Tech Stack

**Python | PySpark | Databricks | Delta Lake | JSON | Databricks Workflows**

### 📊 Pipeline Flow

**Raw JSON Data → Data Ingestion → Data Cleaning & Transformation → Staging Delta Tables → Merge/Upsert → Target Delta Tables**

This project demonstrates practical **data engineering concepts including ETL processing, data quality, incremental loading, Delta Lake operations, and workflow orchestration**.
