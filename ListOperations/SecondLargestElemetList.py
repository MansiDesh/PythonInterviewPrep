def second_largest_element(list1):
    largest = list1[0]
    second_largest = list1[0]
    for ele in list1:
        if ele > largest:
            largest = ele
    print(largest)

    for ele1 in list1:
        if ele1 > second_largest and ele1 != largest:
            second_largest = ele1
    print(second_largest)


list1 = [10, 9000, 5, 150, 56, 100, 300,8000]
second_largest_element(list1)
