import pandas as pd
from sqlalchemy import create_engine
import logging

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

try:
    # Read data from CSV into a Pandas DataFrame
    city_traffic_data = pd.read_csv(data_file_path)

    # Connect to PostgreSQL
    engine = create_engine(
        f"postgresql://{db_credentials['user']}:{db_credentials['password']}@{db_credentials['host']}:{db_credentials['port']}/{db_credentials['database']}"
    )

    # Write data to PostgreSQL table
    table_name = "raw_traffic_data"
    city_traffic_data.to_sql(name=table_name, con=engine, if_exists="replace", index=False)

    logging.info(f"Data loaded into '{table_name}' table successfully!")

except Exception as e:
    logging.error(f"An error occurred: {str(e)}")

finally:
    # Close the database connection
    if 'engine' in locals():
        engine.dispose()
