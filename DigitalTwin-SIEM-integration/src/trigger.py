##### Script to trigger data collection in PLC1 node #####
import os
import sys
import time

#enter 120 for 2 hours
delay=60*int(sys.argv[1])
close_time=time.time()+delay
count=0
while close_time > time.time():
    os.system('touch trigger.txt')
else:
    os.system('rm -rf trigger.txt')


