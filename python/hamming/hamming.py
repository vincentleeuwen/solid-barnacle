def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Inputs are not same distance')

    distance = 0
    for i, v in enumerate(strand_a):
        if strand_b[i] != v:
            distance += 1

    return distance
