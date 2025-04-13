def solution(number):
    y = 0
    for x in range (0,number):
        if (x % 3 == 0 and x % 5 == 0):
            y = y+x
        elif(x % 3 == 0 or x % 5 == 0):
            y = y+x
    return y