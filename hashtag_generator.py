import string
def generate_hashtag(s):
    if s == "":
        return False
    ss = string.capwords(s)
    sss = ss.replace(" ","")
    new = ("#"+(sss))
    if len(new) > 140:
        return False
    else:
        return (new)
