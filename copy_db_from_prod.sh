#!/bin/zsh
scp 'pi@192.168.1.35:/home/pi/dev/fvmonitor/data/*' data/
cp data/inverter_log.db data/inverter_log.db.bak
