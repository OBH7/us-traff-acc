# US Accidents Data Engineering Project

## Project Overview
This project is designed to process and analyze **US accidents data** using **Apache Airflow**. It automates the process of loading, cleaning, and transforming the accident data from multiple CSV files into a single cleaned dataset. The project uses **Airflow** to define the ETL pipeline, which is scheduled to run daily, cleaning the data and storing it in a more accessible format (e.g., a cleaned CSV or database).

## Project Components
- **Airflow DAG**: The ETL process is defined in `us_acc_etl.py`, which handles the extraction, transformation, and loading (ETL) of accident data.
- **Data**: Example CSV files are included in the `/data` directory (e.g., `acc_16.csv`, `acc_17.csv`).
- **Dependencies**: The project requires specific Python packages, listed in `requirements.txt`. Ensure you install these packages before running the DAGs.

## File Structure

airflow-us-accidents-project/ 
├── dags/
│ └── us_acc_etl.py # The Airflow DAG defining the ETL process 
├── requirements.md # Python dependencies 
├── README.md # Project documentation 
└── .gitignore # Git ignore file to avoid uploading unnecessary files


## Getting Started

### Prerequisites
1. **Apache Airflow**: Ensure you have Airflow installed. You can follow the official documentation for installation: [Airflow Installation](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html).
2. **Python 3.9+**: This project was developed with Python 3.9, and it's recommended to use the same or higher version.
3. **Install Dependencies**: Install the necessary Python dependencies by running:
   ```bash
   pip install -r requirements.txt

Setting Up Airflow
Start the Airflow scheduler:
bash
Copy code
airflow scheduler
Start the Airflow webserver:
bash
Copy code
airflow webserver
Open your browser and go to http://localhost:8080 to access the Airflow UI.
Running the DAG
Copy the DAG file (us_acc_etl.py) into the dags/ directory in your Airflow home directory.
Ensure the necessary CSV files are present in the /data directory.
In the Airflow UI, unpause the DAG to start it manually or wait for it to run based on the daily schedule.
DAG Details
DAG Name: etl_us_accidents
Schedule: Runs daily to process and clean accident data.
Tasks:
Load and Clean Data: Extracts data from multiple CSV files, fills in missing values, and writes the cleaned data to a new CSV.
How the DAG Works
The us_acc_etl.py DAG handles the following tasks:

Load Data: Reads accident data from multiple CSV files (acc_16.csv, acc_17.csv, etc.).
Clean Data: Fills missing values and performs basic data transformations.
Store Cleaned Data: Outputs the cleaned data into a new CSV or loads it into a database (e.g., PostgreSQL).
Future Improvements
Add functionality to load the cleaned data into a SQL database.
Integrate more sophisticated data validation steps.
Support for incremental data updates.

Data Source: https://www.kaggle.com/datasets/jonbown/us-2020-traffic-accidents