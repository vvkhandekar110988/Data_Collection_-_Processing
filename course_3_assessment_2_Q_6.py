# Write code using zip and filter so that these lists (l1 and l2) are combined into one big list and assigned to the
# variable opposites if they are both longer than 3 characters each.

l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
l3 = list(zip(l1, l2))


def check_len(value):
    res = [lis for lis in value if len(lis[0]) > 3 and len(lis[1]) > 3]
    return res


opposites = filter(check_len, l3)
print(list(opposites))

