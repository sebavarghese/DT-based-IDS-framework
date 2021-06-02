import csv

with open('logs/data.csv','r') as csvinput:
    with open('logs/labelled.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput)
        for row in csv.reader(csvinput):
            if row[0] == "timestamp":
                writer.writerow(row+["traffic_type"])
            elif row[4] == '' or row[6] == '':
                writer.writerow(row+['anomaly'])
            else:
                writer.writerow(row+['normal'])
