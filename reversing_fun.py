def reverse_fun(n):
    list = []
    for x in range (0, len(n)):
        n = n[::-1]
        list.append(n[0])
        n = n[1:]
    a=""
    n = a.join(list)
    return n