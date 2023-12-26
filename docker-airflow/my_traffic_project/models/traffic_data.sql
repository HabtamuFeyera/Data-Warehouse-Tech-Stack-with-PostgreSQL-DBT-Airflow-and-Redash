
WITH cleaned_trajectories AS (
  SELECT
    id,
    unique_id,
    lat,
    lon,
    speed,
    lon_acc,
    lat_acc,
    time
  FROM {{ ref('raw-traffic_data') }}
)

SELECT
  t.id,
  t.unique_id,
  t.lat,
  t.lon,
  t.speed,
  t.lon_acc,
  t.lat_acc,
  t.time,
  v.track_id,
  v.veh_type,
  v.traveled_distance,
  v.avg_speed
FROM cleaned_trajectories t
JOIN {{ ref('raw_traffic_data') }} v
ON t.unique_id = v.unique_id;
