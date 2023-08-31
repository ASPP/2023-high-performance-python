''' START OF CODE TO BE OPTIMIZED '''
# Do not use any additional packages!
# Several improvements are possible

def numerical_integration(f, a, b, n):
    s = []
    for i in range(n):
        dx = (b - a) / n
        x = a + (i + 0.5) * dx
        y = f(x)
        s.append(y * dx)
    return s


def measure_integration_errors(f, F, n_values, a, b):
    # Calculate all integrals
    F_a_list = []
    F_n_list = []
    for n in n_values:
        F_analytical = F(b) - F(a)
        F_numerical_boxes = numerical_integration(f, a, b, n)
        F_a_list.append(F_analytical)
        F_n_list.append(F_numerical_boxes)

    # Calculate and sum error
    errors = []
    for F_analytical, F_numerical_boxes in zip(F_a_list, F_n_list):
        F_numerical = sum(F_numerical_boxes)
        error = abs(F_analytical - F_numerical)
        errors.append(error)

    return errors


# def numerical_integration(f, a, b, n):
#     s = 0
#     for i in range(n):
#         dx = (b - a) / n
#         x = a + (i + 0.5) * dx
#         y = f(x)
#         s += y*dx
#     return s


# def measure_integration_errors(f, F, n_values, a, b):
#     # Calculate and sum error
#     errors = []
#     for n in n_values:
#         F_analytical = F(b) - F(a)
#         F_numerical = numerical_integration(f, a, b, n)
#         error = abs(F_analytical - F_numerical)
#         errors = errors + [error]

#     return errors

''' END OF CODE TO BE OPTIMIZED '''

# This is the function to be integrated
def f(x):
    return x ** 4 - 3 * x

# This is the analytical solution to the integral
def F(x):
    return 1 / 5 * x ** 5 - 3 / 2 * x ** 2


if __name__ == "__main__":

    # Parameters
    n_values = range(500, 20001, 500)
    a = 0
    b = 10

    # Call functions
    errors = measure_integration_errors(f, F, n_values, a, b)
    
    # Print results
    print('  N     Error')
    for n, e in zip(n_values, errors):
        print("{:05d}".format(n), "{:1.3e}".format(e))


