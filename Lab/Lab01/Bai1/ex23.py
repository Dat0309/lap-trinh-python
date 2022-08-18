def substring_copy(str, n):
    flen = 2
    result = ""
    if flen > len(str):
        flen = len(str)

    for i in range(n):
        result = result + str[:flen]
    return result

