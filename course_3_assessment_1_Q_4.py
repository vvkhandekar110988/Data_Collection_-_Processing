# Provided is a nested data structure. Follow the instructions in the comments below. Do not hard code.


nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum',
                                                                            ['math', 'calculus', 'algebra', 'geometry',
                                                                             'statistics',
                                                                             ['physics', 'chemistry', 'biology']]]}

# Check to see if the string data is a key in nested, if it is, assign True to the variable data, otherwise assign
# False.
data = False
for item in nested:
    if 'data' in item:
        data = True
print(data)

# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the
# value of True, otherwise False.
twentyfour = False
for list1 in nested:
    if 'data' in list1:
        if 24 == nested['data']:
            twentyfour = True
print(twentyfour)

# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the
# variable whole the value of True, otherwise False.
whole = False
for list1 in nested:
    if 'window' in list1:
        if 'whole' not in nested['window']:
            whole = True
print(whole)
# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics,
# the value of True, otherwise False.
physics = False
for item in nested:
    if 'physics' in item:
        physics = True
print(physics)

