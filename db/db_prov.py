import sqlite3
from dataclasses import dataclass, asdict
from pathlib import Path

DATABASE_LOCATION = str(Path(__file__).resolve().parent.joinpath("data")) + "/inverter_log.db"
print("DATABASE_LOCATION: " + DATABASE_LOCATION)


@dataclass
class InverterLog:
    vpv1: float
    ipv1: float
    ppv1: float
    pv1_mode: float
    pv1_mode_label: str
    vpv2: float
    ipv2: float
    ppv2: float
    pv2_mode: float
    pv2_mode_label: str
    ppv: float
    vbattery1: float
    battery_status: float
    battery_temperature: float
    ibattery1: float
    pbattery1: float
    battery_charge_limit: float
    battery_discharge_limit: float
    battery_error: float
    battery_soc: float
    battery_soh: float
    battery_mode: float
    battery_mode_label: str
    battery_warning: float
    meter_status: float
    vgrid: float
    igrid: float
    pgrid: float
    fgrid: float
    grid_mode: float
    grid_mode_label: str
    vload: float
    iload: float
    pload: float
    fload: float
    load_mode: float
    load_mode_label: str
    work_mode: float
    work_mode_label: str
    temperature: float
    error_codes: float
    e_total: float
    h_total: float
    e_day: float
    e_load_day: float
    e_load_total: float
    total_power: float
    effective_work_mode: float
    effective_relay_control: float
    grid_in_out: float
    grid_in_out_label: str
    pback_up: float
    plant_power: float
    meter_power_factor: float
    diagnose_result: float
    diagnose_result_label: str
    house_consumption: float


def __create_table():
    conn = sqlite3.connect(DATABASE_LOCATION)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS inverter_log
                 (id integer primary key autoincrement
                 ,t TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                ,vpv1 REAL
                    ,ipv1 REAL
                    ,ppv1 REAL
                    ,pv1_mode REAL
                    ,pv1_mode_label TEXT
                    ,vpv2 REAL
                    ,ipv2 REAL
                    ,ppv2 REAL
                    ,pv2_mode REAL
                    ,pv2_mode_label TEXT
                    ,ppv REAL
                    ,vbattery1 REAL
                    ,battery_status REAL
                    ,battery_temperature REAL
                    ,ibattery1 REAL
                    ,pbattery1 REAL
                    ,battery_charge_limit REAL
                    ,battery_discharge_limit REAL
                    ,battery_error REAL
                    ,battery_soc REAL
                    ,battery_soh REAL
                    ,battery_mode REAL
                    ,battery_mode_label TEXT
                    ,battery_warning REAL
                    ,meter_status REAL
                    ,vgrid REAL
                    ,igrid REAL
                    ,pgrid REAL
                    ,fgrid REAL
                    ,grid_mode REAL
                    ,grid_mode_label TEXT
                    ,vload REAL
                    ,iload REAL
                    ,pload REAL
                    ,fload REAL
                    ,load_mode REAL
                    ,load_mode_label TEXT
                    ,work_mode REAL
                    ,work_mode_label TEXT
                    ,temperature REAL
                    ,error_codes REAL
                    ,e_total REAL
                    ,h_total REAL
                    ,e_day REAL
                    ,e_load_day REAL
                    ,e_load_total REAL
                    ,total_power REAL
                    ,effective_work_mode REAL
                    ,effective_relay_control REAL
                    ,grid_in_out REAL
                    ,grid_in_out_label TEXT
                    ,pback_up REAL
                    ,plant_power REAL
                    ,meter_power_factor REAL
                    ,diagnose_result REAL
                    ,diagnose_result_label TEXT
                    ,house_consumption REAL
                  )''')
    conn.commit()
    conn.close()
    print("Database table inverter_log created")


def insert_inverter_log(inverter_log: InverterLog):
    conn = sqlite3.connect(DATABASE_LOCATION)
    c = conn.cursor()
    c.execute("""INSERT INTO inverter_log (
    vpv1,
ipv1,
ppv1,
pv1_mode,
pv1_mode_label,
vpv2,
ipv2,
ppv2,
pv2_mode,
pv2_mode_label,
ppv,
vbattery1,
battery_status,
battery_temperature,
ibattery1,
pbattery1,
battery_charge_limit,
battery_discharge_limit,
battery_error,
battery_soc,
battery_soh,
battery_mode,
battery_mode_label,
battery_warning,
meter_status,
vgrid,
igrid,
pgrid,
fgrid,
grid_mode,
grid_mode_label,
vload,
iload,
pload,
fload,
load_mode,
load_mode_label,
work_mode,
work_mode_label,
temperature,
error_codes,
e_total,
h_total,
e_day,
e_load_day,
e_load_total,
total_power,
effective_work_mode,
effective_relay_control,
grid_in_out,
grid_in_out_label,
pback_up,
plant_power,
meter_power_factor,
diagnose_result,
diagnose_result_label,
house_consumption

    ) VALUES (
:vpv1,
:ipv1,
:ppv1,
:pv1_mode,
:pv1_mode_label,
:vpv2,
:ipv2,
:ppv2,
:pv2_mode,
:pv2_mode_label,
:ppv,
:vbattery1,
:battery_status,
:battery_temperature,
:ibattery1,
:pbattery1,
:battery_charge_limit,
:battery_discharge_limit,
:battery_error,
:battery_soc,
:battery_soh,
:battery_mode,
:battery_mode_label,
:battery_warning,
:meter_status,
:vgrid,
:igrid,
:pgrid,
:fgrid,
:grid_mode,
:grid_mode_label,
:vload,
:iload,
:pload,
:fload,
:load_mode,
:load_mode_label,
:work_mode,
:work_mode_label,
:temperature,
:error_codes,
:e_total,
:h_total,
:e_day,
:e_load_day,
:e_load_total,
:total_power,
:effective_work_mode,
:effective_relay_control,
:grid_in_out,
:grid_in_out_label,
:pback_up,
:plant_power,
:meter_power_factor,
:diagnose_result,
:diagnose_result_label,
:house_consumption
    
    
    )""",
              asdict(inverter_log))
    conn.commit()
    conn.close()


def get_inverter_log():
    conn = sqlite3.connect(DATABASE_LOCATION)
    c = conn.cursor()
    c.execute("SELECT * FROM inverter_log")
    rows = c.fetchall()
    conn.close()
    return rows


if __name__ == '__main__':
    __create_table()
    result = get_inverter_log()
    print(result)
