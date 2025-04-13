def disemvowel(string):
    vowels = ["a","e","i","o","u","A","E","I","O","U",]
    for i in range (0,len(vowels)):
        string = string.replace(vowels[i], "" )
    return string