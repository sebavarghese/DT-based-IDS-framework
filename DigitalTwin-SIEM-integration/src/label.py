##### Script to label generated dataset at level1; uses threshold condition to detect command injection attacks and network DoS attacks#####
##### Results are labelled dataset stored as 'data1.csv' in logs folder ######
##### Level 2 labelling takes this data1.csv as input and label the remaining attacks wrt attack durations #####
import csv
import math
SENSOR2_THRESH = 3.00
tank_lb = 0.3
tank_ub = 5.81
bottle_ub = 0.9

with open('logs/data.csv','r') as csvinput:
    with open('logs/data1.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput)
        for row in csv.reader(csvinput):
            if row[0] == "timestamp":
                writer.writerow(row+["class"])
            else:
                # Handle all anomalous case in here; and mark anything that is outside these cases as Normal.                                                                                                               ############################################################################################################################
                ### For command injection attacks
                ### Anomaly when motor valve closed when bottle_ll < bottle_ub and when tank_ll > tank_lb
                ### Anomaly when motor valve is open if bottle_ll >= bottle_ub or if flowlevel >= sensor2_threshold or if tank_ll <= tank_ll
                ############################################################################################################################
                if int(row[4]) == 1 and (float(row[1]) <= tank_lb or (float(row[2]) >= SENSOR2_THRESH and float(row[2]) != 999) or (float(row[3]) >= bottle_ub and float(row[3]) != 999)):
                    writer.writerow(row+['Command Injection'])
                elif int(row[4]) == 0 and float(row[3]) < bottle_ub and float(row[1]) > tank_lb:
                    writer.writerow(row+['Command Injection'])
                ################################################################################
                ### For Network DoS: MitM attacks as well as Network DoS: TCP SYN flood attacks
                ### Anomaly if flowlevel or bottle_ll is marked as 999
                ################################################################################
                elif float(row[2]) == 999 or float(row[3]) == 999:
                    writer.writerow(row+['Network DoS'])
                #Final case
                else:
                    writer.writerow(row+['Normal'])
