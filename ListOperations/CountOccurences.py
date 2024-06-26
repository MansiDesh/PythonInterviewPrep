def count_occ(list1):
    count = {}
    for ele in list1:
        if ele in count:
            count[ele] += 1
        else:
            count[ele] = 1

    for key in count:
        print(key, count[key])


count_occ([1, 3, 4, 5, 1, 1, 1])
