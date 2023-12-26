CREATE TABLE IF NOT EXISTS traject
(
    "id" SERIAL NOT NULL,
    "unique_id" TEXT NOT NULL,
    "lat" FLOAT NOT NULL,
    "lon" FLOAT DEFAULT NULL,
    "speed" FLOAT DEFAULT NULL,
    "lon_acc" FLOAT DEFAULT NULL,
    "lat_acc" FLOAT DEFAULT NULL,
    "time" FLOAT DEFAULT NULL,
    PRIMARY KEY ("id"),
    CONSTRAINT fk_traffic_data
        FOREIGN KEY("unique_id") 
            REFERENCES traffic_data(unique_id)
            ON DELETE CASCADE
    