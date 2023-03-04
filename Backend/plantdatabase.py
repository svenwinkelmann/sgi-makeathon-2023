# file to create a database via python script
import sqlite3


class PlantDataBase:
    """
    Class to create Makeathon database
    """
    def __init__(self):
        self.db_file = 'backend_database.db'
        self.conn = None
        try:
            self.conn = sqlite3.connect(self.db_file, check_same_thread=False)
            print(sqlite3.version)
        except sqlite3.Error as e:
            print(e)
        #        finally:
        #           if self.conn:
        #              self.conn.close()
        self.cur = self.conn.cursor()

    def create_table(self):
        table_config = "CREATE TABLE IF NOT EXISTS plants " \
                       "(plant_ID INTEGER PRIMARY KEY AUTOINCREMENT," \
                       " gps TEXT," \
                       " plant_type TEXT)"
        self.cur.execute(table_config)

        table_config = "CREATE TABLE IF NOT EXISTS measurement_values " \
                       "(measurement_id INTEGER PRIMARY KEY AUTOINCREMENT," \
                       "Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP," \
                       "plant_ID INTEGER, " \
                       "sensordata_temp REAL," \
                       "sensordata_humidity REAL," \
                       "sensordata_ground_humidity REAL," \
                       "pest_infestation INTEGER," \
                       "light_intensity REAL," \
                       "FOREIGN KEY (plant_ID)" \
                       "    REFERENCES plants (plant_ID) )"
        self.cur.execute(table_config)

    def insert_plant(self, gps: str, plant_type: str):
        self.cur.execute(f"INSERT INTO plants (gps, plant_type) VALUES ({gps}, {plant_type})")
        self.conn.commit()

    def insert_measurement_data(self, plant_id,
                                sensordata_temp,
                                sensordata_humidity,
                                sensordata_ground_humidity,
                                pest_infestation,
                                light_intensity):
        self.cur.execute(f"INSERT INTO measurement_values (plant_ID, sensordata_temp, sensordata_humidity, sensordata_ground_humidity, "
                         f"pest_infestation, light_intensity) VALUES "
                         f"({plant_id}, {sensordata_temp}, {sensordata_humidity}, {sensordata_ground_humidity}, {pest_infestation}"
                         f", {light_intensity})")
        self.conn.commit()

    def get_latest_data(self, plant_id) -> dict:
        """
        Gets the newest parameter of specific plant and returns all parameters in json format
        :param plant_id:
        :return:
        """
        self.cur.execute(f"SELECT * FROM measurement_values where plant_ID = {plant_id} ORDER BY Timestamp DESC LIMIT 1")
        data = self.cur.fetchone()
        json_file = {
            "measurement_id": data[0],
            "plant_id": data[2],
            "timestamp": data[1],
            "sensordata_temp": data[3],
            "sensordata_humidity": data[4],
            "sensordata_ground_humidity": data[5],
            "pest_infestation": data[6],
            "light_intensity": data[7]
        }
        return json_file

    def delete_data(self, table_name):
        self.cur.execute(f"DELETE FROM {table_name}")
        self.conn.commit()
