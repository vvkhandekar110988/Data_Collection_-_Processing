# The variable nested contains a nested list. Assign ‘snake’ to the variable output using indexing.


nested = [['dog', 'cat', 'horse'], ['frog', 'turtle', 'snake', 'gecko'], ['hamster', 'gerbil', 'rat', 'ferret']]
output = ''

for lst1 in nested:
    for animal in lst1:
        if 'snake' in animal:
            output += animal
print(output)
