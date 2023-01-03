import asyncio
import json
import threading
import time

import goodwe


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


def get_runtime_data():
    asyncio.set_event_loop(asyncio.SelectorEventLoop())
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(__get_runtime_data())
    return result


if __name__ == '__main__':
    while (True):
        result = get_runtime_data()
        print(json.dumps(result, indent=4))

        time.sleep(1)
