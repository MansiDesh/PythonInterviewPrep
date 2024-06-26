def remove_duplicates(list1):
    result = []
    for ele in list1:
        if ele not in result:
            result.append(ele)
    print(result)


remove_duplicates([10, 1, 1, 3, 4, 3, 10])
