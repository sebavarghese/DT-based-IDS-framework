import csv
SENSOR2_THRESH = 3.00
tank_lb = 0.3
tank_ub = 5.81
bottle_ub = 0.9

with open('logs/data.csv','r') as csvinput:
    with open('logs/labelled.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput)

        for row in csv.reader(csvinput):
            if row[0] == "timestamp":
                writer.writerow(row+["traffic_type"])
            elif int(row[11]) == 0 and (float(row[1]) <= tank_lb or float(row[5]) >= SENSOR2_THRESH or float(row[8]) >= bottle_ub):
                writer.writerow(row+['normal'])
            elif int(row[11]) == 1 and float(row[8]) < bottle_ub and float(row[1]) > tank_lb:
                writer.writerow(row+['normal'])
            else:
                writer.writerow(row+['anomaly'])
