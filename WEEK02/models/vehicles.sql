-- models/vehicles.sql

SELECT
  id,
  unique_id,
  track_id,
  veh_type,
  traveled_distance,
  avg_speed
FROM raw_data.vehicles
-- Assuming 'raw_data' is your source name
