def get_count(sentence):
    list_sentence = list(sentence)
    vowel_count = 0
    vowels = ["a","e","i","o","u"]
    for i in range (0, len(list_sentence)):
        if list_sentence[i] in vowels:
            vowel_count += 1
    return(vowel_count)
        