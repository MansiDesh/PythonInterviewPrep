def largest_element(list1):
    largest = list1[0]
    for ele in list1:
        if ele > largest:
            largest = ele
    print(largest)


list1 = [10, 9000, 5, 150, 56, 100, 300]
largest_element(list1)
