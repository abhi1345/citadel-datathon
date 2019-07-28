import json
data = {}
provinces = ['Newfoundland and Labrador', 'Prince Edward Island', 'Nova Scotia', \
            'New Brunswick', 'Quebec', 'Ontario', 'Manitoba', 'Saskatchewan', \
            'Alberta', 'British Columbia']

with open ("unemployment.csv", 'r') as f:
    for line in f:
        val = line.split()
        data[val[0]] = {}
        i = 1
        for prov in provinces:
            data[val[0]][prov] = val[i]
            i += 1
with open("unemployment.json", 'w') as f:
    json.dump(data, f)
