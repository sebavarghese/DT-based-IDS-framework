"""
FP physical process

LiquidTank has an outflow pipe
- mere physical process (only get and set methods)
"""

from minicps.devices import Tank

from utils import STATE
from utils import PUMP_FLOWRATE_OUT
from utils import TANK_M, TANK_SECTION, TANK_INIT_LEVEL
from utils import PP_PERIOD_SEC, PP_PERIOD_HOURS  # PP_SAMPLES

import time

SENSOR1 = ('SENSOR1-LL-tank', 1)
ACTUATOR1 = ('ACTUATOR1-MV', 1)
SENSOR2 = ('SENSOR2-FL', 2)


class LiquidTank(Tank):

    # boot process
    def pre_loop(self):
        # simulates closed valve
        self.set(ACTUATOR1, 0)
        # simulates init level of liquid tank
        self.level = self.set(SENSOR1, TANK_INIT_LEVEL)

    def main_loop(self):
        # count = 0
        # while(count <= PP_SAMPLES):
        while True:
            new_level = self.level

            # compute water volume
            water_volume = self.section * new_level

            # outflow volumes
            actuator = self.get(ACTUATOR1)
            if int(actuator) == 1:
                self.set(SENSOR2, PUMP_FLOWRATE_OUT)             
                outflow = PUMP_FLOWRATE_OUT * PP_PERIOD_HOURS
                # print "DEBUG phys-proc: Tank outflow  ", outflow
                water_volume -= outflow
            elif int(actuator) == 0:
                self.set(SENSOR2, 0.00)  # no outflow

            # compute new water_level
            new_level = water_volume / self.section

            # update internal and state water level
            print "DEBUG phys-proc: new_level  %.5f m \t delta (volume): %.5f m3" % (
                new_level, (new_level - self.level) * self.section)
            self.level = self.set(SENSOR1, new_level)

            if new_level <= TANK_M['LowerBound']:
                print 'DEBUG phys-proc: Tank below lowerbound threshold ', TANK_M['LowerBound']
                # break
                # simulates refill of tank
                time.sleep(PP_PERIOD_SEC*10)    # simulate time to refill the tank
                self.level = self.set(SENSOR1, TANK_INIT_LEVEL)
                print 'DEBUG phys-proc: Tank has been refilled'

            # count += 1
            time.sleep(PP_PERIOD_SEC)

    def _stop(self):

        print "physical process stopped (TANK)"


if __name__ == '__main__':

    rwt = LiquidTank(
        name='tank',
        state=STATE,
        protocol=None,
        section=TANK_SECTION,
        level=TANK_INIT_LEVEL
    )