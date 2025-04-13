def square_digits(num):
    list = []
    num = str(num)
    for x in range (0, len(num)):
        list.append(str(int(num[x])**2))
    num = "".join(list)
    return (int(num))