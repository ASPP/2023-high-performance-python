import numpy as np
import numba

@numba.njit
def estimate_pi(n):
    np.random.seed(1234)
    count_inside_circle = 0
    for _ in range(n): # Numba likes loops and numpy functions
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)

        if x**2 + y**2 <= 1:
            count_inside_circle += 1

    pi_estimate = 4 * count_inside_circle / n #Numba likes math
    return pi_estimate
