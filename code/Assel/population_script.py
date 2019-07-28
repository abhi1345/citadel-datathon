import csv 
import json
data = {}
provinces = ['Newfoundland and Labrador', 'Prince Edward Island', 'Nova Scotia', \
            'New Brunswick', 'Quebec', 'Ontario', 'Manitoba', 'Saskatchewan', \
            'Alberta', 'British Columbia', "Y.T.", "N.W.T.", "Nun.", "Canada"]

size = [405212, 5660, 55284, 72908, 1542056, 1076395, 647797, 651036, 661848, 944735, 482443, 1346106, 2093190, 9984670]
with open('provincial_level.csv', newline='') as csvfile:
         spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
         for row in spamreader:
            if row[1] == 'Appendix: D.1: Population by year':
                print(row[0])
                data[row[0]] = {}
                for i in range(len(provinces)):
                    if row[3 + i]: 
                        data[row[0]][provinces[i]] = float(row[3 + i]) * 1000  
                        print(float(row[i + 3]) * 1000)#/ size[i])
                        print(provinces[i])

with open('population_count.json', 'w') as f:
    json.dump(data, f)

