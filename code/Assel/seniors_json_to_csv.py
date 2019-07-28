import json
import csv

head = ['Year', 'Newfoundland and Labrador', 'Prince Edward Island', 'Nova Scotia', \
        'New Brunswick', 'Quebec', 'Ontario', 'Manitoba', 'Saskatchewan', \
        'Alberta', 'British Columbia', "Canada"] 

provinces = ['Newfoundland and Labrador', 'Prince Edward Island', 'Nova Scotia', \
        'New Brunswick', 'Quebec', 'Ontario', 'Manitoba', 'Saskatchewan', \
        'Alberta', 'British Columbia', "Canada"] 

years = [1921, 1931, 1941, 1951, 1961, 1971, 1981, 1991, 2001, 2011]
with open ('median_age.json', 'r') as f:
    x = json.load(f)
print(x)

f = csv.writer(open("median_age.csv", "w"))

# Write CSV Header, If you dont need that, remove this line
f.writerow(head)

for year in years:
    print(x[str(year)])
    l = [int(year)]
    for prov in provinces:
        print(x[str(year)])
        l.append(x[str(year)][prov])

    f.writerow(l)
