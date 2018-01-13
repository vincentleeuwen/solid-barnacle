from operator import mul
from functools import reduce


def largest_product(series, size):
    if size < 0:
        raise ValueError('Incorrect input')
    groups = [series[i:i + size] for i in range(len(series) - size + 1)]
    return max(reduce(mul, map(int, group), 1) for group in groups)
