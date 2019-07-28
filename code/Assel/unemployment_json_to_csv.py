import json
import csv

head = ['Year', 'Newfoundland and Labrador', 'Prince Edward Island', 'Nova Scotia', \
            'New Brunswick', 'Quebec', 'Ontario', 'Manitoba', 'Saskatchewan', \
            'Alberta', 'British Columbia']

provinces = ['Newfoundland and Labrador', 'Prince Edward Island', 'Nova Scotia', \
            'New Brunswick', 'Quebec', 'Ontario', 'Manitoba', 'Saskatchewan', \
            'Alberta', 'British Columbia']

years = [i for i in range(1976, 2018)]

with open ('unemployment.json', 'r') as f:
    x = json.load(f)
print(x)

f = csv.writer(open("unemployment.csv", "w"))

# Write CSV Header, If you dont need that, remove this line
f.writerow(head)

for year in years:
    print(x[str(year)])
    l = [int(year)]
    for prov in provinces:
        l.append(x[str(year)][prov])
    f.writerow(l)
