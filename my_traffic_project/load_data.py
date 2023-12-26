import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL credentials
db_credentials = {
    "user": "postgres",
    "password": "habte",
    "host": "localhost",
    "port": "5432",
    "database": "city_traffic_db",
}

# File path to your city traffic data CSV file
data_file_path = "/home/habte/Downloads/20181024_d1_0830_0900.csv"

# Read data from CSV into a Pandas DataFrame
city_traffic_data = pd.read_csv(data_file_path)

# Connect to PostgreSQL
engine = create_engine(
    f"postgresql://{db_credentials['user']}:{db_credentials['password']}@{db_credentials['host']}:{db_credentials['port']}/{db_credentials['database']}"
)

# Write data to PostgreSQL table
table_name = "raw_traffic_data"
city_traffic_data.to_sql(name=table_name, con=engine, if_exists="replace", index=False)

# Close the database connection
engine.dispose()

print(f"Data loaded into '{table_name}' table successfully!")
