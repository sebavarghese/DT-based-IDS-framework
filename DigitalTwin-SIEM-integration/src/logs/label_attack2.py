import csv

with open('data.csv','r') as csvinput:
    with open('labelled.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput)
        for row in csv.reader(csvinput):
            if row[0] == "motor_status":
                writer.writerow(row+["traffic"])
            elif row[2] == '' or row[4] == '':
                writer.writerow(row+['anomaly'])
            else:
                writer.writerow(row+['normal'])
