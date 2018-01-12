def sum_of_multiples(limit, multiples):
    results = []
    for i in range(1, limit):
        for m in multiples:
            if i % m == 0:
                results.append(i)
    return sum(list(set(results)))
