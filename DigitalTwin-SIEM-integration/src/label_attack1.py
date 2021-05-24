import csv
SENSOR2_THRESH = 3.00
tank_lb = 0.3
tank_ub = 5.81
bottle_ub = 0.9

with open('logs/data.csv','r') as csvinput:
    with open('labelled.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput)

        for row in csv.reader(csvinput):
            if row[0] == "motor_status":
                writer.writerow(row+["traffic"])
            elif int(row[0]) == 0 and (float(row[7]) <= tank_lb or float(row[4]) >= SENSOR2_THRESH or float(row[2]) >= bottle_ub):
                writer.writerow(row+['normal'])
            elif int(row[0]) == 1 and float(row[2]) < bottle_ub and float(row[7]) > tank_lb:
                writer.writerow(row+['normal'])
            else:
                writer.writerow(row+['anomaly'])
