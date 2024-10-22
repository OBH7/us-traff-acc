from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd

# ETL functions (copy your Jupyter logic here)
def load_and_clean_accident_data():
    # Logic to load and clean accident data
    accident_files = [
        'acc_16.csv',
        'acc_17.csv',
        'acc_18.csv',
        'acc_19.csv',
        'acc_20.csv'
    ]
    accident_data = []
    for file in accident_files:
        df = pd.read_csv(file)
        df.fillna('Unknown', inplace=True)
        accident_data.append(df)
    accident_data_cleaned = pd.concat(accident_data, ignore_index=True)
    accident_data_cleaned.to_csv('cleaned_accidents.csv', index=False)

def load_and_clean_person_data():
    # Logic to load and clean person data
    person_files = [
        'pers_16.csv',
        'pers_17.csv',
        'pers_18.csv',
        'pers_19.csv',
        'pers_20.csv'
    ]
    person_data = []
    for file in person_files:
        df = pd.read_csv(file, encoding='ISO-8859-1', low_memory=False)
        df.fillna('Unknown', inplace=True)
        person_data.append(df)
    person_data_cleaned = pd.concat(person_data, ignore_index=True)
    person_data_cleaned.to_csv('cleaned_person.csv', index=False)

def load_and_clean_vehicle_data():
    # Logic to load and clean vehicle data
    vehicle_files = [
        'veh_16.csv',
        'veh_17.csv',
        'veh_18.csv',
        'veh_19.csv',
        'veh_20.csv'
    ]
    vehicle_data = []
    for file in vehicle_files:
        df = pd.read_csv(file, encoding='ISO-8859-1', low_memory=False)
        df.fillna('Unknown', inplace=True)
        vehicle_data.append(df)
    vehicle_data_cleaned = pd.concat(vehicle_data, ignore_index=True)
    vehicle_data_cleaned.to_csv('cleaned_vehicle.csv', index=False)

# Define the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 10, 1),
    'retries': 1,
}

with DAG('etl_us_accidents', default_args=default_args, schedule_interval='@daily', catchup=False) as dag:

    # Define the ETL tasks
    task_clean_accidents = PythonOperator(
        task_id='clean_accidents_task',
        python_callable=load_and_clean_accident_data
    )

    task_clean_persons = PythonOperator(
        task_id='clean_persons_task',
        python_callable=load_and_clean_person_data
    )

    task_clean_vehicles = PythonOperator(
        task_id='clean_vehicles_task',
        python_callable=load_and_clean_vehicle_data
    )

    # Define task dependencies (if needed)
    task_clean_accidents >> task_clean_persons >> task_clean_vehicles


       
  
