import pandas as pd
import os
from sqlalchemy import create_engine

class DataReader:
    def __init__(self, file_path=None):
        self.filepath = file_path

    @staticmethod
    def get_uid(filename, row_num):
        return f"{filename}_{row_num}"

    @staticmethod
    def read_file(path):
        with open(path, 'r') as f:
            return [line.strip('\n') for line in f.readlines()[1:]]

    @staticmethod
    def parse(lines, filename):
        veh_info, trajectories = [], []

        for row_num, line in enumerate(lines):
            uid = DataReader.get_uid(filename, row_num)
            line = line.split("; ")[:-1]
            assert len(line[4:]) % 6 == 0, f"Error in row number {row_num}: {line}"

            veh_info.append([uid, int(line[0]), line[1], float(line[2]), float(line[3])])

            for i in range(0, len(line[4:]), 6):
                trajectories.append([uid, float(line[4+i]), float(line[4+i+1]),
                                     float(line[4+i+2]), float(line[4+i+3]), float(line[4+i+4]), float(line[4+i+5])])

        vehicle_df = pd.DataFrame(veh_info, columns=["unique_id", "track_id", "veh_type", "traveled_distance", "avg_speed"])
        trajectories_df = pd.DataFrame(trajectories, columns=["unique_id", "lat", "lon", "speed", "lon_acc", "lat_acc", "time"])
        return vehicle_df, trajectories_df

    def get_dfs(self, file_path=None, v=0):
        if not file_path and self.filepath:
            file_path = self.filepath

        lines = DataReader.read_file(file_path)
        filename = os.path.splitext(os.path.basename(file_path))[0]
        vehicle_df, trajectories_df = self.parse(lines, filename)

        if v > 0:
            print("Vehicle DataFrame:")
            print(vehicle_df.head())
            print(vehicle_df.info())
            print("\nTrajectories DataFrame:")
            print(trajectories_df.head())
            print(trajectories_df.info())

        return vehicle_df, trajectories_df

    def load_data_to_postgresql(self, vehicle_df, trajectories_df, database_url):
        engine = create_engine(database_url)
        
        # Load the DataFrames into PostgreSQL
        vehicle_df.to_sql('vehicles', engine, if_exists='replace', index=False)
        trajectories_df.to_sql('trajectories', engine, if_exists='replace', index=False)

if __name__ == "__main__":
    data_reader = DataReader(file_path="/home/habte/Downloads/20181024_d1_0830_0900.csv")
    vehicle_data, trajectories_data = data_reader.get_dfs(v=1)

    # Specify your corrected PostgreSQL database connection URL
    database_url = "postgresql://postgres:habte@localhost:5432/WEEK@2"

    # Load data into PostgreSQL
    data_reader.load_data_to_postgresql(vehicle_data, trajectories_data, database_url)
