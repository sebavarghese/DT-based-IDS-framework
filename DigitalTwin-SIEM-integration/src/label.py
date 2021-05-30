import csv
import math

with open('logs/data.csv','r') as csvinput:
    with open('logs/labelled.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput)
        for row in csv.reader(csvinput):
            if row[0] == "timestamp":
                writer.writerow(row+["traffic_type"])
            else:
                if float(row[4]) == 1.5:
                    writer.writerow(row+['anomaly'])
                else:
                    writer.writerow(row+['normal'])
