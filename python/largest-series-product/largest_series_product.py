from operator import mul
from functools import reduce


def largest_product(series, size):
    if size == 0:
        return 1
    products = []
    for i, s in enumerate(list(series)):
        try:
            subset = [int(obj) for obj in series[i:i + size]]
            if len(subset) == size:
                products.append(reduce(mul, subset, 1))
        except IndexError:
            continue
    return max(products)
