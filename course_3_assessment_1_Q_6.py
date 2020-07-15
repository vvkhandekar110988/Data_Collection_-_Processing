# Below, we have provided a nested dictionary. Index into the dictionary to create variables that we have listed in
# the ActiveCode window.


sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'], 'diving': ['springboard', 'platform', 'synchronized'], 'track': ['sprint', 'distance', 'jumps', 'throws'], 'gymnastics': {'women':['vault', 'floor', 'uneven bars', 'balance beam'], 'men': ['vault', 'parallel bars', 'floor', 'rings']}}

# Assign the string 'backstroke' to the name v1
for key in sports.keys():
    if key == 'swimming':
        swim_type = (sports[key])
        for item in swim_type:
            if item == 'backstroke':
                v1 = item
print(v1)
# Assign the string 'platform' to the name v2
for key in sports.keys():
    if key == 'diving':
        swim_type = (sports[key])
        for item in swim_type:
            if item == 'platform':
                v2 = item
print(v2)
# Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the name v3


v3 = sports['gymnastics']['women']
print(v3)


# Assign the string 'rings' to the name v4
v4_lst = sports['gymnastics']['men']
for item in v4_lst:
    if 'rings' == item:
        v4 = item
print(v4)
