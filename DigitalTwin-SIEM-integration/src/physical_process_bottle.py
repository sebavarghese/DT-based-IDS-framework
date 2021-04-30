"""
FP physical process

Bottle is filled by the LiquidTank, whenever the
actuator1 is open and filled by the liquid running by sensor2 (flow level).

- mere physical process (only get and set methods)
"""

from minicps.devices import Tank

from utils import STATE
from utils import BOTTLE_SECTION
from utils import BOTTLE_M, BOTTLE_INIT_LEVEL
from utils import PP_PERIOD_SEC, PP_PERIOD_HOURS  # PP_SAMPLES

import time

ACTUATOR1 = ('ACTUATOR1-MV', 1)
SENSOR2 = ('SENSOR2-FL', 2)
SENSOR3 = ('SENSOR3-LL-bottle', 3)


class Bottle(Tank):

    # boot process
    def pre_loop(self):
        # simulates init level of bottle
        self.level = self.set(SENSOR3, BOTTLE_INIT_LEVEL)

    def main_loop(self):
        # count = 0
        # while(count <= PP_SAMPLES):
        while True:
            new_level = self.level

            # compute water volume
            water_volume = self.section * new_level

            # inflow volumes
            actuator = self.get(ACTUATOR1)
            if int(actuator) == 1:
                sensor2 = self.get(SENSOR2)
                inflow = float(sensor2) * PP_PERIOD_HOURS
                water_volume += inflow

            # compute new water_level
            new_level = water_volume / self.section

            # update internal and state liquid level
            print "DEBUG phys-proc bottle: new_level  %.5f m \t delta (volume): %.5f m3" % (
                new_level, (new_level - self.level) * self.section)
            self.level = self.set(SENSOR3, new_level)

            if new_level >= BOTTLE_M['UpperBound']:
                print 'DEBUG phys-proc: Bottle above upperbound threshold ', BOTTLE_M['UpperBound']
                # break
                # simulates change of bottle
                time.sleep(PP_PERIOD_SEC*10)  # simulate time to remove the bottle and hand in a empty one
                self.level = self.set(SENSOR3, BOTTLE_INIT_LEVEL)
                print 'DEBUG phys-proc: New bottle to fill'

            # count += 1
            time.sleep(PP_PERIOD_SEC)

    def _stop(self):

        print "physical process stopped (BOTTLE)"


if __name__ == '__main__':

    rwt = Bottle(
        name='bottle',
        state=STATE,
        protocol=None,
        section=BOTTLE_SECTION,
        level=BOTTLE_INIT_LEVEL
    )