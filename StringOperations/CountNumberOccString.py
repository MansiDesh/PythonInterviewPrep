def count_occ(string, char):
    count = 0
    for character in string:
        if character == char:
            count = count + 1
    print(count)


count_occ("abcccccbbbbb", "b")
