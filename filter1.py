#  Write code to assign to the variable filter_testing all the elements in lst_check that have a w in them using filter.


def check_w(value):
    alist = []
    for item in value:
        if 'w' in item:
            alist.append(item)
    return alist


def keep_w(nums):
    new_seq = filter(check_w, nums)
    return list(new_seq)


lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
filter_testing = keep_w(lst_check)
print(filter_testing)
