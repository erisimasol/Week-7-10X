# README for Week 7 - KAIM Data Warehouse Project


## Overview

This document outlines the project for building a data warehouse to store data on Ethiopian medical businesses scraped from Telegram channels. The project involves creating a robust and scalable data pipeline with object detection capabilities using YOLO (You Only Look Once).

## Business Need

Kara Solutions, a data science company, requires a centralized data warehouse to enhance data analysis, improve decision-making, and facilitate efficient querying and reporting on Ethiopian medical businesses.

## Project Goals

1. Develop a data scraping and collection pipeline.
2. Build a data cleaning and transformation pipeline.
3. Implement object detection using YOLO.
4. Design and implement the data warehouse.
5. Integrate and enrich the collected data.


# README for Week-7-KAIM-10X Jupyter Notebook

## Overview

This Jupyter Notebook performs data analysis on Telegram messages related to "Doctors Ethiopia." It includes data cleaning, manipulation, and visualization techniques using libraries such as Pandas, NumPy, Matplotlib, Seaborn, and Streamlit.

## Contents

1. **Data Importing**
   - Imports necessary libraries.
   - Loads the dataset from a CSV file.

2. **Data Exploration**
   - Displays the first few rows of the dataset.
   - Prints the data frame's information, including the number of entries and data types.

3. **Missing Values Check**
   - Checks for and reports missing values in the dataset.

4. **Data Cleaning**
   - Drops irrelevant columns (`Media Path`, `Channel Title`, `Channel Username`).
   - Converts the `Date` column to a datetime format.
   - Creates new columns for date-only and time-only values extracted from the `Date` column.

5. **Word Count Calculation**
   - Defines a function to count words in each message.
   - Adds a new column to the DataFrame that holds the word count for each message.

6. **Data Visualization (Future Work)**
   - Plans for visualizing the data using Matplotlib and Seaborn for further insights.

## Requirements

To run this notebook, ensure you have the following libraries installed:

- pandas
- numpy
- matplotlib
- seaborn
- streamlit
- scipy
- ipywidgets
- !pip install torch torchvision
- !pip install opencv-python
- !pip install tensorflow 

You can install these libraries using pip:

```bash
pip install pandas numpy matplotlib seaborn streamlit scipy ipywidgets
```

## Usage

1. Open the Jupyter Notebook using Jupyter Lab or Jupyter Notebook.
2. Run each cell sequentially to execute the data analysis steps.
3. Modify the CSV file path in the code if necessary to match your local setup.

## Notes

- Ensure that the data file `1_telegram_data.csv` is available in the specified directory.


### Task 1: Data Scraping and Collection Pipeline

- Use Telegram API or scripts to extract data from relevant channels.
- Collect images for object detection.
- Store raw data in a temporary location and implement logging.

### Task 2: Data Cleaning and Transformation

- Clean data by removing duplicates, handling missing values, and standardizing formats.
- Use DBT (Data Build Tool) for data transformation and load cleaned data into the warehouse.

### Task 3: Object Detection Using YOLO

- Set up the environment and install necessary dependencies.
- Download the YOLO model and prepare the data.
- Process detection results and store them in the database.

### Task 4: Expose Data Using FastAPI

- Set up a FastAPI application to create API endpoints for data access.
- Implement CRUD operations and configure the database connection.

