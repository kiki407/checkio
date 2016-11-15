from math import floor, ceil
import math
from collections import defaultdict


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


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance


def dijsktra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path


def checkio(bunker):
    def build_variables(b):
        bats = {}
        walls = []
        # firstbat = '00'
        batcounter = 1
        line = 0
        for lines in b:
            col = 0
            for cols in lines:
                startpoint = (col == 0 and line == 0)
                if 'A' == cols:
                    bats[str(line)+str(col)] = 'alpha'
                if 'B' == cols and startpoint:
                    bats[str(line)+str(col)] = 'firstbat'
                elif 'B' == cols and not startpoint:
                    bats[str(line)+str(col)] = 'bat{}'.format(batcounter)
                    batcounter += 1
                elif 'W' == cols:
                    walls.append(str(line)+str(col))
                col += 1
            line += 1
        return (bats, walls)

    def can_reach3(sbat1, sbat2, wall_list):
        bat1 = [int(i) for i in sbat1]
        bat2 = [int(i) for i in sbat2]
        if bat1[0] == bat2[0]:
            # check if wall between bat1 and bat2
            for wall in wall_list:
                wall_inbetween = bat1[1] < int(wall[1]) < bat2[1]
                wall_inbetween = wall_inbetween or bat1[1] > int(wall[1]) > bat2[1]
                if int(wall[0]) == bat1[0] and wall_inbetween:
                    return False
            else:
                return abs(bat1[1] - bat2[1])
        # check if bat is same col
        elif bat1[1] == bat2[1]:
            # check if wall between bat1 and bat2
            for wall in wall_list:
                wall_inbetween = bat1[0] < int(wall[0]) < bat2[0]
                wall_inbetween = wall_inbetween or bat1[0] > int(wall[0]) > bat2[0]
                if int(wall[1]) == bat1[1] and wall_inbetween:
                    return False
            else:
                return abs(bat1[0] - bat2[0])

        else:
            wotw = find_intercepts(bat1, bat2)
            for it in wotw:
                srt_it = '{}{}'.format(*it)
                if srt_it in wall_list:
                    return False
            return math.sqrt(
                abs(bat1[1] - bat2[1])**2 +
                abs(bat1[0] - bat2[0])**2)

    def can_reach2(sbat1, sbat2, wall_list):
        bat1 = [int(i) for i in sbat1]
        bat2 = [int(i) for i in sbat2]
        graphy = Graph()
        if bat1[0] >= bat2[0]:
            lines = range(bat2[0], bat1[0] + 1)
        else:
            lines = range(bat1[0], bat2[0] + 1)
        if bat1[1] >= bat2[1]:
            cols = range(bat2[1], bat1[1] + 1)
        else:
            cols = range(bat1[1], bat2[1] + 1)
        for li in lines:
            for col in cols:
                if '{}{}'.format(li,col) not in wall_list:
                    graphy.add_node('{}{}'.format(li,col))

        for n1 in graphy.nodes:
            for n2 in graphy.nodes:
                # print("n1 = {}".format(n1))
                # print("n2 = {}".format(n2))
                if int(n1[0]) + 1 == int(n2[0]) and int(n1[1]) == int(n2[1]):
                    graphy.add_edge(n1, n2, 1)
                if int(n1[0]) == int(n2[0]) and int(n1[1]) + 1 == int(n2[1]):
                    graphy.add_edge(n1, n2, 1)
                if int(n1[0]) - 1 == int(n2[0]) and int(n1[1]) == int(n2[1]):
                    graphy.add_edge(n1, n2, 1)
                if int(n1[0]) == int(n2[0]) and int(n1[1]) - 1 == int(n2[1]):
                    graphy.add_edge(n1, n2, 1)

        if len(graphy.edges) > 0:
            res = False
            try:
                dij = dijsktra(graphy, sbat1)
                res = dij[0][sbat2]
                print("dij = {}".format(dij))
                print("dij[1].keys() = {}".format(dij[1].keys()))
                print("dij[1].values() = {}".format(dij[1].values()))
            except:
                pass

            try:
                dij = dijsktra(graphy, sbat2)
                res = dij[0][sbat1]
                print("dij = {}".format(dij))
                print("dij[1].keys() = {}".format(dij[1].keys()))
                print("dij[1].values() = {}".format(dij[1].values()))
            except:
                pass

        else:
            return False

        if res:
            if bat1[0] == bat2[0] or bat1[1] == bat2[1]:
                return res
            else:
                return math.sqrt(
                    abs(bat1[1] - bat2[1])**2 +
                    abs(bat1[0] - bat2[0])**2)
        else:
            return False

    def can_reach(sbat1, sbat2, wall_list):
        bat1 = [int(i) for i in sbat1]
        bat2 = [int(i) for i in sbat2]
        # check if bat is same line
        if bat1[0] == bat2[0]:
            # check if wall between bat1 and bat2
            for wall in wall_list:
                wall_inbetween = bat1[1] < int(wall[1]) < bat2[1]
                wall_inbetween = wall_inbetween or bat1[1] > int(wall[1]) > bat2[1]
                if int(wall[0]) == bat1[0] and wall_inbetween:
                    return False
            else:
                return abs(bat1[1] - bat2[1])
        # check if bat is same col
        elif bat1[1] == bat2[1]:
            # check if wall between bat1 and bat2
            for wall in wall_list:
                wall_inbetween = bat1[0] < int(wall[0]) < bat2[0]
                wall_inbetween = wall_inbetween or bat1[0] > int(wall[0]) > bat2[0]
                if int(wall[1]) == bat1[1] and wall_inbetween:
                    return False
            else:
                return abs(bat1[0] - bat2[0])
        else:
            # check if wall between
            for wall in wall_list:
                hor_w_inbtw = bat1[1] <= int(wall[1]) < bat2[1]
                hor_w_inbtw = hor_w_inbtw or bat1[1] < int(wall[1]) <= bat2[1]
                hor_w_inbtw = hor_w_inbtw or bat1[1] >= int(wall[1]) > bat2[1]
                hor_w_inbtw = hor_w_inbtw or bat1[1] > int(wall[1]) >= bat2[1]
                vert_w_inbtw = bat1[0] <= int(wall[0]) < bat2[0]
                vert_w_inbtw = vert_w_inbtw or bat1[0] < int(wall[0]) <= bat2[0]
                vert_w_inbtw = vert_w_inbtw or bat1[0] >= int(wall[0]) > bat2[0]
                vert_w_inbtw = vert_w_inbtw or bat1[0] > int(wall[0]) >= bat2[0]
                if hor_w_inbtw and vert_w_inbtw:
                    return False
            else:
                rult = math.sqrt(
                    abs(bat1[1] - bat2[1])**2 +
                    abs(bat1[0] - bat2[0])**2)
                return rult

    def build_graph(batlist, wall_list):
        g = Graph()
        # already_in_list = []
        for pos1, bat1 in batlist.iteritems():
            for pos2, bat2 in batlist.iteritems():
                if pos1 != pos2:
                    g.add_node(bat1)
                    # res2 = can_reach(pos1, pos2, wall_list)
                    # res = can_reach2(pos1, pos2, wall_list)
                    res = can_reach3(pos1, pos2, wall_list)
                    print("+")
                    print("|")
                    print("res = {}".format(res))
                    # print("res2 = {}".format(res2))
                    print("|")
                    print("+")
                    if res:
                        g.add_edge(bat1, bat2, res)
        return g

    bats, walls = build_variables(bunker)

    graph1 = build_graph(bats, walls)
    dj = dijsktra(graph1, 'firstbat')
    res = dj[0]['alpha'] if len(dj[0]) > 1 else 0

    print("|")
    print("|")
    print("bats = {}".format(bats))
    print("walls = {}".format(walls))
    print("graph1.edges = {}".format(graph1.edges))
    print("res = {}".format(res))
    print("dj = {}".format(dj))

    # return 2.83 if len(walls) == 0 else 4
    return res

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(checkio([
        "A--",
        "---",
        "---"]), 0), "Zero"
    assert almost_equal(checkio([
        "BWA-B-",
        "-W----",
        "-WW-B-",
        "-W---B",
        "--B---",
        "B-B---"]), 12.83), "Diagonals"
    assert almost_equal(checkio([
        "B--",
        "---",
        "--A"]), 2.83), "1st example"
    assert almost_equal(checkio([
        "B-B",
        "BW-",
        "-BA"]), 4), "2nd example"
    assert almost_equal(checkio([
        "BWB--B",
        "-W-WW-",
        "B-BWAB"]), 12), "3rd example"
    assert almost_equal(checkio([
        "B---B-",
        "-WWW-B",
        "-WA--B",
        "-W-B--",
        "-WWW-B",
        "B-BWB-"]), 9.24), "4th example"
