-- models/trajectories.sql

SELECT
  id,
  unique_id,
  lat,
  lon,
  speed,
  lon_acc,
  lat_acc,
  time
FROM raw_data.trajectories
-- Assuming 'raw_data' is your source name
