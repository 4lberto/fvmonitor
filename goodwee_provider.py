import asyncio
import json
import threading
import time
from dataclasses import asdict

import goodwe

from db.db_prov import InverterLog


async def __get_runtime_data():
    ip_address = '192.168.1.18'
    sensors = [
        "ppv",  # PV power (W)
        "pbattery1",  # battery power (W) + = charging, - = discharging
        "battery_mode",  # 1=standby, 2=discharge, 3=charge
        "battery_soc",  # battery state of charge (%)
        "active_power",  # grid power (W): - = buy, + = sell
        "grid_in_out",  # 1=sell or export, 2=buy or import
        "house_consumption",  # own consumption (W)
        "e_day",  # today's PV energy production (kWh)
        "e_total",  # total PV energy production (kWh)
        "meter_e_total_exp",  # total sold (exported) energy (kWh)
        "meter_e_total_imp"  # total bought or imported energy (kWh)
    ]

    inverter = await goodwe.connect(ip_address)
    runtime_data = await inverter.read_runtime_data()
    return runtime_data


def get_runtime_data() -> dict:
    asyncio.set_event_loop(asyncio.SelectorEventLoop())
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(__get_runtime_data())
    return result


def get_runtime_data_as_dataclass()-> InverterLog:
    data_as_dict = get_runtime_data()
    data_as_dataclass = InverterLog(**data_as_dict)
    return data_as_dataclass



if __name__ == '__main__':
    while (True):
        result = get_runtime_data_as_dataclass()
        print(json.dumps(asdict(result), indent=4))

        time.sleep(1)
