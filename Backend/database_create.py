import sqlite3

db_file = 'backend_database.db'
conn = None
try:
    conn = sqlite3.connect(db_file)
    print(sqlite3.version)
except sqlite3.Error as e:
    print(e)


cur = conn.cursor()

cur.execute("INSERT INTO plants(plant_ID, gps, plant_type) VALUES (1, '40°N,35°O', 'plant')")
conn.commit()
cur.execute("INSERT INTO measurement_values(plant_ID, sensordata_temp, sensordata_humidity, sensordata_ground_humidity,"
            "pest_infestation, light_intensity) VALUES (1, 22.2, 59.3, 83.2, 1, 60)")
conn.commit()
