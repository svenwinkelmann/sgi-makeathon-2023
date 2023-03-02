import sqlite3

db_file = 'backend_database.db'
conn = None
try:
    conn = sqlite3.connect(db_file)
    print(sqlite3.version)
except sqlite3.Error as e:
    print(e)


cur = conn.cursor()

table_config = "CREATE TABLE IF NOT EXISTS plants (plant_ID INTEGER PRIMARY KEY AUTOINCREMENT, gps, plant_type)"
cur.execute(table_config)

table_config = "CREATE TABLE IF NOT EXISTS measurement_values " \
               "(measurement_id INTEGER PRIMARY KEY AUTOINCREMENT," \
               "Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP," \
               "plant_ID INTEGER, " \
               "sensordata_temp INTEGER," \
               "sensordata_humidity INTEGER," \
               "FOREIGN KEY (plant_ID)" \
               "REFERENCES plants (plant_ID) )"
cur.execute(table_config)

cur.execute("INSERT INTO measurement_values(plant_ID, sensordata_temp, sensordata_humidity) VALUES (1, 20, 30)")
conn.commit()
cur.execute("SELECT * FROM measurement_values where plant_ID = 1 ORDER BY timestamp DESC LIMIT 1")
print(type(cur.fetchone()[1]))
