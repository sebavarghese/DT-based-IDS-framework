"""
FP plc2.py
"""

from minicps.devices import PLC
from utils import PLC2_DATA, STATE
from utils import PLC2_PROTOCOL, PLC2_ADDR
from utils import PLC_PERIOD_SEC  # PLC_SAMPLES

import time
import logging


SENSOR2 = ('SENSOR2-FL', 2)


class FPPLC2(PLC):

    # boot process
    def pre_loop(self, sleep=0.6):
        print 'DEBUG: FP PLC2 booting process (enter pre_loop)'
        print
        # wait for the other plcs
        time.sleep(sleep)

    def main_loop(self, sleep=0.0):
        """plc2 main loop.
                    - read flow level (sensor2)
                    - update internal enip server
                """

        print 'DEBUG: FP PLC2 enters main_loop.'
        print
        # FYI: BSD-syslog format (RFC 3164), e.g. <133>Feb 25 14:09:07 webserver syslogd: restart   PRI <Facility*8+Severity>, HEADER (timestamp host), MSG (program/process message)
        logging.basicConfig(filename='logs/plc2.log',
                            format='%(levelname)s %(asctime)s ' + PLC2_ADDR + ' %(funcName)s %(message)s',
                            datefmt='%m/%d/%Y %H:%M:%S', level=logging.DEBUG)

        # count = 0
        # while count <= PLC_SAMPLES:
        while True:
            # physical process
            flowlevel = float(self.get(SENSOR2))
           # print "PLC2 - get flowlevel (SENSOR 2): %f" % flowlevel

            # network capabilities
            try:
                self.send(SENSOR2, flowlevel, PLC2_ADDR)
                # sensor2 = self.receive(SENSOR2, PLC2_ADDR)
                print "DEBUG PLC2 - receive flowlevel (SENSOR 2): ", flowlevel
                logging.info("Internal ENIP tag (SENSOR 2) updated: %.2f" % (
                    flowlevel))
            except:
                logging.info("Could not update internal ENIP tag (SENSOR 2)")

            time.sleep(PLC_PERIOD_SEC)
            # count += 1

        print 'DEBUG FP PLC2 shutdown'


if __name__ == "__main__":

    plc2 = FPPLC2(
        name='plc2',
        state=STATE,
        protocol=PLC2_PROTOCOL,
        memory=PLC2_DATA,
        disk=PLC2_DATA)