import logging
import azure.functions as func
import pyodbc
import os
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('GetSensorStats function triggered.')

    try:
        conn = pyodbc.connect(os.environ["DB_CONN"])
        cursor = conn.cursor()

        cursor.execute("""
            SELECT SensorID,
                MIN(Temperature) AS MinTemp,
                MAX(Temperature) AS MaxTemp,
                ROUND(AVG(CAST(Temperature AS FLOAT)), 2) AS AvgTemp,
                MIN(WindSpeed) AS MinWind,
                MAX(WindSpeed) AS MaxWind,
                ROUND(AVG(CAST(WindSpeed AS FLOAT)), 2) AS AvgWind,
                MIN(Humidity) AS MinHumidity,
                MAX(Humidity) AS MaxHumidity,
                ROUND(AVG(CAST(Humidity AS FLOAT)), 2) AS AvgHumidity,
                MIN(CO2) AS MinCO2,
                MAX(CO2) AS MaxCO2,
                ROUND(AVG(CAST(CO2 AS FLOAT)), 2) AS AvgCO2
            FROM SensorData
            GROUP BY SensorID
            ORDER BY SensorID
        """)

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        conn.close()

        return func.HttpResponse(json.dumps(results, indent=2), mimetype="application/json", status_code=200)

    except Exception as e:
        logging.error(f"Error: {e}")
        return func.HttpResponse(f"Error: {e}", status_code=500)
