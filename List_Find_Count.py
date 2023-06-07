listA = [19, 19, 5, 3, 5, 5, 3, 5]
listB = [19, 12, 23, 345, 3, 3, 3]
listC = [35, 56, 55, 2, 2, 5, 2, 3]


def findcountnums(used_list):
    list_length = len(used_list)
    fifth_num = used_list[4]
    fifth_num_count = used_list.count(fifth_num)
    if list_length == 8 and fifth_num_count >= fifth_num_count:
        print(True)
    else:
        print(False)


findcountnums(listA)
findcountnums(listB)
findcountnums(listC)
