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
LIQUID_LEVEL_TANK = ('SENSOR1-LL-tank', 1) # to be received from PLC1

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
            # network capabilities
            motor_status = int(self.receive(ACTUATOR1, PLC1_ADDR))
            #liquid_level = float(self.get(LIQUID_LEVEL_TANK))
            print(motor_status)
            #print(liquid_level)
            try:
                user_input = int(raw_input(
                    "\n Please choose from the following options: \n Read motor status: Press 1 \n Change motor status: Press 2\n Shutdown HMI program: Press 99 \n"))
                print('DEBUG: input = ', user_input)

                if user_input == 1:  # read motor status 
                    print("DEBUG pressed 2 (read motor status) \n Motor status: ", motor_status)

                elif user_input == 2:
                    print("DEBUG pressed 2 \n Motor status: ", motor_status)
                    change = raw_input("Do you wish to change the motor status? Y/N \n")
                    print("DEBUG typed ", change)
                    if change == "Y" or change == "y":
                        new_status = int(raw_input("Enter 1 to turn on and 0 to turn off the motor:"))
                        print("DEBUG typed ", new_status)
                    try:
                        logging.info('Sent status to PLC (%s): %d' % (PLC1_ADDR, new_status))
                        self.set(ACTUATOR1, new_status)
                        self.send(ACTUATOR1, new_status, PLC1_ADDR)
                        print('Changed motor status from %d to %d' % (motor_status, new_status))
                    except (RuntimeError, TypeError, NameError):
                        logging.warning('New status (%d) could not be sent to PLC (%s).' % (new_status, PLC1_ADDR))

                elif change == "N" or change == "n":
                    print("Current motor status  remains: ", motor_status)
                    continue

                elif user_input == 99:
                    logging.info('Shutdown HMI program.')
                    print("DEBUG pressed 3 (shutdown HMI program)")
                    print('DEBUG: HMI Shutdown')
                    break
            except ValueError:
                print("Oops! That was no valid number. Please try again...")

        time.sleep(HMI_PERIOD_SEC)

if __name__ == "__main__":

    hmi = FPHMI(
        name='hmi',
        state=STATE,
        protocol=HMI_PROTOCOL,
        memory=HMI_DATA,
        disk=HMI_DATA)
                                                                                                                        

                                                                                                                                                                                                  

