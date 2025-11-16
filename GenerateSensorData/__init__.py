import logging
import azure.functions as func
import random
import pyodbc
import os

def generate_sensor_data():
    sensors = []
    for i in range(1, 21):
        sensors.append({
            'sensor_id': i,
            'temperature': random.randint(5, 18),
            'wind_speed': random.randint(12, 24),
            'humidity': random.randint(30, 60),
            'co2': random.randint(400, 1600)
        })
    return sensors

def insert_to_db(sensor_data):
    conn = pyodbc.connect(os.environ["DB_CONN"])
    cursor = conn.cursor()
    for sensor in sensor_data:
        cursor.execute("""
            INSERT INTO SensorData (SensorID, Temperature, WindSpeed, Humidity, CO2)
            VALUES (?, ?, ?, ?, ?)
        """, sensor['sensor_id'], sensor['temperature'], sensor['wind_speed'], sensor['humidity'], sensor['co2'])
    conn.commit()
    conn.close()

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Sensor simulation function triggered.')

    try:
        data = generate_sensor_data()
        insert_to_db(data)
        return func.HttpResponse("Data inserted successfully", status_code=200)
    except Exception as e:
        logging.error(f"Error: {e}")
        return func.HttpResponse(f"Error: {e}", status_code=500)
