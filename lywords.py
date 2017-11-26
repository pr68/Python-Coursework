def get_words(file_name):
    import string
    file = open(file_name, "r")
    text = file.read().lower()
    for c in string.punctuation:
        text = text.replace(c, "")
    words = text.split()
    return words


def get_dic(words):
    unique = set(words)
    lywords = [w for w in unique if w.endswith('ly')]
    counts = []
    for word in lywords:
        counts.append(words.count(word))
    com = zip(lywords, counts)
    dic = dict(com)
    return dic


def get_top_10(dic):
    lytuple = dic.items()
    srt = sorted(lytuple, key=lambda lyw: lyw[1])
    srt = srt[::-1]
    srt = srt[0:9]
    return srt


get_top_10(get_dic(get_words("sense.txt")))
