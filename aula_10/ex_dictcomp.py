
def dic_comprehension(num):
    dic = {}
    for elem in range(num):
        dic[chr(elem+ 65)] = elem * elem
    return dic
