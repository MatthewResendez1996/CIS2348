##Matthew James Resendez
##1431242
import csv
file = input()
wf = {}

with open(file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in  csvreader:
        for word in row:
            if word not in wf.keys():
                wf[word] = 1
            else:
                wf[word] += 1
for key in wf.keys():
    print(key + " " + str(wf[key]))
