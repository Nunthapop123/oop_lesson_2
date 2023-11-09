import copy


def gen_comb_list(list_set):
    if len(list_set) == 1:
        start_list = []
        for item in list_set[0]:
            start_list.append([item])
        return start_list
    comb_list_temp = gen_comb_list(list_set[0:-1])
    start_list = []
    for list_item in comb_list_temp:
        for val in list_set[-1]:
            temp_item = copy.deepcopy(list_item)
            temp_item.append(val)
            start_list.append(temp_item)
    return start_list


print(gen_comb_list([[1, 2, 3]]))
print(gen_comb_list([[1, 2, 3], [4, 5]]))
print(gen_comb_list([[1, 2, 3], [4, 5], [6, 7, 8]]))
