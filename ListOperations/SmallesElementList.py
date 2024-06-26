def smallest(list1):
    smallest_el = list1[0]
    for ele in list1:
        if ele < smallest_el:
            smallest_el = ele
    print(smallest_el)


list1 = [10, 9000, 5, 150, 56, 100, 300, 8000, 0, 1]
smallest(list1)
