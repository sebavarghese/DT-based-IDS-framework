#!/usr/bin/env python

"""
FP init.py

Run this script just once to create and init the sqlite table.
"""

from minicps.states import SQLiteState
from utils import PATH, SCHEMA, SCHEMA_INIT
from sqlite3 import OperationalError
import os


if __name__ == "__main__": 
    try: 
        os.remove(PATH)
    except OSError:
        print "{} does not exist.".format(PATH)
    try:
        SQLiteState._create(PATH, SCHEMA)
        SQLiteState._init(PATH, SCHEMA_INIT)
        print "{} successfully created.".format(PATH)
    except OperationalError:
        print "{} already exists.".format(PATH)
    
    #os.system('mkdir pcaps && cd pcaps && touch cap1.pcap && touch cap2.pcap && touch cap3.pcap && touch cap4.pcap && touch cap5.pcap') 

