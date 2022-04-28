import random
import csv

values = []
with open("PRO-C111-v1-Project-Solution-main\medium_data.csv.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        values.append(row[7])

print(values)

sample_1 = [[values[0]]]
sample_2 = [[values[0]]]
sample_3 = [[values[0]]]

for i in range(100):
    sample_1.append([random.choice(values)])

for i in range(100):
    sample_2.append([random.choice(values)])

for i in range(100):
    sample_3.append([random.choice(values)])

with open("sample_1.csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerows(sample_1)

with open("sample_2.csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerows(sample_2)

with open("sample_3.csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerows(sample_3)