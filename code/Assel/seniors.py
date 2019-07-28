import json                                                                                                                                       
data = {}                                                                                                                                         
provinces = ['Newfoundland and Labrador', 'Prince Edward Island', 'Nova Scotia', \
	'New Brunswick', 'Quebec', 'Ontario', 'Manitoba', 'Saskatchewan', \
	'Alberta', 'British Columbia']                                                                                                       
years = [1921, 1931, 1941, 1951, 1961, 1971, 1981, 1991, 2001, 2011]
for year in years:
	data[year] = {}
                                                                                                                                                  
with open ("median_age.csv", 'r') as f:                                                                                                         
    for line in f:                                                                                                                             
        val = line.split(',')                                                                                                                     
        print(val[1])
        print(val[13])
        for prov in provinces:                                                                                                                    
            data[int(val[4])][val[1]] = val[14]

with open("median_age.json", 'w') as f:                                                                                                         
    json.dump(data, f)   
