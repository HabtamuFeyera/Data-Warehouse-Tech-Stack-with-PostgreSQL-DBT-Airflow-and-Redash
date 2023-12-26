-- Create the  table
CREATE TABLE IF NOT EXISTS raw_traffic_data(
    id SERIAL PRIMARY KEY,
    unique_id TEXT NOT NULL,
    track_id INTEGER NOT NULL,
    veh_type VARCHAR(255) NOT NULL,
    traveled_distance FLOAT NOT NULL,
    avg_speed FLOAT NOT NULL
);

-- Create the table
CREATE TABLE IF NOT EXISTS traffic_data (
    id SERIAL PRIMARY KEY,
    unique_id TEXT NOT NULL,
    lat FLOAT NOT NULL,
    lon FLOAT NOT NULL,
    speed FLOAT,
    lon_acc FLOAT,
    lat_acc FLOAT,
    time FLOAT,
    FOREIGN KEY (unique_id) REFERENCES raw_traffic_data(unique_id) ON DELETE CASCADE
);


