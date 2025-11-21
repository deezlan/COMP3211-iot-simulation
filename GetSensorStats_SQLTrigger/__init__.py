import json
import logging

def main(changes):
    logging.info("SQL Changes: %s", json.loads(changes))
