def nth_prime(n):
    n_found = 0
    candidate = 2
    while True:
        good = True
        for div in range(2, candidate):
            if candidate % div == 0:
                good = False
                break
        if good:
            n_found += 1
            if n_found == n:
                return candidate
        # try with the next number
        candidate += 1
