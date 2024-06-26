def count_dup(string):
    count = {}
    for char in string:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for key in count:
        if count[key] > 1:
            print(key, count[key])
