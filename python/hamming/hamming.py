def distance(strand_a, strand_b):
    """
    Interesting solution using zip(): http://exercism.io/submissions/74655d216b42445c86bb98cf818d23ee
    """
    if len(strand_a) != len(strand_b):
        raise ValueError('Inputs are not same distance')

    distance = 0
    for i, v in enumerate(strand_a):
        if strand_b[i] != v:
            distance += 1

    return distance
