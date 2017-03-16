def verify_anagrams(first_word, second_word):
    return sorted(map(lambda x: x.lower(),filter(lambda x: x.isalpha(), (_ for _ in first_word)))) == sorted(map(lambda x: x.lower(),filter(lambda x: x.isalpha(), (_ for _ in second_word))))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams(u"a", u"z"), bool), "Boolean!"
    assert verify_anagrams(u"Programming", u"Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams(u"Hello", u"Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams(u"Kyoto", u"Tokyo") == True, "The global warming crisis of 3002"