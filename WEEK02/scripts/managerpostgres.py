from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
import pandas as pd

def create_tables(schema_file, database_url):
    with open(schema_file, 'r') as file:
        schema = file.read()

    engine = create_engine(database_url)

    try:
        with engine.connect() as connection:
            connection.execute(schema)
    except ProgrammingError as e:
        print(f"Error creating tables: {e}")

def insert_data(df, table_name, database_url):
    engine = create_engine(database_url)
    try:
        df.to_sql(table_name, engine, if_exists='replace', index=False)
    except ProgrammingError as e:
        print(f"Error inserting data into {table_name} table: {e}")
