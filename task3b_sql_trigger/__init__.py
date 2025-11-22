import datetime
import logging
import os
import requests

def main(sensorChanges: str):
    start_time = datetime.datetime.now(datetime.timezone.utc)
    logging.info(f"[T3] SQL Trigger fired at {start_time.isoformat()}")

    # Make internal call to Task 2's HTTP function
    try:
        function_url = os.environ.get("FUNC_URL_GET_SENSOR_STATS")
        if not function_url:
            raise ValueError("FUNC_URL_GET_SENSOR_STATS not set in environment.")

        response = requests.get(function_url)
        
        end_time = datetime.datetime.now(datetime.timezone.utc)
        delta = (end_time - start_time).total_seconds()
        logging.info(f"Task 2 HTTP function response: {response.status_code} - {response.text}")
        logging.info(f"[T4] Task 2 HTTP responded at {end_time.isoformat()} (Delta: {delta:.3f} seconds)") # Log time taken for graph plotting

    except Exception as e:
        logging.error(f"Failed to trigger GetSensorData HTTP function: {e}")
