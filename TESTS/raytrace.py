from math import floor, ceil


def printseq():
    import random
    for i in range(random.randint(10, 200)):
        print(i)


def sign(n):
    return (n > 0) - (n < 0)


def find_intercepts(A, B):
    (xA, yA) = (A[0] + .5, A[1] + .5)
    (xB, yB) = (B[0] + .5, B[1] + .5)
    m = (yA - yB)/(xA - xB)

    # move A towards B
    if xA > xB:
        allX = [i for i in range(
            int(floor(xB)),
            int(ceil(xA)))][::-1]
    elif xB > xA:
        allX = [i for i in range(
            int(floor(xA)),
            int(ceil(xB)))]
    else:
        allX = []

    if yA > yB:
        allY = [i for i in range(
            int(floor(yB)),
            int(ceil(yA)))][::-1]
    elif yB > yA:
        allY = [i for i in range(
            int(floor(yA)),
            int(ceil(yB)))]
    else:
        allY = []

    intersectY = [(x, m * (x-xA)+yA) for x in allX]
    intersectX = [((y-yA)/m+xA, y) for y in allY]

    def lims(x, y):
        return (
            x <= max(allX) and
            x >= min(allX) and
            y <= max(allY) and
            y >= min(allY))

    allintercts = []

    def add_to_i(x, y):
        tadd = (int(floor(x)), int(floor(y)))
        if tadd[0] in allX and tadd[1] in allY:
            if tadd not in allintercts and tadd != A and tadd != B:
                allintercts.append(tadd)

    for i in intersectX:
        add_to_i(*i)
        add_to_i(i[0], i[1] - 1)
        if i[0] % 1 == 0:
            add_to_i(i[0]-1, i[1] - 1)

    for i in intersectY:
        add_to_i(*i)
        add_to_i(i[0] - 1, i[1])
        if i[1] % 1 == 0:
            add_to_i(i[0]-1, i[1] - 1)

    return allintercts


def raytrace(A, B):
    """ Return all cells of the unit grid crossed by the line segment between
        A and B.
    """

    (xA, yA) = A
    (xB, yB) = B
    (dx, dy) = (xB - xA, yB - yA)
    (sx, sy) = (sign(dx), sign(dy))

    grid_A = (floor(A[0]), floor(A[1]))
    grid_B = (floor(B[0]), floor(B[1]))
    (x, y) = grid_A
    traversed = [grid_A]

    tIx = dy * (x + sx - xA) if dx != 0 else float("+inf")
    tIy = dx * (y + sy - yA) if dy != 0 else float("+inf")

    count = 0
    maxiloop = 10
    while (x, y) != grid_B:
        (movx, movy) = (tIx <= tIy, tIy <= tIx)

        if movx:
            # intersection is at (x + sx, yA + tIx / dx^2)
            x += sx
            tIx = dy * (x + sx - xA)

        if movy:
            # intersection is at (xA + tIy / dy^2, y + sy)
            y += sy
            tIy = dx * (y + sy - yA)

        traversed.append((x, y))
        count += 1
        if count > maxiloop:
            break

    return traversed


def testres(testarray, testresult):
    result = find_intercepts(
        testarray[0],
        testarray[1])
    print("find_intercepts({}, {})=".format(
        testarray[0],
        testarray[1]))
    print("{}".format(set(result)))
    print("testresult = ")
    print("{}".format(set(testresult)))
    assert set(testresult) == set(result)


if "__main__" == __name__:
    printseq()

    testarrays = {
        ((4, 1), (2, 4)): (
            (3, 2), (4, 2), (3, 3), (2, 3)),
        ((0, 5), (2, 4)): (
            (1, 4), (1, 5)),
        ((6, 1), (2, 5)): (
            (6, 2),
            (5, 1),
            (5, 2),
            (5, 3),
            (4, 2),
            (4, 3),
            (4, 4),
            (3, 4),
            (3, 3),
            (3, 5),
            (2, 4)),
        ((2, 3), (1, 6)): ((2, 4), (1, 4), (2, 5), (1, 5)),
    }

    for array, result in testarrays.iteritems():
        print("******************************")
        testres(array, result)
        print("******************************")
