import csv
import math
SENSOR2_THRESH = 3.00
tank_lb = 0.3
tank_ub = 5.81
bottle_ub = 0.9

with open('logs/data.csv','r') as csvinput:
    with open('logs/labelled.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput)
        for row in csv.reader(csvinput):
            if row[0] == "timestamp":
                writer.writerow(row+["class"]+["attack_type"])
            else:
                # Handle all anomalous case in here; and mark anything that is outside these cases as normal.                                                                                                               ############################################################################################################################
                ### For false data injection attacks
                ### Anomaly when motor valve closed when bottle_ll < bottle_ub and when tank_ll > tank_lb
                ### Anomaly when motor valve is open if bottle_ll >= bottle_ub or if flowlevel >= sensor2_threshold or if tank_ll <= tank_ll
                ############################################################################################################################
                if int(row[9]) == 1 and (float(row[1]) <= tank_lb or (float(row[4]) >= SENSOR2_THRESH and float(row[4]) != 999) or (float(row[6]) >= bottle_ub and float(row[6]) != 999)):
                    writer.writerow(row+['anomaly']+['False data injection'])
                elif int(row[9]) == 0 and float(row[6]) < bottle_ub and float(row[1]) > tank_lb:
                    writer.writerow(row+['anomaly']+['False data injection'])
                ###########################################################
                ### For MitM/DoS attacks as well as TCP SYN flood attacks
                ### Anomaly if flowlevel or bottle_ll is marked as 999
                ###########################################################
                elif float(row[4]) == 999 or float(row[6]) == 999:
                    writer.writerow(row+['anomaly']+['DoS'])
                

                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                #Final case
                else:
                    writer.writerow(row+['normal']+['nil'])
