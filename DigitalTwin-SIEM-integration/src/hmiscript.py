"""
FP hmi.py
"""

from minicps.devices import HMI
from utils import STATE, PLC1_ADDR
from utils import HMI_PROTOCOL, HMI_DATA, HMI_ADDR, HMI_PERIOD_SEC

import time
import logging

ACTUATOR1 = ('ACTUATOR1-MV', 1) # to be received from PLC1 
ACTUATOR1_HMI = ('ACTUATOR1-HMI', 1) # to be sent to PLC1

class FPHMI(HMI):

    def main_loop(self, sleep=0.0):
        """hmi main loop.
                    - monitor PLC1 tag (actuator1)
                """

        print('DEBUG: FP HMI enters main_loop.')
        print

        logging.basicConfig(filename='logs/hmi.log',
                            format='%(levelname)s %(asctime)s ' + HMI_ADDR + ' %(funcName)s %(message)s',
                            datefmt='%m/%d/%Y %H:%M:%S', level=logging.DEBUG)
        while(True):
            self.set(ACTUATOR1, 0)
            self.send(ACTUATOR1, 0, PLC1_ADDR)
        
            time.sleep(180)

if __name__ == "__main__":

    hmi = FPHMI(
        name='hmi',
        state=STATE,
        protocol=HMI_PROTOCOL,
        memory=HMI_DATA,
        disk=HMI_DATA)
                                                                                                                        

                                                                                                                                                                                                  

