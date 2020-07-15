# Using filter, filter lst so that it only contains words containing the letter “o”. Assign to variable lst2. Do not
# hardcode this.

def check_o(value):
    alist = []
    for item in value:
        if 'o' in item:
            alist.append(item)
    return alist


def keep_o(nums):
    new_seq = filter(check_o, nums)
    return list(new_seq)


lst = ["witch", "halloween", "pumpkin", "cat", "candy", "wagon", "moon"]
lst2 = keep_o(lst)
print(lst2)
