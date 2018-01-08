def sieve(limit):
    primes = []
    for i in range(2, limit + 1):
        hits = 0
        for j in range(2, i):
            if i % j == 0 and i != j:
                hits += 1
        if not hits:
            primes.append(i)
    return primes
