-- trajectory_schema.sql

-- Create the vehicles table
CREATE TABLE IF NOT EXISTS vehicles (
    id SERIAL PRIMARY KEY,
    unique_id TEXT NOT NULL,
    track_id INTEGER NOT NULL,
    veh_type VARCHAR(255) NOT NULL,
    traveled_distance FLOAT NOT NULL,
    avg_speed FLOAT NOT NULL
);

-- Create the trajectories table
CREATE TABLE IF NOT EXISTS trajectories (
    id SERIAL PRIMARY KEY,
    unique_id TEXT NOT NULL,
    lat FLOAT NOT NULL,
    lon FLOAT NOT NULL,
    speed FLOAT,
    lon_acc FLOAT,
    lat_acc FLOAT,
    time FLOAT,
    FOREIGN KEY (unique_id) REFERENCES vehicles(unique_id) ON DELETE CASCADE
);
