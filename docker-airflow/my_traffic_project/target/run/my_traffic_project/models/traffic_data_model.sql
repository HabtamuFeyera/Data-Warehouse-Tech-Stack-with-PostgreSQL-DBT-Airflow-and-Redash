
  create view "city_traffic_db"."public"."traffic_data_model__dbt_tmp"
    
    
  as (
    -- models/traffic_data_model.sql

-- Example: Replace this with your actual SQL to define the traffic_data_model.
WITH traffic_data_model AS (
  SELECT
    *
  FROM
    my_traffic.raw_traffic_data
)
SELECT
  *
FROM
  traffic_data_model
  );