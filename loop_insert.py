import json
import time
from dataclasses import asdict

from db.db_prov import insert_inverter_log
from goodwee_provider import get_runtime_data_as_dataclass

SLEEP_TIME = 8
SLEEP_TIME_ON_FAIL = 1

if __name__ == '__main__':
    print("crontab -e and then:")
    print("*/8 * * * * /home/pi/venv/bin/python /home/pi/Goodwee/loop_insert.py")
    print ("Starting loop")
    while (True):

        # print(json.dumps(asdict(result), indent=4))
        try:
            result = get_runtime_data_as_dataclass()
            insert_inverter_log(result)
            print(f"Inserted: {result}")

            time.sleep(SLEEP_TIME)
        except:
            print("Error while reading / inserting data. Retrying in 1 second")
            time.sleep(SLEEP_TIME_ON_FAIL)
