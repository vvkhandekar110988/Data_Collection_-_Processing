# Iterate through the contents of l_of_l and assign the third element of sublist to a new list called third.

l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'], ['sea green', 'cornflower', 'lavender', 'indigo'], ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]

third = []

for colours in l_of_l:
    for colour in colours[2:3]:
        third.append(colour)
print(third)