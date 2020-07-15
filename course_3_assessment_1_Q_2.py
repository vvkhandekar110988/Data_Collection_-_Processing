lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]

# Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``

for lst1 in lst:
    if type(lst1) is list:
        for fruit in lst1:
            if 'yellow' in lst1:
                yellow = True

print(yellow)

# Test to see if 4 is in the second list of lst. Save to variable ``four``
four = False
for lst1 in lst[1:2]:
    for item in lst1:
        if 4 == item:
            four = True

print(four)

# Test to see if 'orange' is in the first element of lst. Save to variable ``orange``


orange = False
for lst1 in lst[0:1]:
    for item in lst1:
        if 'orange' in lst1:
            orange = True
print(orange)
