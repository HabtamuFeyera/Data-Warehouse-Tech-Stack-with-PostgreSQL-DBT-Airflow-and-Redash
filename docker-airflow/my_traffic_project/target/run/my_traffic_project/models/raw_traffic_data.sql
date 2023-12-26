
  create view "city_traffic_db"."public"."raw_traffic_data__dbt_tmp"
    
    
  as (
    -- models/raw_traffic_data.sql

-- Example: Replace this with your actual SQL to define the raw_traffic_data model.
WITH raw_traffic_data AS (
  SELECT
    *
  FROM
    your_source_table
)
SELECT
  *
FROM
  raw_traffic_data
  );