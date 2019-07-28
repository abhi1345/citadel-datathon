import json
import csv

head = ['Year', 'Newfoundland and Labrador', 'Prince Edward Island', 'Nova Scotia', \
        'New Brunswick', 'Quebec', 'Ontario', 'Manitoba', 'Saskatchewan', \
        'Alberta', 'British Columbia', "Y.T.", "N.W.T.", "Nun.", "Canada"] 

provinces = ['Newfoundland and Labrador', 'Prince Edward Island', 'Nova Scotia', \
        'New Brunswick', 'Quebec', 'Ontario', 'Manitoba', 'Saskatchewan', \
        'Alberta', 'British Columbia', "Y.T.", "N.W.T.", "Nun.", "Canada"] 

years = [i for i in range(1975, 2018)]

with open ('population_count.json', 'r') as f:
    x = json.load(f)
print(x)

f = csv.writer(open("population_count.csv", "w"))

# Write CSV Header, If you dont need that, remove this line
f.writerow(head)

for year in years:
    print(x[str(year)])
    l = [int(year)]
    for prov in provinces:
        print(x[str(year)])
        if prov == "Nun.": l.append("")
        else:
            l.append(x[str(year)][prov])


    f.writerow(l)
