from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator

from datetime import datetime
from random import randint
# Define the data loading function
def load_data_function():
    import subprocess

    # Path to your load_data.py script
    load_data_script = "/home/habte/WEEK02/my_traffic_project/load_data.py"

    # Execute the script
    subprocess.run(["python", load_data_script])

# Default arguments for the DAG
default_args = {
    'owner': 'habtef',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Instantiate a DAG
dag = DAG(
    'city_traffic_dag',
    default_args=default_args,
    description='ELT Process for City Traffic Data',
    schedule_interval=timedelta(days=1),
)

# Define Python and Bash operators for data loading and dbt run
load_data_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data_function,
    dag=dag,
)

run_dbt_task = BashOperator(
    task_id='run_dbt',
    bash_command='docker-compose run dbt run --profiles-dir /root/.dbt',
    dag=dag,
)

# Set up task dependencies
load_data_task >> run_dbt_task
