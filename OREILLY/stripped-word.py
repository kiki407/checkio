import re
VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    supercounter = 0
    checked = False
    words = re.findall(r"[\w']+", text)

    for word in words:
        goodword = False
        previous = ''
        for i in word:

            if (previous.upper() in VOWELS) and (i.upper() in CONSONANTS):
                goodword = True
                checked = True
            elif (previous.upper() in CONSONANTS) and (i.upper() in VOWELS):
                goodword = True
                checked = True
            else:
                checked = False
                break
            previous = i
        if len(word) > 1 and goodword and checked:
            supercounter += 1

    return supercounter

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"My name is ...") == 3, "All words are striped"
    assert checkio(u"Hello world") == 0, "No one"
    assert checkio(u"A quantity of striped words.") == 1, "Only of"
    assert checkio(u"Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
