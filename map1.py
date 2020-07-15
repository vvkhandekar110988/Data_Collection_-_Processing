# Using map, create a list assigned to the variable greeting_doubled that doubles each element in the list lst


def double(value):
    return 2 * value


def doublestuff(alist):
    new_seq = map(double, alist)
    return list(new_seq)


lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
greeting_doubled = doublestuff(lst)
print(greeting_doubled)


