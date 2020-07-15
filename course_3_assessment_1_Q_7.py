# Given the dictionary, nested_d, save the medal count for the USA from all three Olympics in the dictionary to the
# list US_count.

nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}

US_count = []

for city in nested_d.keys():
    countries = nested_d[city]
    for country in countries.keys():
        if country == 'USA':
            US_count.append(countries[country])
print(US_count)