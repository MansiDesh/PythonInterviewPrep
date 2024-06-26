def remove_dup(string):
    result = ""
    for char in string:
        if char not in result:
            result = result + char
    print(result)





# abbcce
remove_dup("abbeec")
