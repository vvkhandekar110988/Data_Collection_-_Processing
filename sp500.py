fileref = open('SP500.txt', 'r')
# contents = fileref.read()
lines = fileref.readlines()
# print(contents)
sp_500 = []
long_term = []
for line in lines[1:]:
    date = line.split(',')[0]
    print(date)
    if '6/1/2016' <= date >= '5/1/2017':
        sp_500.append(line.split(',')[1])
        long_term.append(line.split(',')[5])
print(sp_500)
print(long_term)

mean_SP = 0
sum = 0
for item in sp_500:
    sum += float(item)

mean_SP = sum / len(sp_500)
print(mean_SP)


'''
mean_SP = 0.0
sum = 0.0
for item in abc:
    sum += float(item)
mean_SP = sum / len(abc)
print(mean_SP)


max_interest = abc[0]
for item in abc:
    if max_interest > item:
        continue
    else:
        max_interest = item
print(max_interest)
'''