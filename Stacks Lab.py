def merge_sorted_lists(list1, list2):
    samp = (None, None)
    now = samp

    while list1 is not None and list2 is not None:
        if list1[0] < list2[0]:
            now = (list1[0], now)
            list1 = list1[1]
        else:
            now = (list2[0], now)
            list2 = list2[1]
    if list1 is not None:
        now = (list1[0], now)
        now = now[1]
    elif list2 is not None:
        now = (list2[0], now)
        now = now[1]

    merged_list = None
    while now is not None and now[0] is not None:
        merged_list = (now[0], merged_list)
        now = now[1]

    return merged_list

list1 = (1, (2, (4, None)))
list2 = (1, (3, (4, None)))

merged_list = merge_sorted_lists(list1, list2)

while merged_list is not None and merged_list[0] is not None:
    print(merged_list[0], end=" -> ")
    merged_list = merged_list[1]