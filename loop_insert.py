import json
import logging
import time
from dataclasses import asdict

from db.db_prov import insert_inverter_log
from goodwee_provider import get_runtime_data_as_dataclass

SLEEP_TIME = 8
SLEEP_TIME_ON_FAIL = 1

if __name__ == '__main__':
    print("Starting loop")
    print("Call to start_loop_in_background to let it working in the environmment")
    while (True):

        # print(json.dumps(asdict(result), indent=4))
        try:
            result = get_runtime_data_as_dataclass()
            insert_inverter_log(result)
            print(f"Inserted: {result}")

            time.sleep(SLEEP_TIME)
        except Exception as e:

            logging.error("Error while reading / inserting data. Retrying in 1 second", exc_info=True)
            time.sleep(SLEEP_TIME_ON_FAIL)
