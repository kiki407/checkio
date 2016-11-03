
import string
def checkio(str_number, radix):
    all = string.digits + string.ascii_uppercase
    res = 0
    unit = len(str_number) - 1
    for x in str_number:
        if all.index(x) < radix:
            r = 1
            for i in range(unit):
                r *= radix
            res += all.index(x) * r
            unit -= 1
        else:
            return -1
    return res

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"AF", 16) == 175, "Hex"
    assert checkio(u"101", 2) == 5, "Bin"
    assert checkio(u"101", 5) == 26, "5 base"
    assert checkio(u"Z", 36) == 35, "Z base"
    assert checkio(u"AB", 10) == -1, "B > A > 10"
