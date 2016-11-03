def safe_pawns(pawns):
    import string
    cols = list(string.lowercase[0:8])
    rows = [str(i) for i in range(1, 9)]

    def stringtopos(s):
        return [
            cols.index(s[0]),
            rows.index(s[1])]

    def is_safe(pos):
        P = stringtopos(pos)
        for pawn in pawns:
            if pos != pawn:
                Pa = stringtopos(pawn)
                testrow = (P[1] == Pa[1] + 1)
                testcol1 = (P[0] == Pa[0] - 1)
                testcol2 = (P[0] == Pa[0] + 1)
                if testrow and (testcol1 or testcol2):
                    return True
        return False

    res = 0
    for p in pawns:
        if is_safe(p):
            res += 1
    return res

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
