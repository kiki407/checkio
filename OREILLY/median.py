def checkio(data):
    data.sort()
    # replace this for solution
    if len(data) % 2 == 0:
        return (list(data)[len(data) / 2 - 1] + list(data)[len(data) / 2]) / 2.0
    else:
        return list(data)[len(data) / 2]
