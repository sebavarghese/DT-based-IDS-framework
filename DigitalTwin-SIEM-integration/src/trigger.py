import os
import sys
import time

delay=60*int(sys.argv[1])
close_time=time.time()+delay
count=0
while close_time > time.time():
    os.system('touch trigger.txt')
else:
    os.system('sudo rm -rf trigger.txt')


