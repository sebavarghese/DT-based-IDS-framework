##### Script to do second level of automated labelling of dataset from level 1, i.e., label.py #####
##### Takes 3 command line arguments: 1) Start time of attack 2) End time of attack 3)  Label: Calculated measurement modification, Naive measurement modification etc #####
##### Example: run 'python label1.py '2021-07-01 16:04:07.681880' '2021-07-01 16:05:11.900075' Calculated Measurement Modification #####
import csv
import math
import sys

start_time = sys.argv[1]
end_time = sys.argv[2]
attack_type = sys.argv[3]
print(start_time)
print(end_time)
print(attack_type)
with open('logs/data1.csv','r') as csvinput:
    with open('logs/labelled.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput)
        for row in csv.reader(csvinput):
            if row[0] != "timestamp" and (row[0] >= start_time and  row[0] <= end_time):
                row[5] = str(attack_type)
                writer.writerow(row)
            else:
                writer.writerow(row)
