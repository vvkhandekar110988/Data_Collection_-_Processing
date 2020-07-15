# Below, we’ve provided a list of lists. Use in statements to create variables with Boolean values - see the
# ActiveCode window for further directions.

L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]

# Test if 'hola' is in the list L. Save to variable name test1
test1 = True
for list1 in L:
    if type(list1) is list:
        for item in list1:
            if 'hola' in list1:
                test1 = False
print(test1)

# Test if [5, 8, 7] is in the list L. Save to variable name test2
test2 = False
for item in L:
    if [5, 8, 7] in L:
        test2 = True

print(test2)

# Test if 6.6 is in the third element of list L. Save to variable name test3
test3 = False
for list1 in L[2:3]:
    for item in list1:
        if item == 6.6:
            test3 = True
print(test3)