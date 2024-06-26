def reverse_string(sting):
    result = ""
    for char in sting:
        if char not in result:
            result = char + result
            print(result)
    print(result)

string = "gslab"
print(string[::-1])

reverse_string("abcdef")