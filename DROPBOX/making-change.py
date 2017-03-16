import itertools
def checkio(price, deno):
    res = {}
    deno_combinations = itertools.chain(
        *[[_ for _ in itertools.combinations(deno, j)] for j in range(1, len(deno)+1)])
    for comb in deno_combinations:
        print(comb)
        for j in range(1, len(comb)+1):
            for i, d in enumerate(deno):
                _price = price
                tmpres = {}
                for d in reversed(comb[0:i+1]):
                    tmpres[str(d)] = _price // d
                    _price = _price % d
                if _price > 0:
                    pass
                elif sum(res.values()) == 0:
                    res = dict(**tmpres)
                elif sum(tmpres.values()) < sum(res.values()):
                    res = dict(**tmpres)
    print(res)
    if len(res) > 0:
        return sum(res.values())
    else:
        return None
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(8, [1, 3, 5]) == 2
    assert checkio(12, [1, 4, 5]) == 3
    assert checkio(123456, [1,6,7,456,678]) == 187
    print('Done')

