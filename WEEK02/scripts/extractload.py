# scripts/extractload.py

from managerpostgres import create_tables, insert_data
from datareader import DataReader
import os

class ExtractLoadTransform:
    def __init__(self):
        self.TRAJECTORY_SCHEMA = "schemas/trajectory_schema.sql"

    def load_trajectory_data(self, database_url):
        data_reader = DataReader(file_path="/home/habte/Downloads/20181024_d1_0830_0900.csv")
        vehicle_data, trajectories_data = data_reader.get_dfs(v=1)

        
        schema_path = os.path.join(os.path.dirname(__file__), self.TRAJECTORY_SCHEMA)
        
        # Create tables
        create_tables(schema_path, database_url)

        # Insert data into PostgreSQL
        insert_data(vehicle_data, 'vehicles', database_url)
        insert_data(trajectories_data, 'trajectories', database_url)

if __name__ == "__main__":
    elt = ExtractLoadTransform()
    database_url = "postgresql://postgres:habte@localhost:5432/WEEK@2"
    elt.load_trajectory_data(database_url)
