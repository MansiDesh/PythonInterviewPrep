def smallest(list1):
    smallest_el = list1[0]
    second_smallest = list1[0]
    for ele in list1:
        if ele < smallest_el:
            second_smallest = smallest_el
            smallest_el = ele
        elif ele < second_smallest:
            second_smallest = ele

    print(second_smallest)

#second_smallest,smallest
#10,10
#10,10
#5,10
#5,10
#5,0
#1,0

list1 = [10, 9000, 5, 150, 56, 100, 300, 8000, 0, 1]
smallest(list1)
