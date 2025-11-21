import datetime
import logging
import os
import requests
import azure.functions as func

def main(mytimer: func.TimerRequest) -> None:
    start_time = datetime.datetime.now(datetime.timezone.utc)
    logging.info(f"[T1] Task 3a Timer trigger started at {start_time.isoformat()}")

    # Make internal call to Task 1's HTTP function
    try:
        function_url = os.environ.get("FUNC_URL_GENERATE_SENSOR_DATA")
        if not function_url:
            raise ValueError("FUNC_URL_GENERATE_SENSOR_DATA not set in environment.")

        response = requests.get(function_url)
        
        end_time = datetime.datetime.now(datetime.timezone.utc)
        delta = (end_time - start_time).total_seconds()
        
        logging.info(f"Task 1 HTTP function response: {response.status_code} - {response.text}")
        logging.info(f"[T2] Task 1 HTTP function responded at {end_time.isoformat()} (Delta: {delta:.3f} seconds)") # Log time taken for graph plotting

    except Exception as e:
        logging.error(f"Failed to trigger GenerateSensorData HTTP function: {e}")
