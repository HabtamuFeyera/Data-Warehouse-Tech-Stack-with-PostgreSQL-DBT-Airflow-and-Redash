import os
import sys
sys.path.append('/home/habte/WEEK02/airflow/dags/')
from datetime import datetime
import pandas as pd
from scripts.datareader import DataReader
from scripts.managerpostgres import create_tables, insert_data

class ELT:
    TRAJECTORY_SCHEMA = "dags/scripts/trajectory_info_schema.sql"
    VEHICLE_SCHEMA = "dags/scripts/vehicle_info_schema.sql"

    def __init__(self, read_dag_path, save_dag_path):
        self.read_dag_path = read_dag_path
        self.save_dag_path = save_dag_path

    def extract_data(self, file_path=None) -> None:
        if file_path is not None:
            self.read_dag_path = file_path

        reader = DataReader()
        vehicle_df, trajectories_df = reader.get_dfs(file_path=self.read_dag_path, v=0)
        
        vehicle_df.to_csv(os.path.join(self.save_dag_path, 'vehicle_info.csv'), index=False)
        trajectories_df.to_csv(os.path.join(self.save_dag_path, 'trajectories_info.csv'), index=False)

    def load_trajectory_data(self):
        trajectories_df = pd.read_csv(os.path.join(self.save_dag_path, 'trajectories_info.csv'))
        create_tables(self.TRAJECTORY_SCHEMA)
        print('Created trajectory table')
        insert_data(trajectories_df[:10000], "trajectories")
    
    def load_vehicle_data(self):
        vehicle_df = pd.read_csv(os.path.join(self.save_dag_path, 'vehicle_info.csv'))
        create_tables(self.VEHICLE_SCHEMA)
        print('Created vehicle table')
        insert_data(vehicle_df, "vehicles")
        
    def execution_date_to_millis(self, execution_date):
        date = datetime.strptime(execution_date, "%Y-%m-%d")
        epoch = datetime.utcfromtimestamp(0)
        return int((date - epoch).total_seconds() * 1000.0)

if __name__ == "__main__":
    # Example usage
    csv_file_path = "/home/habte/Downloads/20181024_d1_0830_0900.csv"
    save_dag_path = "/path/to/your/output/directory"  # Replace with the actual output directory

    elt = ELT(read_dag_path=csv_file_path, save_dag_path=save_dag_path)
    elt.extract_data()
    elt.load_trajectory_data()
    elt.load_vehicle_data()
