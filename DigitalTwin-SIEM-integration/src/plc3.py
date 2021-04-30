"""
FP plc3.py
"""

from minicps.devices import PLC
from utils import PLC3_DATA, STATE
from utils import PLC3_PROTOCOL, PLC3_ADDR
from utils import PLC_PERIOD_SEC  # PLC_SAMPLES

import time
import logging


SENSOR3 = ('SENSOR3-LL-bottle', 3)


class FPPLC3(PLC):

    # boot process
    def pre_loop(self, sleep=0.6):
        print 'DEBUG: FP PLC3 booting process (enter pre_loop)'
        print
        # wait for the other plcs
        time.sleep(sleep)

    def main_loop(self, sleep=0.0):
        """plc3 main loop.
                    - read liquid level of bottle (sensor3)
                    - update internal enip server
                """

        print 'DEBUG: FP PLC3 enters main_loop.'
        print
        # FYI: BSD-syslog format (RFC 3164), e.g. <133>Feb 25 14:09:07 webserver syslogd: restart   PRI <Facility*8+Severity>, HEADER (timestamp host), MSG (program/process message)
        logging.basicConfig(filename='logs/plc3.log',
                            format='%(levelname)s %(asctime)s ' + PLC3_ADDR + ' %(funcName)s %(message)s',
                            datefmt='%m/%d/%Y %H:%M:%S', level=logging.DEBUG)

        # count = 0
        # while count <= PLC_SAMPLES:
        while True:
            # physical process
            liquidlevel_bottle = float(self.get(SENSOR3))
            print "PLC3 - get liquidlevel_bottle (SENSOR 3): %i" % liquidlevel_bottle

            try:
                # network capabilities
                self.send(SENSOR3, liquidlevel_bottle, PLC3_ADDR)
                # sensor3 = self.receive(SENSOR3, PLC3_ADDR)
                print "DEBUG PLC3 - receive liquidlevel_bottle (SENSOR 3): ", liquidlevel_bottle
                logging.info("Internal ENIP tag (SENSOR 3) updated: %.2f" % (
                    liquidlevel_bottle))
            except:
                logging.info("Could not update internal ENIP tag (SENSOR 3)")

            time.sleep(PLC_PERIOD_SEC)
            # count += 1

        print 'DEBUG FP PLC3 shutdown'


if __name__ == "__main__":

    plc3 = FPPLC3(
        name='plc3',
        state=STATE,
        protocol=PLC3_PROTOCOL,
        memory=PLC3_DATA,
        disk=PLC3_DATA)