def flatten(d):
    res = {}
    k = []

    def dig(dik, depth):
        for key, v in dik.iteritems():
            if len(k) < depth + 1:
                k.insert(depth, key)
            else:
                k[depth] = key
            for i in reversed(range(depth + 1, len(k))):
                k.pop(i)
            if v:
                if type(v) is dict:
                    dig(v, depth + 1)
                else:
                    res['/'.join(k)] = v
            else:
                res['/'.join(k)] = ''
    dig(d, 0)
    return res


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({
        "name": {
            "first": "One",
            "last": "Drone"},
        "job": "scout",
        "recent": {},
        "additional": {
            "place": {
                "zone": "1",
                "cell": "2"}}}
        ) == {"name/first": "One",
              "name/last": "Drone",
              "job": "scout",
              "recent": "",
              "additional/place/zone": "1",
              "additional/place/cell": "2"}
