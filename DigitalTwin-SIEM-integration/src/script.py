"""
FP plc1.py
"""

from minicps.devices import HMI
from utils import HMI_PROTOCOL, HMI_DATA, HMI_ADDR, HMI_PERIOD_SEC
from utils import PLC1_DATA, PLC1_PROTOCOL, PLC1_ADDR, STATE
from utils import PLC2_ADDR, PLC3_ADDR
from utils import PLC_PERIOD_SEC   # PLC_SAMPLES
from utils import TANK_M, BOTTLE_M, SENSOR2_THRESH
import time
import logging
import csv
import datetime
import sys

# tag addresses
SENSOR1 = ('SENSOR1-LL-tank', 1)
ACTUATOR1 = ('ACTUATOR1-MV', 1)
SENSOR2 = ('SENSOR2-FL', 2)
SENSOR3 = ('SENSOR3-LL-bottle', 3)

class FPHMI(HMI):

    def main_loop(self):
        """plc1 main loop.
                    - reads values from sensors
                    - drives actuator according to the control strategy
                    - updates its enip server
                    - logs the control strategy events (info, exceptions)
                """
        delay=60*3 
        close_time=time.time()+delay        
        count=0
        while close_time > time.time():
            with open('logs/data.csv', 'a+') as writeobj:
                fieldnames={'timestamp','ll_tank', 'ub_tank','lb_tank', 'flowlevel', 'sensor2_thresh','ll_bottle','ub_bottle','lb_bottle','motor_status'}
        	csv_writer = csv.DictWriter(writeobj, fieldnames=fieldnames)
                if count == 0:
                    csv_writer.writeheader()
                count = 1

                csv_writer.writerow({ 'timestamp': str(datetime.datetime.now()),'ll_tank': float(self.receive(SENSOR1, PLC1_ADDR)), 'ub_tank': TANK_M['UpperBound'], 'lb_tank': TANK_M['LowerBound'], 'flowlevel': float(self.receive(SENSOR2, PLC2_ADDR)), 'sensor2_thresh': SENSOR2_THRESH,'ll_bottle': float(self.receive(SENSOR3, PLC3_ADDR)),'ub_bottle': BOTTLE_M['UpperBound'],'lb_bottle': BOTTLE_M['LowerBound'],'motor_status': int(self.receive(ACTUATOR1, PLC1_ADDR))})

            time.sleep(0.25)

if __name__ == "__main__":
    hmi = FPHMI(
        name='hmi',
        state=STATE,
        protocol=HMI_PROTOCOL,
        memory=HMI_DATA,
        disk=HMI_DATA)
