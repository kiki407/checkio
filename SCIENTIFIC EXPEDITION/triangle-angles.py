def checkio(a, b, c):
    from math import acos, degrees
    _a, _b, _c = (float(a), float(b), float(c))
    
    if sorted([a,b,c])[-1] < sorted([a,b,c])[0] + sorted([a,b,c])[1]:
        angleC = int(round(degrees(acos((_a**2 + _b**2 - _c**2)/(2*_a*_b)))))
        angleA = int(round(degrees(acos((_c**2 + _b**2 - _a**2)/(2*_c*_b)))))
        angleB = int(round(degrees(acos((_a**2 + _c**2 - _b**2)/(2*_a*_c)))))
        return sorted([angleA, angleB, angleC])
    else:
        return [0,0,0]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
