"""
FP utils.py

sqlite and enip use name (string) and pid (int) has key and the state stores
values as strings.

sqlite uses float keyword and cpppo use REAL keyword.

if ACTUATOR1MV is 1 then is OPEN otherwise is CLOSE.

abbr. LL: liquid level
      FL: flow level
      MV: motor valve
"""

from minicps.utils import build_debug_logger

fp_logger = build_debug_logger(
    name=__name__,
    bytes_per_file=10000,
    rotating_files=2,
    lformat='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    ldir='logs/',
    suffix='')

# data
PLC1_DATA = {
    'SENSOR1-LL-tank': '1.7',
    'ACTUATOR1-MV': '0',  # 0 means CLOSE and 1 means OPEN
    'SENSOR2-FL': '0.0',  # interlock with PLC2
    'SENSOR3-LL-bottle': '0.0'  # interlock with PLC3
}
PLC2_DATA = {
    'SENSOR2-FL': '0'  # interlock with PLC1
}
PLC3_DATA = {
    'SENSOR3-LL-bottle': '0'  # interlock with PLC1
}
HMI_DATA = {
    'ACTUATOR1-MV': '0'  # interlock with PLC1
}

# PLC1
PLC1_MAC = '00:00:00:00:00:01'
PLC1_TAGS = (
    ('SENSOR1-LL-tank', 1, 'REAL'),
    ('ACTUATOR1-MV', 1, 'INT'),  # 0 means CLOSE and 1 means OPEN
    ('SENSOR2-FL', 1, 'REAL'),  # interlock with PLC2
    ('SENSOR3-LL-bottle', 1, 'REAL')  # interlock with PLC3
)
PLC1_ADDR = '10.0.0.1'
PLC1_SERVER = {
    'address': PLC1_ADDR,
    'tags': PLC1_TAGS
}
PLC1_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC1_SERVER
}

# PLC2
PLC2_MAC = '00:00:00:00:00:02'
PLC2_ADDR = '10.0.0.2'
PLC2_TAGS = (('SENSOR2-FL', 2, 'REAL'),)
PLC2_SERVER = {
    'address': PLC2_ADDR,
    'tags': PLC2_TAGS
}
PLC2_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC2_SERVER
}

# PLC3
PLC3_MAC = '00:00:00:00:00:03'
PLC3_ADDR = '10.0.0.3'
PLC3_TAGS = (('SENSOR3-LL-bottle', 3, 'REAL'),)
PLC3_SERVER = {
    'address': PLC3_ADDR,
    'tags': PLC3_TAGS
}
PLC3_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC3_SERVER
}

# HMI
HMI_MAC = '00:00:00:00:00:04'
HMI_ADDR = '10.0.0.4'
HMI_TAGS = (('ACTUATOR1-MV', 4, 'INT'),('ACTUATOR1-HMI', 4, 'INT'),)  # HMI-pid: 4
HMI_SERVER = {
    'address': HMI_ADDR,
    'tags': HMI_TAGS
}
HMI_PROTOCOL = {
    'name': 'enip',
    'mode': 0,    # client only
    'server': HMI_SERVER
}

# ATTACKER
ATTCKR_MAC = '00:00:00:00:00:05'
ATTCKR_ADDR = '10.0.0.5'

NETMASK = '/24'


# samples for simulation
PLC_PERIOD_SEC = 0.50  # plc update rate in seconds
PLC_PERIOD_HOURS = PLC_PERIOD_SEC / 3600.0
# PLC_SAMPLES = 1000

PP_RESCALING_HOURS = 100   # physical process (pp)
PP_PERIOD_SEC = 0.25  # physical process update rate in seconds
PP_PERIOD_HOURS = (PP_PERIOD_SEC / 3600.0) * PP_RESCALING_HOURS
# PP_SAMPLES = int(PLC_PERIOD_SEC / PP_PERIOD_SEC) * PLC_SAMPLES

HMI_PERIOD_SEC = 1

# physical conditions
TANK_SECTION = 1.50      # m2
TANK_INIT_LEVEL = 5.80  # l   #1.80

PUMP_FLOWRATE_OUT = 2.45  # m3/h

BOTTLE_SECTION = 0.75      # m2
BOTTLE_INIT_LEVEL = 0.0   # l


SENSOR2_THRESH = 3.00   # m3/h upperbound

TANK_M = {  # liquid tank thresholds [m]
    'LowerBound': 0.3,
    'UpperBound': 5.81,       #1.81
}
BOTTLE_M = {  # bottle thresholds [m]
    'LowerBound': 0.0,
    'UpperBound': 0.9,
}


# physical state
PATH = 'fp_db.sqlite'
NAME = 'fp_table'

STATE = {
    'name': NAME,
    'path': PATH
}

# pid is device id (e.g. plc number)
SCHEMA = """
CREATE TABLE fp_table (
    name              TEXT NOT NULL,
    pid               INTEGER NOT NULL,
    value             TEXT,
    PRIMARY KEY (name, pid)
);
"""

SCHEMA_INIT = """
    INSERT INTO fp_table VALUES ('SENSOR1-LL-tank',   1, '1.7');
    INSERT INTO fp_table VALUES ('SENSOR2-FL',    2, '0.0');
    INSERT INTO fp_table VALUES ('SENSOR3-LL-bottle',   3, '0.0');
    INSERT INTO fp_table VALUES ('ACTUATOR1-MV',     1, '0');
"""
