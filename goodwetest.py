import asyncio
import goodwe


async def get_runtime_data():
    ip_address = '192.168.1.18'

    inverter = await goodwe.connect(ip_address)
    runtime_data = await inverter.read_runtime_data()

    for sensor in inverter.sensors():
        if sensor.id_ in runtime_data:
            print(f"{sensor.id_}: \t\t {sensor.name} = {runtime_data[sensor.id_]} {sensor.unit}")


asyncio.run(get_runtime_data())

if __name__ == '__main__':
    asyncio.run(get_runtime_data())

