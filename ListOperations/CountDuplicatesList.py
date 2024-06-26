def count_dub_list(list1):
    count = {}
    for ele in list1:
        if ele in count:
            count[ele] += 1
        else:
            count[ele] = 1
    for key in count:
        if count[key] > 1:
            print(key, count[key])


count_dub_list([1, 1, 3, 4, 4, 5])
