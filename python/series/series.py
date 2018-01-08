def slices(series, length):
    if not length or length > len(series):
        raise ValueError('Invalid input')
    o = []
    for i in range(0, len(series) + 1 - length):
        o.append([int(i) for i in list(series)][i:i + length])
    return o
