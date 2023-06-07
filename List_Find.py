listA = [19, 19, 5, 3, 5, 5, 3, 5, 0]
listB = [19, 12, 23, 345, 3]
listC = [35, 56, 55]


def findnums(used_list):
    number_nineteen = used_list.count(19)
    number_five = used_list.count(5)
    if number_nineteen == 2 and number_five >= 3:
        print(True)
    else:
        print(False)


findnums(listA)
findnums(listB)
findnums(listC)
