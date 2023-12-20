# We'll start by importing the DAG object
import sys
import pendulum
sys.path.append('/home/habte/WEEK02/airflow-environment')
from scripts.extractload import ELT

# Rest of your script...
from datetime import timedelta, datetime
from pathlib import Path

from airflow import DAG
# We need to import the operators used in our tasks
from airflow.operators.python import PythonOperator

import pandas as pd
import sqlite3
import os,sys

# get dag directory path
dag_path = os.getcwd()
sys.path.append('./scripts')

from scripts.extractload import ELT

elt = ELT(read_dag_path="/home/habte/Downloads/20181024_d1_0830_0900.csv",
         save_dag_path=f"{dag_path}/processed_data/")

# initializing the default arguments that we'll pass to our DAG
default_args = {
    'owner': 'airflow',
    'start_date': pendulum.today('UTC'),  # Start running today
}

ingestion_dag = DAG(
    'traffic_data_ingestion',
    default_args=default_args,
    description='Aggregates booking records for data analysis',
    schedule=timedelta(hours=6),  # Repeat every 6 hours
    catchup=False,
    user_defined_macros={'date_to_millis': elt.execution_date_to_millis}
)

task_1 = PythonOperator(
    task_id='extract_data',
    python_callable=elt.extract_data,
    dag=ingestion_dag,
)

task_2 = PythonOperator(
    task_id='load_vehicle_data',
    python_callable=elt.load_vehicle_data,
    dag=ingestion_dag,
)

task_3 = PythonOperator(
    task_id='load_trajectory_data',
    python_callable=elt.load_trajectory_data,
    dag=ingestion_dag,
)

task_1 >> [task_2, task_3]  # Changed to a list for multiple downstream tasks